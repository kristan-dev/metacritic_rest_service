from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.config import cfg

class Selenium_Test:
  def phantomjs_test(self):
    driver = webdriver.PhantomJS(
      executable_path=cfg['webdriver']['phantomjs']['macos']['path'],
      port=int(cfg['webdriver']['phantomjs']['macos']['port']))
    
    # fireFoxOptions = webdriver.FirefoxOptions()
    # fireFoxOptions.set_headless()
    # brower = webdriver.Firefox(firefox_options=fireFoxOptions)

    driver.get("https://metacritic.com/game")
    driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
    driver.find_element_by_id("search_button_homepage").click()
    print(driver.current_url)
    driver.quit()


if(__name__ ==  "__main__"):
  start = Selenium_Test()
  start.phantomjs_test()
  pass
