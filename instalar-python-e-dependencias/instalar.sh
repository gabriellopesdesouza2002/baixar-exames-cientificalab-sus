#!/bin/bash

echo 'Esse é o assistente de instalação para fazer o bot Científicalab funcionar corretamente'
echo
echo 'Limpando a tela...'
sleep 2  # Espera 2 segundos
clear

echo 'Verificando se o Sistema é 32 ou 64 bits.'

sleep 2  # Espera 2 segundos

arquitetura=$(uname -m)

if [ $arquitetura == 'x86_64' ] ;
then
  echo
	echo '--------------------------------------'
  echo '|    A sua arquitetura é 64 bits.    |'
  echo '--------------------------------------'
  echo
  echo 'Verificando atualizações...'
  echo
  ## Removendo travas eventuais do apt ##
  sudo rm /var/lib/dpkg/lock-frontend
  sudo rm /var/cache/apt/archives/lock
  ## Removendo travas eventuais do apt ##

  sudo apt update && sudo apt upgrade && sudo apt dist-upgrade && sudo apt autoremove  -y
  echo
  echo 'Limpando a tela...'
  sleep 2  # Espera 2 segundos
  clear

  echo '---------------------------------------------------------'
  echo '|  Instalando pacotes para o funcionamento do "bot"...  |'
  echo '---------------------------------------------------------'
  echo
  sleep 2  # Espera 2 segundos
  sudo apt install git -y
  sudo apt install wget -y
  sudo apt install python3 -y
  sudo apt install python3-dev -y
  sudo apt install python3-tk -y
  sudo apt install python3-pip -y
  sleep 2  # Espera 2 segundos
  echo
  echo 'Limpando a tela...'
  sleep 2  # Espera 2 segundos
  clear

  echo '-------------------------------------------------------------------------'
  echo '|  Fazendo configurações para Selenium, Pyautogui e Webdriver Manager   |'
  echo '-------------------------------------------------------------------------'
  sleep 2  # Espera 2 segundos
  echo
  sudo pip3 install selenium
  sudo pip3 install pyautogui
  sudo pip3 install webdriver-manager
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

        if [ $install_chrome == 's' ] ; then
          echo
          echo 'INSTALADO O GOOGLE CHROME'
          sleep 3  # Espera 3 segundos
          sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb -y
        elif [ $install_chrome == 'S' ]; then
          echo
          echo 'INSTALADO O GOOGLE CHROME'
          sleep 3  # Espera 3 segundos
          sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb -y
        elif [ $install_chrome == 'SIM' ]; then
          echo
          echo 'INSTALADO O GOOGLE CHROME'
          sleep 3  # Espera 3 segundos
          sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb -y
        elif [ $install_chrome == 'sim' ]; then
          echo
          echo 'INSTALADO O GOOGLE CHROME'
          sleep 3  # Espera 3 segundos
          sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb -y
        elif [ $install_chrome == 'y' ]; then
          echo
          echo 'INSTALADO O GOOGLE CHROME'
          sleep 3  # Espera 3 segundos
          sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb -y
        elif [ $install_chrome == 'Y' ]; then
          echo
          echo 'INSTALADO O GOOGLE CHROME'
          sleep 3  # Espera 3 segundos
          sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb -y
        elif [ $install_chrome == '' ]; then
          echo
          echo 'INSTALADO O GOOGLE CHROME'
          sleep 3  # Espera 3 segundos
          sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb -y
        else
          echo
          echo 'SE NÃO HOUVER O CHROME INSTALADO O BOT PODE NÃO FUNCIONAR...'
          exit
        fi
else
  echo
  echo '----------------------------------------'
  echo '|     A sua arquitetura é 32 bits.     |'
  echo '----------------------------------------'
  echo
  echo 'Fazendo configurações referentes ao seu sistema operacional.'
  echo
  echo 'Verificando atualizações...'
  echo
  ## Removendo travas eventuais do apt ##
  sudo rm /var/lib/dpkg/lock-frontend
  sudo rm /var/cache/apt/archives/lock
  ## Removendo travas eventuais do apt ##
  sudo apt update && sudo apt upgrade && sudo apt autoremove -y
  echo
  echo 'Limpando a tela...'
  sleep 2  # Espera 2 segundos
  clear

  echo 'Fazendo configurações...'
  echo
  sudo apt install git -y
  sudo apt install wget -y
  sudo apt install python3 -y
  sudo apt install python3-dev -y
  sudo apt install python3-tk -y
  sudo apt install python3-pip -y
  sleep 2  # Espera 2 segundos
  echo
  echo 'Limpando a tela...'
  sleep 2  # Espera 2 segundos
  clear

  echo 'Fazendo configurações para Selenium, Pyautogui e webdriver-manager'
  sleep 2  # Espera 2 segundos
  echo
  sudo pip3 install selenium
  sudo pip3 install pyautogui
  sudo pip3 install webdriver-manager
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
        then
          echo
          echo 'INSTALADO O MOZILA FIREFOX'
          sleep 3  # Espera 3 segundos
          sudo apt-get install firefox firefox-locale-pt -y
        else
          echo
          echo 'SE NÃO HOUVER O MOZILA INSTALADO O BOT PODE NÃO FUNCIONAR...'
          exit
        fi
fi
