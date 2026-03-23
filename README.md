 Test Automation Framework – SauceDemo


This project is a professional end-to-end web test automation framework built with Python, Selenium, and PyTest, following the **Page Object Model (POM)** design pattern.

It automates key user flows in the SauceDemo application and integrates with GitHub Actions for continuous test execution.


##  Tech Stack
* Python 3.x
* PyTest
* Selenium WebDriver
* PyTest-HTML
* GitHub Actions
* Page Object Model (POM)

##  Test Coverage

This framework covers the following scenarios:

- Valid login with correct credentials  
- Invalid login with incorrect credentials  
- Add a product to the cart  
- Complete checkout flow  

##  Setup and Installation

1. Clone the repository: `https://github.com/camilamoyano1208-QA/SauceDemo-Automation-Python`
2. Create and activate a virtual environment: 
  `Windows`
   python -m venv venv
   venv\Scripts\activate

3.Install dependencies: `pip install -r requirements.txt`.

##  Run Tests
Run tests and generate HTML report:
```bash
pytest --html=report.html

## CI/CD

Tests are automatically executed using GitHub Actions on each push.