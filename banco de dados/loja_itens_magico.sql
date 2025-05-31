SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- Banco de dados: `loja_itens_magico
-- Estrutura para tabela `categorias`

CREATE TABLE `categorias` (
  `categoria_id` int(11) NOT NULL
  , `nome` varchar(50) NOT NULL
  , `descricao` text DEFAULT NULL
  , `restricao_nivel` int(11) DEFAULT 1
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- --------------------------------------------------------

-- Estrutura para tabela `clientes`


CREATE TABLE `clientes` (
  `cliente_id` int(11) NOT NULL
  , `nome` varchar(100) NOT NULL
  , `email` varchar(100) DEFAULT NULL
  , `data_nascimento` date DEFAULT NULL
  , `nivel_magia` int(11) DEFAULT 1
  , `saldo_ouro` decimal(10, 2) DEFAULT 0.00
  , `data_cadastro` datetime DEFAULT current_timestamp()
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `clientes_missoes`
  --
  CREATE TABLE `clientes_missoes` (
    `cliente_id` int(11) NOT NULL
    , `missao_id` int(11) NOT NULL
    , `data_inicio` datetime NOT NULL DEFAULT current_timestamp()
    , `data_conclusao` datetime DEFAULT NULL
    , `status` enum('Ativa', 'Concluída', 'Fracassada') DEFAULT 'Ativa'
    , `avaliacao` int(11) DEFAULT NULL CHECK (
      `avaliacao` between 1 and 5
    )
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `encantamentos`
  --
  CREATE TABLE `encantamentos` (
    `encantamento_id` int(11) NOT NULL
    , `nome` varchar(50) NOT NULL
    , `descricao` text DEFAULT NULL
    , `efeito` text NOT NULL
    , `nivel_requerido` int(11) DEFAULT 1
    , `custo_mana` decimal(6, 2) NOT NULL
    , `duracao` varchar(30) DEFAULT NULL
    , `escola_magia` varchar(30) NOT NULL
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `fornecedores`
  --
  CREATE TABLE `fornecedores` (
    `fornecedor_id` int(11) NOT NULL
    , `nome` varchar(100) NOT NULL
    , `reino_origem` varchar(50) DEFAULT NULL
    , `especialidade` varchar(50) DEFAULT NULL
    , `contato` varchar(100) DEFAULT NULL
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `funcionarios`
  --
  CREATE TABLE `funcionarios` (
    `funcionario_id` int(11) NOT NULL
    , `nome` varchar(100) NOT NULL
    , `cargo` varchar(50) NOT NULL
    , `nivel_acesso` int(11) NOT NULL
    , `data_contratacao` date NOT NULL
    , `salario` decimal(10, 2) NOT NULL
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `historico_compras_clientes`
  --
  CREATE TABLE `historico_compras_clientes` (
    `historico_id` int(11) NOT NULL
    , `cliente_id` int(11) NOT NULL
    , `item_id` int(11) NOT NULL
    , `data_compra` datetime DEFAULT current_timestamp()
    , `quantidade` int(11) NOT NULL
    , `preco_unitario` decimal(10, 2) NOT NULL
    , `venda_id` int(11) DEFAULT NULL
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `itensmagicos`
  --
  CREATE TABLE `itensmagicos` (
    `item_id` int(11) NOT NULL
    , `nome` varchar(100) NOT NULL
    , `descricao` text DEFAULT NULL
    , `preco` decimal(10, 2) NOT NULL
    , `estoque` int(11) NOT NULL DEFAULT 0
    , `categoria_id` int(11) DEFAULT NULL
    , `fornecedor_id` int(11) DEFAULT NULL
    , `data_fabricacao` date DEFAULT NULL
    , `potencia_magica` int(11) DEFAULT NULL
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `itens_encantamentos`
  --
  CREATE TABLE `itens_encantamentos` (
    `item_id` int(11) NOT NULL
    , `encantamento_id` int(11) NOT NULL
    , `intensidade` int(11) DEFAULT 1
    , `data_aplicacao` datetime DEFAULT current_timestamp()
    , `mestre_encantador_id` int(11) DEFAULT NULL
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `missoes`
  --
  CREATE TABLE `missoes` (
    `missao_id` int(11) NOT NULL
    , `titulo` varchar(100) NOT NULL
    , `descricao` text DEFAULT NULL
    , `recompensa` decimal(10, 2) NOT NULL
    , `nivel_requerido` int(11) DEFAULT 1
    , `duracao_estimada` varchar(50) DEFAULT NULL
    , `tipo_missao` varchar(30) NOT NULL
  )
  -- --------------------------------------------------------
  --
  -- Estrutura para tabela `vendas`
  --
  CREATE TABLE `vendas` (
    `venda_id` int(11) NOT NULL
    , `cliente_id` int(11) NOT NULL
    , `funcionario_id` int(11) NOT NULL
    , `data_venda` datetime DEFAULT current_timestamp()
    , `total` decimal(10, 2) NOT NULL
    , `forma_pagamento` varchar(50) DEFAULT NULL
  )
  --
  -- Índices para tabelas despejadas
  --
  --
  -- Índices de tabela `categorias`
  --
  ALTER TABLE `categorias`
  ADD PRIMARY KEY (`categoria_id`);

  --
  -- Índices de tabela `clientes`
  --
  ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cliente_id`)
  , ADD UNIQUE KEY `email` (`email`);

  --
  -- Índices de tabela `clientes_missoes`
  --
  ALTER TABLE `clientes_missoes`
  ADD PRIMARY KEY (`cliente_id`, `missao_id`, `data_inicio`)
  , ADD KEY `missao_id` (`missao_id`);

  --
  -- Índices de tabela `encantamentos`
  --
  ALTER TABLE `encantamentos`
  ADD PRIMARY KEY (`encantamento_id`);

  --
  -- Índices de tabela `fornecedores`
  --
  ALTER TABLE `fornecedores`
  ADD PRIMARY KEY (`fornecedor_id`);

  --
  -- Índices de tabela `funcionarios`
  --
  ALTER TABLE `funcionarios`
  ADD PRIMARY KEY (`funcionario_id`);

  --
  -- Índices de tabela `historico_compras_clientes`
  --
  ALTER TABLE `historico_compras_clientes`
  ADD PRIMARY KEY (`historico_id`)
  , ADD KEY `cliente_id` (`cliente_id`)
  , ADD KEY `item_id` (`item_id`)
  , ADD KEY `venda_id` (`venda_id`);

  --
  -- Índices de tabela `itensmagicos`
  --
  ALTER TABLE `itensmagicos`
  ADD PRIMARY KEY (`item_id`)
  , ADD KEY `categoria_id` (`categoria_id`)
  , ADD KEY `fornecedor_id` (`fornecedor_id`);

  --
  -- Índices de tabela `itens_encantamentos`
  --
  ALTER TABLE `itens_encantamentos`
  ADD PRIMARY KEY (`item_id`, `encantamento_id`)
  , ADD KEY `encantamento_id` (`encantamento_id`)
  , ADD KEY `mestre_encantador_id` (`mestre_encantador_id`);

  --
  -- Índices de tabela `missoes`
  --
  ALTER TABLE `missoes`
  ADD PRIMARY KEY (`missao_id`);

  --
  -- Índices de tabela `vendas`
  --
  ALTER TABLE `vendas`
  ADD PRIMARY KEY (`venda_id`)
  , ADD KEY `cliente_id` (`cliente_id`)
  , ADD KEY `funcionario_id` (`funcionario_id`);

  --
  -- AUTO_INCREMENT para tabelas despejadas
  --

  --
  -- AUTO_INCREMENT de tabela `categorias`
  --
  ALTER TABLE `categorias` MODIFY `categoria_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `clientes`
  --
  ALTER TABLE `clientes` MODIFY `cliente_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `encantamentos`
  --
  ALTER TABLE `encantamentos` MODIFY `encantamento_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `fornecedores`
  --
  ALTER TABLE `fornecedores` MODIFY `fornecedor_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `funcionarios`
  --
  ALTER TABLE `funcionarios` MODIFY `funcionario_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `historico_compras_clientes`
  --
  ALTER TABLE `historico_compras_clientes` MODIFY `historico_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `itensmagicos`
  --
  ALTER TABLE `itensmagicos` MODIFY `item_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `missoes`
  --
  ALTER TABLE `missoes` MODIFY `missao_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de tabela `vendas`
  --
  ALTER TABLE `vendas` MODIFY `venda_id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- Restrições para tabelas despejadas
  --

  --
  -- Restrições para tabelas `clientes_missoes`
  --
  ALTER TABLE `clientes_missoes`
  ADD CONSTRAINT `clientes_missoes_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`)
  , ADD CONSTRAINT `clientes_missoes_ibfk_2` FOREIGN KEY (`missao_id`) REFERENCES `missoes` (`missao_id`);

  --
  -- Restrições para tabelas `historico_compras_clientes`
  --
  ALTER TABLE `historico_compras_clientes`
  ADD CONSTRAINT `historico_compras_clientes_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`)
  , ADD CONSTRAINT `historico_compras_clientes_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `itensmagicos` (`item_id`)
  , ADD CONSTRAINT `historico_compras_clientes_ibfk_3` FOREIGN KEY (`venda_id`) REFERENCES `vendas` (`venda_id`)
  ON DELETE SET NULL;

  --
  -- Restrições para tabelas `itensmagicos`
  --
  ALTER TABLE `itensmagicos`
  ADD CONSTRAINT `itensmagicos_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`categoria_id`)
  , ADD CONSTRAINT `itensmagicos_ibfk_2` FOREIGN KEY (`fornecedor_id`) REFERENCES `fornecedores` (`fornecedor_id`);

  --
  -- Restrições para tabelas `itens_encantamentos`
  --
  ALTER TABLE `itens_encantamentos`
  ADD CONSTRAINT `itens_encantamentos_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `itensmagicos` (`item_id`)
  ON DELETE CASCADE
  , ADD CONSTRAINT `itens_encantamentos_ibfk_2` FOREIGN KEY (`encantamento_id`) REFERENCES `encantamentos` (`encantamento_id`)
  , ADD CONSTRAINT `itens_encantamentos_ibfk_3` FOREIGN KEY (`mestre_encantador_id`) REFERENCES `funcionarios` (`funcionario_id`);

  --
  -- Restrições para tabelas `vendas`
  --
  ALTER TABLE `vendas`
  ADD CONSTRAINT `vendas_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`)
  , ADD CONSTRAINT `vendas_ibfk_2` FOREIGN KEY (`funcionario_id`) REFERENCES `funcionarios` (`funcionario_id`);
  COMMIT;

  /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */
;
  /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */
;
  /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */
;