import PySimpleGUI as sg


def create_window(theme):
    sg.set_options(font="Calibri 30", button_element_size=(6,3))
    sg.theme(theme)
    layer1 = [
        sg.Text("", key = "OUTPUT", font="Franklin 40", justification="center",expand_x=True, pad=(10,20), right_click_menu= theme_menu)
    ]
    layer2 = [
        sg.Button("ENTER", key="ENTER", size=(4,1),expand_x=True), sg.Button("CLEAR", key="CLEAR", size=(4,1), expand_x=True)
    ]
    layer3 = [
        sg.Input(key="INPUTER", size = (5,0)), sg.Input(key="INPUTER2", size = (5,0)),sg.Spin(["Sumar", "Restar", "Multiplicar", "Dividir"], key = "SPINNER", size=(7,1))
    ]
    layer4 = [
        #sg.Text("")
    ]
    layout = [
        layer1,
        layer2,
        layer3,
        layer4
        ]
    return sg.Window("Probando", layout)

theme_menu = ["menu", ["LightGrey1", "dark", "DarkGrey8", "random"]]
window = create_window("LightGrey1")


output = ""
entrada2 = ""

while True:
    #Para cerrar la venta sin que de errores ni na
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    #Primera parte para el funcionamiento principal
    #Uso de operadores a traves de inputs y Spin
    if event == "ENTER":
        try:
            output = int(values["INPUTER"])
            entrada2 = int(values["INPUTER2"])
            int(values["INPUTER2"])
            if values["SPINNER"] == "Sumar":
                output += entrada2
            elif values["SPINNER"] == "Restar":
                output -= entrada2
            elif values["SPINNER"] == "Multiplicar":
                output = output * entrada2
            elif values["SPINNER"] == "Dividir":
                output = output / entrada2
                if output % 1 == 0.0:
                    output = int(output)
        except:
            pass
    #Segunda parte del funcionamiento principal
    #Si el usuario da a "clear" borrar el output
    elif event == "CLEAR":
        output = ""
        print(values)
    elif event in theme_menu[1]:
        window.close()
        create_window(event)
    #Tercera parte del funcionamiento principal
    #Resetar la ventana que muestra el output
    window["OUTPUT"].update(output)






window.close()