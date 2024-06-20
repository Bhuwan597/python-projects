import tkinter as tk
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text,source='English',output='Hindi'):
    t = Translator()
    translated = t.translate(text,src=source,dest=output)
    # translated = t.translate('Hello  are you',dest=output)
    print(translated)
    return translated
    pass

def getdata():
    s= source_combo_box.get()
    o = output_combo_box.get()
    src_text = source_text.get('1.0','end')
    print(s,o,src_text)
    # opt_text = change(src_text,source=s,output=o)
    # output_text.delete('1.0','end')
    # output_text.insert(opt_text.text)
    print(Translator().translate('안녕하세요.', dest='ja')
)

root = tk.Tk()
root.state('zoom')

root.title('Google Translator')

main_frame = tk.Frame(root,bg='Red')
main_frame.pack(fill='both', expand=True)


label_text = ttk.Label(main_frame, text='Google Translator', font=('Times New Roman',40,'bold'),background='Red',foreground='White')
# label_text.place(x=100,y=40,height=50,width=300)
label_text.pack(padx=40,pady=30)

l = list(LANGUAGES.values())
source_combo_box = ttk.Combobox(main_frame,values=l, state='readonly')
source_combo_box.set('English')
output_combo_box = ttk.Combobox(main_frame,values=l, state='readonly')
output_combo_box.set('English')

source_text = tk.Text(main_frame, height = 10,
                width = 500,
                bg = "light yellow")

output_text = tk.Text(main_frame, height = 10,
              width = 500,
              bg = "light cyan")

translate_button = tk.Button(main_frame,text='Translate Now',relief='raised',command=getdata)
 
source_combo_box.pack()
source_text.pack(padx=40,pady=30)
translate_button.pack(padx=40,pady=30)
output_combo_box.pack()
output_text.pack(padx=40,pady=30)


root.mainloop()
