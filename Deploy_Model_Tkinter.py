import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from ai_spleen_seg_app import app
import sys

sys.path.insert(1, 'C:\\Users\\Suchithra V S\\Desktop\\Tkinter_Sample\\ai_spleen_seg_app')


def __init__(self):
    Toplevel.__init__(self)


root = Tk()
max_geom = '%dx%d+%d+%d' % (root.winfo_screenwidth(), root.winfo_screenheight(), 0, 0)
root.geometry(max_geom)
root.title("MONAI Deploy")

# set window color
root.configure(bg='teal')

# Create a photo image object of the image in the path
# Ground Truth Image

image1 = Image.open("C:\\Users\\Suchithra V S\\Pictures\\Ligaments-of-the-Spleen.jpg")

# Resize the image using resize() method
resize_image = image1.resize((500, 450), resample=3)
test = ImageTk.PhotoImage(resize_image)

label1 = tkinter.Label(image=test, borderwidth=4, relief="solid")
label1.image = test

# Position image
label1.place(x=50, y=100)

label2 = tkinter.Label(text="Ground Truth", font=("Arial", 25), bg='teal', fg='white')
label2.place(x=200, y=50)

# Predicted Images

predicted_image = Image.open("C:\\Users\\Suchithra V S\\Pictures\\Ligaments-of-the-Spleen.jpg")

# Resize the image using resize() method
resize_predicted_image = predicted_image.resize((500, 450), resample=3)
display_predicted_image = ImageTk.PhotoImage(resize_predicted_image)

predicted_label = tkinter.Label(image=display_predicted_image, borderwidth=4, relief="solid")
predicted_label.image = test

# Position image
predicted_label.place(x=600, y=100)

predicted_text_label = tkinter.Label(text="Predicted Image", font=("Arial", 25), bg='teal', fg='white')
predicted_text_label.place(x=750, y=50)

global model_name
global input_image_folder


# Button for Model

def get_model():
    global model_name
    filetypes = (('model files', '*.pt'), ('All files', '*.*'))
    model_filename = fd.askopenfilename(initialdir=r'C:\Users\Suchithra V S\Desktop\Tkinter_Sample',
                                        filetypes=filetypes)
    model_name = model_filename
    print(model_filename)


btn_model = Button(root, text="Model", height=5, width=10, borderwidth=4, command=get_model)
btn_model.place(x=1200, y=200)


# Button for Input Image
def get_input():
    global input_image_folder
    input_folder = fd.askdirectory(initialdir=r'C:\Users\Suchithra V S\Desktop\Tkinter_Sample')
    input_image_folder = input_folder
    print(input_folder)


btn_input = Button(root, text="Input", height=5, width=10, borderwidth=4, command=get_input)
btn_input.place(x=1200, y=300)

w2 = Scale(root, from_=0, to=200, tickinterval=10, length=700, orient=HORIZONTAL, width=15)
w2.set(23)
w2.place(x=250, y=590)


# Button for MONAI deploy

def model_deploy():
    print("Entered Monai deploy")
    print(model_name, input_image_folder)

    app.deploy(r'C:/Users/Suchithra V S/Desktop/Tkinter_Sample/model/model.pt', r'C:/Users/Suchithra V S/Desktop/Tkinter_Sample/output', r'C:/Users/Suchithra V S/Desktop/Tkinter_Sample/input')


btn_deploy = Button(root, text="Deploy", height=5, width=10, borderwidth=4, command=model_deploy)
btn_deploy.place(x=1200, y=400)

root.mainloop()
