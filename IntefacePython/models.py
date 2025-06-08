import sqlite3
from datetime import datetime

from colorama import Fore, Style
from tabulate import tabulate

from banco import conectar, Procedures


class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

        """Salva o cliente no banco"""
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)',
            (self.nome, self.email, self.telefone, self.endereco)
        )
        conn.commit()
        conn.close()

    """Deleta um cliente pelo ID."""
    def deletar(id_cliente):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clientes WHERE id_cliente = ?', (id_cliente,))
        conn.commit()
        conn.close()

    """Retorna todos os clientes como dicionários."""

    @classmethod
    def listar_todos(cls):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes = [{
            'id': row[0],
            'nome': row[1],
            'email': row[2],
            'telefone': row[3],
            'endereco': row[4]
        } for row in cursor.fetchall()]
        conn.close()
        return clientes

class Produto:
    def __init__(self, nome, descricao, preco, categoria_id, conexao):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria_id = categoria_id
        self.conn = conexao

    """Salva o produto no banco."""
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO produtos (nome, descricao, preco, id_categoria) VALUES (?, ?, ?, ?)',
            (self.nome, self.descricao, self.preco, self.categoria_id)
        )
        conn.commit()
        conn.close()

    def deletar(id_produto):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id_produto = ?', (id_produto,))
        conn.commit()
        conn.close()

    @classmethod
    def listar_todos(cls):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = [{
            'id': row[0],
            'nome': row[1],
            'descricao': row[2],
            'preco': row[3],
            'categoria_id': row[4]
        } for row in cursor.fetchall()]
        conn.close()
        return produtos

    @classmethod
    def cadastrar_produto(self):
        print(f"\n{Fore.BLUE}🌟 Cadastrar Novo Produto{Style.RESET_ALL}")
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: R$ "))
        id_categoria = int(input("ID da categoria: "))

        produto = Produto(nome, descricao, preco, id_categoria)
        produto.salvar()
        print(f"{Fore.GREEN}✅ Produto cadastrado com sucesso!{Style.RESET_ALL}")

    @classmethod
    def listar_produtos(self):
        produtos = Produto.listar_todos()
        if not produtos:
            print(f"{Fore.YELLOW}⚠️ Nenhum produto cadastrado.{Style.RESET_ALL}")
            return

        # Formatação profissional com tabulate
        print(f"\n{Fore.CYAN}📦 Lista de Produtos:{Style.RESET_ALL}")
        print(tabulate(
            produtos,
            headers={
                "id": "ID",
                "nome": "Nome",
                "descricao": "Descrição",
                "preco": "Preço",
                "categoria_id": "Categoria"
            },
            tablefmt="grid",
            floatfmt=".2f"
        ))

    @classmethod
    def buscar_produto_por_id(self):
        id_produto = int(input("ID do produto: "))
        produto = Produto.buscar_por_id(id_produto)

        if produto:
            print(f"\n{Fore.CYAN}🔍 Detalhes do Produto:{Style.RESET_ALL}")
            print(tabulate([produto], headers="keys", tablefmt="pretty"))
        else:
            print(f"{Fore.RED}⚠️ Produto não encontrado!{Style.RESET_ALL}")

    @classmethod
    def buscar_por_id(cls, id_produto):
        """Busca um produto pelo ID e retorna como dicionário"""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Produtos WHERE id_produto = ?', (id_produto,))
        produto = cursor.fetchone()
        conn.close()

        if produto:
            return {
                'id_produto': produto[0],
                'nome': produto[1],
                'descricao': produto[2],
                'preco': produto[3],
                'id_categoria': produto[4]
            }
        return None

    @classmethod
    def atualizar_produto(self):
        id_produto = int(input("ID do produto a atualizar: "))
        produto = Produto.buscar_por_id(id_produto)

        if not produto:
            print(f"{Fore.RED}⚠️ Produto não encontrado!{Style.RESET_ALL}")
            return

        print(f"\n{Fore.BLUE}✏️ Editando Produto ID: {id_produto}{Style.RESET_ALL}")
        novo_nome = input(f"Nome ({produto['nome']}): ") or produto['nome']
        nova_descricao = input(f"Descrição ({produto['descricao']}): ") or produto['descricao']
        novo_preco = float(input(f"Preço ({produto['preco']}): ") or produto['preco'])
        nova_categoria = int(input(f"Categoria ID ({produto['categoria_id']}): ") or produto['categoria_id'])

        # Atualização no banco (adicione este método à classe Produto)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE Produtos 
        SET nome = ?, descricao = ?, preco = ?, id_categoria = ?
        WHERE id_produto = ?
        ''', (novo_nome, nova_descricao, novo_preco, nova_categoria, id_produto))
        conn.commit()
        conn.close()

        print(f"{Fore.GREEN}✅ Produto atualizado!{Style.RESET_ALL}")

    @classmethod
    def deletar_produto(self):
        id_produto = int(input("ID do produto a deletar: "))

        # Confirmação extra para evitar acidentes!
        confirmacao = input(
            f"{Fore.RED}Tem certeza que deseja deletar o produto {id_produto}? (s/n): {Style.RESET_ALL}")
        if confirmacao.lower() == 's':
            Produto.deletar(id_produto)
            print(f"{Fore.GREEN}✅ Produto deletado!{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}❌ Operação cancelada.{Style.RESET_ALL}")

    @staticmethod
    def visualizar_historico_precos():
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT p.nome, v.preco_antigo, v.preco_novo, v.data_alteracao
            FROM HistoricoPrecos v
            JOIN Produtos p ON v.id_produto = p.id_produto
            ORDER BY v.data_alteracao DESC
        ''')

        resultados = cursor.fetchall()
        conn.close()

        if resultados:
            headers = ["Produto", "Preço Antigo", "Preço Novo", "Data da Alteração"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid", floatfmt=".2f"))
        else:
            print("Nenhum histórico de preços encontrado.")

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)',
            (self.nome, self.cargo, self.salario)
        )
        conn.commit()
        conn.close()

    def deletar(id_funcionario):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Funcionarios WHERE id_funcionario = ?', (id_funcionario,))
        conn.commit()
        conn.close()

    @classmethod
    def listar_todos(cls):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM funcionarios')
        funcionarios = [{
            'id': row[0],
            'nome': row[1],
            'cargo': row[2],
            'salario': row[3]
        } for row in cursor.fetchall()]
        conn.close()
        return funcionarios

    @classmethod
    def cadastrar_funcionario(self):
        print(f"\n{Fore.GREEN}🌟 Novo Funcionário{Style.RESET_ALL}")
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: R$ "))

        funcionario = Funcionario(nome, cargo, salario)
        funcionario.salvar()
        print(f"{Fore.GREEN}✅ Funcionário cadastrado! ID: {funcionario.id}{Style.RESET_ALL}")

    @classmethod
    def listar_funcionarios(self):
        funcionarios = Funcionario.listar_todos()

        if not funcionarios:
            print(f"{Fore.YELLOW}⚠️ Nenhum funcionário cadastrado.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.CYAN}📋 Lista de Funcionários:{Style.RESET_ALL}")
        print(tabulate(
            funcionarios,
            headers={
                "id": "ID",
                "nome": "Nome",
                "cargo": "Cargo",
                "salario": "Salário"
            },
            tablefmt="grid",
            floatfmt=".2f",
            colalign=("center", "left", "left", "right")
        ))

    @classmethod
    def buscar_por_id(cls, id_funcionario):
        """Busca um funcionário pelo ID e retorna como dicionário"""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Funcionarios WHERE id_funcionario = ?', (id_funcionario,))
        funcionario = cursor.fetchone()
        conn.close()

        if funcionario:
            return {
                'id': funcionario[0],
                'nome': funcionario[1],
                'cargo': funcionario[2],
                'salario': funcionario[3]
            }
        return None

    @classmethod
    def buscar_funcionario_por_id(self):
        id_func = int(input("ID do funcionário: "))
        funcionario = next(
            (f for f in Funcionario.listar_todos() if f['id'] == id_func),
            None
        )

        if funcionario:
            print(f"\n{Fore.CYAN}🔍 Detalhes:{Style.RESET_ALL}")
            print(tabulate(
                [funcionario],
                headers="keys",
                tablefmt="pretty"
            ))
        else:
            print(f"{Fore.RED}⚠️ Funcionário não encontrado!{Style.RESET_ALL}")

    @classmethod
    def atualizar_funcionario(self):
        id_func = int(input("ID do funcionário: "))
        funcionarios = Funcionario.listar_todos()
        funcionario = next((f for f in funcionarios if f['id'] == id_func), None)

        if not funcionario:
            print(f"{Fore.RED}⚠️ Funcionário não encontrado!{Style.RESET_ALL}")
            return

        print(f"\n{Fore.BLUE}✏️ Editando Funcionário ID: {id_func}{Style.RESET_ALL}")
        novo_nome = input(f"Nome ({funcionario['nome']}): ") or funcionario['nome']
        novo_cargo = input(f"Cargo ({funcionario['cargo']}): ") or funcionario['cargo']
        novo_salario = input(f"Salário ({funcionario['salario']}): ") or funcionario['salario']

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            '''UPDATE Funcionarios 
            SET nome = ?, cargo = ?, salario = ? 
            WHERE id_funcionario = ?''',
            (novo_nome, novo_cargo, novo_salario, id_func)
        )
        conn.commit()
        conn.close()
        print(f"{Fore.GREEN}✅ Funcionário atualizado!{Style.RESET_ALL}")

    @classmethod
    def deletar_funcionario(self):
        id_func = int(input("ID do funcionário: "))

        # Confirmação extra para evitar acidentes!
        confirmacao = input(f"{Fore.RED}Tem certeza que deseja deletar? (s/n): {Style.RESET_ALL}")
        if confirmacao.lower() == 's':
            Funcionario.deletar(id_func)
            print(f"{Fore.GREEN}✅ Funcionário removido!{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}❌ Operação cancelada.{Style.RESET_ALL}")

