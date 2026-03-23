import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(): 
    chrome_options= Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless") #corra en la nube sin ventana
    chrome_options.add_argument("--no-sandbox")#le dice a chrome que confia en el sitio y no es necesario poner paredes de seguridad extra
    chrome_options.add_argument("--disable-dev-shm-usage")#para que no use la carpeta compartida limitada, use la RAM normal del sistema
    chrome_options.add_argument("--start-maximized")

    #Desactivar el aviso de "Software automatizado"
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    #Configurar las PREFS para bloquear el letrero de Google (IMPORTANTE)
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # CREAR EL DRIVER AL FINAL (Pasándole todas las opciones de arriba)
    driver = webdriver.Chrome(options=chrome_options)

    yield driver #entrega el navegador al test
    driver.quit() #cerrar el terminar

@pytest.hookimpl(tryfirst=True, hookwrapper= True) #detecta fallos y toma foto automaticamente
def pytest_runtest_makereport(item, call):
    outcome= yield
    rep= outcome.get_result()  
    if rep.when =='call' and rep.failed:   #solo actua si el test falla
        try: #si el test falla, busca el driver y toma foto
            driver= item.funcargs['driver']  #accede al driver que usa el test
            driver.save_screenshot(f"fallo_{item.name}.png") #guarda foto con nombre del test
        except Exception as e:
            print (f"The capture could not be taken: {e}")

    

 
