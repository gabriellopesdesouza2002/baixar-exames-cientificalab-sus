import platform

# Verificação se o sistema operacional é 32 ou 64 bits
arquitetura = platform.machine()  # Arquitetura do OS

'''
Caso o sistema operacional seja 64 bits, o bot seguirá normalmente.
Caso seja 32 bits, o bot mostrará uma mensagem.

Se o sistema é 64 bits, executará com o navegador do Chrome, mas se 32 bits, utiliza o Firefox
'''

if '64' in arquitetura:
    import pyautogui  # Automação de GUI
    from selenium import webdriver  # Automação de testes de sistemas
    from selenium.webdriver.common.by import By
    from time import sleep
    from webdriver_manager.chrome import ChromeDriverManager  # Verifica a versão atual do webdriver (Chrome)

    try:
        def req():
            try:
                nrequest = pyautogui.prompt(text='Coloque o número da requisição:\n\n'
                                                 'Exemplo: 5784235481', title='Digite o Número da Requisição.',
                                            default='')

                if len(nrequest) >= 11 or len(nrequest) < 10 or nrequest.isalpha() or nrequest.islower() or nrequest.istitle():
                    pyautogui.alert(text=f'Você digitou algo inválido!\n'
                                         f'O que você digitou: {nrequest}\n\n'
                                         f'O sistema será reiniciado para que seus dados não sejam salvos.',
                                    title='SENHA!',
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
                        pyautogui.alert(text='Por sua segurança, o sistema será reiniciado. Para não salvar suas informações.',
                                        title='Reiniciando a aplicação', button='Reinicie')

                        # Reinicia a aplicação
                        import sys
                        import os
                        python = sys.executable
                        os.execl(python, python, *sys.argv)
                    elif confirma == 'ESTÁ TUDO CERTO!':
                        return nrequest
            except TypeError:  # Caso o user clique em "Cancel", retornará None e vai parar o aplicativo.
                pyautogui.alert(text='Finalizando a aplicação... ', title='Finalizando a aplicação', button='OK')
                exit()
            except Exception as description:
                pyautogui.alert(text='Algo deu errado...\n'
                                     f'Mostre isso ao Desenvolvedor: {description}',
                                title='Erro inesperado!',
                                button='Sair')


        nrequest = req()


        def passwd():
            try:
                password = pyautogui.password(text='Digite a senha do para acessar os resultados de exames.\n'
                                                   'Exemplo: 159732',
                                              title='Digite Sua Senha.',
                                              default='', mask='')

                if len(password) >= 13 or len(password) < 4 or password.isalpha() or password.islower() or password.istitle():
                    pyautogui.alert(text=f'Você digitou algo inválido!\n'
                                         f'O que você digitou: {password}\n\n'
                                         f'O sistema será reiniciado para que seus dados não sejam salvos.',
                                    title='SENHA!',
                                    button='Tente novamente!')
                    import sys
                    import os
                    python = sys.executable
                    os.execl(python, python, *sys.argv)

                confirma = pyautogui.confirm(text=f'Confira agora seus dados... \n'
                                                  f'A senha que você digitou, tem {len(password)} caracteres.\n\n'
                                                  f'Senha: {password}', title='CONFIRA SEUS DADOS!',
                                             buttons=['ESTÁ TUDO CERTO!', 'PRECISO ALTERAR...'])
                if confirma == 'PRECISO ALTERAR...':
                    pyautogui.alert(text='Por sua segurança, o sistema será reiniciado. Para não salvar suas informações.',
                                    title='Reiniciando a aplicação', button='Reinicie')

                    # Reinicia a aplicação
                    import sys
                    import os
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                else:
                    return password
            except TypeError:
                pyautogui.alert(text='Finalizando a aplicação...', title='Finalizando a aplicação', button='OK')
                exit()
            except Exception as description:
                pyautogui.alert(text='Algo deu errado...\n'
                                     f'Mostre isso ao Desenvolvedor: {description}',
                                title='Erro inesperado!',
                                button='Sair')


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
    except Exception:
        pyautogui.alert(
            text=f'Ocorreu um erro inesperado!\n\n'
                 f'Veja se você não colocou nenhum dado incorreto.\n'
                 f'Tente novamente, se o erro persistir, entre em contato com o Desenvolvedor.',
            title='Erro Crítico',
            button='Tente novamente mais tarde.')
        quit()
        exit()
else:  # Se o sistema operacional for de 32 bits, executa esse bloco else.
    import pyautogui  # Automação de GUI
    from selenium.webdriver.common.by import By
    from time import sleep
    from selenium import webdriver  # Automação de testes de sistemas
    from webdriver_manager.firefox import GeckoDriverManager  # Verifica a versão atual do webdriver (Chrome)

    try:
        def req():
            try:
                nrequest = pyautogui.prompt(text='Coloque o número da requisição:\n\n'
                                                 'Exemplo: 5784235481', title='Digite o Número da Requisição.',
                                            default='')

                if len(nrequest) >= 11 or len(nrequest) < 10 or nrequest.isalpha() or nrequest.islower() or nrequest.istitle():
                    pyautogui.alert(text=f'Você digitou algo inválido!\n'
                                         f'O que você digitou: {nrequest}\n\n'
                                         f'O sistema será reiniciado para que seus dados não sejam salvos.',
                                    title='SENHA!',
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
                        pyautogui.alert(text='Por sua segurança, o sistema será reiniciado. Para não salvar suas informações.',
                                        title='Reiniciando a aplicação', button='Reinicie')

                        # Reinicia a aplicação
                        import sys
                        import os
                        python = sys.executable
                        os.execl(python, python, *sys.argv)
                    elif confirma == 'ESTÁ TUDO CERTO!':
                        return nrequest
            except TypeError:  # Caso o user clique em "Cancel", retornará None e vai parar o aplicativo.
                pyautogui.alert(text='Finalizando a aplicação... ', title='Finalizando a aplicação', button='OK')
                exit()
            except Exception as description:
                pyautogui.alert(text='Algo deu errado...\n'
                                     f'Mostre isso ao Desenvolvedor: {description}',
                                title='Erro inesperado!',
                                button='Sair')


        nrequest = req()


        def passwd():
            try:
                password = pyautogui.password(text='Digite a senha do para acessar os resultados de exames.\n'
                                                   'Exemplo: 159732',
                                              title='Digite Sua Senha.',
                                              default='', mask='')

                if len(password) >= 13 or len(password) < 4 or password.isalpha() or password.islower() or password.istitle():
                    pyautogui.alert(text=f'Você digitou algo inválido!\n'
                                         f'O que você digitou: {password}\n\n'
                                         f'O sistema será reiniciado para que seus dados não sejam salvos.',
                                    title='SENHA!',
                                    button='Tente novamente!')
                    import sys
                    import os
                    python = sys.executable
                    os.execl(python, python, *sys.argv)

                confirma = pyautogui.confirm(text=f'Confira agora seus dados... \n'
                                                  f'A senha que você digitou, tem {len(password)} caracteres.\n\n'
                                                  f'Senha: {password}', title='CONFIRA SEUS DADOS!',
                                             buttons=['ESTÁ TUDO CERTO!', 'PRECISO ALTERAR...'])
                if confirma == 'PRECISO ALTERAR...':
                    pyautogui.alert(text='Por sua segurança, o sistema será reiniciado. Para não salvar suas informações.',
                                    title='Reiniciando a aplicação', button='Reinicie')

                    # Reinicia a aplicação
                    import sys
                    import os
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                else:
                    return password
            except TypeError:
                pyautogui.alert(text='Finalizando a aplicação...', title='Finalizando a aplicação', button='OK')
                exit()
            except Exception as description:
                pyautogui.alert(text='Algo deu errado...\n'
                                     f'Mostre isso ao Desenvolvedor: {description}',
                                title='Erro inesperado!',
                                button='Sair')


        passw = passwd()

        firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        firefox.maximize_window()
        firefox.get('https://tmlablaudos.cientificalab.com.br/laudos/#')
        firefox.find_element(By.XPATH, '//*[@id="ztmFormLogin"]/div/button/span[1]').click()
        firefox.find_element(By.XPATH, '//*[@id="ztmFormLogin"]/div/div/ul/li[2]/a/span[2]').click()
        firefox.find_element(By.XPATH, '//*[@id="ztmLogin"]').send_keys(nrequest)
        firefox.find_element(By.XPATH, '//*[@id="ztmSenha"]').send_keys(passw)
        firefox.find_element(By.XPATH, '//*[@id="ztmEntrar"]').click()

        sleep(1)
        firefox.find_element(By.XPATH, '//*[@id="accordion"]/div/div[1]/div[1]/div').click()
        sleep(6)

        download_exames = pyautogui.confirm(text='Você gostaria de baixar o(s) exame(s)?',
                                            title='Baixar?',
                                            buttons=['Sim', 'Não'])

        if download_exames == 'Sim':
            pyautogui.alert(text='ATENÇÃO: NÃO UTILIZE SEU TECLADO, ATÉ QUE O PRÓXIMO AVISO SEJA MOSTRADO!',
                            title='ALERTA!',
                            button='TUDO BEM...')

            firefox.find_element(By.XPATH, '//*[@id="btnImprimeReq"]/span').click()
            firefox.maximize_window()
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
    except Exception as description:
        pyautogui.alert(text=f'Ocorreu um erro inesperado!\n\n '
                             f'Veja se você não colocou nenhum dado incorreto.\n '
                             f'Se o erro persistir, mostre a descrição da exceção para o Desenvolvedor. '
                             f'\n\n Descrição da exceção: {description}\n\n '
                             f'O navegador ficará aberto para que você possa fazer o que quiser...',
                        title='Erro Crítico',
                        button='OK')
        exit()