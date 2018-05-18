import sys
from selenium import webdriver

browser = webdriver.Chrome()
out = sys.stdout
sys.stdout = open('browserHelper.txt', 'w')
help(browser)
sys.stdout.close()
sys.stdout = out
browser.quit()
exit()