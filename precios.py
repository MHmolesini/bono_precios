from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

# Configuración del navegador Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Configuración del navegador Chrome para Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# Agregar opciones para abrir Chrome en modo incógnito y maximizado
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--start-maximized')

# Crear instancia del navegador Chrome
driver = webdriver.Chrome(options=chrome_options)

especies = ['TX31', 'PARP', 'AL30D', 'TX28', 'TX26']
especies_detalles = []

for especie in especies:
    # Formatear la URL con la especie actual
    url = f'https://www.cohen.com.ar/Bursatil/Especie/{especie}'
    print(f'Navegando a: {url}')
    
    # Navegar a la página
    driver.get(url)

    # Esperar a que el menú esté presente en la página
    wait = WebDriverWait(driver, 10)

    try:    
        detailSimbolo = driver.find_element(By.XPATH, '//*[@id="page-body-container"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/h2')
        detailDescripcionNombre = driver.find_element(By.XPATH, '//*[@id="page-body-container"]/div[2]/div/div[2]/div[1]/div[1]/div[5]')
        detailCotizacion = driver.find_element(By.XPATH, '//*[@id="page-body-container"]/div[2]/div/div[2]/div[1]/div[1]/div[4]/span[1]')
        
        moneda = driver.find_element(By.XPATH, '//*[@id="page-body-container"]/div[2]/div/div[2]/div[1]/div[2]/ul/li[2]/span[2]')
        volumen = driver.find_element(By.XPATH, '//*[@id="page-body-container"]/div[2]/div/div[2]/div[1]/div[2]/ul/li[8]/span[2]')
        montoNegociado = driver.find_element(By.XPATH, '//*[@id="page-body-container"]/div[2]/div/div[2]/div[1]/div[2]/ul/li[9]/span[2]')
        operaciones = driver.find_element(By.XPATH, '//*[@id="page-body-container"]/div[2]/div/div[2]/div[1]/div[2]/ul/li[10]/span[2]')
        
        # Obtener la fecha y hora actuales
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Almacenar los datos en el diccionario
        especies_detalle = {
            'Fecha': current_datetime,
            'Ticker': detailSimbolo.text,
            'Nombre': detailDescripcionNombre.text,
            'Precio': detailCotizacion.text,
            'Moneda': moneda.text,
            'Volumen': volumen.text,
            'Volumen $': montoNegociado.text,
            'Cantidad de operaciones': operaciones.text
        }
        
        # Añadir el diccionario a la lista
        especies_detalles.append(especies_detalle)
        
        print(especies_detalle)
    except Exception as e:
        print(f'No se pudo encontrar los valores para {especie}: {e}')
        continue  # Continuar con el siguiente elemento de la lista

# Cerrar el navegador
driver.quit()

# Convertir la lista de diccionarios a un DataFrame de pandas
df = pd.DataFrame(especies_detalles)
print(df)