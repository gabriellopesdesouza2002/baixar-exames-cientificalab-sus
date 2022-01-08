import pyautogui
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import data


def req():
    request = pyautogui.prompt(text='Coloque o número da requisição:\n\n'
                                    'É parecido como esse -> 1234567890', title='Número da Requisição...',
                               default=data.default_request)

    if len(request) >= 11 or len(request) < 10 or request.isalpha() or request.islower() or request.istitle():
        pyautogui.alert(text=f'Você digitou algo que não é válido!', title='NÚMERO DA REQUISIÇÃO!',
                        button='Tente novamente!')
        import sys
        import os
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        confirma = pyautogui.confirm(text='Confira agora seus dados...\n'
                                          f'Número da requisição: {request}',
                                     title='CONFIRA SEUS DADOS!',
                                     buttons=['ESTÁ TUDO CERTO!', 'PRECISO ALTERAR...'])

        if confirma == 'PRECISO ALTERAR...':
            import sys
            import os
            python = sys.executable
            os.execl(python, python, *sys.argv)
        elif confirma == 'ESTÁ TUDO CERTO!':
            return request


request = req()


def passwd():
    password = pyautogui.password(text='Digite a senha do para acessar os resultados de exames.\n'
                                       'Exemplo: 123456', title='Senha', default=data.default_password, mask='')

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

chrome = webdriver.Chrome(ChromeDriverManager().install())  # Define o driver como o Chrome
chrome.maximize_window()  # Maximiza a janela do Navegador
chrome.get('https://tmlablaudos.cientificalab.com.br/laudos/#')  # Vai para o site de Login da CientíficaLab
chrome.find_element_by_xpath('//*[@id="ztmFormLogin"]/div/button/span[1]').click()  # Clica no button "Consultas"
chrome.find_element_by_xpath('//*[@id="ztmFormLogin"]/div/div/ul/li[2]/a/span[2]').click()  # Define o button como "Paciente"
chrome.find_element_by_xpath('//*[@id="ztmLogin"]').send_keys(request)  # Envia o Número da Requisição
chrome.find_element_by_xpath('//*[@id="ztmSenha"]').send_keys(passw)  # Envia a Senha da Requisição
chrome.find_element_by_xpath('//*[@id="ztmEntrar"]').click()  # Clica no button "Ok"

sleep(3)
chrome.find_element_by_xpath('//*[@id="accordion"]/div/div[1]/div[1]/div').click()  # Clica na div "Ver Laudo"
sleep(6)

download_exames = pyautogui.confirm(text='Você gostaria de baixar o(s) exame(s)?', title='Baixar?',
                                    buttons=['Sim', 'Não'])

if download_exames == 'Sim':
    pyautogui.alert(text='ATENÇÃO: NÃO UTILIZE SEU TECLADO, ATÉ QUE O DOWNLOAD SEJÁ CONCLUIDO!', title='ALERTA!',
                    button='TUDO BEM...')
    chrome.find_element_by_xpath('//*[@id="btnImprimeReq"]/span').click()  # Clica no botáo "Imprimir"
    sleep(10)

    pyautogui.hotkey('ctrl', 's')
    sleep(5)
    pyautogui.alert(text=f'Meu trabalho acaba por aqui, você pode baixar o arquivo, com o nome que desejar e '
                         f'no local que desejar também!',
                    title='MEU TRABALHO ACABOU',
                    button='Tudo bem, vou escolher um local e um nome para o arquivo...')
else:
    pyautogui.alert(text=f'Meu trabalho acaba por aqui, você pode ver o(s) exame(s), ou baixar manualmente...!',
                    title='MEU TRABALHO POR AQUI ACABOU!',
                    button='OK...')