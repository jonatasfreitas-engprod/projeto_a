# VARIÁVEIS

var_Sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
var_Login = "jonatasfreitas.engprod@gmail.com"
var_Senha = "minhasenha"

# BIBLIOTECAS UTILIZADAS NO PROJETO
    #pyautogui
    #pandas numpy openpyxl

# AUTOMAÇÃO

import time
import pyautogui as atg

atg.press("win")
atg.write("edge")
atg.press("enter")

time.sleep(2)

atg.press("f4")
atg.write(var_Sistema)
atg.press("enter")

time.sleep(2)

atg.press("tab")
atg.write(var_Login)
atg.press("tab")
atg.write(var_Senha)
atg.press("enter")

time.sleep(2)

atg.press("tab")

import pandas as pd

tabela_produtos = pd.read_csv("G:\Meu Drive\Cursos\Python\Aula 01\produtos.csv")

print(tabela_produtos)

for linha  in tabela_produtos.index:
     
    atg.click(x=669, y=307)
    atg.write(str(tabela_produtos.loc[linha,"codigo"]))
    atg.press("tab")
    atg.write(str(tabela_produtos.loc[linha,"marca"]))
    atg.press("tab")
    atg.write(str(tabela_produtos.loc[linha,"tipo"]))
    atg.press("tab")
    atg.write(str(tabela_produtos.loc[linha,"categoria"]))
    atg.press("tab")
    atg.write(str(tabela_produtos.loc[linha,"preco_unitario"]))
    atg.press("tab")
    atg.write(str(tabela_produtos.loc[linha,"custo"]))
    atg.press("tab")
    obs = str(tabela_produtos.loc[linha,"obs"])
    if obs != "nan":
        atg.write(str(tabela_produtos.loc[linha,"obs"]))
    atg.press("tab")
    atg.press("enter")
    time.sleep(2)
    atg.scroll(5000)
    time.sleep(2)   
    