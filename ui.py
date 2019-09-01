from tkinter import *
from PIL import ImageTk, Image
from ruoka import *


window = Tk()
window.geometry("800x400")
window.resizable(0,0)
window.config(background="white")

img = ImageTk.PhotoImage(Image.open("wine-glass.png"))

# to rename the title of the window
window.title("Arkea App")
Label(window, text = "Tänään on " + daystring, font=("Comic Sans MS", 16), bg="white").pack()
# pack is used to s
# ow the object in the window
def ruokaa():
    if viikonloppu == False and stringed[8:12] == "uuni":
        Label(window, text = "UUNIMAKKARA", font=("Comic Sans MS", 16), fg="red", bg="white").pack()
    elif viikonloppu == False:
        Label(window, text = splitted[0], font=("Comic Sans MS", 16), fg="red", bg="white").pack()
        Label(window, text = splitted[1], font=("Comic Sans MS", 16), fg="red", bg="white").pack()
    else:
        Label(window, text = "Det är weekend my boys!", font=("Comic Sans MS", 16), fg="red", bg="white").pack()
Button(window, text = "Mitä tänään syötäisiin?", command = ruokaa).pack()
Label(window, image=img).pack()
window.mainloop()
