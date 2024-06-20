import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbx
import qrcode,random,time,os
from PIL import ImageTk
win = tk.Tk()
#getting screen width and height of display
# width= win.winfo_screenwidth()
# height= win.winfo_screenheight()
#setting tkinter window size
# win.geometry("%dx%d" % (width, height))
win.state('zoom')

win.title('QR CODE 📝')
# win.geometry('500x500')

# QR Frame
qr_frame = ttk.Labelframe(win,text='Generate QR code')
qr_frame.pack(padx=50,pady=60)

# qr_label = ttk.Label()


# QR Label
qr_label = ttk.Label(qr_frame,text='Type what you want to generate:',font=('Lato',14))
qr_label.configure(foreground='blue')
qr_label.grid(row=0,column=0,pady=20,padx=20)

# QR Entry Box
qr_var = tk.StringVar()

qr_entrybox= ttk.Entry(qr_frame,width=40,textvariable=qr_var)
qr_entrybox.focus()
qr_entrybox.grid(row=1,columnspan=2,pady=2,padx=20)


# generate function
def generate():
    for file in os.listdir():
          os.remove(file) if file.endswith('.png') else ''
    qr_text=qr_var.get()
    if  qr_text == '':
        mbx.showwarning('Empty','Fill the required fields.')
    elif len(qr_text) > 100:
        mbx.showerror('Too Long','QR Text too long.')
    else:
        qr = qrcode.QRCode(version=1,error_correction= qrcode.ERROR_CORRECT_H, box_size=10,border=4)
        qr.add_data(qr_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color = 'red',back_color = 'white')
        qr_location = str(random.randint(0,9))+ str(random.randint(0,9))+str(random.randint(0,9))+ '.png'
        img.save(qr_location)
        image_preview(qr_location)
        qr_entrybox.delete(0,tk.END)

def image_preview(location):
        time.sleep(1)
        image= ImageTk.PhotoImage(file=location)
        image_label.config(image=image)
        image_label.image = image


image_label = tk.Label(win)
image_label.pack()
# Generate Button
generate_button = ttk.Button(qr_frame,text='Generate Now',command=generate)
generate_button.grid(row=2,columnspan=2,padx=40,pady=20)


win.mainloop()