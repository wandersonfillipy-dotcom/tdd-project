from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element("id", "id_list_table")
        rows = table.find_elements("tag name", "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)

        header_text = self.browser.find_element("tag name", "h1").text
        self.assertIn("Your To-Do list", header_text)

        inputbox = self.browser.find_element("id", "id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        inputbox.send_keys("Estudar testes funcionais")
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        self.check_for_row_in_list_table(
            "1: Estudar testes funcionais"
        )

        inputbox = self.browser.find_element("id", "id_new_item")
        inputbox.send_keys("Estudar testes de unidade")
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        self.check_for_row_in_list_table(
            "1: Estudar testes funcionais"
        )

        self.check_for_row_in_list_table(
            "2: Estudar testes de unidade"
        )


if __name__ == "__main__":
    unittest.main()