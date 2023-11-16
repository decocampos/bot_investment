# bot_investment
Imagine if you had a personal assistant to decide with you the best options to invest in that moment? To facilitate this, I have developed a Robotic Process Automation (RPA) system. By incorporating your curated list and investment thesis, it guides you towards the most favorable opportunities. Rest assured, it's not a scam. Instead, it operates on a user-centric model—you define the parameters that signal the opportune moment to buy. Following your input, it meticulously analyzes the provided stock list, presenting you with options that align with your specified parameters.

**Requirements** 

pip install selenium
pip install Pillow
pip install webdriver_manager

You also need to have installed the chromedriver in the correct version of your Google Chrome
https://chromedriver.chromium.org/downloads < Official Website

**You need to change these lines**
21: Put the path of your folder to the bot put the printscreen of opportunities to buy
22: Put the path of your folder to the bot put the printscreen of opportunities to sell
27: Put the path of the chromedriver 
35: Put in the list the codes of companies that you want to analyze. Example Apple is: AAPL, Google is GOOGL. Be sure of the code of the company
102;107;111: Put your margins of the RSI that you think is a good opportunity to buy
115;115: Put the margins of the RSI that you think is a good opportunity to sell


