# Nós queremos:
# Acessar a página
# Pegar os links
# DataFrame

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/"

driver.get(url)
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, value="a")
print(links)
print(len(links))

#Os livros começam no 54 e terminam no 92

x = driver.find_elements(By.TAG_NAME, value="a")[54].text
print(x)

y = driver.find_elements(By.TAG_NAME, value="a")[54].get_attribute("title")
print(y)

print(driver.find_elements(By.TAG_NAME, value="a")[54:94:2])

elementostitulo = driver.find_elements(By.TAG_NAME, value="a")[54:94:2]

listatitulos = [title.get_attribute("title") for title in elementostitulo]
print(listatitulos)

elementostitulo[1].click()
time.sleep(2)
stok = driver.find_element(By.CLASS_NAME, value="instock").text
time.sleep(2)
print(stok)
estoque = int(stok.replace("In stock (","").replace(" available)", ""))
print(estoque)
driver.back()

listaestoque = []

for titulo in elementostitulo:
    titulo.click()
    time.sleep(1)
    quantidade = int( driver.find_element(By.CLASS_NAME, value="instock").text.replace("In stock (","").replace(" available)", ""))
    listaestoque.append(quantidade)
    driver.back()
    time.sleep(1)

print(listaestoque)

data = {"Titulo": listatitulos, "Estoque": listaestoque}
print(pd.DataFrame(data))
dados = pd.DataFrame(data)
dados.to_excel("dados.xlsx")