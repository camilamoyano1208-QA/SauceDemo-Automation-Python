from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver= driver
        self.wait= WebDriverWait(self.driver,10) #espera estandar 10 seg

    def visit(self,url):
        self.driver.get(url) #url especifica

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)) #espera hasta que elemento sea visible
    
    def click_element(self, locator):
        element= self.wait.until(EC.element_to_be_clickable(locator)) #espera hasta que sea clickable y hace clic
        element.click()

    def type_text(self, locator, text):
        element= self.find_element(locator)#espera elemento, lo limpia y escribe texto
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.find_element(locator).text #obtiene el texto en un elemento