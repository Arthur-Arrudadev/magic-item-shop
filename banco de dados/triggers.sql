---- Registra_receita_pedido ----
Insere automaticamente uma nova linha na tabela receita sem que um novo pedido é feito 

CREATE TRIGGER trg_registra_receita_pedido
AFTER INSERT ON PedidosClientes
FOR EACH ROW
BEGIN
    INSERT INTO Receita (
        data_movimentacao, tipo, valor, descricao, forma_pagamento, categoria, observacao
    )
    VALUES (
        NOW(),
        'Entrada',
        NEW.valor_total,
        CONCAT('Receita do pedido #', NEW.id_pedido),
        'Desconhecida',
        'Venda de produtos',
        NULL
    );
END;

---- Atualiza_estoque_apos_pedido ----
Atualiza o estoque ao inserir o item no pedido

CREATE TRIGGER trg_atualiza_estoque_apos_pedido
AFTER INSERT ON ItensDePedidos
FOR EACH ROW
BEGIN
    UPDATE Estoque
    SET quantidade_disponivel = quantidade_disponivel - NEW.quantidade
    WHERE id_produto = NEW.id_produto;
END;

---- Inserir_estoque_apos_produto ---- 
Sempre que um novo produto for inserido na tabela produto, a trigger verifica se
ele já existe na tabela estoque, e se não existir ela o insere automaticamente com a quantidade 0

CREATE TRIGGER trg_inserir_estoque_apos_produto
AFTER INSERT ON Produtos
FOR EACH ROW
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM Estoque WHERE id_produto = NEW.id_produto
    ) THEN
        INSERT INTO Estoque (id_produto, quantidade_disponivel)
        VALUES (NEW.id_produto, 0);
    END IF;
END

---- Verifica_estoque ----
Envia uma mensagem quando não se tem estoque suficiente para fazer o pedido

CREATE TRIGGER trg_verifica_estoque
BEFORE INSERT ON ItensDePedidos
FOR EACH ROW
BEGIN
    DECLARE qtd_atual INT;
    SELECT quantidade_disponivel INTO qtd_atual FROM Estoque WHERE id_produto = NEW.id_produto;
    
    IF qtd_atual < NEW.quantidade THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Estoque insuficiente para esse pedido!';
    END IF;
END;
