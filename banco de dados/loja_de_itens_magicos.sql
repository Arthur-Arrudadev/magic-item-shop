Tabelas da Loja de Itens Magicos

----- Tabela de Clientes -----
  
CREATE TABLE Cliente (
id_Cliente INT AUTO_INCREMENT PRIMARY KEY,
nome varchar(255) NOT NULL,
email varchar(255),
data_cadastro date
);

----- Tabela de Produtos -----

CREATE TABLE Produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    tipo VARCHAR(50),
    descricao TEXT
);

----- Tabela de Funcionários -----

CREATE TABLE Funcionario (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    email VARCHAR(100),
    telefone VARCHAR(20)
);

----- Tabela de Encantamentos -----
CREATE TABLE Encantamento (
    id_encantamento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    tipo VARCHAR(50)
);

----- Tabela de Produtos Encantados -----

CREATE TABLE ProdutoEncantamento (
    id_produto INT,
    id_encantamento INT,
    id_encantador INT,
    data_aplicacao DATE,
    PRIMARY KEY (id_produto, id_encantamento),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY (id_encantamento) REFERENCES Encantamento(id_encantamento),
    FOREIGN KEY (id_encantador) REFERENCES Encantador(id_encantador)
);

----- Tabela de Pedidos -----

CREATE TABLE Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_funcionario INT,
    data_pedido DATE NOT NULL,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

----- Tabela de Itens relacionados com o Pedido -----

CREATE TABLE PedidoItem (
    id_pedido INT,
    id_produto INT,
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);

----- Tabela de Fornecedor de Produtos -----

CREATE TABLE Fornecedor (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(100),
    telefone VARCHAR(20)
);

----- Tabela de Estoque -----

CREATE TABLE Estoque (
    id_produto INT PRIMARY KEY,
    quantidade INT NOT NULL,
    id_fornecedor INT,
    data_entrada DATE,
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(id_fornecedor)
);

----- Tabela de Encantadores de produtos -----

CREATE TABLE Encantador (
    id_encantador INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100),
    nivel_magico INT
);

----- Tabela de Categorias -----

CREATE TABLE Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

----- Tabela de Produtos Categorizados -----

CREATE TABLE ProdutoCategoria (
    id_produto INT,
    id_categoria INT,
    PRIMARY KEY (id_produto, id_categoria),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);
