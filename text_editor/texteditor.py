import sys
if sys.version_info[0] == 2:
    from Tkinter import *
    import tkFileDialog
elif sys.version_info[0] == 3:
    from tkinter import *
    import tkinter.filedialog as tkFileDialog

root = Tk()
root.title("Text Editor")

text = Text(root)
text.grid()

def saveas():
    t = text.get("1.0", "end-1c")  # Corrected end index
    savelocation = tkFileDialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt"),
                                                             ("All Files", "*.*")])
    if savelocation:  # Ensure a file name was chosen
        with open(savelocation, "w") as file1:
            file1.write(t)

button = Button(root, text="Save", command=saveas)
button.grid()

def FontHelvetica():
    text.config(font=("Helvetica", 12))

def FontCourier():
    text.config(font=("Courier", 12))

menu = Menu(root)
root.config(menu=menu)

fontmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Font", menu=fontmenu)
fontmenu.add_command(label="Courier", command=FontCourier)
fontmenu.add_command(label="Helvetica", command=FontHelvetica)

root.mainloop()
