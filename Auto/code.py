# pip install pyautogui
# pip install pandas openpyxl numpy

import pyautogui
import time

# pyautogui.click - click
# pyautogui.write - write
# pyautogui.press - press one bind
# pyautogui.hotkey - more one bind
# pyautogui.scroll - scroll the screen

pyautogui.PAUSE = 0.5

# Enter
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# Login
pyautogui.click(x=674, y=460)
pyautogui.write("marco@hotmail.com")
pyautogui.press("tab")
pyautogui.write("12332132")
pyautogui.press("enter")

# Form
import pandas
table = pandas.read_csv("produtos.csv")
print(table)

# Product
for linha in table.index:
    
# Table Code
    pyautogui.click(x=714, y=344)
    
    # pyautogui.write(str(tabela.loc[linha, "marca"])) SAME
    codigo = str(table.loc[linha,"codigo"])
    pyautogui.write(codigo)
    
    marca = str(table.loc[linha,"marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
        
    tipo = str(table.loc[linha,"tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    
    categoria = str(table.loc[linha,"categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    
    
    preco = str(table.loc[linha,"preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)
    
    custo = str(table.loc[linha,"custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    
    pyautogui.press("tab")
    obs = str(table.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(str(table.loc[linha, "obs"]))
        pyautogui.write(obs)
    time.sleep(1)
    # Send
    pyautogui.press("tab")
    pyautogui.press("enter")



    # First AUTO Python

