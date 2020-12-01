from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.webdriver import WebDriver

import unittest


class ExampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefox_options = options.Options()
        firefox_options.headless = False
        cls.driver = WebDriver(options=firefox_options)

    def tearDown(self):
        self.driver.quit()

    def test_can_see_google(self):
        self.driver.get('https://www.google.com')

        self.assertIn('Google', self.driver.title)
