import sqlite3

from colorama import Fore, Style

"""Cria/conecta ao banco e retorna a conexão"""
def conectar():
    return sqlite3.connect('dados.db')

"""Cria as tabelas se não existirem"""
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100),
        telefone VARCHAR(20),
        endereco VARCHAR(500)
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produtos (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        descricao TEXT,
        preco DECIMAL(10,2) NOT NULL,
        id_categoria INT,
        FOREIGN KEY (id_categoria) REFERENCES CategoriaProdutos(id_categoria)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CategoriaProdutos (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_categoria VARCHAR(100) NOT NULL,
        descricao TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PedidosClientes (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INT,
        data_pedido DATE NOT NULL,
        id_funcionario INT,
        valor_total DECIMAL(10,2) NOT NULL DEFAULT 0.00,
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
        FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ItensDePedidos (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INT,
        id_produto INT,
        quantidade INT NOT NULL,
        preco_unitario DECIMAL(10,2) NOT NULL,
        FOREIGN KEY (id_pedido) REFERENCES PedidosClientes(id_pedido),
        FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estoque (
        id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INT NOT NULL,
        quantidade_disponivel INT NOT NULL,
        FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto),
        UNIQUE (id_produto)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        cargo VARCHAR(50),
        salario DECIMAL(10,2)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fornecedores (
        id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        contato VARCHAR(100),
        endereco VARCHAR(200)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Receita (
        id_receita INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL CHECK (tipo IN ('Entrada', 'Saida')),
        descricao TEXT,
        valor REAL NOT NULL,
        data_movimentacao TEXT NOT NULL,
        forma_pagamento TEXT,
        categoria TEXT,
        observacao TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS AgendamentoDeServicos (
        id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INT,
        tipo_servico VARCHAR(100) NOT NULL,
        data_agendada DATE NOT NULL,
        status VARCHAR(50),
        id_funcionario INT,
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
        FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
    )
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS HistoricoEstoque (
        id_historico INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER,
        quantidade_antes INTEGER,
        quantidade_depois INTEGER,
        data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS HistoricoPrecos (
        id_historico INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER,
        preco_antigo REAL,
        preco_novo REAL,
        data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
    );
    ''')

    #Triggers

    cursor.execute('''DROP TRIGGER IF EXISTS trigger_estoque_update''')

    cursor.execute('''CREATE TRIGGER IF NOT EXISTS trigger_estoque_update
        AFTER UPDATE ON Estoque
        FOR EACH ROW
        WHEN OLD.quantidade_disponivel != NEW.quantidade_disponivel
        BEGIN
            INSERT INTO HistoricoEstoque (id_produto, quantidade_antes, quantidade_depois)
            VALUES (OLD.id_produto, OLD.quantidade_disponivel, NEW.quantidade_disponivel);
        END;
    ''')

    cursor.execute('''DROP TRIGGER IF EXISTS trigger_preco_update''')

    cursor.execute('''CREATE TRIGGER IF NOT EXISTS trigger_preco_update
        AFTER UPDATE ON Produtos
        FOR EACH ROW
        WHEN OLD.preco != NEW.preco
        BEGIN
            INSERT INTO HistoricoPrecos (id_produto, preco_antigo, preco_novo)
            VALUES (OLD.id_produto, OLD.preco, NEW.preco);
        END;
    ''')

    cursor.execute('DROP TRIGGER IF EXISTS trg_registra_receita_pedido_update')

    cursor.execute('''CREATE TRIGGER trg_registra_receita_pedido_update
    AFTER UPDATE OF valor_total ON PedidosClientes
    WHEN NEW.valor_total > 0
    BEGIN
        INSERT INTO Receita (
            data_movimentacao, tipo, valor, descricao, forma_pagamento, categoria, observacao
        )
        VALUES (
            datetime('now', 'localtime'),
            'Entrada',
            NEW.valor_total,
            'Receita do pedido #' || NEW.id_pedido,
            'Desconhecida',
            'Venda de produtos',
            NULL
        );
    END;
    ''')

    cursor.execute('''DROP TRIGGER IF EXISTS trg_remove_receita_zero''')

    cursor.execute('''CREATE TRIGGER IF NOT EXISTS trg_remove_receita_zero
    AFTER UPDATE OF valor_total ON PedidosClientes
    WHEN NEW.valor_total > 0
    BEGIN
        DELETE FROM Receita
        WHERE descricao = 'Receita do pedido #' || NEW.id_pedido
        AND valor = 0;
    END;
    ''')

    conn.commit()
    conn.close()


class Procedures:
    @staticmethod
    def atualizar_estoque_apos_pedido(id_pedido: int):
        """Procedure: Atualiza o estoque quando um pedido é finalizado"""
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            # 1. Busca os itens do pedido
            cursor.execute('''
                SELECT id_produto, quantidade 
                FROM ItensDePedidos 
                WHERE id_pedido = ?
            ''', (id_pedido,))
            itens = cursor.fetchall()

            # 2. Para cada item, atualiza o estoque
            for id_produto, quantidade in itens:
                cursor.execute('''
                    UPDATE Estoque 
                    SET quantidade_disponivel = quantidade_disponivel - ?
                    WHERE id_produto = ?
                ''', (quantidade, id_produto))

            conn.commit()
            print(f"{Fore.GREEN}✅ Estoque atualizado para o pedido {id_pedido}!{Style.RESET_ALL}")
            return True

        except sqlite3.Error as e:
            conn.rollback()
            print(f"{Fore.RED}⚠️ Falha ao atualizar estoque: {e}{Style.RESET_ALL}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def calcular_media_mensal(tipo: str, meses: int = 6):
        """Procedure: Calcula média mensal de entradas/saídas"""
        try:
            with conectar() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT 
                        strftime('%Y-%m', data_movimentacao) as mes,
                        AVG(valor) as media
                    FROM Receita
                    WHERE tipo = ? 
                    AND data_movimentacao >= date('now', ?)
                    GROUP BY mes
                    ORDER BY mes DESC
                ''', (tipo, f'-{meses} months'))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro na procedure: {e}{Style.RESET_ALL}")
            return []

    @staticmethod
    def gerar_relatorio_financeiro_anual(ano: int):
        """Procedure: Relatório completo com entradas, saídas e saldo mensal"""
        try:
            with conectar() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT 
                        strftime('%m', data_movimentacao) as mes,
                        SUM(CASE WHEN tipo = 'Entrada' THEN valor ELSE 0 END) as entradas,
                        SUM(CASE WHEN tipo = 'Saida' THEN valor ELSE 0 END) as saidas,
                        SUM(valor) as saldo
                    FROM Receita
                    WHERE strftime('%Y', data_movimentacao) = ?
                    GROUP BY mes
                    ORDER BY mes
                ''', (str(ano),))

                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro no relatório anual: {e}{Style.RESET_ALL}")
            return []

    @staticmethod
    def adicionar_ao_estoque(id_produto: int, quantidade: int) -> bool:
        """
        Simula a procedure AdicionarAoEstoque
        Parâmetros:
            id_produto (int): ID do produto
            quantidade (int): Quantidade a adicionar (pode ser negativo para remover)
        Retorna:
            bool: True se bem-sucedido, False se falhar
        """
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            # Verifica se o produto existe
            cursor.execute('SELECT id_produto FROM Produtos WHERE id_produto = ?', (id_produto,))
            if not cursor.fetchone():
                print(f"{Fore.RED}⚠️ Produto não encontrado!{Style.RESET_ALL}")
                return False

            # Atualiza o estoque (usando SQL idêntico à sua procedure)
            cursor.execute('''
                    UPDATE Estoque
                    SET quantidade_disponivel = quantidade_disponivel + ?
                    WHERE id_produto = ?
                ''', (quantidade, id_produto))

            # Se não existir registro, cria um novo
            if cursor.rowcount == 0:
                cursor.execute('''
                        INSERT INTO Estoque (id_produto, quantidade_disponivel)
                        VALUES (?, ?)
                    ''', (id_produto, quantidade))

            conn.commit()
            print(f"{Fore.GREEN}✅ Estoque atualizado! Produto {id_produto}: {quantidade:+} unidades{Style.RESET_ALL}")
            return True

        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Falha na procedure: {e}{Style.RESET_ALL}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def atualizar_preco_produto(id_produto: int, novo_preco: float):
        """Atualiza preço e recalcula valor do estoque - VERSÃO CORRIGIDA"""
        try:
            with conectar() as conn:
                cursor = conn.cursor()

                # 1. Atualiza preço na tabela Produtos
                cursor.execute('''
                    UPDATE Produtos 
                    SET preco = ? 
                    WHERE id_produto = ?
                ''', (novo_preco, id_produto))

                conn.commit()
                print(f"{Fore.GREEN}✅ Preço e valor de estoque atualizados!{Style.RESET_ALL}")
                return True

        except sqlite3.Error as e:
            print(f"{Fore.RED}⚠️ Erro na procedure: {e}{Style.RESET_ALL}")
            return False
