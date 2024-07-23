from tkinter import Tk,PhotoImage,Label,Frame,Button
from a import info, baixa
from leitor_crlv import ini_crlv_pdf
import os 
#from Planilha_notas import ini_crlv_pdf
       

root = Tk()
root.title("Aplicativo de Apoio Vamos")
root.geometry("330x330")
bg=PhotoImage(file="vamo3.png",width="200", height="200")
label = Label(root,image=bg)
label.configure(image=bg)
label.place(x=0,y=0,relheight=1,relwidth=1)
label.configure(bg = "white")
frame = Frame(root)
frame.pack(side="left")
frame.place(x=100,y=200, relheight=1, relwidth=1)
frame.configure(background="White")
botao1 = Button(frame, text="ADQUIRIR INFOS - PLACA",command=info)
botao2 = Button(frame, text="BAIXAR - CRLV",command=baixa)
botao3 = Button(frame, text="Planilhar CRLVs - PDFS",command=ini_crlv_pdf)
botao1.grid()
botao2.grid()
botao3.grid()
root.mainloop()



