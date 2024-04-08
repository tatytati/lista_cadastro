import csv
import tkinter as tk
import tkinter as tk
from tkinter import messagebox
import os

def gravar_contato():

    if entry_nome.get() == "" or entry_fone.get() == "" or entry_email.get() == "":
        messagebox.showerror("erro ao gravar","todos os campos deve ser enseridos!")
    else:
       with open("dados.csv", "a",newline="") as arquivo_dados:
        escritor = csv.writer(arquivo_dados)
        escritor.writerow([entry_nome.get().strip(),entry_fone.get().strip(), entry_email.get().strip()])
        messagebox.showinfo("sistema contatos","contato cadastrado com sucesso!")
        limpar_dados()
        entry_nome.focus_set()


    print("\nDados gravados com sucesso!")
    ler_contatos()


def ler_contatos():
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        lista_contatos.delete(0,tk.END) # Limpar a lista
        for linha in leitor:
            lista_contatos.insert("end", linha[0])


def buscar_contato_pelo_indice(indice_procurado):
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        volta = 0
        for linha in leitor:
            if volta == indice_procurado:
                entry_nome.insert(tk.END, linha[0])
                entry_fone.insert(tk.END, linha[1])
                entry_email.insert(tk.END, linha[2])
                break
            volta = volta + 1

def obter_indice(event):
    indice = lista_contatos.curselection()[0]
    limpar_dados()
    buscar_contato_pelo_indice(indice)

def limpar_dados():
    entry_nome.delete(0, tk.END)
    entry_fone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
def excluir_contato():

    with open('dados.csv', 'r')as arquivo_dados, open('temp.csv', 'a',newline="")as arquivo_temp:
        leitor = csv.reader(arquivo_dados)
        escritor = csv.writer(arquivo_temp)

        for contato in leitor:
            if entry_nome.get() != contato[0] and entry_fone.get()[1] and entry_email.get()[2]:
                escritor.writerow([contato[0], contato[1], contato[2]])

#apagar os dados_csv
    os.remove('dados.csv')
#renomear temp.csv para dados.csv
    os.rename('temp.csv','dados.csv')
    messagebox.showinfo("exclui contato","operação cancelado pelo usuario")


janela = tk.Tk()
janela.geometry("460x300")
label_nome = tk.Label(janela, text="Nome:")
label_fone = tk.Label(janela, text="Telefone:")
label_email = tk.Label(janela, text="E-mail:")
label_contatos = tk.Label(janela, text="contatos:")
entry_nome = tk.Entry(janela)
entry_fone = tk.Entry(janela)
entry_email = tk.Entry(janela)


button_gravar = tk.Button(text="salvar", command=gravar_contato)
button_excluir = tk.Button(text="excluir", command=excluir_contato)

lista_contatos = tk.Listbox(janela, selectmode="single")
lista_contatos.bind("<<ListboxSelect>>", obter_indice)
label_contatos.config(font=("arial",16))
label_contatos.place(x=320, y=10)

label_nome.config(font=("arial",16))
label_nome.place(x=10, y=10)

entry_nome.config(font=("arial",16))
entry_nome.place(x=10, y=40, width=300, height=30)


label_fone.config(font=("arial",16))
label_fone.place(x=10, y=80)
entry_fone.place(x=10, y=110,width=300, height=30)

label_email.config(font=("arial",16))
label_email.place(x=10, y=150)
entry_email.place(x=10, y=110, width=300, height=30)

button_gravar.config(font=("arial",16))
button_gravar.place(x=10, y=230, width=150, height=60)
button_excluir.config(font=("arial",16))
button_excluir.place(x=160, y=230, width=150, height=60)


lista_contatos.config(font=("arial",16))
lista_contatos.place(x=320, y=40, width=300, height=250)

ler_contatos()

janela.mainloop()





