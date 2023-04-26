import tkinter as tk


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        
        self.btn_abrir_janela_secundaria = tk.Button(self, text="Abrir janela secundária", command=self.abrir_janela_secundaria)
        self.btn_abrir_janela_secundaria.pack(pady=20)

    def abrir_janela_secundaria(self):
        self.withdraw() # Oculta a janela principal
        self.janela_secundaria = JanelaSecundaria(self)
        self.janela_secundaria.protocol("WM_DELETE_WINDOW", self.voltar_janela_principal)

    def voltar_janela_principal(self):
        self.janela_secundaria.destroy() # Destrói a janela secundária
        self.update() # Atualiza a janela principal
        self.deiconify() # Exibe novamente a janela principal


class JanelaSecundaria(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("200x200")
        
        self.btn_voltar = tk.Button(self, text="Voltar", command=master.voltar_janela_principal)
        self.btn_voltar.pack(pady=20)


if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()
