import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


def req():
    nrequest = pyautogui.prompt(text='Coloque o número da requisição:\n\n'
                                    'Exemplo: 5784235481', title='Digite o Número da Requisição.',
                               default='')

    if len(nrequest) >= 11 or len(nrequest) < 10 or nrequest.isalpha() or nrequest.islower() or nrequest.istitle():
        pyautogui.alert(text=f'Você digitou algo que não é válido!', title='NÚMERO DA REQUISIÇÃO!',
                        button='Tente novamente!')
        import sys
        import os
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        confirma = pyautogui.confirm(text='Confira se os dados estão corretos...\n\n'
                                          f'Número da requisição: {nrequest}',
                                     title='CONFIRA SEUS DADOS!',
                                     buttons=['ESTÁ TUDO CERTO!', 'PRECISO ALTERAR...'])

        if confirma == 'PRECISO ALTERAR...':
            import sys
            import os
            python = sys.executable
            os.execl(python, python, *sys.argv)
        elif confirma == 'ESTÁ TUDO CERTO!':
            return nrequest


nrequest = req()


def passwd():
    password = pyautogui.password(text='Digite a senha do para acessar os resultados de exames.\n'
                                       'Exemplo: 159732', title='Digite Sua Senha.', default='', mask='')

    if len(password) >= 7 or len(password) < 6 or password.isalpha() or password.islower() or password.istitle():
        pyautogui.alert(text=f'Você digitou algo que não é válido!', title='SENHA!',
                        button='Tente novamente!')
        import sys
        import os
        python = sys.executable
        os.execl(python, python, *sys.argv)

    confirma = pyautogui.confirm(text='Confira agora seus dados... \n'
                                      f'Senha: {password}', title='CONFIRA SEUS DADOS!',
                                 buttons=['ESTÁ TUDO CERTO!', 'PRECISO ALTERAR...'])
    if confirma == 'PRECISO ALTERAR...':
        import sys
        import os
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        return password


passw = passwd()

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.maximize_window()
chrome.get('https://tmlablaudos.cientificalab.com.br/laudos/#')
chrome.find_element(By.XPATH, '//*[@id="ztmFormLogin"]/div/button/span[1]').click()
chrome.find_element(By.XPATH, '//*[@id="ztmFormLogin"]/div/div/ul/li[2]/a/span[2]').click()
chrome.find_element(By.XPATH, '//*[@id="ztmLogin"]').send_keys(nrequest)
chrome.find_element(By.XPATH, '//*[@id="ztmSenha"]').send_keys(passw)
chrome.find_element(By.XPATH, '//*[@id="ztmEntrar"]').click()

sleep(1)
chrome.find_element(By.XPATH, '//*[@id="accordion"]/div/div[1]/div[1]/div').click()
sleep(6)

download_exames = pyautogui.confirm(text='Você gostaria de baixar o(s) exame(s)?',
                                    title='Baixar?',
                                    buttons=['Sim', 'Não'])

if download_exames == 'Sim':
    pyautogui.alert(text='ATENÇÃO: NÃO UTILIZE SEU TECLADO, ATÉ QUE O PRÓXIMO AVISO SEJA MOSTRADO!',
                    title='ALERTA!',
                    button='TUDO BEM...')

    chrome.find_element(By.XPATH, '//*[@id="btnImprimeReq"]/span').click()
    chrome.maximize_window()
    sleep(12)

    pyautogui.hotkey('ctrl', 's')
    sleep(5)
    pyautogui.hotkey('backspace')
    pyautogui.alert(text=f'Meu trabalho acaba por aqui, você pode baixar o arquivo, com o nome que desejar e '
                         f'no local que desejar também!\n\n'
                         f'LEMBRE-SE DE COLOCAR O .pdf NO FINAL DO NOME DO ARQUIVO 😉',
                    title='MEU TRABALHO ACABOU',
                    button='Tudo bem, vou escolher um local e um nome para o arquivo...')
else:
    pyautogui.alert(text=f'Meu trabalho acaba por aqui, você pode ver o(s) exame(s), ou baixar manualmente...!',
                    title='MEU TRABALHO POR AQUI ACABOU!',
                    button='OK...')