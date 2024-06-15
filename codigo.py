# Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui as py
import time

#py.click → clicar em algum lugar da tela
#py.write('alguma coisa ') → escrever um texto
#py.press('enter') → pressionar 1 tecla do teclado
#py.hotkey('ctrl', 'v') → pressionar uma combinação de teclaschrome

#tempo entre cada ação do pyautogui
py.PAUSE = 2


    # Abrir o navegador
py.press('win')
py.write('chrome')
py.press('enter')
time.sleep(2)

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
py.write(link)
py.press('enter')
time.sleep(5)


    # Fazer login
py.press('tab')
py.write('rafasolmainieri@gmail.com')
py.press('tab')
py.write('123')
py.press('enter')
time.sleep(2)


    # Importar base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv')
print(tabela)


    # Cadastrar um produto

for linha in tabela.index:
    #selecionar 1º campo
    py.press('tab')

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    py.write(codigo)
    py.press('tab')

    #marca
    py.write(tabela.loc[linha, "marca"])
    py.press('tab')

    #tipo
    py.write(tabela.loc[linha, "tipo"])
    py.press('tab')
    
    #categoria
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press('tab')
    
    #preco
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press('tab')

    #custo
    py.write(str(tabela.loc[linha, "custo"]))
    py.press('tab')

    #obs
    obs = tabela.loc[linha, "obs"]
    if pd.isna(obs):
        py.press('tab')
    else:
        py.write(obs)

    #cadastrar e voltar pro inicio da página
    py.press('enter')
    py.scroll(5000)
    py.click(x=214, y=231)   
