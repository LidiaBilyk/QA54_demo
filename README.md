# QA54_demo
Markdown
# UI Test Automation - Demo Web Shop 🛒

A UI test automation project for the login form of the [Demo Web Shop](https://demowebshop.tricentis.com/) web application. 
Developed as part of a homework assignment (HW12) with a focus on automating negative test scenarios.

## 🛠 Technologies and Tools
* **Language:** Python 3
* **Testing Framework:** pytest
* **Automation Tool:** Selenium WebDriver
* **Secrets Management:** python-dotenv
* **Architecture Pattern:** Page Object Model (POM)

## 📁 Project Structure
* `pages/base_page.py` — base page class encapsulating explicit waits (WebDriverWait).
* `pages/login_page.py` — login page class containing locators and interaction methods.
* `test_login.py` — executable tests with assertions.
* `conftest.py` — pytest configuration and fixtures (WebDriver initialization and setup).

## 🧪 Covered Scenarios

1. **Test Login Form Available:** Verifies the visibility of the login icon and form elements.
2. **Valid Login (Positive):** Successful authorization using valid credentials.
3. **Invalid Email Format (Negative):** Login attempt with an incorrectly formatted email.
4. **Unregistered Email (Negative):** Login attempt with an email that is not registered in the system.
5. **Wrong Password (Negative):** Login attempt with a valid email but an incorrect password.

## 🚀 How to Run Tests Locally

1. **Clone the repository:**
   ```bash
   git clone <your_repository_link>
   cd <repository_folder_name>
2. Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
# or
venv\Scripts\activate     # For Windows


3. Install dependencies:

Bash
pip install pytest selenium python-dotenv


4. Set up environment variables:
Create a .env file in the root of the project and add the following variables:
...
TEST_USER_PASSWORD=your_valid_password
TEST_USER_WRONG_PASSWORD=any_wrong_password
...

5. Run the tests:

Bash
pytest -v