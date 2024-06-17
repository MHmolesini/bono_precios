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

especies = ['PARP', 'DICP', 'CUAP', 'PAP0', 'DIP0', 'TO26', 'T5X4', 'T2X4', 'T4X4', 'TC25P', 'TX25', 'TX26', 'TX28', 'TX31', 'TZX25', 'TZX26', 'TZX27', 'TZX28', 'TZXD5', 'TZXD6', 'TZXD7', 'TZXM6', 'TDG24', 'TDJ24', 'TDE25', 'TV25', 'TZV25', 'S01L4', 'S12L4', 'S26L4', 'S16G4', 'S30G4', 'S13S4', 'S14O4', 'S29N4', 'S31E5', 'S28F5', 'S31M5', 'AL30D']
categorias = {
    'PARP': 'BONCER',
    'DICP': 'BONCER',
    'CUAP': 'BONCER',
    'PAP0': 'BONCER',
    'DIP0': 'BONCER',
    'TO26': 'BONO',
    'T5X4': 'BONCER',
    'T2X4': 'BONCER',
    'T4X4': 'BONCER',
    'TC25P': 'BONCER',
    'TX25': 'BONCER',
    'TX26': 'BONCER',
    'TX28': 'BONCER',
    'TX31': 'BONCER',
    'TZX25': 'BONCER',
    'TZX26': 'BONCER',
    'TZX27': 'BONCER',
    'TZX28': 'BONCER',
    'TZXD5': 'BONCER',
    'TZXD6': 'BONCER',
    'TZXD7': 'BONCER',
    'TZXM6': 'BONCER',
    'TDG24': 'BONO DUAL',
    'TDJ24': 'BONO DUAL',
    'TDE25': 'BONO DUAL',
    'TV25': 'BONO LINKED',
    'TZV25': 'BONO LINKED',
    'S01L4': 'LECAP',
    'S12L4': 'LECAP',
    'S26L4': 'LECAP',
    'S16G4': 'LECAP',
    'S30G4': 'LECAP',
    'S13S4': 'LECAP',
    'S14O4': 'LECAP',
    'S29N4': 'LECAP',
    'S31E5': 'LECAP',
    'S28F5': 'LECAP',
    'S31M5': 'LECAP',
    'AL30D': 'BONO DOLARES L.ARG',
}
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
        
        # Obtener la categoría correspondiente al Ticker
        categoria = categorias.get(especie, 'Desconocido')

        # Almacenar los datos en el diccionario
        especies_detalle = {
            'Fecha': current_datetime,
            'Categoria': categoria,
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
nuevo_df = pd.DataFrame(especies_detalles)
print(nuevo_df)

# Nombre del archivo CSV donde guardarás los datos
archivo_csv = 'datos.csv'

# Leer los datos existentes (si el archivo existe)
try:
    datos_existentes = pd.read_csv(archivo_csv)
except FileNotFoundError:
    # Si el archivo no existe, crear un DataFrame vacío
    datos_existentes = pd.DataFrame()

# Combinar los datos existentes con los nuevos datos
df_combinado = pd.concat([datos_existentes, nuevo_df], ignore_index=True)

# Guardar el DataFrame combinado de vuelta al archivo CSV
df_combinado.to_csv(archivo_csv, index=False)

print("Datos combinados guardados exitosamente.")
