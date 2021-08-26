# YibanChen Integration Tests

## Setup

Please make sure you are running the [YibanChen-app](https://github.com/YibanChen/yibanchen-app) locally and that it is reachable at http://localhost:3000

Also make sure that you do not already have Google Chrome opened.

## Running the tests

To start the tests, cd into the testing directory and enter the command

`python3 tests.py`

Some manual configuration is required after running the above command before the automated tests can begin.

Selenium will open a chrome browser and navigate to the YibanChen site. Manually sign into a Polkadot account via the Polkadot extension, or create a new one.

After signing in via the extension, reload the page and then select your account from the dropdown menu. At this point, no more input is required and you can wait for the automated tests to complete.

The integration tests are run as a monolith. This is because each Python unit test would require the user to again sign in via the extension. Running the tests as a monolith avoids this problem with minimal complications.
