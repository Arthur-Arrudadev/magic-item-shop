import sqlite3

from banco import criar_tabelas, conectar, Procedures
from models import Cliente, Funcionario, Produto, Pedido, CategoriaProdutos, AgendarServicos, Fornecedor, Estoque, \
    Receita
from colorama import Fore, Style, init
from tabulate import tabulate

init()

criar_tabelas()


def menu_principal():
    while True:
        print(f"\n{Fore.CYAN}🪄✨ {Style.BRIGHT}Loja de Itens Mágicos{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. {Style.RESET_ALL}Clientes")
        print(f"{Fore.YELLOW}2. {Style.RESET_ALL}Categorias")
        print(f"{Fore.YELLOW}3. {Style.RESET_ALL}Produtos")
        print(f"{Fore.YELLOW}4. {Style.RESET_ALL}Fornecedores")
        print(f"{Fore.YELLOW}5. {Style.RESET_ALL}Pedidos")
        print(f"{Fore.YELLOW}6. {Style.RESET_ALL}Estoque")
        print(f"{Fore.YELLOW}7. {Style.RESET_ALL}Receita")
        print(f"{Fore.YELLOW}8. {Style.RESET_ALL}Funcionários")
        print(f"{Fore.YELLOW}9. {Style.RESET_ALL}Agendar Serviços")
        print(f"{Fore.YELLOW}0. {Style.RESET_ALL}Relatórios")
        print(f"{Fore.YELLOW}999. {Style.RESET_ALL}Sair")

        try:
            opcao = int(input(f"{Fore.MAGENTA}>>> Escolha:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            menu_clientes()
        elif opcao == 2:
            menu_categorias()
        elif opcao == 3:
            menu_produtos()
        elif opcao == 4:
            menu_fornecedores()
        elif opcao == 5:
            menu_pedidos()
        elif opcao == 6:
            menu_estoque()
        elif opcao == 7:
            menu_receitas()
        elif opcao == 8:
            menu_funcionarios()
        elif opcao == 9:
            menu_agendarservicos()
        elif opcao == 0:
            menu_relatorios()
        elif opcao == 999:
            break
        else:
            print(f"{Fore.RED}⚠️ Opção inválida!{Style.RESET_ALL}")


def menu_clientes():
    while True:
        print(f"\n{Fore.BLUE}🧙 Menu de Clientes{Style.RESET_ALL}")
        print("1. Cadastrar\n2. Listar\n3. Deletar\n4. Voltar")

        try:
            opcao = int(input(f"{Fore.MAGENTA}>>> Escolha:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            try:
                cliente = Cliente(
                    nome=input("Nome: "),
                    email=input("Email: "),
                    telefone=input("Telefone: "),
                    endereco=input("Endereço: ")
                )
                cliente.salvar()
                print(f"{Fore.GREEN}✅ Cliente cadastrado!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 2:
            print(tabulate(Cliente.listar_todos(), headers="keys", tablefmt="pretty"))

        elif opcao == 3:
            try:
                id_cliente = int(input("ID do cliente: "))
                Cliente.deletar(id_cliente)
                print(f"{Fore.GREEN}✅ Cliente removido!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 4:
            break

def menu_categorias():
    while True:
        print(f"\n{Fore.BLUE}📚 {Style.BRIGHT}Menu de Categorias{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. {Style.RESET_ALL}Cadastrar")
        print(f"{Fore.YELLOW}2. {Style.RESET_ALL}Listar")
        print(f"{Fore.YELLOW}3. {Style.RESET_ALL}Buscar")
        print(f"{Fore.YELLOW}4. {Style.RESET_ALL}Atualizar")
        print(f"{Fore.YELLOW}5. {Style.RESET_ALL}Remover")
        print(f"{Fore.YELLOW}6. {Style.RESET_ALL}Voltar")

        try:
            opcao = int(input(f"{Fore.CYAN}>>> Escolha:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número válido!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            nome = input("Nome da categoria: ")
            descricao = input("Descrição (opcional): ") or None
            CategoriaProdutos(nome, descricao).salvar()
            print(f"{Fore.GREEN}✅ Categoria cadastrada!{Style.RESET_ALL}")

        elif opcao == 2:
            categorias = CategoriaProdutos.listar_todos()
            print(tabulate(
                categorias,
                headers={'id': 'ID', 'nome': 'Nome', 'descricao': 'Descrição'},
                tablefmt='grid'
            ))

        elif opcao == 3:
            id_cat = int(input("ID da categoria: "))
            categoria = CategoriaProdutos.buscar_por_id(id_cat)
            if categoria:
                print(tabulate([categoria], headers="keys", tablefmt="pretty"))
            else:
                print(f"{Fore.RED}⚠️ Categoria não encontrada!{Style.RESET_ALL}")

        elif opcao == 4:
            try:
                id_cat = int(input("ID da categoria: "))
                novo_nome = input("Novo nome (deixe em branco para manter atual): ") or None
                nova_desc = input("Nova descrição (deixe em branco para manter atual): ") or None

                CategoriaProdutos.atualizar(
                    id_categoria=id_cat,
                    novo_nome=novo_nome if novo_nome != "" else None,
                    nova_descricao=nova_desc if nova_desc != "" else None
                )

            except ValueError as e:
                print(f"{Fore.RED}⚠️ {e}{Style.RESET_ALL}")

        elif opcao == 5:
            id_categoria = int(input("ID da categoria: "))
            if input(f"{Fore.RED}Tem certeza? (s/n):{Style.RESET_ALL} ").lower() == 's':
                CategoriaProdutos.deletar(id_categoria)
                print(f"{Fore.GREEN}✅ Categoria removida!{Style.RESET_ALL}")

        elif opcao == 6:
            break

def menu_produtos():
    while True:
        print(f"\n{Fore.GREEN}🧪 Menu de Produtos{Style.RESET_ALL}")
        print(
            '1. Cadastrar\n2. Listar\n3. Buscar\n4. Atualizar\n5. Atualizar Preço\n6. Deletar\n7. Historico de Preços'
            '\n8. Voltar')

        try:
            opcao = int(input(f"{Fore.MAGENTA}>>> Escolha:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            try:
                produto = Produto(
                    nome=input("Nome: "),
                    descricao=input("Descrição: "),
                    preco=float(input("Preço: R$ ")),
                    categoria_id=int(input("ID Categoria: "))
                )
                produto.salvar()
                print(f"{Fore.GREEN}✅ Produto cadastrado!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 2:
            print(tabulate(Produto.listar_todos(), headers="keys", tablefmt="grid"))

        elif opcao == 3:
            try:
                id_produto = int(input("ID do produto: "))
                produto = Produto.buscar_por_id(id_produto)
                if produto:
                    print(tabulate([produto], headers="keys", tablefmt="pretty"))
                else:
                    print(f"{Fore.YELLOW}⚠️ Produto não encontrado!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 4:
            try:
                id_produto = int(input("ID do produto a atualizar: "))
                produto = Produto.buscar_por_id(id_produto)

                if not produto:
                    print(f"{Fore.RED}⚠️ Produto não encontrado!{Style.RESET_ALL}")
                    continue

                print(f"\n{Fore.BLUE}✏️ Editando Produto ID: {id_produto}{Style.RESET_ALL}")
                novo_nome = input(f"Nome ({produto['nome']}): ") or produto['nome']
                nova_desc = input(f"Descrição ({produto['descricao']}): ") or produto['descricao']
                novo_preco = float(input(f"Preço (R${produto['preco']:.2f}): ") or produto['preco'])
                nova_cat = int(input(f"Categoria ID ({produto['id_categoria']}): ") or produto['id_categoria'])

                conn = conectar()
                cursor = conn.cursor()
                cursor.execute('''
                                UPDATE Produtos SET
                                nome = ?, descricao = ?, preco = ?, id_categoria = ?
                                WHERE id_produto = ?
                            ''', (novo_nome, nova_desc, novo_preco, nova_cat, id_produto))
                conn.commit()
                conn.close()

                print(f"{Fore.GREEN}✅ Produto atualizado com sucesso!{Style.RESET_ALL}")

            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro ao atualizar: {e}{Style.RESET_ALL}")

        elif opcao == 5:
            print(f"\n{Fore.BLUE}🔄 Atualizar Preço do Produto{Style.RESET_ALL}")
            try:
                id_produto = int(input("ID do produto: "))

                # Verifica se o produto existe
                produto = Produto.buscar_por_id(id_produto)
                if not produto:
                    print(f"{Fore.RED}⚠️ Produto não encontrado!{Style.RESET_ALL}")
                    continue

                print(f"\n{Fore.CYAN}Produto Selecionado:{Style.RESET_ALL}")
                print(f"Nome: {produto['nome']}")
                print(f"Preço Atual: R$ {produto['preco']:.2f}")

                novo_preco = float(input("\nNovo preço: R$ "))
                if novo_preco <= 0:
                    print(f"{Fore.RED}⚠️ Preço deve ser positivo!{Style.RESET_ALL}")
                    continue

                # Confirmação importante!
                confirmar = input(f"{Fore.YELLOW}⚠️ Confirmar alteração? (s/n): {Style.RESET_ALL}").lower()
                if confirmar == 's':
                    if Procedures.atualizar_preco_produto(id_produto, novo_preco):
                        print(f"{Fore.GREEN}✅ Preço atualizado com sucesso!{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}⚠️ Falha ao atualizar preço!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.BLUE}❌ Operação cancelada{Style.RESET_ALL}")

            except ValueError:
                print(f"{Fore.RED}⚠️ Valor inválido! Digite números.{Style.RESET_ALL}")

        elif opcao == 6:
            try:
                id_produto = int(input("ID do produto a deletar: "))

                # Confirmação extra pra evitar acidentes!
                confirmacao = input(
                    f"{Fore.RED}Tem certeza? Isso apagará TODOS os itens associados! (s/n): {Style.RESET_ALL}")
                if confirmacao.lower() != 's':
                    print(f"{Fore.YELLOW}❌ Operação cancelada.{Style.RESET_ALL}")
                    continue

                Produto.deletar(id_produto)
                print(f"{Fore.GREEN}✅ Produto deletado com sucesso!{Style.RESET_ALL}")

            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro ao deletar: {e}{Style.RESET_ALL}")

        elif opcao == 7:
            Produto.visualizar_historico_precos()

        elif opcao == 8:
            break


def menu_funcionarios():
    while True:
        print(f"\n{Fore.MAGENTA}👔 Menu de Funcionários{Style.RESET_ALL}")
        print("1. Cadastrar\n2. Listar\n3. Buscar\n4. Atualizar\n5. Deletar\n6. Voltar")

        try:
            opcao = int(input(f"{Fore.MAGENTA}>>> Escolha:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            try:
                funcionario = Funcionario(
                    nome=input("Nome: "),
                    cargo=input("Cargo: "),
                    salario=float(input("Salário: R$ "))
                )
                funcionario.salvar()
                print(f"{Fore.GREEN}✅ Funcionário cadastrado!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 2:
            print(tabulate(Funcionario.listar_todos(), headers="keys", tablefmt="grid"))

        elif opcao == 3:
            try:
                id_func = int(input("ID do funcionário: "))
                funcionario = Funcionario.buscar_por_id(id_func)

                if funcionario:
                    print(f"\n{Fore.GREEN}🔍 Funcionário encontrado:{Style.RESET_ALL}")
                    print(tabulate(
                        [funcionario],
                        headers={
                            "id": "ID",
                            "nome": "Nome",
                            "cargo": "Cargo",
                            "salario": "Salário (R$)"
                        },
                        tablefmt="pretty",
                        floatfmt=".2f"
                    ))
                else:
                    print(f"{Fore.RED}⚠️ Funcionário não encontrado!{Style.RESET_ALL}")

            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 4:
            try:
                id_func = int(input("ID do funcionário: "))
                funcionario = Funcionario.buscar_por_id(id_func)

                if not funcionario:
                    print(f"{Fore.RED}⚠️ Funcionário não encontrado!{Style.RESET_ALL}")
                    continue

                print(f"\n{Fore.BLUE}✏️ Editando Funcionário ID {id_func}{Style.RESET_ALL}")
                novo_nome = input(f"Nome ({funcionario['nome']}): ") or funcionario['nome']
                novo_cargo = input(f"Cargo ({funcionario['cargo']}): ") or funcionario['cargo']
                novo_salario = input(f"Salário (R${funcionario['salario']:.2f}): ") or funcionario['salario']

                # Atualização no banco
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute('''
                            UPDATE Funcionarios 
                            SET nome = ?, cargo = ?, salario = ?
                            WHERE id_funcionario = ?
                        ''', (novo_nome, novo_cargo, novo_salario, id_func))
                conn.commit()
                conn.close()

                print(f"{Fore.GREEN}✅ Funcionário atualizado!{Style.RESET_ALL}")

            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro ao atualizar: {e}{Style.RESET_ALL}")

        elif opcao == 5:
            try:
                id_func = int(input("ID do funcionário: "))
                if input(f"{Fore.RED}Tem certeza? (s/n):{Style.RESET_ALL} ").lower() == 's':
                    Funcionario.deletar(id_func)
                    print(f"{Fore.GREEN}✅ Funcionário removido!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 6:
            break


def menu_pedidos():
    while True:
        print(f"\n{Fore.YELLOW}📦 Menu de Pedidos{Style.RESET_ALL}")
        print("1. Criar Novo Pedido"
              "\n2. Adicionar Item ao Pedido"
              "\n3. Remover Item do Pedido"
              "\n4. Ver Detalhes de um Pedido"
              "\n5. Deletar um pedido"
              "\n6. Voltar")

        try:
            opcao = int(input(f"{Fore.MAGENTA}>>> Escolha:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            try:
                pedido = Pedido(
                    id_cliente=int(input("ID Cliente: ")),
                    id_funcionario=int(input("ID Funcionário: "))
                )
                id_pedido = pedido.salvar()
                print(f"{Fore.GREEN}✅ Pedido #{id_pedido} criado!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 2:
            id_pedido = int(input("ID do pedido: "))
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            Pedido.adicionar_item(id_pedido, id_produto, quantidade)
            print("✅ Item adicionado ao pedido!")

        elif opcao == 3:
            id_item = int(input("ID do item do pedido a remover: "))
            Pedido.deletar_item_pedido(id_item)

        elif opcao == 4:
            try:
                id_pedido = int(input("ID Pedido: "))
                print(tabulate(Pedido.listar_itens_detalhados(id_pedido), headers="keys", tablefmt="grid"))
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 5:
            id_pedido = int(input("ID do pedido a deletar: "))
            Pedido.deletar(id_pedido)

        elif opcao == 6:
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

def menu_agendarservicos():
    agendador = AgendarServicos()

    while True:
        print(f"\n{Fore.LIGHTYELLOW_EX}📦 Menu de Agendamento de Serviços{Style.RESET_ALL}")
        print("1. Agendar serviço")
        print("2. Listar serviços agendados")
        print("3. Cancelar serviço")
        print("4. Sair")
        opcao = input(f"{Fore.MAGENTA}Escolha uma opção: {Style.RESET_ALL}")

        if opcao == "1":
            cliente = input("Nome do cliente: ")
            servico = input("Serviço a ser agendado: ")
            data = input("Data do serviço (ex: 2025-06-10): ")
            agendador.agendar(cliente, servico, data)

        elif opcao == "2":
            agendador.listar()

        elif opcao == "3":
            try:
                id_cancelar = int(input("Digite o ID do serviço para cancelar: "))
                agendador.cancelar(id_cancelar)
            except ValueError:
                print("ID inválido. Digite um número.")

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


def menu_fornecedores():
    while True:
        print(f"\n{Fore.MAGENTA}🏭 {Style.BRIGHT}Menu de Fornecedores{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. {Style.RESET_ALL}Cadastrar")
        print(f"{Fore.YELLOW}2. {Style.RESET_ALL}Listar")
        print(f"{Fore.YELLOW}3. {Style.RESET_ALL}Buscar")
        print(f"{Fore.YELLOW}4. {Style.RESET_ALL}Atualizar")
        print(f"{Fore.YELLOW}5. {Style.RESET_ALL}Remover")
        print(f"{Fore.YELLOW}6. {Style.RESET_ALL}Voltar")

        try:
            opcao = int(input(f"{Fore.CYAN}>>> Escolha:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            nome = input("Nome do fornecedor: ")
            contato = input("Contato (telefone/email): ")
            endereco = input("Endereço (opcional): ") or None

            Fornecedor(nome, contato, endereco).salvar()
            print(f"{Fore.GREEN}✅ Fornecedor cadastrado!{Style.RESET_ALL}")

        elif opcao == 2:
            fornecedores = Fornecedor.listar_todos()
            print(tabulate(
                fornecedores,
                headers={
                    'id': 'ID',
                    'nome': 'Nome',
                    'contato': 'Contato',
                    'endereco': 'Endereço'
                },
                tablefmt='grid'
            ))

        elif opcao == 3:
            id_forn = int(input("ID do fornecedor: "))
            forn = Fornecedor.buscar_por_id(id_forn)
            if forn:
                print(tabulate([forn], headers="keys", tablefmt="pretty"))
            else:
                print(f"{Fore.RED}⚠️ Fornecedor não encontrado!{Style.RESET_ALL}")

        elif opcao == 4:
            id_forn = int(input("ID do fornecedor: "))
            novo_nome = input("Novo nome (deixe em branco para manter): ") or None
            novo_contato = input("Novo contato (deixe em branco para manter): ") or None
            novo_endereco = input("Novo endereço (deixe em branco para manter): ") or None

            try:
                Fornecedor.atualizar(id_forn, novo_nome, novo_contato, novo_endereco)
                print(f"{Fore.GREEN}✅ Fornecedor atualizado!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}⚠️ Erro: {e}{Style.RESET_ALL}")

        elif opcao == 5:
            id_forn = int(input("ID do fornecedor: "))
            if input(f"{Fore.RED}Tem certeza? (s/n):{Style.RESET_ALL} ").lower() == 's':
                Fornecedor.deletar(id_forn)
                print(f"{Fore.GREEN}✅ Fornecedor removido!{Style.RESET_ALL}")

        elif opcao == 6:
            break


def menu_estoque():
    while True:
        print(f"\n{Fore.BLUE}📦 {Style.BRIGHT}MENU DE ESTOQUE{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. {Style.RESET_ALL}Gerenciar produto específico")
        print(f"{Fore.YELLOW}2. {Style.RESET_ALL}Listar estoque baixo")
        print(f"{Fore.YELLOW}3. {Style.RESET_ALL}Relatório completo")
        print(f"{Fore.YELLOW}4. {Style.RESET_ALL}Ajuste Rápido de Estoque")
        print(f"{Fore.YELLOW}5. {Style.RESET_ALL}Voltar")
        print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")

        try:
            opcao = int(input(f"{Fore.MAGENTA}🔮 Escolha uma opção:{Style.RESET_ALL} "))
        except ValueError:
            print(f"{Fore.RED}⚠️ Digite um número válido!{Style.RESET_ALL}")
            continue

        if opcao == 1:
            gerenciar_produto_especifico()
        elif opcao == 2:
            listar_estoque_baixo()
        elif opcao == 3:
            gerar_relatorio_completo()
        elif opcao == 4:
            try:
                id_produto = int(input("ID do produto: "))
                quantidade = int(input("Quantidade (+/-): "))
                Procedures.adicionar_ao_estoque(id_produto, quantidade)
            except ValueError:
                print(f"{Fore.RED}⚠️ Valores inválidos!{Style.RESET_ALL}")
        elif opcao == 5:
            break
        else:
            print(f"{Fore.RED}⚠️ Opção inválida!{Style.RESET_ALL}")


def gerenciar_produto_especifico():
    try:
        id_produto = int(input("\nDigite o ID do produto: "))
        produto = Produto.buscar_por_id(id_produto)

        if not produto:
            print(f"{Fore.RED}⚠️ Produto não encontrado!{Style.RESET_ALL}")
            return

        estoque = Estoque(id_produto)

        while True:
            print(f"\n{Fore.GREEN}🧪 Gerenciando: {produto['nome']} (ID: {id_produto}){Style.RESET_ALL}")
            print(f"Estoque atual: {estoque.consultar()} unidades")
            print(f"{Fore.CYAN}1. {Style.RESET_ALL}Adicionar itens")
            print(f"{Fore.CYAN}2. {Style.RESET_ALL}Remover itens")
            print(f"{Fore.CYAN}3. {Style.RESET_ALL}Voltar")

            sub_opcao = input(f"{Fore.MAGENTA}>>> Escolha:{Style.RESET_ALL} ")

            if sub_opcao == "1":
                quantidade = int(input("Quantidade a adicionar: "))
                estoque.adicionar(quantidade)
            elif sub_opcao == "2":
                quantidade = int(input("Quantidade a remover: "))
                estoque.remover(quantidade)
            elif sub_opcao == "3":
                break
            else:
                print(f"{Fore.RED}⚠️ Opção inválida!{Style.RESET_ALL}")

    except ValueError:
        print(f"{Fore.RED}⚠️ ID deve ser um número!{Style.RESET_ALL}")


def listar_estoque_baixo():
    limite = int(input("\nDefina o limite para alerta (padrão 5): ") or 5)
    itens_baixos = Estoque.listar_estoque_baixo(limite)

    if not itens_baixos:
        print(f"{Fore.GREEN}✨ Nenhum produto com estoque baixo!{Style.RESET_ALL}")
        return

    print(f"\n{Fore.YELLOW}⚠️ PRODUTOS COM ESTOQUE BAIXO:{Style.RESET_ALL}")
    print(tabulate(
        [(p[0], p[1], p[2], "🟢" if p[2] > 2 else "🔴") for p in itens_baixos],
        headers=["ID", "Produto", "Qtd", "Status"],
        tablefmt="grid",
        colalign=("center", "left", "center", "center")
    ))


def gerar_relatorio_completo():
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT 
                    p.id_produto, 
                    p.nome, 
                    c.nome_categoria,
                    COALESCE(e.quantidade_disponivel, 0) as estoque,
                    p.preco,
                    (COALESCE(e.quantidade_disponivel, 0) * p.preco) as valor_total
                FROM Produtos p
                LEFT JOIN Estoque e ON p.id_produto = e.id_produto
                LEFT JOIN CategoriaProdutos c ON p.id_categoria = c.id_categoria
                ORDER BY p.nome
            ''')
            dados = cursor.fetchall()

        if not dados:
            print(f"{Fore.YELLOW}⚠️ Nenhum produto cadastrado!{Style.RESET_ALL}")
            return

        print(f"\n{Fore.CYAN}📊 RELATÓRIO COMPLETO DE ESTOQUE:{Style.RESET_ALL}")
        print(tabulate(
            dados,
            headers=["ID", "Produto", "Categoria", "Estoque", "Preço", "Valor Total"],
            tablefmt="grid",
            floatfmt=("", "", "", "", ".2f", ".2f"),
            numalign="right"
        ))

        # Totalizadores
        total_itens = sum(d[3] for d in dados)
        total_valor = sum(d[5] for d in dados)
        print(f"\n{Fore.GREEN}💰 TOTAL GERAL: {total_itens} itens (R$ {total_valor:.2f}){Style.RESET_ALL}")

    except sqlite3.Error as e:
        print(f"{Fore.RED}⚠️ Erro ao gerar relatório: {e}{Style.RESET_ALL}")


def menu_receitas():
    while True:
        print(f"\n{Fore.GREEN}💰 {Style.BRIGHT}MENU DE RECEITAS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. {Style.RESET_ALL}Registrar Nova Movimentação")
        print(f"{Fore.YELLOW}2. {Style.RESET_ALL}Consultar por Período")
        print(f"{Fore.YELLOW}3. {Style.RESET_ALL}Saldo Atual")
        print(f"{Fore.YELLOW}4. {Style.RESET_ALL}Relatório de Fluxo de Caixa")
        print(f"{Fore.YELLOW}5. {Style.RESET_ALL}Voltar")
        print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")

        opcao = input(f"{Fore.MAGENTA}🔮 Escolha uma opção:{Style.RESET_ALL} ")

        if opcao == "1":
            registrar_movimentacao()
        elif opcao == "2":
            consultar_periodo()
        elif opcao == "3":
            mostrar_saldo()
        elif opcao == "4":
            gerar_relatorio_fluxo()
        elif opcao == "5":
            break
        else:
            print(f"{Fore.RED}⚠️ Opção inválida!{Style.RESET_ALL}")


def registrar_movimentacao():
    print(f"\n{Fore.BLUE}📝 Nova Movimentação{Style.RESET_ALL}")
    tipo = selecionar_tipo()
    descricao = input("Descrição: ").strip()

    try:
        valor = float(input("Valor: R$ "))
        data = input("Data (YYYY-MM-DD ou Enter para hoje): ") or None
        forma_pag = input("Forma de pagamento (opcional): ") or None
        categoria = input("Categoria (opcional): ") or None
        obs = input("Observações (opcional): ") or None

        receita = Receita(
            tipo=tipo,
            descricao=descricao,
            valor=valor,
            data_movimentacao=data,
            forma_pagamento=forma_pag,
            categoria=categoria,
            observacao=obs
        )

        if receita.salvar():
            print(f"{Fore.GREEN}✅ Movimentação registrada com sucesso!{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}⚠️ Erro nos dados: {e}{Style.RESET_ALL}")

def selecionar_tipo():
    while True:
        print(f"\n{Fore.YELLOW}1. {Style.RESET_ALL}Entrada (Receita)")
        print(f"{Fore.YELLOW}2. {Style.RESET_ALL}Saída (Despesa)")
        op = input("Tipo: ")
        return 'Entrada' if op == '1' else 'Saida' if op == '2' else None


def mostrar_saldo():
    """Exibe o saldo atual formatado"""
    saldo = Receita.calcular_saldo()
    cor = Fore.GREEN if saldo >= 0 else Fore.RED
    print(f"\n{cor}💰 SALDO ATUAL: R$ {saldo:.2f}{Style.RESET_ALL}")

    # Detalhamento adicional
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                SUM(CASE WHEN tipo='Entrada' THEN valor ELSE 0 END) as total_entradas,
                SUM(CASE WHEN tipo='Saida' THEN valor ELSE 0 END) as total_saidas
            FROM Receita
        ''')
        totais = cursor.fetchone()

    print(f"\n{Fore.CYAN}📊 Detalhamento:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}↑ Entradas: R$ {totais[0] or 0:.2f}{Style.RESET_ALL}")
    print(f"{Fore.RED}↓ Saídas: R$ {abs(totais[1] or 0):.2f}{Style.RESET_ALL}")


def consultar_periodo():
    print(f"\n{Fore.BLUE}📅 Consulta por Período{Style.RESET_ALL}")

    # Pede as datas com validação simples
    data_inicio = input("Data inicial (YYYY-MM-DD): ")
    data_fim = input("Data final (YYYY-MM-DD): ")

    # Validação básica das datas
    if not data_inicio or not data_fim:
        print(f"{Fore.RED}⚠️ Ambas as datas são obrigatórias!{Style.RESET_ALL}")
        return

    # Busca os dados no modelo
    movimentacoes = Receita.buscar_por_periodo(data_inicio, data_fim)

    if not movimentacoes:
        print(f"{Fore.YELLOW}⚠️ Nenhuma movimentação encontrada!{Style.RESET_ALL}")
        return

    # Formatação profissional com tabulate
    tabela = []
    for mov in movimentacoes:
        cor = Fore.GREEN if mov[2] == 'Entrada' else Fore.RED  # mov[2] = tipo
        tabela.append([
            mov[4],  # Data
            mov[1],  # Descrição
            f"{cor}{mov[2]}{Style.RESET_ALL}",  # Tipo colorido
            f"R$ {abs(mov[3]):.2f}",  # Valor absoluto
            mov[5] or "Não informado"  # Categoria
        ])

    # Cabeçalho bonito
    print(f"\n{Fore.CYAN}📊 Movimentações de {data_inicio} a {data_fim}{Style.RESET_ALL}")
    print(tabulate(
        tabela,
        headers=["Data", "Descrição", "Tipo", "Valor", "Categoria"],
        tablefmt="grid",
        stralign="left"
    ))

    # Totalizador
    total_entradas = sum(mov[3] for mov in movimentacoes if mov[2] == 'Entrada')
    total_saidas = sum(abs(mov[3]) for mov in movimentacoes if mov[2] == 'Saida')

    print(f"\n{Fore.GREEN}↑ Total Entradas: R$ {total_entradas:.2f}{Style.RESET_ALL}")
    print(f"{Fore.RED}↓ Total Saídas: R$ {total_saidas:.2f}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}➞ Saldo do Período: R$ {total_entradas - total_saidas:.2f}{Style.RESET_ALL}")

def gerar_relatorio_fluxo():
    dados = Receita.gerar_relatorio_fluxo_caixa()

    if not dados:
        print(f"{Fore.YELLOW}⚠️ Nenhuma movimentação registrada!{Style.RESET_ALL}")
        return

    # Prepara os dados para exibição
    tabela = []
    for linha in dados:
        cor = Fore.GREEN if linha[1] == 'Entrada' else Fore.RED
        tabela.append([
            linha[0] or "Sem categoria",
            f"{cor}{linha[1]}{Style.RESET_ALL}",
            f"R$ {linha[2]:.2f}",
            linha[3]
        ])

    print(f"\n{Fore.CYAN}📈 FLUXO DE CAIXA POR CATEGORIA{Style.RESET_ALL}")
    print(tabulate(
        tabela,
        headers=["Categoria", "Tipo", "Total", "Operações"],
        tablefmt="grid",
        stralign="left"
    ))

def menu_relatorios():
    while True:
        print(f"\n{Fore.MAGENTA}📊 {Style.BRIGHT}MENU DE RELATÓRIOS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. {Style.RESET_ALL}Média Mensal")
        print(f"{Fore.YELLOW}2. {Style.RESET_ALL}Relatório Anual")
        print(f"{Fore.YELLOW}3. {Style.RESET_ALL}Voltar")
        print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")

        opcao = input(f"{Fore.MAGENTA}🔮 Escolha:{Style.RESET_ALL} ")

        if opcao == "1":
            # Chama a procedure de média mensal
            meses = int(input("Número de meses para análise (padrão 6): ") or 6)

            print(f"\n{Fore.BLUE}📈 Média de Entradas{Style.RESET_ALL}")
            dados_entradas = Procedures.calcular_media_mensal('Entrada', meses)
            print(tabulate(dados_entradas, headers=["Mês", "Média"], tablefmt="grid"))

            print(f"\n{Fore.RED}📉 Média de Saídas{Style.RESET_ALL}")
            dados_saidas = Procedures.calcular_media_mensal('Saida', meses)
            print(tabulate(dados_saidas, headers=["Mês", "Média"], tablefmt="grid"))

        elif opcao == "2":
            # Relatório anual
            ano = input("Digite o ano (YYYY): ")
            dados = Procedures.gerar_relatorio_financeiro_anual(ano)

            if dados:
                print(f"\n{Fore.GREEN}📅 Relatório Anual {ano}{Style.RESET_ALL}")
                print(tabulate(
                    dados,
                    headers=["Mês", "Entradas", "Saídas", "Saldo"],
                    tablefmt="grid",
                    floatfmt=".2f"
                ))
            else:
                print(f"{Fore.RED}⚠️ Nenhum dado encontrado!{Style.RESET_ALL}")

        elif opcao == "3":
            break
        else:
            print(f"{Fore.RED}⚠️ Opção inválida!{Style.RESET_ALL}")

if __name__ == "__main__":
    menu_principal()
