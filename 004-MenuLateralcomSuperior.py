import tkinter as tk

class ControleEstoque(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Crinado janela
        self.title("Controle de Estoque")
        #Definindo dimensôes
        self.geometry("800x600")
        
        self.menu_frame = tk.Frame(self, bg="white", width=200,height=600)
        self.menu_frame.pack(side="left", fill="y")
        
        self.conteudo_frame = tk.Frame(self, bg="light gray", width=600, height=600)
        self.conteudo_frame.pack(side="right", fill="both", expand=True)
        
        
        ## Criando menu superior
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        ## Adicioando menu superior na janela
        menu_arquivo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_arquivo.add_command(label="Novo")
        menu_arquivo.add_command(label="Abrir")
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.quit)        
        
        menu_editar = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=menu_editar)
        menu_editar.add_command(label="Novo")
        menu_editar.add_command(label="Abrir")
        menu_editar.add_separator()
        menu_editar.add_command(label="Sair", command=self.quit)        
        
        
        
        
        
        # Criando os botoes lateral
        self.cadastrar_button = tk.Button(self.menu_frame, text="Cadastrar Produtos")
        self.cadastrar_button.pack(pady=10)
        
        
        self.estoque_button = tk.Button(self.menu_frame, text="Visualizar Estoque")
        self.estoque_button.pack(pady=10)
        
        
        self.vendas_button = tk.Button(self.menu_frame, text="Realizar Vendas")
        self.vendas_button.pack(pady=10)
        
        
        self.relatorios_button = tk.Button(self.menu_frame, text="Gerar Relatórios")
        self.relatorios_button.pack(pady=10)
        

          
app = ControleEstoque()
app.mainloop()
