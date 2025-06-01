Dados para Testes

---- Tabela de Funcionários ----

INSERT INTO Funcionarios (nome, cargo, salario) VALUES
('Aurélio Magus', 'Atendente', 3000.00),
('Celina Luz', 'Encantadora', 4500.00),
('Darlan Poe', 'Gerente de loja', 5500.00);

---- Tabela de Clientes ----

INSERT INTO Clientes (nome, email, telefone, endereco) VALUES
('Lina Feiticeira', 'lina@exemplo.com', '11999999999', 'Rua das Runas, 101'),
('Théo dos Encantos', 'theo@encantos.com', '21988888888', 'Av. das Magias, 200'),
('Maga Ilhabela', 'ilhabela@magiapura.com', '31977777777', 'Travessa Mística, 300');

---- Tabela de Categoria de Produtos ----

INSERT INTO CategoriaProdutos (nome_categoria, descricao) VALUES
('Poções', 'Substâncias mágicas com efeitos variados'),
('Encantamentos', 'Itens encantados com propriedades especiais'),
('Ingredientes', 'Itens usados na criação de poções ou feitiços'),
('Acessórios Mágicos', 'Amuletos, varinhas, capas e mais');

---- Tabela de produtos ---- 

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção de Cura', 'Recupera vida instantaneamente', 25.50, 1),
('Anel da Invisibilidade', 'Permite ficar invisível por 10 segundos', 150.00, 2),
('Raiz de Mandrágora', 'Ingrediente raro para poções avançadas', 40.00, 3),
('Varinha de Carvalho', 'Usada para canalizar magia elemental', 95.00, 4);

---- Tabela de pedidos ---- 

INSERT INTO PedidosClientes (id_cliente, data_pedido, id_funcionario) VALUES
(1, '2025-05-15', 1),
(2, '2025-05-16', 2);

---- Tabela Itens de Pedidos ---- 

INSERT INTO ItensDePedidos (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 2, 25.50),
(1, 3, 1, 40.00),
(2, 2, 1, 150.00);

---- Tabela de estoque ----

INSERT INTO Estoque (id_produto, quantidade_disponivel) VALUES
(1, 50),
(2, 10),
(3, 25),
(4, 15);

---- Tabela de Fornecedores ----

INSERT INTO Fornecedores (nome, contato, endereco) VALUES
('Alquimia Verde Ltda.', 'alquimia@verde.com', 'Vale das Ervas, 45'),
('Oficina Encantada', 'encantada@magia.com', 'Rua das Fadas, 10');

---- Tabela de receita ----

INSERT INTO Receita (tipo, descricao, valor, data_movimentacao, forma_pagamento, categoria, observacao) VALUES
('Entrada', 'Venda de poções', 51.00, '2025-05-15', 'Dinheiro', 'Vendas', 'Cliente comprou 2 poções'),
('Entrada', 'Venda de anel encantado', 150.00, '2025-05-16', 'Cartão', 'Vendas', ''),
('Saida', 'Compra de ingredientes', 90.00, '2025-05-14', 'Transferência', 'Compras', 'Fornecedor Alquimia Verde');

---- Tabela de agendamento de serviços ----

INSERT INTO AgendamentoDeServicos (id_cliente, tipo_servico, data_agendada, status, id_funcionario) VALUES
(1, 'Consulta de magia', '2025-05-20', 'Agendado', 2),
(3, 'Encantamento de objeto', '2025-05-21', 'Confirmado', 2);
