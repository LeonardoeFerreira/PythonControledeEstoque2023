import tkinter as tk

#---------------Criando uma janela
janela = tk.Tk()

#---------------Definir um titulo 
janela.title("Controle de Estoque")


#---------------Definir dimensões da janela
janela.geometry("400x300")

#---------------Criando um menu superior 
menu_superior = tk.Menu(janela)

menu1 = tk.Menu(menu_superior, tearoff=0)
menu1.add_command(label="Opção 01", command=menu1)
menu1.add_command(label="Opção 02", command=menu1)
menu_superior.add_cascade(label="Menu 01", menu=menu1)


menu2 = tk.Menu(menu_superior, tearoff=0)
menu2.add_command(label="Opção 01", command=menu2)
menu2.add_command(label="Opção 02", command=menu2)
menu_superior.add_cascade(label="Menu 02", menu=menu2)


menu3 = tk.Menu(menu_superior, tearoff=0)
menu3.add_command(label="Opção 01", command=menu3)
menu3.add_command(label="Opção 02", command=menu2)
menu_superior.add_cascade(label="Menu 03", menu=menu3)


menu4 = tk.Menu(menu_superior, tearoff=0)
menu4.add_command(label="Opção 01", command=menu4)
menu4.add_command(label="Opção 02", command=menu4)
menu_superior.add_cascade(label="Menu 04", menu=menu4)



# Adiciona o menu superior na janela
janela.config(menu=menu_superior)


#---------------Inicia o loop principal da janela
janela.mainloop()
