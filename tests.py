import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class YibanChenTestSuite(unittest.TestCase):
    def setUp(self):
        ext_dir = "extension_0_38_3_0.crx.crx"

        chrome_options = Options()
        chrome_options.add_extension(ext_dir)
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_a(self):
        driver = self.driver
        driver.get("http://localhost:3000/inbox")
        self.assertIn("YibanChen", driver.title)

        input("Press any key to continue running tests...")

        # Inbox test

        try:
            reply_button = driver.find_element_by_xpath('//*[@id="wide"]/div/div[1]/div[4]/button[1]')
            reply_button.click()
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        except:
            no_messages = driver.find_element_by_xpath('//*[@id="parent"]/div[1]/div[2]/div/p').text
            self.assertEqual("No messages found", no_messages)

        compose_button = driver.find_element_by_xpath('//*[@id="responsive-navbar-nav"]/div[1]/a[2]')
        compose_button.click()

        driver.get("http://localhost:3000/compose")
        time.sleep(5)

        to_field = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/textarea')
        to_field.clear()
        to_field.send_keys("5H3tev113c7xnoLV8NJMAUFg15Egs4SR1sakKRpPQbszjvFd")
        body_field = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/textarea')
        body_field.clear()
        body_field.send_keys("body of message")
        send_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/button')
        send_button.click()

        # Wait for the alert to be displayed
        time.sleep(1)

        # Store the alert in a variable for reuse
        alert = driver.switch_to.alert

        # Store the alert text in a variable
        alert_text = alert.text
        self.assertEqual("You are about to send your message with no subject. Continue?", alert_text)

        # Press the Cancel button
        alert.dismiss()

        body_field.clear()

        to_field = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/textarea')
        to_field.clear()
        # Junk wallet
        to_field.send_keys("bad address")
        subject_field = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/textarea')
        subject_field.clear()
        body_field = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/textarea')
        send_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/button')
        send_button.click()
        time.sleep(1)

        expected_error_message = driver.find_element_by_xpath('//*[@id="root"]/div/div/p').text
        self.assertIn("The recipient address you have entered is not a valid Polkadot address.", expected_error_message)
        back_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/button')
        back_button.click()
        time.sleep(1)

        # Settings page test

        settings_button = driver.find_element_by_xpath('//*[@id="responsive-navbar-nav"]/div[1]/a[3]')
        settings_button.click()

        pinata_key_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/form/label/div/div[1]')
        pinata_key_button.click()
        time.sleep(5)

        balance_text = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/h5').text

        self.assertIn("Balance", balance_text)

        account_dropdown_button = driver.find_element_by_xpath('//*[@id="dropdown-basic"]')
        account_dropdown_button.click()
        time.sleep(1)

        account_select_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/div[1]/a')
        account_select_button.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
