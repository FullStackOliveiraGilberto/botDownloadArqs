from selenium import webdriver
import time

# Especifique o caminho do driver do Chrome aqui
chrome_driver_path = "C:/projetos/botDownloadArqs/chromedriver.exe"

# Configurar as opções do driver (opcional)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Caminho para o executável do Chrome

# Inicializar o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Agora você pode usar o driver para automatizar tarefas de navegação web

# Abrir o Google e fazer uma pesquisa por "seguro desemprego"
driver.get("https://www.google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("seguro desemprego")
search_box.submit()

# Aguardar um tempo para os resultados carregarem
time.sleep(5)

# Encontrar todos os links na página
all_links = driver.find_elements_by_tag_name("a")

# Procurar por links para arquivos .xls, .txt e .pdf e baixá-los
file_extensions = [".xls", ".txt", ".pdf"]

for link in all_links:
    link_text = link.get_attribute("href")
    for extension in file_extensions:
        if extension in link_text:
            link.click()
            time.sleep(2)  # Aguardar o download ser concluído

# Fechar o navegador após o download
driver.quit()
