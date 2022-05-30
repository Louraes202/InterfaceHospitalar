## ---- Head ----
import os
import PySimpleGUI as sg
## ---- Funções ----

## ---- Layouts e assets ----
from layouts import *
## ---- Var ----
caminho = os.getcwd()
f = open("DB/utentes.txt", "r", encoding="UTF-8")
utentes = f.read().splitlines()

## ---- Body ----
# sg.popup_notify("Projeto Final de PSI - MOD7 Ficheiros", display_duration_in_ms=500)
window = sg.Window("IH - Menu", menu(), icon=logo) # definição dos elementos da janela
running = True
# atualjanela = "menu"
while running == True: # loop da verificação e atualizaçáo de valores e eventos na janela
    atualjanela = "menu"
    event, values = window.read()
    print(atualjanela)
    if event == sg.WIN_CLOSED or event == "Sair" and atualjanela == "menu":
        running = False
    if event == "Entrar":
        atualjanela = "entrar"
        w_entrar = sg.Window("Entrar", entrar(), icon=logo)
        event, values = w_entrar.read()

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar":
            atualjanela = "menu"
            w_entrar.close()

        if event == "Login":
            username = values["UsernameValue"]
            password = values["PasswordValue"]
            utilizador = username + " " + password
            print(utilizador)
            w_entrar.close()
    if event == "Ajuda":
        atualjanela = "Ajuda"
        w_ajuda = sg.Window("Ajuda", ajuda(), icon=logo)
        event, values = w_ajuda.read()

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar":
            atualjanela = "menu"
            w_ajuda.close()


    if event == "Shortcut": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Interface"
        w_interface = sg.Window("Interface", interface(), icon=logo)
        event, values = w_interface.read()

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar":
            atualjanela = "menu"
            w_interface.close()

f.close()