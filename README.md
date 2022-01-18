
# Acesse seu(s) exame(s) do SUS (Sistema Único de Saúde) no site da [CientíficaLab](https://cientificalab.com.br/) ®.  
  
### **Com esse “bot”, você pode acessar, ver e baixar os seus exames rapidamente.**  
  
## Como foi feito esse robô?  
Esse robô foi feito com Python na versão 3.8 e as suas bibliotecas:
- Pyautogui
- Selenium
- Webdriver Manager
  
> O "bot" irá acessar ao site da [CientíficaLab](https://cientificalab.com.br/) ®, entrará com o número da requisição
> e a senha, e perguntará se você quer baixar os exames ou simplesmente ver os mesmos. 
> 
> O número da requisição e a senha foi entregue pelo enfermeiro(a), médico(a) ou Aux. de Enfermagem
> na hora em que você fez o exame.

## Requisitos para usar o robô...  
1 – Utilizar Linux.

2 – Ter instalado na máquina o **Python na versão 3.8, Selenium, Pyautogui e Webdriver Manager** 

 - (**Tudo será instalado por um 
assistente, para lhe ajudar!**)  
 

> - Se o seu sistema for de **64 bits**, é necessário ter o **Google Chrome** instalado.
>
> - Se o seu sistema for de **32 bits**, é necessário ter o **Mozila Firefox** instalado.
> 
> **De qualquer forma, o assistente identificará e se necessário instalará.**
  
5 – Protocolo de retirada de exames, que contém o ***Número da Requisição*** e a ***Senha***.

---  
  
> Atualmente o robô foi feito para utilizar no Linux Mint como Sistema operativo.
> 
> Você pode tentar utilizar o robô em outras distribuições, que são baseadas no Ubuntu.
> 
> Posteriormente, irei desenvolver estas soluções para as demais distribuições Linux e quem sabe, 
> até para o Windows...
> 
> Distribuições Linux testadas até o momento:
> 
> - Linux Mint 64 bits e 32 bits (19).
> - Linux Lite 64 bits (5.4).
  
---

# Instalação e configuração, para utilizar o bot.
> Essa configuração só será necessária fazer uma vez!
### Antes de tudo verifique se existem atualizações no *Gerenciador de Atualizações*  
---

![verifica_atualizacoes](https://user-images.githubusercontent.com/65515076/148704585-143a80c5-dbd5-481e-a561-5f3665378694.gif)  
  
  
  
---  
 - Abra o *Terminal* (Ctrl + Alt + T)  
  
![abrir_terminal](https://user-images.githubusercontent.com/65515076/148704248-26ac5689-a0ef-450d-9052-bed30a15283b.gif)  
  
---  
- Instale o *Git* (para poder clonar este repositório).  
  
       sudo apt-get install git -y  
  
![install git](https://user-images.githubusercontent.com/65515076/148704613-9a5a3379-6ef7-4254-85fe-e6b85342d871.gif)  
  
---  
  
- Vá para uma pasta da sua preferência (eu utilizarei a pasta Documentos):  
  
      cd Documentos  
  
![fui_para_documentos](https://user-images.githubusercontent.com/65515076/148705513-3f49f222-3fa7-42a8-b27e-fb6f822ded16.gif)  
  
---  
  
- Faça o clone (baixe) deste repositório.  
  
      git clone https://github.com/gabriellopesdesouza2002/baixar-exames-cientificalab-sus.git  
  
  
![clone_repositorio](https://user-images.githubusercontent.com/65515076/148705543-3d61a20d-e069-478c-bcbb-471ef8af024e.gif)  
  
---  
  
 - Vá para a pasta ***baixar-exames-cientificalab-sus*** e depois para a pasta: ***instalar-python-e-dependencias*** mude as permissões com `chmod` e inicie o assistente de configuração.  
  
 1. Ir para a pasta: `cd baixar-exames-cientificalab-sus`  
 2. Ir para a pasta: `cd instalar-python-e-dependencias`  
 3. Alterar permissões: `chmod +x instalar.sh`  
 4. Iniciar o assistente de configuração: `./instalar.sh`  
  
> Abaixo mostra também como funcionará o assistente de configuração.  
  
![iniciar assistente](https://user-images.githubusercontent.com/65515076/148705816-3ba8fa8b-ca07-4f6d-af64-3233715c5fcc.gif)  
  
---  
  

 - ### Após a finalização do assistente acima, inicie o robô:  
Agora, devemos ir para a pasta raiz do "bot", na qual é **`baixar-exames-cientificalab-sus`** e iniciar o robô.  
  
Ir para a pasta raiz: 

		cd ..  
  
![ir para a pasta raiz](https://user-images.githubusercontent.com/65515076/149239063-4a528b2e-33e1-4b8a-b6ab-0f17277b1590.gif)

## Finalmente, execute o Robô:  
  
		python3 main.py  

![inicia_bot](https://user-images.githubusercontent.com/65515076/149240609-a95997cb-7efd-4c33-9df5-e8204fb043c3.gif)



>  ## Atenção  
> Qualquer erro ocorrido, por favor, entre em contato. Resolveremos juntos!  
> ;-)

Existe uma versão inicial para Windows, porém, pode não funcionar corretamente...
---
Ensina-me a fazer a tua vontade, pois tu és o meu Deus; 
que o teu bondoso Espírito me conduza por terreno plano.

Salmos 143:10

---