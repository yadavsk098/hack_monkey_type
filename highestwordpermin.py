import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach",True)
browser = webdriver.Chrome(options=options)

url = "https://monkeytype.com/"
browser.get(url)
time.sleep(5)
cookie_click = browser.find_element(By.XPATH,"//div[text()='Accept all']")
time.sleep(2)

cookie_click.click()
# word = browser.find_elements(By.XPATH,"/html/body/div[9]/div[2]/div[2]/div/div[3]/div[8]/div[3]/div[1]")
# print(word[0].get_attribute("class"))

activeidx = 0

while True:
    #sabse phele word list find karte hai xpath sy
    wordlist = browser.find_elements(By.XPATH,"/html/body/div[9]/div[2]/div[2]/div/div[3]/div[8]/div[3]/div")
    # print(wordlist)
    # div ka active class find karege
    for i in range(len(wordlist)):
        if "active" in wordlist[i].get_attribute("class"):
            activeidx = i
            break
    # ek baar my ek word bejegy but ussy phele word ko store karvate hai
    wordlist = wordlist[activeidx:]
    # print(wordlist)
    for word in wordlist:
        letters = ""
        chars = word.find_elements(By.XPATH,"./letter")
        for char in chars:
            letters += char.text
        letters += " "
        ActionChains(browser).send_keys(letters).perform()