class Fornecedor:
    def __init__(self, nome, contato, endereco):
        self.nome = nome
        self.contato = contato
        self.endereco = endereco

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO fornecedores (nome, contato, endereco) VALUES (?, ?, ?)',
            (self.nome, self.contato, self.endereco)
        )
        conn.commit()
        conn.close()

    def deletar(id_fornecedor):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM fornecedores WHERE id_fornecedor = ?', (id_fornecedor,))
        conn.commit()
        conn.close()

    @classmethod
    def listar_todos(cls):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM fornecedores')
        fornecedores = [{
            'id': row[0],
            'nome': row[1],
            'contato': row[2],
            'endereco': row[3]
        } for row in cursor.fetchall()]
        conn.close()
        return fornecedores

class CategoriaProdutos:
    def __init__(self, nome_categoria, descricao):
        self.nome_categoria = nome_categoria
        self.descricao = descricao

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO CategoriaProdutos (nome_categoria, descricao) VALUES (?, ?)',
            (self.nome_categoria, self.descricao)
        )
        conn.commit()
        conn.close()

    def deletar(id_categoria):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM CategoriaProdutos WHERE id_categoria = ?', (id_categoria,))
        conn.commit()
        conn.close()

    @classmethod
    def listar_todos(cls):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM CategoriaProdutos')
        CategoriaProdutos = [{
            'id': row[0],
            'nome_categoria': row[1],
            'descricao': row[2]
        } for row in cursor.fetchall()]
        conn.close()
        return CategoriaProdutos

    @classmethod
    def buscar_por_id(cls, id_categoria):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM CategoriaProdutos WHERE id_categoria = ?', (id_categoria,))
        categoria = cursor.fetchone()
        conn.close()

        if categoria:
            return {
                'id': categoria[0],
                'nome': categoria[1],
                'descricao': categoria[2] or "Sem descrição"
            }
        return None

    @classmethod
    def atualizar(cls, id_categoria: int, novo_nome: str = None, nova_descricao: str = None):
        """Atualiza uma categoria existente"""
        conn = conectar()
        cursor = conn.cursor()

        try:
            # Primeiro busca a categoria atual
            cursor.execute('SELECT * FROM CategoriaProdutos WHERE id_categoria = ?', (id_categoria,))
            categoria_atual = cursor.fetchone()

            if not categoria_atual:
                raise ValueError(f"{Fore.RED}⚠️ Categoria com ID {id_categoria} não encontrada!{Style.RESET_ALL}")

            # Mantém os valores atuais se nenhum novo for fornecido
            nome = novo_nome if novo_nome is not None else categoria_atual[1]
            descricao = nova_descricao if nova_descricao is not None else categoria_atual[2]

            # Atualiza no banco
            cursor.execute('''
                UPDATE CategoriaProdutos 
                SET nome_categoria = ?, descricao = ?
                WHERE id_categoria = ?
            ''', (nome, descricao, id_categoria))

            conn.commit()
            print(f"{Fore.GREEN}✅ Categoria atualizada com sucesso!{Style.RESET_ALL}")

        except Exception as e:
            conn.rollback()
            print(f"{Fore.RED}⚠️ Erro ao atualizar categoria: {e}{Style.RESET_ALL}")
            raise

        finally:
            conn.close()

