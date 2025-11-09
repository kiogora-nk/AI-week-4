"""
Task 2: Automated Testing with AI
Selenium test automation for login page testing
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class LoginPageTest(unittest.TestCase):
    """Test case for login page functionality"""
    
    def setUp(self):
        """Set up the WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_valid_login(self):
        """Test login with valid credentials"""
        driver = self.driver
        try:
            # Navigate to test login page (using a demo site)
            driver.get("https://www.saucedemo.com/")
            
            # Enter valid credentials
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
            username_field.send_keys("standard_user")
            
            password_field = driver.find_element(By.ID, "password")
            password_field.send_keys("secret_sauce")
            
            # Click login button
            login_btn = driver.find_element(By.ID, "login-button")
            login_btn.click()
            
            # Verify successful login
            self.wait.until(EC.url_contains("/inventory.html"))
            print("✓ Valid login test passed - Successfully logged in")
            
        except Exception as e:
            print(f"✗ Valid login test failed: {e}")
            raise
    
    def test_invalid_login(self):
        """Test login with invalid credentials"""
        driver = self.driver
        try:
            # Navigate to test login page
            driver.get("https://www.saucedemo.com/")
            
            # Enter invalid credentials
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
            username_field.send_keys("invalid_user")
            
            password_field = driver.find_element(By.ID, "password")
            password_field.send_keys("wrong_password")
            
            # Click login button
            login_btn = driver.find_element(By.ID, "login-button")
            login_btn.click()
            
            # Check for error message
            error_container = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            error_message = error_container.text
            
            self.assertIn("Username and password do not match", error_message)
            print("✓ Invalid login test passed - Proper error message displayed")
            
        except Exception as e:
            print(f"✗ Invalid login test failed: {e}")
            raise
    
    def test_empty_credentials(self):
        """Test login with empty credentials"""
        driver = self.driver
        try:
            # Navigate to test login page
            driver.get("https://www.saucedemo.com/")
            
            # Leave fields empty and click login
            login_btn = driver.find_element(By.ID, "login-button")
            login_btn.click()
            
            # Check for error message
            error_container = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            error_message = error_container.text
            
            self.assertIn("Username is required", error_message)
            print("✓ Empty credentials test passed - Proper validation message")
            
        except Exception as e:
            print(f"✗ Empty credentials test failed: {e}")
            raise
    
    def tearDown(self):
        """Clean up after each test"""
        self.driver.quit()

def run_tests():
    """Run all tests and generate report"""
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print("TEST EXECUTION SUMMARY")
    print(f"{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {(result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100:.1f}%")
    
    return result

if __name__ == "__main__":
    print("Starting Automated Login Page Tests...")
    run_tests()

"""
Summary (150 words):

AI significantly improves test coverage compared to manual testing by automatically 
generating edge case scenarios, identifying dynamic elements, and adapting to UI changes. 
Tools like Selenium with AI plugins can maintain test scripts when applications evolve, 
reducing maintenance overhead by 60%. AI analyzes application usage patterns to prioritize 
test scenarios and identifies areas needing comprehensive testing that humans might overlook.

The automated tests executed above demonstrate how AI-enhanced testing provides 
consistent, repeatable results across multiple test cycles. While manual testing might 
catch 70-80% of issues, AI-driven testing can achieve 95%+ coverage by systematically 
exploring all possible user interactions. This leads to higher software quality and 
faster release cycles, making AI an indispensable tool in modern software testing.
"""