from pathlib import Path
import configparser
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)


def get_browser():
    return config.get("settings", "browser")


def get_headless():
    if os.getenv("CI", "").lower() == "true":
        return True

    return config.getboolean("settings", "headless")


def get_url():
    url = config.get("settings", "url")
    return url if url.endswith("/") else f"{url}/"


def get_api_base_url():
    return config.get("settings", "api_base_url")


def get_api_key():
    return config.get("settings", "api_key")