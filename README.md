# bumble_bot
Weekend project; a limited bot to automate your Bumble swiping, some horrible code here but gets the job done.

## To run:

[Install](https://chromedriver.chromium.org/) ChromeDriver and Selenium locally. 

cd inside `src` and stick your Bumble account phone number (without contry code) and password inside the `credentials` file:
```
$ cat credentials
phone_num = 0123456789
password = 'YourPa$$word'
```

Then, create a virtualenv on your local terminal and activate it:
```
$ virtualenv venv
$ source venv/bin/activate
```
Now simply do `python bumble_bot.py` (or `python -i bumble_bot.py` for interactive runtime) and thank me later.

folks seem to have strong opinions around python's `sleep()` vs. selenium's `WebDriverWait()`, I went with sleep for simplicity, you choose your joy. 

:warning: This only works when logging in by phone number (for now), feel free to raise PR's to add other auth methods in.

