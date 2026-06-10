import pyautogui
import time
pyautogui.PAUSE = 2

#PASSO A PASSO PARA AUTOMAÇÃO:
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
#Passo 1: Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(6)
pyautogui.press('Tab')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write(link)
pyautogui.press('enter')

#Passo 2: Fazer login no sistema
pyautogui.click(x=-1450, y=106) #Clica no campo de email
pyautogui.write('nome@gmail.com')
pyautogui.press('Tab')
pyautogui.write('senha1234')
pyautogui.press('enter') 
time.sleep(3)

#Passo 3: Abrir base de dados
import pandas as pd
tabela = pd.read_csv('Jornada python/bot/produtos.csv') #Lê a base de dados

#Passo 4: Cadastrar produtos
for linha in tabela.index:
    pyautogui.click(x=-1411, y=-34) #Clica no botão de novo produto
    código = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(código)
    pyautogui.press('Tab')

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press("Tab")

    tipo_produto = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo_produto)
    pyautogui.press("Tab")

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press("Tab")

    preço = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preço)
    pyautogui.press("Tab")

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press("Tab")

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press("Tab")
    pyautogui.press("enter") #Salva o produto

    pyautogui.scroll(5000) #Rola para o incinio da página 




