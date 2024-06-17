# Bonds Price Scraper

Este proyecto es un script de Python que utiliza Selenium para rastrear datos de bonos desde la página web de Cohen. Los datos extraídos se almacenan en un archivo CSV que se actualiza periódicamente.

## Requisitos

Para ejecutar este script, necesitarás tener instaladas las siguientes bibliotecas de Python:

- `selenium`
- `pandas`
- `datetime`

Puedes instalarlas utilizando pip:

```bash
pip install selenium pandas
```

## Uso

Clona este repositorio en tu máquina local:

``git clone https://github.com/tu_usuario/bond-data-scraper.git``

Navega al directorio del proyecto:

``cd bond-data-scraper``

Abre el archivo scrape_data.py y asegúrate de que la ruta a tu ejecutable de Chrome esté correctamente configurada:

``chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"``

Ejecuta el script:

`python scrape_data.py`

El script realizará las siguientes acciones:

- Navegará a la página de Cohen para cada ticker de bono especificado en la lista especies.
- Extraerá datos como el símbolo del bono, su nombre, precio, moneda, volumen, monto negociado y cantidad de operaciones.
- Guardará estos datos en un archivo CSV (datos.csv). Si el archivo ya existe, los nuevos datos se añadirán a los datos existentes.
- El script se ejecutará en un bucle infinito, extrayendo y guardando datos cada hora.

# Contribuciones

- Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1) Haz un fork del repositorio.
2) Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3) Realiza tus cambios y haz commits (`git commit -m 'Añadir nueva funcionalidad'`).
4) Empuja tu rama (`git push origin feature/nueva-funcionalidad`).
5) Abre un Pull Request.

# Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

# Contacto

Para cualquier duda o sugerencia, puedes abrir un issue en el repositorio o contactarme directamente a través de Mhmolesini@gmail.com.
