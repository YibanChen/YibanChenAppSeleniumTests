# YibanChen Integration Tests

## About the tests

These are automated web browser tests; the Selenium client interacts with the Chrome Driver to ensure that the web functionalties work as expected in the browser environment. Some manual configuration is required to run the tests as the chromedriver extension cannot access your existing polkadot wallets.

While the tests do not currently cover the web app's use of our blockchain API due to security concerns and other issues, mainly due to the fact that transacations performed through our blockchain API require tokens, we plan to extend our coverage to include these interactions by making use of a test blockchain operating seperately from the main blockchain.

## Setup

Make sure you are running the YibanChen [YibanChen-app](https://github.com/YibanChen/yibanchen-app) build locally and that it is reachable at http://localhost:3000

Also check that you do not already have Google Chrome opened, as the tests will automatically fail if Chrome is already opened in another window.

Make sure your version of Google Chrome matches the version of the chromedriver in this directory. We have included a chromedriver for version 91 of Google Chrome built for the m1-mac, but you may need to download the version matching your Google Chrome installation.

You can download different versions from https://chromedriver.chromium.org/downloads

If you are using MacOS and the chromedriver fails when you try to run it, or if you run into the following error:

```
selenium.common.exceptions.WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: -9
```

You will need to set up your security settings to allow the chromedriver to run. Please navigate to System Preferences > Security and Privacy and there will be a prompt asking you allow the chromedriver to run.

You will also need to add chromedriver to your shell path. If you want to use the local version we have included, in your terminal `PATH=$PATH:.`

## Running the tests

Make sure you are using Python 3.

To install the required python modules, run the command pip

`pip install -r requirements.txt`

To start the tests, simply run the command

`python tests.py`

Some manual configuration is required after running the above command before the automated tests can begin.

Selenium will open a chrome browser and navigate to the YibanChen site. The website will inform you that "An application, self-identifying as YibanChen is requesting access". Allow this access, and then create a new account through the polkadot extension, or optionally import your own using the account's mnemonic seed. Reload the page (a hard refresh CMD + SHIFT +R may be required ) and then select your account from the dropdown menu that appears.

After completing these tests, navigate back to the termninal running the test script and press any key to continue running the tests.

[Example video of running the test](https://youtu.be/nkAdblH0GW0)
