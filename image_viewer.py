from tkinter import *
from PIL import ImageTk, Image
import glob

root = Tk()
root.title("Image Viewer")
i = 0
img_files = glob.glob(r"filepath")
img_list = [ImageTk.PhotoImage(Image.open(file)) for file in img_files]

img_label = Label(image=img_list[0])
img_label.grid(row=0, column=0, columnspan=3)


def change_status():
    global i
    status["text"] = "Image " + str(i + 1) + " of  " + str(len(img_list))


def change_image():
    global i
    img_label.configure(image=img_list[i])
    change_status()
    img_label["image"] = img_list[i]


def forward():
    global i, img_label
    back_button["state"] = "normal"
    i = i + 1

    if i == (len(img_list) - 1):
        change_image()
        forward_button["state"] = "disabled"
    else:
        change_image()


def backward():
    global i, img_label
    forward_button["state"] = "normal"
    i = i - 1

    if i == 0:
        change_image()
        back_button["state"] = "disabled"
    else:
        change_image()


forward_button = Button(root, text=">>", command=forward)
back_button = Button(root, text="<<", command=backward,state='disabled')
exit_button = Button(root, text="Exit", command=root.quit)
status = Label(root, text="Image 1 of " + str(len(img_list)))

forward_button.grid(row=1,column=2)
back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1,pady=10)
status.grid(row=2,column=0,columnspan=3)

root.mainloop()

