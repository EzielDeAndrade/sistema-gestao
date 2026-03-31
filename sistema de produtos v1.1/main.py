import tkinter as tk
from tkinter import messagebox, scrolledtext
import editarP as funcoes  #  funções de busca, salvar e editar

class SistemaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão 1.1 By: Eziel")
        self.root.geometry("400x500")
        self.arquivo_usuarios = "DadosLogin.txt"
        self.usuario_admin = "log_adm.txt"
        self.tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- LÓGICA DE LOGIN ---
    def verificar_login(self, usuario, senha):
        try:
            with open(self.arquivo_usuarios, "r") as f:
                for linha in f:
                    u_db, s_db = linha.strip().split(',')
                    if u_db == usuario.upper() and s_db == senha:
                        return True
        except FileNotFoundError:
            return False
        return False
    
    def verificar_loginAdm(self, usuario, senha,identificador_ADM):
        try:
            with open(self.usuario_admin, "r") as f:
                for linha in f:
                    u_db, s_db, id_ADM = linha.strip().split(',')
                    if u_db == usuario.upper() and s_db == senha and id_ADM == identificador_ADM:
                        return True
        except FileNotFoundError:
            return False
        return False

    def cadastrar_novo_ADM(self):
        def salvar():
            u, s = ent_u.get().upper().strip(), ent_s.get().strip()
            if u and s:
                with open(self.usuario_admin, "a") as f:
                    f.write(f"{u},{s},Adm\n")
                messagebox.showinfo("Sucesso", "Usuário ADM criado!")
                janela_cad.destroy()
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos!")

        janela_cad = tk.Toplevel(self.root)
        janela_cad.title("Cadastrar Novo ADM")
        janela_cad.geometry("350x150")
        tk.Label(janela_cad, text="Novo Usuário:").pack()
        ent_u = tk.Entry(janela_cad); ent_u.pack()
        tk.Label(janela_cad, text="Nova Senha:").pack()
        ent_s = tk.Entry(janela_cad, show="*"); ent_s.pack()
        tk.Button(janela_cad, text="Salvar", command=salvar).pack(pady=10)
    def cadastrar_novo_login(self):
        def salvar():
            u, s = ent_u.get().upper().strip(), ent_s.get().strip()
            if u and s:
                with open(self.arquivo_usuarios, "a") as f:
                    f.write(f"{u},{s}\n")
                messagebox.showinfo("Sucesso", "Usuário criado!")
                janela_cad.destroy()
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos!")

        janela_cad = tk.Toplevel(self.root)
        janela_cad.title("Cadastrar Novo Usuário")
        janela_cad.geometry("350x150")
        tk.Label(janela_cad, text="Novo Usuário:").pack()
        ent_u = tk.Entry(janela_cad); ent_u.pack()
        tk.Label(janela_cad, text="Nova Senha:").pack()
        ent_s = tk.Entry(janela_cad, show="*"); ent_s.pack()
        tk.Button(janela_cad, text="Salvar", command=salvar).pack(pady=10)

    def tela_loginAdm(self,):
        self.limpar_tela()
        tk.Label(self.root, text="LOGIN", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Usuário ADMIN:").pack()
        self.ent_user = tk.Entry(self.root); self.ent_user.pack()
        tk.Label(self.root, text="Senha:").pack()
        self.ent_pass = tk.Entry(self.root, show="*"); self.ent_pass.pack()
        
        
        tk.Button(self.root, text="Entrar", width=15, command=self.fazer_loginAdm).pack(pady=10)
        
        tk.Button(self.root, text="Voltar", width=15, command=self.tela_login).pack(pady=10)

    # --- TELAS ---
    def tela_login(self):
        self.limpar_tela()
        
        tk.Label(self.root, text="LOGIN", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Usuário:").pack()
        self.ent_user = tk.Entry(self.root); self.ent_user.pack()
        tk.Label(self.root, text="Senha:").pack()
        self.ent_pass = tk.Entry(self.root, show="*"); self.ent_pass.pack()
        
        
        tk.Button(self.root, text="Entrar", width=15, command=self.fazer_login).pack(pady=10)
        
        tk.Button(self.root, text="Logim Admin", width=15, command= self.tela_loginAdm).pack(pady=20)

    
    def fazer_loginAdm(self):
        identificador_ADM = "Adm"
        if self.verificar_loginAdm(self.ent_user.get(), self.ent_pass.get(),identificador_ADM):
            self.adm_menu()
        else:
            messagebox.showerror("Erro", "Login Inválido!")
    def fazer_login(self):
        if self.verificar_login(self.ent_user.get(), self.ent_pass.get()):
            self.menu_principal()
        else:
            messagebox.showerror("Erro", "Login Inválido!")

    
    def adm_menu(self):
        self.limpar_tela()
        tk.Label(self.root, text="MENU ADMIN ", font=("Arial", 14)).pack(pady=20)
        
        opcoes = [
            ("Crar Conta de Login", self.cadastrar_novo_login),
            ("Ir para menu Principal", self.menu_principal),
            ("Cadastrar Adm", self.cadastrar_novo_ADM),
            
            ("Sair", self.tela_login)
        ]
        for texto, cmd in opcoes:
            tk.Button(self.root, text=texto, width=25, command=cmd).pack(pady=5)
        
        tk.Button(self.root, text="Voltar", command=self.tela_login).pack(pady=10)

    def menu_principal(self):
        self.limpar_tela()
        tk.Label(self.root, text="MENU PRINCIPAL", font=("Arial", 14)).pack(pady=20)
        tamanhodetela = self.root
        tamanhodetela.geometry("400x500")
        opcoes = [
            ("Pesquisar Produto", self.tela_pesquisa),
            ("Cadastrar Produto", self.tela_cadastro_prod),
            ("Mostrar Todos", self.mostrar_tudo),
            ("Editar Produto", self.tela_editar),
            ("Sair", self.tela_login)
           
        ]
        for texto, cmd in opcoes:
            tk.Button(self.root, text=texto, width=25, command=cmd).pack(pady=5)
        
        tk.Button(self.root, text="Voltar", command=self.tela_login).pack(pady=10)
        tk.Button(self.root, text="Logim Admin", width=15, command= self.tela_loginAdm).pack(pady=20)
    def tela_pesquisa(self):
        self.limpar_tela()
        tamanhodetela = self.root
        tamanhodetela.geometry("920x500")
        tk.Label(self.root,height=2, text="Pesquisar:",).pack(pady=5)
        ent = tk.Entry(self.root); ent.pack()
        
        res_area = scrolledtext.ScrolledText(self.root, width=100, height=20); res_area.pack(pady=10)
        
        def acao():
            res = funcoes.buscar_produto(ent.get())
            res_area.delete('1.0', tk.END); res_area.insert(tk.END, res)

        tk.Button(self.root, text="Buscar", command=acao).pack()
        tk.Button(self.root, text="Voltar", command=self.menu_principal).pack(pady=10)

    def tela_cadastro_prod(self):
        janela = tk.Toplevel(self.root)
        janela.geometry("400x300")
        tk.Label(janela, text="Tipo:").pack(); e_t = tk.Entry(janela); e_t.pack()
        tk.Label(janela, text="Nome:").pack(); e_n = tk.Entry(janela); e_n.pack()
        tk.Label(janela, text="Preço:").pack(); e_p = tk.Entry(janela); e_p.pack()
        
        def salvar():
            msg = funcoes.criar_produto(e_t.get(), e_n.get(), e_p.get())
            messagebox.showinfo("Status", msg); janela.destroy()
        
        tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)
        tk.Button(janela, text="Voltar", bg="orange",command=self.menu_principal).pack(pady=10)

    def mostrar_tudo(self):
        self.limpar_tela()
        tamanhodetela = self.root
        tk.Label(tamanhodetela, text="TODOS PRODUTOS CADASTRADOS", font=("Arial", 14)).pack(pady=20)
        tamanhodetela.geometry("680x600")
        area = scrolledtext.ScrolledText(self.root, width=45, height=30); area.pack()
        # Chama busca vazia para retornar tudo (ajuste no editarP se necessário)
        area.insert(tk.END, funcoes.listar_produtos()) 
        tk.Button(self.root, text="Voltar", command=self.menu_principal).pack(pady=10)

    def tela_editar(self):
        # Cria uma janela flutuante para edição
        janela_edit = tk.Toplevel(self.root)
        janela_edit.title("Editar Produto")
        janela_edit.geometry("548x680")

        # Campo para localizar o produto (ID ou Nome atual)
        tk.Label(janela_edit, text="Nome produto a editar:", fg="red").pack(pady=5)
        ent_id_busca = tk.Entry(janela_edit)
        
        ent_id_busca.pack()
        #res_area = scrolledtext.ScrolledText(self.root, width=45, height=10); res_area.pack(pady=10)
        tk.Label(janela_edit, text="Resultados:").pack(pady=5)
        res_area = scrolledtext.ScrolledText(janela_edit, width=45, height=10); res_area.pack(pady=10)
        def acao_buscar():
            res = funcoes.buscar_produto(ent_id_busca.get())
            res_area.delete('1.0', tk.END); res_area.insert(tk.END, res)
        #tk.Button(janela_edit, text="Buscar", bg="orange", 
         #         command=acao_buscar).pack(pady=20)
        tk.Label(janela_edit, text="--- Novos Dados ---", font=("Arial", 10, "bold")).pack(pady=10)

        tk.Label(janela_edit, text="Novo Tipo:").pack()
        ent_novo_id = tk.Entry(janela_edit)
        ent_novo_id.pack()

        tk.Label(janela_edit, text="Novo Nome:").pack()
        ent_novo_nome = tk.Entry(janela_edit)
        ent_novo_nome.pack()

        tk.Label(janela_edit, text="Novo Preço:").pack()
        ent_novo_preco = tk.Entry(janela_edit)
        ent_novo_preco.pack()

        def confirmar_edicao():
            # Pega os valores dos campos
            id_velho = ent_id_busca.get()
            
            n_id = ent_novo_id.get()
            n_nome = ent_novo_nome.get()
            n_preco = ent_novo_preco.get()

            if not id_velho or not n_id or not n_nome or not n_preco:
                messagebox.showwarning("Atenção", "Preencha todos os campos!")
                return

            # Chama a função do  arquivo funcoes.py (ou editarP.py)
            # A função deve retornar uma mensagem de sucesso ou erro
            resultado = funcoes.editar_produtos(id_velho, n_id, n_nome, n_preco,)
            
            messagebox.showinfo("Resultado", resultado)
            if "sucesso" in resultado.lower():
                janela_edit.destroy()
        
        tk.Button(janela_edit, text="Buscar", bg="orange", 
                  command=acao_buscar).pack(pady=20)
        tk.Button(janela_edit, text="Salvar Alterações", bg="orange", 
                  command=confirmar_edicao).pack(pady=20)
        
        tk.Button(janela_edit, text="Voltar", bg="orange",command=self.menu_principal).pack(pady=10)
        
    #def tela_editar(self):
     #   messagebox.showinfo("Editar", "Implemente a lógica de substituição de linha no editarP.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaApp(root)
    root.mainloop()
