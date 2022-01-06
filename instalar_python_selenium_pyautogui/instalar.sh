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

tput setaf 2; echo 'Fazendo configurações para Selenium e Pyautogui'
sleep 2  # Espera 2 segundos
echo