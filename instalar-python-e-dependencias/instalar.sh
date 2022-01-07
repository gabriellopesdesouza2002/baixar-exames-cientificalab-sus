#!/bin/bash

tput setaf 3; echo 'Esse é o assistente de instalação para Python3, Selenium e Pyautogui'
echo
echo 'Limpando a tela...'
sleep 2  # Espera 2 segundos
clear

tput setaf 2; echo 'Verificando atualizações'
echo
sudo apt update && sudo apt upgrade -y
echo
echo 'Limpando a tela...'
sleep 2  # Espera 2 segundos
clear

tput setaf 2; echo 'Fazendo configurações para Python 3'
echo
sudo apt install curl git python3 python3-dev python3-venv idle-python3.8 python3-pip virtualenv gcc default-libmysqlclient-dev libssl-dev -y
sleep 2  # Espera 2 segundos
echo
echo 'Limpando a tela...'
sleep 2  # Espera 2 segundos
clear

tput setaf 2; echo 'Fazendo configurações para Selenium, Pyautogui e webdriver-manager'
sleep 2  # Espera 2 segundos
echo
sudo pip install selenium && pip install pyautogui && pip install webdriver-manager
sleep 2  # Espera 2 segundos
echo
echo 'Limpando a tela...'
sleep 2  # Espera 2 segundos
clear

tput setaf 2; echo 'Você gostaria de instalar o Google Chrome?  [s | n]'
echo
echo "Caso a resposta seja negativa, e você NÃO TIVER O CHROME INSTALADO o bot pode NÃO funcionar..."

read install_chrome

# shellcheck disable=SC2109
if [ $install_chrome == 's' ] ;
then    echo
        tput setaf 1; echo 'INSTALADO O GOOGLE CHROME'
        sleep 3  # Espera 3 segundos
        sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo apt install ./google-chrome-stable_current_amd64.deb
else    echo
        tput setaf 3; echo 'SE NÃO HOUVER O CHROME INSTALADO O BOT PODE NÃO FUNCIONAR...'
        read
fi