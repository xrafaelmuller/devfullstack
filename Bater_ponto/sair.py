from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "03302364075"
PASSWORD = "Bombs666"
WEBSITE_URL = "https://dell.populisservicos.com.br/populisII-web/paginas/protegidas/basico/funcionario.xhtml?f=true&igHisNav=true"

# Inicializa o WebDriver
driver = webdriver.Chrome()
driver.get(WEBSITE_URL)

def wait_for_element(locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def wait_for_clickable(locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

try:
    # Login
    username_field = wait_for_element((By.NAME, "formLogin:usuarioInput"))
    password_field = wait_for_element((By.NAME, "formLogin:senhaInput"))  # Verifique o nome correto do campo de senha

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    # Aguarda o login ser processado
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Garante o foco na página
    body = driver.find_element(By.TAG_NAME, 'body')
    body.click()

    # Simula SHIFT + C
    ActionChains(driver).key_down(Keys.SHIFT).send_keys('C').key_up(Keys.SHIFT).perform()

    # Aguarda o efeito do atalho (verifique o seletor correto para a ação esperada)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "seletor_apos_atalho")))

    # Botão de saída
    sair_button = wait_for_clickable((By.NAME, "marcacaoPresencaSairBtn"))
    sair_button.click()

finally:
    driver.quit()
