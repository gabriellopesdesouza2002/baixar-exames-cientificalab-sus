#!/bin/bash

echo 'Esse é o assistente de instalação para fazer o bot Científicalab funcionar corretamente'
echo
echo 'Limpando a tela...'
sleep 2  # Espera 2 segundos
clear

echo 'Verificando se o Sistema é 32 ou 64 bits.'

arquitetura=$(uname -m)

if [ $arquitetura == 'x86_64' ] ;
then    echo
	echo '--------------------------------------------------------------------------------'
        echo '|    A sua arquitetura é 64 bits. Por isso, o processo seguirá normalmente!    |'
        echo '--------------------------------------------------------------------------------'
        echo
        echo 'Verificando atualizações...'
        echo
        sudo apt update && sudo apt upgrade && sudo apt autoremove -y
        echo
        echo 'Limpando a tela...'
        sleep 2  # Espera 2 segundos
        clear

        echo 'Fazendo configurações...'
        echo
        sudo apt install git wget python3 python python3-dev python-dev python3-tk python-tk python3-pip python-pip -y
        sleep 2  # Espera 2 segundos
        echo
        echo 'Limpando a tela...'
        sleep 2  # Espera 2 segundos
        clear

        echo 'Fazendo configurações para Selenium, Pyautogui e Webdriver Manager'
        sleep 2  # Espera 2 segundos
        echo
        sudo pip3 install selenium pyautogui webdriver-manager
        sleep 2  # Espera 2 segundos
        sudo pip3 install --upgrade requests
        sleep 2  # Espera 2 segundos
	sudo pip3 install --upgrade setuptools
        echo
        echo 'Limpando a tela...'
        sleep 2  # Espera 2 segundos
        clear

        echo 'Você gostaria de instalar o Google Chrome?  [s | n]'
        echo
        echo "Caso a resposta seja negativa, e você NÃO TIVER O CHROME INSTALADO o bot pode NÃO funcionar..."
        echo
        read install_chrome

        if [ $install_chrome == 's' ] || [ $install_chrome == 'S' ] || [ $install_chrome == 'SIM' ] || [ $install_chrome == 'sim' ] || [ $install_chrome == 'y' ] || [ $install_chrome == 'Y' ] || [ $install_chrome == '' ] ;
        then    echo
                echo 'INSTALADO O GOOGLE CHROME'
                sleep 3  # Espera 3 segundos
                sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                sudo apt install ./google-chrome-stable_current_amd64.deb
        else    echo
                echo 'SE NÃO HOUVER O CHROME INSTALADO O BOT PODE NÃO FUNCIONAR...'
                exit
        fi
else    echo
	echo '----------------------------------------'
        echo '|     A sua arquitetura é 32 bits.     |'
        echo '----------------------------------------'
        echo
        echo 'Fazendo configurações referentes ao seu sistema operacional.'
        echo
        echo 'Verificando atualizações...'
        echo
        sudo apt update && sudo apt upgrade && sudo apt autoremove -y
        echo
        echo 'Limpando a tela...'
        sleep 2  # Espera 2 segundos
        clear

        echo 'Fazendo configurações...'
        echo
        sudo apt install git wget python3 python3-dev python3-tk python3-pip -y
        sleep 2  # Espera 2 segundos
        echo
        echo 'Limpando a tela...'
        sleep 2  # Espera 2 segundos
        clear

        echo 'Fazendo configurações para Selenium, Pyautogui e webdriver-manager'
        sleep 2  # Espera 2 segundos
        echo
        sudo pip3 install selenium pyautogui webdriver-manager
        sleep 2  # Espera 2 segundos
        sudo pip3 install --upgrade requests
        sleep 2  # Espera 2 segundos
	sudo pip3 install --upgrade setuptools
        echo
        echo 'Limpando a tela...'
        sleep 2  # Espera 2 segundos
        clear

        echo 'Você gostaria de instalar ou verificar atualizações do Mozila Firefox?  [s | n]'
        echo
        echo "Caso a resposta seja negativa, e você NÃO TIVER O FIREFOX INSTALADO o bot pode NÃO funcionar..."
        echo
        read install_firefox

        if [ $install_firefox == 's' ] || [ $install_firefox == 'S' ] || [ $install_firefox == 'SIM' ] || [ $install_firefox == 'sim' ] || [ $install_firefox == 'y' ] || [ $install_firefox == 'Y' ] || [ $install_firefox == '' ] ;
        then    echo
                echo 'INSTALADO O MOZILA FIREFOX'
                sleep 3  # Espera 3 segundos
                sudo apt-get install firefox firefox-locale-pt


        else    echo
                echo 'SE NÃO HOUVER O CHROME INSTALADO O BOT PODE NÃO FUNCIONAR...'
                exit
        fi

        # Add instalação e atualização do Firefox
fi
