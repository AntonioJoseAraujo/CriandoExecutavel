from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoEsperada


def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--start-maximized',
                 '--incognito']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Colocar sempre duas barras para o caminho \\
    caminho_padrao_para_download = 'C:\\Users\\anton\\Downloads'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        # Desabilita notificações (pode atrapalhar na automatização )
        "profile.default_content_setting_values.notifications": 2,
        # Permite realizar múltiplos downlaods multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)

    # Aqui fica a alteração para poder usar o wait
    wait = WebDriverWait(
        driver,
        10,  # tempo que vai usar para carregar a página
        poll_frequency=1,  # ele vai tentar fazer uma ação de 1 em 1 seg
        # dentro do ignored_exceptions vamos colocar os erros que pode acontecer dentro da automação caso a página não tenha carregado, assim não vai aparecer o erro dentro do programa e ele vai continuar até que ele consiga executar
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
        # LEMBRANDO ele vai carregar a página por 10seg, vai tentar fazer a primeira ação no intervalo de 1seg e os erros que mais acontece estão sendo ignorados de aparecer. Tem a documentação salva no arquivo "wait ou sleep"
    )
    return driver, wait


driver, wait = iniciar_driver()
# Quais são os passos a fazer?

# 1 - Navegar até https://automatize.netlify.app/
driver.get('https://automatize.netlify.app')
sleep(2)
# Encontrar o elemento
campo_email = driver.find_element(By.ID, 'email')
sleep(2)
# 2 - Clicar no campo de e-mail
campo_email.click()
sleep(2)
# 3 - Digitar um e-mail
campo_email.send_keys('antonioaraujo@hotmail.com')
sleep(2)
# encontrar campo senha
campo_senha = driver.find_element(By.XPATH, "//input[@type='password']")
sleep(2)
# 4 - Clicar no campo de senha
campo_senha.click()
sleep(2)
# 5 - Digitar uma senha
campo_senha.send_keys('123456')
sleep(2)
# 6 - Clicar no botão iniciar
botao_iniciar = driver.find_element(
    By.XPATH, "//button[@class='btn btn-primary']")
sleep(2)
botao_iniciar.click()
input()