class AgendamentoServico:
    def __init__(self, id_cliente, tipo_servico, data_agendada, id_funcionario, status="Agendado"):
        self.id_cliente = id_cliente
        self.tipo_servico = tipo_servico
        self.data_agendada = data_agendada
        self.id_funcionario = id_funcionario
        self.status = status

        """Salva o agendamento no banco de dados."""
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO AgendamentoDeServicos 
        (id_cliente, tipo_servico, data_agendada, status, id_funcionario)
        VALUES (?, ?, ?, ?, ?)''',
        (self.id_cliente, self.tipo_servico, self.data_agendada, self.status, self.id_funcionario))
        conn.commit()
        conn.close()

        """Lista todos os agendamentos de um cliente."""
    @classmethod
    def listar_por_cliente(cls, id_cliente):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM AgendamentoDeServicos 
            WHERE id_cliente = ?''', (id_cliente,))
        agendamentos = [{
            'id_agendamento': row[0],
            'tipo_servico': row[2],
            'data': row[3],
            'status': row[4],
            'funcionario': row[5]
        } for row in cursor.fetchall()]
        conn.close()
        return agendamentos

    """Atualiza o status de um agendamento"""
    @classmethod
    def atualizar_status(cls, id_agendamento, novo_status):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE AgendamentoDeServicos 
        SET status = ? 
        WHERE id_agendamento = ?''', (novo_status, id_agendamento))
        conn.commit()
        conn.close()

    """Cancela um agendamento (status = 'Cancelado')."""
    @classmethod
    def cancelar(cls, id_agendamento):
        cls.atualizar_status(id_agendamento, "Cancelado")

    """Lista TODOS os agendamentos."""
    @classmethod
    def listar_todos(cls):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM AgendamentoDeServicos')
        agendamentos = [{
            'id': row[0],
            'cliente_id': row[1],
            'servico': row[2],
            'data': row[3],
            'status': row[4],
            'funcionario_id': row[5]
        } for row in cursor.fetchall()]
        conn.close()
        return agendamentos

class Pedido:
    def __init__(self, id_cliente, id_funcionario, valor_total=0.00):
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.valor_total = valor_total

    def salvar(self):
        """Salva o pedido com a data atual e retorna o ID."""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO PedidosClientes 
        (id_cliente, data_pedido, id_funcionario, valor_total)
        VALUES (?, date('now'), ?, ?)''',
                       (self.id_cliente, self.id_funcionario, self.valor_total))
        conn.commit()
        self.id_pedido = cursor.lastrowid  # Guarda o ID
        conn.close()
        return self.id_pedido

    @classmethod
    def deletar(cls, id_pedido):
        """Deleta um pedido e seus itens associados."""
        conn = conectar()
        cursor = conn.cursor()

        # 1. Primeiro deleta os itens do pedido (para não violar chave estrangeira)
        cursor.execute('DELETE FROM ItensDePedidos WHERE id_pedido = ?', (id_pedido,))

        # 2. Depois deleta o pedido
        cursor.execute('DELETE FROM PedidosClientes WHERE id_pedido = ?', (id_pedido,))

        conn.commit()
        conn.close()
        print(f"Pedido {id_pedido} e seus itens foram deletados com sucesso!")

    @classmethod
    def buscar_por_id(cls, id_pedido):
        """Busca um pedido pelo ID com detalhes formatados."""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT 
            p.id_pedido, 
            p.data_pedido, 
            p.valor_total,
            c.nome AS cliente_nome,
            f.nome AS funcionario_nome
        FROM PedidosClientes p
        JOIN Clientes c ON p.id_cliente = c.id_cliente
        JOIN Funcionarios f ON p.id_funcionario = f.id_funcionario
        WHERE p.id_pedido = ?''', (id_pedido,))
        pedido = cursor.fetchone()
        conn.close()

        if pedido:
            return {
                'id': pedido[0],
                'data': pedido[1],
                'valor_total': pedido[2],
                'cliente': pedido[3],
                'funcionario': pedido[4]
            }
        return None

    @classmethod
    def adicionar_item(cls, id_pedido, id_produto, quantidade):
        """Adiciona item ao pedido e atualiza o valor_total."""
        conn = conectar()
        cursor = conn.cursor()

        # 1. Pega preço do produto
        cursor.execute('SELECT preco FROM Produtos WHERE id_produto = ?', (id_produto,))
        preco_unitario = cursor.fetchone()[0]

        # 2. Insere o item
        cursor.execute('''
        INSERT INTO ItensDePedidos 
        (id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (?, ?, ?, ?)''',
                       (id_pedido, id_produto, quantidade, preco_unitario))

        # 3. Atualiza valor_total do pedido
        cursor.execute('''
        UPDATE PedidosClientes 
        SET valor_total = (
            SELECT SUM(quantidade * preco_unitario) 
            FROM ItensDePedidos 
            WHERE id_pedido = ?
        )
        WHERE id_pedido = ?''', (id_pedido, id_pedido))

        conn.commit()
        conn.close()

    @classmethod
    def listar_por_cliente(cls, id_cliente):
        """Lista pedidos de um cliente com JOIN para nomes."""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT 
            p.id_pedido,
            p.data_pedido,
            p.valor_total,
            f.nome AS funcionario
        FROM PedidosClientes p
        JOIN Funcionarios f ON p.id_funcionario = f.id_funcionario
        WHERE p.id_cliente = ?''', (id_cliente,))
        pedidos = [{
            'id': row[0],
            'data': row[1],
            'valor': row[2],
            'atendente': row[3]
        } for row in cursor.fetchall()]
        conn.close()
        return pedidos

    @classmethod
    def listar_itens_detalhados(cls, id_pedido):
        """Lista itens do pedido com nomes dos produtos."""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT 
            p.nome,
            ip.quantidade,
            ip.preco_unitario,
            (ip.quantidade * ip.preco_unitario) AS subtotal
        FROM ItensDePedidos ip
        JOIN Produtos p ON ip.id_produto = p.id_produto
        WHERE ip.id_pedido = ?''', (id_pedido,))
        itens = [{
            'produto': row[0],
            'quantidade': row[1],
            'preco_unitario': row[2],
            'subtotal': row[3]
        } for row in cursor.fetchall()]
        conn.close()
        return itens

    @classmethod
    def calcular_total_periodo(cls, data_inicio, data_fim):
        """Calcula o total de vendas em um período (formato 'YYYY-MM-DD')."""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT SUM(valor_total) 
        FROM PedidosClientes 
        WHERE data_pedido BETWEEN ? AND ?''',
                       (data_inicio, data_fim))
        total = cursor.fetchone()[0] or 0.00
        conn.close()
        return total

    @classmethod
    def deletar_item_pedido(cls, id_item_pedido):
        """Deleta um item específico de um pedido e atualiza o valor total."""
        conn = conectar()
        cursor = conn.cursor()

        try:
            # 1. Pega o id_pedido associado ao item
            cursor.execute('SELECT id_pedido FROM ItensDePedidos WHERE id_item = ?', (id_item_pedido,))
            resultado = cursor.fetchone()

            if not resultado:
                print("❌ Item não encontrado!")
                return False

            id_pedido = resultado[0]

            # 2. Deleta o item
            cursor.execute('DELETE FROM ItensDePedidos WHERE id_item = ?', (id_item_pedido,))

            # 3. Atualiza o valor_total do pedido
            cursor.execute('''
            UPDATE PedidosClientes 
            SET valor_total = (
                SELECT COALESCE(SUM(quantidade * preco_unitario), 0.00)
                FROM ItensDePedidos 
                WHERE id_pedido = ?
            )
            WHERE id_pedido = ?''', (id_pedido, id_pedido))

            conn.commit()
            print(f"✅ Item {id_item_pedido} deletado do pedido {id_pedido}!")
            return True

        except Exception as e:
            conn.rollback()
            print(f"❌ Erro ao deletar item: {e}")
            return False

        finally:
            conn.close()

