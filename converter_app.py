import FreeSimpleGUI as sd

label1 = sd.Text("Enter feet")
input1 = sd.InputText()

label2 = sd.Text("Enter Inches")
input2 = sd.Input()

choose_button3 = sd.Button("Convert")

window = sd.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [choose_button3]])
window.read()
window.close()
