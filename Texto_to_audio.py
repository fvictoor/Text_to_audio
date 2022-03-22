
from email import message
from tkinter import font
from gtts import gTTS
from tkinter import messagebox
from tkinter import *
import customtkinter

radius_defaut = 5
# C:\Users\fvict\appdata\roaming\python\python310\site-packages\customtkinter
  # Themes: "blue" (standard), "green", "dark-blue"

def limpa_tela():
    text_entry.delete(0, END)

def btn_clicked():
    idioma = 'pt'
    texto = text_entry.get()
    audio = gTTS(text=texto, lang=idioma,tld='com.br')
    audio.save('audio.mp3')
    messagebox.showinfo(message="Áudio gerado com sucesso!")
    limpa_tela()

window = customtkinter.CTk()
window.geometry("600x450")
window.title("Conversor de Texto para Áudio")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


Titulo = customtkinter.CTkLabel(master=window,
                              text="Converter Texto em Áudio",
                              width=100,
                              height=50,
                              corner_radius=1,
                              text_font= ("Roboto",'25','bold')
                              )
Titulo.place(relx=0.19,
           rely=0.1,
           )

text = customtkinter.CTkLabel(master=window,
                              text="Insira o texto aqui",
                              width=100,
                              
                              corner_radius=1,
                              text_font= ("Roboto",'12','italic')
                              )
text.place(relx=0.39,
           rely=0.28,
           )

text_entry = customtkinter.CTkEntry(master=window,
                                    width=361,
                                    height=143,
                                    corner_radius=0,
                                    border_width=1,
                                    fg_color="#1673a1"
                                                                       )
text_entry.place(x = 119, y = 152,
    width = 361,
    height = 143)



btn_Consult = customtkinter.CTkButton(master=window,
                                      text='Converter',
                                      corner_radius=radius_defaut,
                                      bg_color=("#b9dbe8"),
                                      command=btn_clicked,
                                      relief = "flat",
                                      highlightthickness = 0)
btn_Consult.place(
    x = 226, y = 335,
    width = 147,
    height = 33)

window.resizable(False, False)
window.mainloop()