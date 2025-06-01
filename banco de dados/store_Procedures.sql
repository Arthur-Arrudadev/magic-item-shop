Stores Procedures baseados no Arquivo loja_de_itens_magicos3.sql

---- Lista os itens de um pedido especifico ----

CREATE DEFINER=`root`@`localhost` PROCEDURE `ItensDoPedido`(
	IN p_id_pedido INT
)
BEGIN
	SELECT p.nome, i.quantidade
    FROM ItensDePedidos i
    JOIN Produtos p ON i.id_produto = p.id_produto
    WHERE i.id_pedido = p_id_pedido;
END

---- Lista todos os produtos registrados no banco ----

CREATE DEFINER=`root`@`localhost` PROCEDURE `ListarProdutos`()
BEGIN
	SELECT * FROM Produtos;
END

---- Lista todos os itens de um pedido de um cliente ----

CREATE DEFINER=`root`@`localhost` PROCEDURE `PedidosPorCliente`(
	IN p_id_cliente INT
)
BEGIN
	SELECT * 
    FROM PedidosClientes
    WHERE id_cliente = p_id_cliente;
END

---- Verifica a quantidades de itens com baixo estoque ----

CREATE DEFINER=`root`@`localhost` PROCEDURE `ProdutosComEstoqueBaixo`(IN limite INT)
BEGIN
    SELECT 
        p.id_produto,
        p.nome,
        e.quantidade_disponivel
    FROM 
        Produtos p
    JOIN 
        Estoque e ON p.id_produto = e.id_produto
    WHERE 
        e.quantidade_disponivel < limite;
END

---- Registra um novo pedido feito por um cliente ----

CREATE DEFINER=`root`@`localhost` PROCEDURE `RegistrarPedido`(
IN p_id_cliente INT,
IN p_data_pedido DATE,
IN p_id_funcionario INT
)
BEGIN
	INSERT INTO PedidosClientes (id_cliente, data_pedido, id_funcionario)
    VALUES (p_id_cliente, p_data_pedido, p_id_funcionario);
END

---- Lista as movimentações financeiras da loja ----

CREATE DEFINER=`root`@`localhost` PROCEDURE `ResumoFinanceiro`(
	IN p_data_inicio DATE,
    IN p_data_fim DATE
)
BEGIN
	SELECT 
        tipo,
        SUM(valor) AS total
    FROM Receita
    WHERE data_movimentacao BETWEEN p_data_inicio AND p_data_fim
    GROUP BY tipo;
END


