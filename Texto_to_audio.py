from tkinter import *
from tkinter import messagebox, filedialog
from gtts import gTTS
from pkg_resources import resource_filename

def limpa_tela():
    entry0.delete(0, END)

def btn_clicked():
    idioma = 'pt'
    texto = entry0.get()
    audio = gTTS(text=texto, lang=idioma,tld='com.br')
    
    def salvar():
        filename = filedialog.asksaveasfilename(title="Salvar Arquivo", filetypes=[("Áudio MP3", ".mp3")])
        audio.save(filename+".mp3")
        messagebox.showinfo(message="Áudio gerado com sucesso!")    
    salvar()
    limpa_tela()

window = Tk()
window.geometry("600x450")
window.configure(bg = "#2e2e2e")
icon_img = resource_filename(__name__,r"ico.ico")
window.title("Conversor de Texto para Áudio")
window.iconbitmap(False, icon_img)
canvas = Canvas(window,bg = "#2e2e2e",height = 450,width = 600,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background_imp = resource_filename(__name__,r"background.png" )
background_img = PhotoImage(file = background_imp)
background = canvas.create_image(299.5, 100.0, image=background_img)
entry0_imp = resource_filename(__name__,r"img_textBox0.png" )
entry0_img = PhotoImage(file = entry0_imp)
entry0_bg = canvas.create_image(299.5, 224.5,image = entry0_img)

entry0 = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
entry0.place(x = 119, y = 152,width = 361,height = 143)

entry_img_imp = resource_filename(__name__,r"img0.png")
img0 = PhotoImage(file = entry_img_imp)
b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat")
b0.place(x = 226, y = 335,width = 147,height = 34)

window.resizable(False, False)
window.mainloop()
