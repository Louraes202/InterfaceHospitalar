import PySimpleGUI as sg
sg.theme("DarkPurple1")
logo = "Imagens/logo.ico"

## constantes
def menu(): # l_menu
    return [ 
        [sg.Text("Interface Hospital", font=("Comic 16 bold"))],
        [sg.Image(source="Imagens/hospital.png", expand_x=True, expand_y=True)],
        [sg.Button("Entrar"), sg.Button("Ajuda"), sg.Button("Shortcut"), sg.Button("Sair")]
        ]

## variáveis 

def entrar(): # l_entrar
    return [ 
        [sg.Text("Username:"), sg.Input("", key="UsernameValue", expand_x=True)],
        [sg.Text("Password:"), sg.Input("", key="PasswordValue", expand_x=True, password_char="⚫")],
        [sg.Button("Login"), sg.Button("Voltar")]
    ] 

def ajuda(): #l_ajuda
    return [
        [sg.Text("Ajuda", font=("Comic 16 bold"))],
        [sg.Text("Como utilizar o programa?")]
    ]

def interface(): # l_interface
    return [
        [sg.Text("Interface Principal", font=("Comic 16 bold"))]
    ]
