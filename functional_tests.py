from selenium import webdriver

browser = webdriver.Chrome('/Users/sean/chromedriver')
browser.get('http://localhost:8000')

assert 'install' in browser.title


