from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# konfiguracja Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--start-maximized")

# otworzenie przeglądarki Chrome
driver = webdriver.Chrome(options=chrome_options)

# nawigacja do strony www
driver.get("https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna")


'''# manipulacja obiektem inputbox na Wikipedia
elem = driver.find_element("xpath",'//*[@id="searchInput"]')
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)'''

link = driver.find_element('xpath','//*[@id="main-page-didyouknow"]/p[2]/i[1]/b/a')
webdriver.ActionChains(driver).move_to_element(link).perform()