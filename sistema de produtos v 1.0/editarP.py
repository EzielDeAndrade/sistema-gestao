import os

# Nome do arquivo onde os produtos serão salvos
ARQUIVO_PRODUTOS = "produtosvarios.txt"

def inicializar_arquivo():
    """Cria o arquivo se ele não existir."""
    if not os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as f:
            pass # Apenas cria o arquivo vazio

def criar_produto(id_prod, nome, preco):
    """Adiciona um novo produto ao final do arquivo."""
    print("\n--- Adicionar Produto ---")
    #id_prod = input("ID do produto: ").upper()
    #nome = input("Nome do produto: ").upper()
    #preco = input("Preço: ").upper()
    
    # Salva no formato: id;nome;preco
    with open(ARQUIVO_PRODUTOS, 'a', encoding='utf-8') as f:
        f.write(f"{id_prod.upper()},{nome.upper()},{preco.upper()}\n")
    print("Produto cadastrado com sucesso!")
    return f"Produto {nome.upper()} cadastrado com sucesso!"                      

def listar_produtos():
    listagem_produtos=[]
    """Lê e exibe todos os produtos."""
    print("\n--- Lista de Produtos ---")
    if not os.path.exists(ARQUIVO_PRODUTOS):
        print("Nenhum produto cadastrado.")
        return

    with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as f:
        for linha in f:
            dados = linha.strip().split(',')
            if len(dados) == 3:
                print(f"ID: {dados[0]} | Nome: {dados[1]} | Preço: R$ {dados[2]}")
                print("-"*30)
                info = f"\n📦 TIPO:{dados[0]} |\n NOME:{dados[1]} |\n PREÇO:R${dados[2]} |"
                listagem_produtos.append(info)
    
    if listagem_produtos:
            return "\n".join(listagem_produtos)
   
def buscar_produtos():
    """Pesquisa um produto pelo ID."""
    print("\n--- Pesquisar Produto ---")
    id_pesquisa =  input("ID ou Nome do produto: ").upper()
    encontrado = False
    #encontrados = []
    
    
    with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as f:
        for linha in f:
            dados = linha.strip().split(',')
            if dados[0] == id_pesquisa or dados[1] == id_pesquisa:
                print(f"Encontrado: ID: {dados[0]} | Nome: {dados[1]} | Preço: R$ {dados[2]}")
                
                #info = f"📦 {dados[0]} | nome {dados[1] } | Preço: R$ {dados[2]}"
                #encontrados.append(info)
            #encontrado = True
            #print(encontrados)
            
            
            #break
    
        if not encontrado:
            print("=="*30)
            print("Produto não encontrado.")    
  
def editar_produtos(id_velho, n_id, n_nome, n_preco):
    """
    Edita um produto no arquivo TXT.
    id_velho: O termo usado para localizar a linha (ID ou Nome).
    n_id, n_nome, n_preco: Os novos dados que substituirão os antigos.
    """
    ARQUIVO_PRODUTOS = 'produtosvarios.txt'
    id_velho = id_velho.upper().strip()
    encontrado = False
    linhas_novas = []

    try:
        # 1. Lê todas as linhas para a memória
        with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        # 2. Processa as linhas
        for linha in linhas:
            dados = linha.strip().split(',')
            
            # Verifica se a linha tem os dados esperados e se coincide com a busca
            if len(dados) >= 3 and (dados[0].upper() == id_velho or dados[1].upper() == id_velho):
                # Cria a nova linha com os dados vindos da interface
                nova_linha = f"{n_id.upper()},{n_nome.upper()},{n_preco}\n"
                linhas_novas.append(nova_linha)
                encontrado = True
            else:
                # Mantém a linha original (importante: manter o \n)
                if not linha.endswith('\n'):
                    linha += '\n'
                linhas_novas.append(linha)

        # 3. Grava tudo de volta se houve alteração
        if encontrado:
            with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as f:
                f.writelines(linhas_novas)
            return "✅ Produto atualizado com sucesso!"
        else:
            return "❌ Produto não encontrado no sistema."

    except Exception as e:
        return f"⚠️ Erro ao editar: {e}"


# --- Menu Principal ---
def menu():
    inicializar_arquivo()
    while True:
        print("=="*30)
        print("== Menu Principal ==")
        print("====================")
        print("\n1. Criar Produto")
        print("2. Listar Produtos")
        print("3. Pesquisar Produto")
        print("4. Editar Produto")
        print("5. Sair \n")
        print("=="*30)
        
        opcao = input("Escolha uma opção: ").upper()[0]
        
        if opcao == '1':
            criar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            buscar_produtos()
        elif opcao == '4':
            editar_produtos()
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()

#ESTOQUE="produtosvarios.txt"

def buscar_produto(termo_busca):
    ESTOQUE = 'produtosvarios.txt'
    encontrados = []
    termo = termo_busca.upper().strip()

    if not termo:
        return "⚠️ Digite o nome de um produto para pesquisar."

    try:
        with open(ESTOQUE, 'r', encoding='utf-8') as f:
            for linha in f:
                # Remove espaços em branco e ignora linhas vazias
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                
                # Divide a linha: CARRO,FUSCA,5000 -> ['CARRO', 'FUSCA', '5000']
                produto_real = linha_limpa.split(',')
                
                # Garante que a linha tem os 3 elementos (Categoria, Nome, Preço)
                if len(produto_real) >= 3:
                    categoria = produto_real[0].upper()
                    nome = produto_real[1].upper()
                    preco = produto_real[2]

                    # Verifica se o termo está na Categoria OU no Nome
                    if termo in categoria or termo in nome:
                        info = f"\n📦 TIPO: {categoria} | \nNOME: {nome} | PREÇO: R$ {preco}"
                        encontrados.append(info)
        
        # Após ler o arquivo TODO, verificamos se algo foi guardado na lista
        if encontrados:
            return "\n".join(encontrados)
        else:
            return "❌ Nenhum produto encontrado."

    except FileNotFoundError:
        return "⚠️ Erro: Arquivo 'produtosvarios.txt' não encontrado."
