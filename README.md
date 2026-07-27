# 🎭 Playwright Automation Framework with Python

## 📌 Overview

This project is a UI test automation framework built using **Playwright with Python and Pytest**.

The framework follows the **Page Object Model (POM)** design pattern to create reusable, maintainable, and scalable automation scripts.

The goal of this framework is to automate end-to-end functional testing of web applications.

---

## 🚀 Tech Stack

| Tool              | Purpose                  |
| ----------------- | ------------------------ |
| Python            | Programming Language     |
| Playwright        | Web Automation           |
| Pytest            | Test Execution Framework |
| Page Object Model | Framework Design Pattern |
| Git & GitHub      | Version Control          |
| HTML Reports      | Test Reporting           |

---

## 📂 Project Structure

```
Playwright_Automation
│
├── tests
│   ├── test_login.py
│   ├── test_add_to_cart.py
│
├── pages
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│
├── utils
│   ├── test_data.py
│
├── logs
│   └── automation.log
│
├── conftest.py
├── config.ini
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Setup

## 1. Clone Repository

```bash
git clone <repository-url>
```

Navigate into project folder:

```bash
cd Playwright_Automation
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

# 🧪 Running Tests

Run all tests:

```bash
pytest
```

Run specific test:

```bash
pytest tests/test_login.py
```

Run with HTML report:

```bash
pytest --html=report.html
```

---

# ✅ Implemented Test Scenarios

## Login Testing

✔ Valid user login
✔ Invalid login validation
✔ Error message verification

## Product Testing

✔ Verify product listing
✔ Add product to cart
✔ Remove product from cart
✔ Verify cart badge count

## Checkout Testing

✔ Enter customer information
✔ Complete purchase flow
✔ Verify order confirmation

---

# 🏗 Framework Features

✅ Page Object Model Architecture
✅ Reusable page classes
✅ Common browser actions in Base Page
✅ Pytest fixtures
✅ Configuration management
✅ Logging implementation
✅ Test data separation
✅ HTML reporting support

---

# 📸 Test Execution Example

Example:

```
============================= test session starts =============================

collected 5 items

tests/test_login.py ........ PASSED
tests/test_add_to_cart.py . PASSED

============================= 5 passed =============================
```

---

# 🔮 Future Enhancements

* Add CI/CD pipeline using GitHub Actions
* Add API automation using Python Requests
* Add database validation
* Add parallel execution
* Add Docker support
* Add AI-powered test case generation

---

# 👨‍💻 Author

**Murali Challa**

Playwright Automation Engineer | Python | QA Automation

---

⭐ If you find this framework useful, feel free to fork and improve it.
