from selenium import webdriver
import time

# Especifique o caminho do driver do Chrome aqui
chrome_driver_path = "C:/projetos/botDownloadArqs/chromedriver.exe"

# Configurar as opções do driver (opcional)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)

# Configurar o serviço do Chrome com o caminho do driver
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Inicializar o driver do Chrome
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# Agora você pode usar o driver para automatizar tarefas de navegação web

# Abrir o Google e fazer uma pesquisa por "seguro desemprego"
driver.get("https://www.google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("seguro desemprego")
search_box.submit()

# Aguardar um tempo para os resultados carregarem
time.sleep(5)

# Encontrar e clicar no link "Documentos"
try:
    doc_link = driver.find_element_by_partial_link_text("Documentos")
    doc_link.click()
except Exception as e:
    print("Link 'Documentos' não encontrado:", str(e))

# Encontrar todos os links na página
all_links = driver.find_elements_by_tag_name("a")

# Procurar por links para arquivos .xls, .txt e .pdf e baixá-los
file_extensions = [".xls", ".txt", ".pdf"]

for link in all_links:
    link_text = link.get_attribute("href")
    if any(extension in link_text for extension in file_extensions):
        link.click()
        time.sleep(2)  # Aguardar o download ser concluído

# Fechar o navegador após o download
driver.quit()
