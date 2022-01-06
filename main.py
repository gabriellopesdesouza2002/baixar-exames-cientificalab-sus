# Atualmente só funciona no Chrome na versáo 96#
# executar as coisas do selenium dentro da funcao, mas um while true...#
import pyautogui
from selenium import webdriver
from time import sleep


def req():
    request = pyautogui.prompt(text='Coloque o número da requisição:\n\n'
                                    'É parecido como esse -> 1234567890', title='Número da Requisição...',
                               default='')

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
                                       'Exemplo: 123456', title='Senha', default='', mask='')

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

chrome = webdriver.Chrome('chromedriver')  # Seta o chrome como o chromedriver
chrome.get('https://tmlablaudos.cientificalab.com.br/laudos/#')  # vai para o site da cientificalab
chrome.find_element_by_xpath('//*[@id="ztmFormLogin"]/div/button/span[1]').click()
chrome.find_element_by_xpath('//*[@id="ztmFormLogin"]/div/div/ul/li[2]/a/span[2]').click()
chrome.find_element_by_xpath('//*[@id="ztmLogin"]').send_keys(request)
chrome.find_element_by_xpath('//*[@id="ztmSenha"]').send_keys(passw)
chrome.find_element_by_xpath('//*[@id="ztmEntrar"]').click()




sleep(1)
chrome.find_element_by_xpath('//*[@id="accordion"]/div/div[1]/div[1]/div').click()
sleep(5)

download_exames = pyautogui.confirm(text='Você gostaria de baixar o(s) exame(s)?', title='Baixar?',
                                    buttons=['Sim', 'Não'])

if download_exames == 'Sim':
    pyautogui.alert(text='ATENÇÃO: NÃO UTILIZE SEU TECLADO, ATÉ QUE O DOWNLOAD SEJÁ CONCLUIDO!', title='ALERTA!',
                    button='TUDO BEM...')
    chrome.find_element_by_xpath('//*[@id="btnImprimeReq"]/span').click()
    sleep(10)

    cont = 1
    while cont <= 8:
        pyautogui.hotkey('tab')
        cont += 1
    else:
        pyautogui.press('space')
        sleep(5)
        pyautogui.write('Exames.pdf')
        pyautogui.press('enter')