class AgendarServicos:
    def __init__(self):
        self.servicos = []
        self.contador_id = 1

    def agendar(self, cliente, servico, data):
        agendamento = {
            "id": self.contador_id,
            "cliente": cliente,
            "servico": servico,
            "data": data
        }
        self.servicos.append(agendamento)
        print(f"Serviço agendado com sucesso! ID: {self.contador_id}")
        self.contador_id += 1

    def listar(self):
        if not self.servicos:
            print("Nenhum serviço agendado.")
            return
        for s in self.servicos:
            print(f"ID: {s['id']} | Cliente: {s['cliente']} | Serviço: {s['servico']} | Data: {s['data']}")

    def cancelar(self, id_servico):
        for s in self.servicos:
            if s['id'] == id_servico:
                self.servicos.remove(s)
                print(f"Serviço ID {id_servico} cancelado com sucesso.")
                return
        print(f"Serviço com ID {id_servico} não encontrado.")

from colorama import Fore
from tabulate import tabulate


class Fornecedor:
    def __init__(self, nome: str, contato: str, endereco: str = None):
        self.nome = nome
        self.contato = contato
        self.endereco = endereco

    def salvar(self):
        """Salva o fornecedor no banco de dados"""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO Fornecedores (nome, contato, endereco) VALUES (?, ?, ?)',
            (self.nome, self.contato, self.endereco)
        )
        conn.commit()
        conn.close()

    @classmethod
    def buscar_por_id(cls, id_fornecedor: int) -> dict:
        """Busca um fornecedor pelo ID"""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Fornecedores WHERE id_fornecedor = ?', (id_fornecedor,))
        fornecedor = cursor.fetchone()
        conn.close()

        if fornecedor:
            return {
                'id': fornecedor[0],
                'nome': fornecedor[1],
                'contato': fornecedor[2],
                'endereco': fornecedor[3]
            }
        return None

    @classmethod
    def listar_todos(cls) -> list:
        """Lista todos os fornecedores"""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Fornecedores')
        fornecedores = [{
            'id': row[0],
            'nome': row[1],
            'contato': row[2],
            'endereco': row[3] or "Não informado"
        } for row in cursor.fetchall()]
        conn.close()
        return fornecedores

    @classmethod
    def atualizar(cls, id_fornecedor: int, novo_nome: str = None, novo_contato: str = None, novo_endereco: str = None):
        """Atualiza os dados do fornecedor"""
        conn = conectar()
        cursor = conn.cursor()

        # Busca dados atuais
        dados_atuais = cls.buscar_por_id(id_fornecedor)
        if not dados_atuais:
            raise ValueError("Fornecedor não encontrado!")

        # Preenche com novos dados ou mantém os atuais
        nome = novo_nome if novo_nome is not None else dados_atuais['nome']
        contato = novo_contato if novo_contato is not None else dados_atuais['contato']
        endereco = novo_endereco if novo_endereco is not None else dados_atuais['endereco']

        cursor.execute(
            'UPDATE Fornecedores SET nome = ?, contato = ?, endereco = ? WHERE id_fornecedor = ?',
            (nome, contato, endereco, id_fornecedor)
        )
        conn.commit()
        conn.close()

    @classmethod
    def deletar(cls, id_fornecedor: int):
        """Remove um fornecedor (com confirmação)"""
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Fornecedores WHERE id_fornecedor = ?', (id_fornecedor,))
        conn.commit()
        conn.close()

