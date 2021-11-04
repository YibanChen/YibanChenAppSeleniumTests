import unittest, time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from random import randint
from webdriver_manager.chrome import ChromeDriverManager


class YibanChenTestSuite(unittest.TestCase):
    def setUp(self):
        ext_dir = "extension_0_38_3_0.crx.crx"

        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_extension(ext_dir)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    def test_a(self):
        driver = self.driver
        driver.get("http://localhost:3000/inbox")
        self.assertIn("YibanChen", driver.title)

        input("Press any key to continue running tests...")

        # Inbox test

        no_messages = driver.find_element_by_xpath('//*[@id="parent"]/div[1]/div[2]/div/p').text

        self.assertEqual("No messages found", no_messages)

        # time.sleep(1)

        compose_button = driver.find_element_by_xpath("/html/body/div/div/nav/div[1]/a[2]")
        compose_button.click()

        driver.get("http://localhost:3000/compose")
        time.sleep(5)

        to_field = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/input")
        to_field.clear()
        to_field.send_keys("5H3tev113c7xnoLV8NJMAUFg15Egs4SR1sakKRpPQbszjvFd")
        body_field = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/textarea")
        body_field.clear()
        body_field.send_keys("body of message")
        send_button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/button")
        send_button.click()

        # Wait for the alert to be displayed
        time.sleep(1)

        # Store the alert in a variable for reuse
        alert = driver.switch_to.alert

        # Store the alert text in a variable
        alert_text = alert.text
        self.assertEqual("You have insufficient funds to make this transacation.", alert_text)

        # Press the Cancel button
        alert.dismiss()

        body_field = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/textarea")
        body_field.clear()

        to_field = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/input")
        to_field.clear()
        # Junk wallet
        to_field.send_keys("bad address")
        subject_field = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/input")
        subject_field.clear()

        send_button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/button")
        send_button.click()
        time.sleep(2)

        # Store the alert in a variable for reuse
        alert = driver.switch_to.alert

        # Store the alert text in a variable
        alert_text = alert.text
        self.assertEqual(
            "The recipient address you have entered is not a valid Polkadot address. Please make sure you have entered it correctly.",
            alert_text,
        )

        alert.dismiss()

        # Settings page test

        settings_button = driver.find_element_by_xpath('//*[@id="root"]/div/nav/div[1]/a[3]')
        settings_button.click()

        pinata_key_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/form/label/div/div[1]')
        pinata_key_button.click()
        time.sleep(2)

        balance_text = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/h5').text

        self.assertIn("Balance", balance_text)

        account_dropdown_button = driver.find_element_by_xpath('//*[@id="dropdown-basic"]')
        account_dropdown_button.click()

    def test_b(self):
        # Site upload, modify, and delete test
        driver = self.driver
        driver.get("http://localhost:3000/upload")
        time.sleep(1)

        # Upload

        site_path = os.path.abspath("sample.html")
        input("Press Enter to Continue\2")
        time.sleep(1)
        driver.get("http://localhost:3000/upload")
        time.sleep(4)

        site_name = str(randint(1000, 900000))

        name_input = driver.find_element_by_id("name-input")
        name_input.send_keys(site_name)
        time.sleep(2)
        file_input = driver.find_element_by_xpath("//input[@type='file']")
        file_input.send_keys(site_path)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        upload_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/button")
        upload_button.click()
        time.sleep(20)

        # Assert site is in my-sites after upload
        driver.get("http://localhost:3000/my-sites")
        time.sleep(10)

        # Modify
        site_dropdown = driver.find_element_by_id(site_name + "-dropdown")
        site_dropdown.click()
        site_modify_button = driver.find_element_by_id(site_name + "-modify")
        site_modify_button.click()
        file_input_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/input")

        file_input_2.send_keys(site_path)
        upload_button_2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/div/button")
        upload_button_2.click()
        time.sleep(20)

        # Delete
        site_dropdown = driver.find_element_by_id(site_name + "-dropdown")
        site_dropdown.click()
        site_delete_button = driver.find_element_by_id(site_name + "-delete")
        site_delete_button.click()
        alert = driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        time.sleep(10)
        driver.get("http://localhost:3000/compose")

        time.sleep(4)

        # Compose and send Note with actual transaction

        to_field = driver.find_element_by_id("to-field")
        to_field.clear()
        to_field.send_keys("5FhWHCbQvAUzYxT4fmmPXXBWEBbTApEcpG25vmjmdDAdubym")
        body_field = driver.find_element_by_id("body-field")
        body_field.clear()
        body_field.send_keys("body of message")
        subject_field = driver.find_element_by_id("subject-field")
        subject_field.send_keys("subject of message")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        send_button = driver.find_element_by_id("send-button")
        send_button.click()

        # Wait for note to be sent
        time.sleep(20)
        expected_message = "Your message was sent!"
        confirmation_message = driver.find_element_by_id("sent-confirmation").text
        # Asser note was sent
        self.assertEqual(confirmation_message, expected_message)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
