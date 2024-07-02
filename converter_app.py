import FreeSimpleGUI as sd
from converters import convert


sd.theme("Black")

label1 = sd.Text("Enter feet")
input1 = sd.InputText(key="feet")

label2 = sd.Text("Enter Inches")
input2 = sd.Input(key="inches")

choose_button3 = sd.Button("Convert")
exit_button = sd.Button("Exit")
output_label = sd.Text("", key="output")

window = sd.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [choose_button3, exit_button, output_label]])
while True:
    try:
        event, values = window.read()
        match event:
            case "Exit":
                break
            case sd.WIN_CLOSED:
                break
        feet = float(values["feet"])
        inches = float(values["inches"])

        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="white")
    except ValueError:
        sd.popup("Please Enter two numbers first")

window.close()