class Estoque:
    def __init__(self, id_produto: int = None):
        """
        Inicializa o controle de estoque para um produto específico ou geral (se id_produto=None)
        """
        self.id_produto = id_produto
        self.conn = None  # Será usada para transações

    def __enter__(self):
        """Para usar com 'with' (gerenciamento automático de conexão)"""
        self.conn = conectar()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Garante que a conexão será fechada"""
        if self.conn:
            self.conn.close()

    def adicionar(self, quantidade: int) -> bool:
        """Adiciona itens ao estoque do produto"""
        if not self.id_produto:
            raise ValueError("ID do produto não definido!")

        try:
            with self as estoque:
                cursor = self.conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO Estoque (id_produto, quantidade_disponivel)
                    VALUES (?, COALESCE(
                        (SELECT quantidade_disponivel FROM Estoque WHERE id_produto = ?), 
                        0
                    ) + ?)
                ''', (self.id_produto, self.id_produto, quantidade))
                self.conn.commit()
                print(f"{Fore.GREEN}✨ {quantidade} itens adicionados ao estoque!{Style.RESET_ALL}")
                return True
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro ao adicionar: {e}{Style.RESET_ALL}")
            return False

    def remover(self, quantidade: int) -> bool:
        """Remove itens do estoque com validação"""
        if not self.id_produto:
            raise ValueError("ID do produto não definido!")

        try:
            with self as estoque:
                cursor = self.conn.cursor()

                # Verifica estoque atual
                cursor.execute('''
                    SELECT quantidade_disponivel FROM Estoque 
                    WHERE id_produto = ?
                ''', (self.id_produto,))
                resultado = cursor.fetchone()

                if not resultado:
                    print(f"{Fore.RED}⚠️ Produto não encontrado no estoque!{Style.RESET_ALL}")
                    return False

                if resultado[0] < quantidade:
                    print(f"{Fore.RED}⚠️ Estoque insuficiente!{Style.RESET_ALL}")
                    return False

                # Atualiza estoque
                cursor.execute('''
                    UPDATE Estoque 
                    SET quantidade_disponivel = quantidade_disponivel - ? 
                    WHERE id_produto = ?
                ''', (quantidade, self.id_produto))

                self.conn.commit()
                print(f"{Fore.GREEN}✅ {quantidade} itens removidos!{Style.RESET_ALL}")
                return True

        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro ao remover: {e}{Style.RESET_ALL}")
            return False

    def consultar(self) -> int:
        """Retorna a quantidade disponível em estoque"""
        try:
            with self as estoque:
                cursor = self.conn.cursor()
                cursor.execute('''
                    SELECT quantidade_disponivel 
                    FROM Estoque 
                    WHERE id_produto = ?
                ''', (self.id_produto,))
                resultado = cursor.fetchone()
                return resultado[0] if resultado else 0
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro na consulta: {e}{Style.RESET_ALL}")
            return 0

    # Métodos estáticos (para operações gerais)
    @staticmethod
    def listar_estoque_baixo(limite: int = 5):
        """Lista todos os produtos com estoque abaixo do limite"""
        try:
            with conectar() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT p.id_produto, p.nome, e.quantidade_disponivel
                    FROM Estoque e
                    JOIN Produtos p ON e.id_produto = p.id_produto
                    WHERE e.quantidade_disponivel < ?
                    ORDER BY e.quantidade_disponivel ASC
                ''', (limite,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro ao listar estoque: {e}{Style.RESET_ALL}")
            return []


class Receita:
    """Classe para gerenciar entradas e saídas financeiras"""

    TIPOS_VALIDOS = ('Entrada', 'Saida')  # Constante de classe

    def __init__(self, tipo: str, descricao: str, valor: float,
                 data_movimentacao: str = None, forma_pagamento: str = None,
                 categoria: str = None, observacao: str = None):
        """
        Inicializa uma movimentação financeira

        :param tipo: 'Entrada' ou 'Saida' (case-sensitive)
        :param valor: Valor positivo (será convertido para negativo se for Saída)
        """
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido! Use: {self.TIPOS_VALIDOS}")

        self.tipo = tipo
        self.descricao = descricao
        self.valor = abs(valor) if tipo == 'Entrada' else -abs(valor)
        self.data_movimentacao = data_movimentacao or datetime.now().strftime('%Y-%m-%d')
        self.forma_pagamento = forma_pagamento
        self.categoria = categoria
        self.observacao = observacao

    def salvar(self) -> int:
        """Salva a receita no banco e retorna o ID"""
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Receita (
                    tipo, descricao, valor, data_movimentacao, 
                    forma_pagamento, categoria, observacao
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                self.tipo, self.descricao, self.valor, self.data_movimentacao,
                self.forma_pagamento, self.categoria, self.observacao
            ))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro ao salvar receita: {e}{Style.RESET_ALL}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def buscar_por_periodo(data_inicio: str, data_fim: str) -> list:
        """Busca movimentações por período (formato 'YYYY-MM-DD')"""
        try:
            with conectar() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM Receita 
                    WHERE data_movimentacao BETWEEN ? AND ?
                    ORDER BY data_movimentacao DESC
                ''', (data_inicio, data_fim))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro ao buscar receitas: {e}{Style.RESET_ALL}")
            return []

    @classmethod
    def calcular_saldo(cls, data_fim: str = None) -> float:
        """Calcula o saldo total até a data especificada"""
        try:
            with conectar() as conn:
                cursor = conn.cursor()
                query = 'SELECT SUM(valor) FROM Receita'
                params = ()

                if data_fim:
                    query += ' WHERE data_movimentacao <= ?'
                    params = (data_fim,)

                cursor.execute(query, params)
                return cursor.fetchone()[0] or 0.0
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro ao calcular saldo: {e}{Style.RESET_ALL}")
            return 0.0

    @staticmethod
    def gerar_relatorio_fluxo_caixa():
        """Gera relatório detalhado agrupado por categoria"""
        try:
            with conectar() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT 
                        categoria,
                        tipo,
                        SUM(valor) as total,
                        COUNT(*) as operacoes
                    FROM Receita
                    GROUP BY categoria, tipo
                    ORDER BY categoria, tipo DESC
                ''')
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro no relatório: {e}{Style.RESET_ALL}")
            return []

def finalizar_pedido(id_pedido):
    if Procedures.atualizar_estoque_apos_pedido(id_pedido):
        print(f"{Fore.GREEN}✨ Pedido finalizado com sucesso!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}⚠️ Falha ao finalizar pedido!{Style.RESET_ALL}")
