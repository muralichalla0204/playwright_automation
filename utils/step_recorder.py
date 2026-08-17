import json
from datetime import datetime
from html import escape
from pathlib import Path

from utils.logger import logger

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_ROOT = PROJECT_ROOT / "reports" / "step_evidence"


class StepRecorder:
    def __init__(self, test_name: str, page):
        self.test_name = test_name
        self.page = page
        self.steps = []
        self._counter = 0
        self.started_at = datetime.now()

        timestamp = self.started_at.strftime("%Y%m%d_%H%M%S")
        safe_name = self._sanitize(test_name)
        self.run_dir = EVIDENCE_ROOT / f"{timestamp}_{safe_name}"
        self.run_dir.mkdir(parents=True, exist_ok=True)

    def run_step(self, action: str, callback):
        try:
            result = callback()
            self.record(action, "PASSED")
            return result
        except Exception as exc:
            self.record(action, "FAILED", str(exc))
            raise

    def record(self, action: str, status: str, error: str | None = None):
        self._counter += 1
        step_num = self._counter
        safe_action = self._sanitize(action)
        filename = f"step_{step_num:03d}_{safe_action}_{status}.png"
        screenshot_path = self.run_dir / filename

        self.page.screenshot(path=str(screenshot_path), full_page=True)

        step = {
            "step": step_num,
            "action": action,
            "status": status,
            "screenshot": filename,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "error": error,
        }
        self.steps.append(step)
        logger.info(
            "Step %s | %s | %s | %s",
            step_num,
            status,
            action,
            screenshot_path.relative_to(PROJECT_ROOT),
        )
        return step

    def finalize(self, test_status: str):
        self._write_json(test_status)
        self._write_html(test_status)
        self._update_index(test_status)
        logger.info(
            "Step report saved: %s",
            (self.run_dir / "step_report.html").relative_to(PROJECT_ROOT),
        )

    def _write_json(self, test_status: str):
        payload = {
            "test_name": self.test_name,
            "test_status": test_status,
            "started_at": self.started_at.isoformat(timespec="seconds"),
            "finished_at": datetime.now().isoformat(timespec="seconds"),
            "total_steps": len(self.steps),
            "passed_steps": sum(1 for step in self.steps if step["status"] == "PASSED"),
            "failed_steps": sum(1 for step in self.steps if step["status"] == "FAILED"),
            "steps": self.steps,
        }
        (self.run_dir / "steps.json").write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8",
        )

    def _write_html(self, test_status: str):
        passed = sum(1 for step in self.steps if step["status"] == "PASSED")
        failed = sum(1 for step in self.steps if step["status"] == "FAILED")
        status_class = "passed" if test_status == "PASSED" else "failed"

        rows = []
        for step in self.steps:
            row_status = step["status"].lower()
            error_block = ""
            if step["error"]:
                error_block = f'<p class="error">{escape(step["error"])}</p>'

            rows.append(
                f"""
                <tr class="{row_status}">
                    <td>{step["step"]}</td>
                    <td>{escape(step["action"])}</td>
                    <td><span class="badge {row_status}">{step["status"]}</span></td>
                    <td>{escape(step["timestamp"])}</td>
                    <td>
                        <a href="{escape(step["screenshot"])}" target="_blank">
                            <img src="{escape(step["screenshot"])}" alt="Step {step["step"]}">
                        </a>
                        {error_block}
                    </td>
                </tr>
                """
            )

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{escape(self.test_name)} - Step Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 24px; background: #f5f7fb; color: #1f2937; }}
        .card {{ background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
        h1 {{ margin-top: 0; }}
        .summary {{ display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 20px; }}
        .pill {{ padding: 8px 12px; border-radius: 999px; background: #eef2ff; }}
        .pill.passed {{ background: #dcfce7; color: #166534; }}
        .pill.failed {{ background: #fee2e2; color: #991b1b; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border-bottom: 1px solid #e5e7eb; padding: 12px; vertical-align: top; text-align: left; }}
        tr.failed {{ background: #fff1f2; }}
        .badge {{ padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: bold; }}
        .badge.passed {{ background: #16a34a; color: white; }}
        .badge.failed {{ background: #dc2626; color: white; }}
        img {{ max-width: 320px; border: 1px solid #d1d5db; border-radius: 8px; }}
        .error {{ color: #b91c1c; margin: 8px 0 0; font-size: 13px; }}
        a {{ color: #2563eb; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{escape(self.test_name)}</h1>
        <div class="summary">
            <div class="pill {status_class}">Test: {test_status}</div>
            <div class="pill">Total Steps: {len(self.steps)}</div>
            <div class="pill passed">Passed: {passed}</div>
            <div class="pill failed">Failed: {failed}</div>
            <div class="pill">Started: {escape(self.started_at.strftime("%Y-%m-%d %H:%M:%S"))}</div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Action</th>
                    <th>Status</th>
                    <th>Time</th>
                    <th>Screenshot</th>
                </tr>
            </thead>
            <tbody>
                {"".join(rows)}
            </tbody>
        </table>
    </div>
</body>
</html>
"""
        (self.run_dir / "step_report.html").write_text(html, encoding="utf-8")

    def _update_index(self, test_status: str):
        index_path = EVIDENCE_ROOT / "index.html"
        EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)

        relative_dir = self.run_dir.relative_to(EVIDENCE_ROOT).as_posix()
        row = (
            f"<tr>"
            f"<td>{escape(self.started_at.strftime('%Y-%m-%d %H:%M:%S'))}</td>"
            f"<td>{escape(self.test_name)}</td>"
            f"<td>{test_status}</td>"
            f"<td>{len(self.steps)}</td>"
            f'<td><a href="{relative_dir}/step_report.html">Open Report</a></td>'
            f"</tr>\n"
        )

        if index_path.exists():
            content = index_path.read_text(encoding="utf-8")
            content = content.replace("</tbody>", f"{row}</tbody>")
            index_path.write_text(content, encoding="utf-8")
            return

        index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Step Evidence Index</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 24px; background: #f5f7fb; }}
        .card {{ background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border-bottom: 1px solid #e5e7eb; padding: 10px; text-align: left; }}
        a {{ color: #2563eb; text-decoration: none; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Step Evidence Index</h1>
        <p>Every test run with step-by-step screenshots (passed and failed).</p>
        <table>
            <thead>
                <tr>
                    <th>Run Time</th>
                    <th>Test</th>
                    <th>Result</th>
                    <th>Steps</th>
                    <th>Report</th>
                </tr>
            </thead>
            <tbody>
                {row}
            </tbody>
        </table>
    </div>
</body>
</html>
"""
        index_path.write_text(index_html, encoding="utf-8")

    @staticmethod
    def _sanitize(value: str) -> str:
        cleaned = "".join(char if char.isalnum() else "_" for char in value)
        while "__" in cleaned:
            cleaned = cleaned.replace("__", "_")
        return cleaned.strip("_").lower()[:50] or "step"
