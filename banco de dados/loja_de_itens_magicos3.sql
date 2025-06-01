-- Tabela: Clientes ---

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200)
);

-- Tabela: Produtos ---

CREATE TABLE Produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES CategoriaProdutos(id_categoria)
);

-- Tabela: CategoriaProdutos ---

CREATE TABLE CategoriaProdutos (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(100) NOT NULL,
    descricao TEXT
);

-- Tabela: PedidosClientes ---

CREATE TABLE PedidosClientes (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    data_pedido DATE NOT NULL,
    id_funcionario INT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
);

-- Tabela: ItensDePedidos ---

CREATE TABLE ItensDePedidos (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT,
    id_produto INT,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES PedidosClientes(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

-- Tabela: Estoque ---

CREATE TABLE Estoque (
    id_estoque INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT,
    quantidade_disponivel INT NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

-- Tabela: Funcionarios ---

CREATE TABLE Funcionarios (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    salario DECIMAL(10,2)
);

-- Tabela: Fornecedores ---

CREATE TABLE Fornecedores (
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(100),
    endereco VARCHAR(200)
);

-- Tabela: Receita ---

CREATE TABLE Receita (
    id_receita INT PRIMARY KEY AUTO_INCREMENT,
    tipo ENUM('Entrada', 'Saida') NOT NULL,
    descricao VARCHAR(255),
    valor DECIMAL(10,2) NOT NULL,
    data_movimentacao DATE NOT NULL,
    forma_pagamento VARCHAR(50),
    categoria VARCHAR(100),
    observacao TEXT
);

-- Tabela: AgendamentoDeServicos ---

CREATE TABLE AgendamentoDeServicos (
    id_agendamento INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    tipo_servico VARCHAR(100) NOT NULL,
    data_agendada DATE NOT NULL,
    status VARCHAR(50),
    id_funcionario INT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
);
