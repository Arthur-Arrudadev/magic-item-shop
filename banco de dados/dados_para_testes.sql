Dados para Testes

---- Tabela de Funcionários ----

INSERT INTO Funcionarios (nome, cargo, salario) VALUES
('Aurélio Magus', 'Atendente', 3000.00),
('Celina Luz', 'Encantadora', 4500.00),
('Darlan Poe', 'Gerente de loja', 5500.00),
('Morgana Stradivarius', 'Encantadora', 5000.00),
('Jorgin Marrelo', 'Atendente', 1400.00);

---- Tabela de Clientes ----

INSERT INTO Clientes (nome, email, telefone, endereco) VALUES
('Lina Feiticeira', 'lina@exemplo.com', '11999999999', 'Rua das Runas, 101'),
('Théo dos Encantos', 'theo@encantos.com', '21988888888', 'Av. das Magias, 200'),
('Maga Ilhabela', 'ilhabela@magiapura.com', '31977777777', 'Travessa Mística, 300');

INSERT INTO Clientes (nome, email, telefone, endereco) VALUES
('Eldrin, o Feiticeiro Arcano', 'eldrin.arcano@magia.com', '(11) 90000-1111', 'Torre de Cristal, Rua das Runas, 13, Aldeia Mística'),
('Lyria Sombravale, Caçadora de Sombras', 'lyria.sombra@aventura.com', '(21) 91111-2222', 'Bosque das Almas Perdidas, Casa 7, Reino de Eldoria'),
('Thalor, Guardião dos Segredos', 'thalor.segredos@oraculo.com', '(31) 92222-3333', 'Fortaleza de Ferro, Setor Norte, Cidade das Estrelas'),
('Mira Luzdourada, Clériga da Aurora', 'mira.luz@templomagia.com', '(41) 93333-4444', 'Templo do Sol, Av. da Divindade, 45, Vale Sagrado'),
('Gorrim Martelo-de-Ferro, Ferreiro Épico', 'gorrim.ferreiro@forja.com', '(51) 94444-5555', 'Distrito das Forjas, Rua do Martelo, 9, Montanhas do Norte'),
('Seraphina, Alquimista do Crepúsculo', 'seraphina.crepusculo@poço.com', '(61) 95555-6666', 'Cabana da Névoa, Lago Sombrio, Floresta Encantada'),
('Darius, o Andarilho das Planícies', 'darius.planicies@aventura.com', '(71) 96666-7777', 'Campina dos Ventos, Estrada Real, 12, Reino de Valen'),
('Elyra Vento-prateado, Mensageira Celestial', 'elyra.celestial@alados.com', '(81) 97777-8888', 'Ninho das Águias, Picos Altos, Terra dos Céus'),
('Kaelen Sussurro-noturno, Mestre dos Espiões', 'kaelen.espiao@sombras.com', '(85) 98888-9999', 'Beco das Serpentes, Número 13, Cidade Velha'),
('Thalia, a Guardiã das Relíquias', 'thalia.relics@magia.com', '(27) 99999-0000', 'Castelo das Lendas, Torre Oeste, Reino de Eldoria');


---- Tabela de Categoria de Produtos ----

INSERT INTO CategoriaProdutos (nome_categoria, descricao) VALUES
('Poções', 'Substâncias mágicas com efeitos variados'),
('Encantamentos', 'Itens encantados com propriedades especiais'),
('Ingredientes', 'Itens usados na criação de poções ou feitiços'),
('Acessórios Mágicos', 'Amuletos, varinhas, capas e mais');

INSERT INTO CategoriaProdutos (nome_categoria, descricao) VALUES
('Armas Mágicas', 'Armas imbuídas com poder mágico'),
('Livros de Magia', 'Tomo contendo feitiços e rituais'),
('Artefatos Antigos', 'Relíquias de poder desconhecido'),
('Vestimentas Místicas', 'Roupas encantadas com propriedades especiais');

---- Tabela de produtos ---- 

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção de Cura', 'Recupera vida instantaneamente', 25.50, 1),
('Anel da Invisibilidade', 'Permite ficar invisível por 10 segundos', 150.00, 2),
('Raiz de Mandrágora', 'Ingrediente raro para poções avançadas', 40.00, 3),
('Varinha de Carvalho', 'Usada para canalizar magia elemental', 95.00, 4);

INSERT INTO Produtos (nome, descricao, preco, id_categoria)
VALUES ('Pedra Mágica', 'Aumenta resistência mágica', 150.00, 1);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Espada Flamejante', 'Causa dano de fogo adicional aos inimigos', 200.00, 5),
('Grimório de Necromancia', 'Contém feitiços de invocação de mortos', 300.00, 6),
('Orbe do Caos', 'Artefato que altera a realidade ao acaso', 500.00, 7),
('Manto da Sombra', 'Concede furtividade aumentada à noite', 120.00, 8),
('Adaga do Vento', 'Permite ataques rápidos com rajadas de ar', 180.00, 5),
('Tomo de Ilusões', 'Ensina magias de disfarce e miragens', 150.00, 6),
('Relógio do Tempo Esquecido', 'Congela o tempo por breves instantes', 800.00, 7),
('Botas da Leveza', 'Permite andar sobre a água e neve sem afundar', 90.00, 8);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção da Brisa Ligeira', 'Aumenta a velocidade de movimento por 30 segundos', 35.00, 1),
('Amuleto dos Ventos Uivantes', 'Gera uma rajada de vento que repele inimigos', 160.00, 2),
('Espada dos Céus', 'Lâmina leve que desferre cortes acompanhados de vento', 220.00, 5),
('Tomo dos Quatro Ventos', 'Permite controlar as direções do vento para manipular o campo de batalha', 275.00, 6),
('Capa das Correntes Aéreas', 'Permite flutuar levemente e reduzir dano de queda', 130.00, 8),
('Orbe da Tempestade', 'Lança uma microtempestade de vento ao ser ativado', 450.00, 7),
('Elixir do Sopro Vital', 'Revigora a respiração e restaura fôlego em combates longos', 28.00, 1),
('Chicote Aéreo', 'Arma feita com fios encantados, usada para manipular vento em combate', 190.00, 5),
('Anel do Redemoinho', 'Cria um pequeno ciclone ao redor do usuário por alguns segundos', 145.00, 2),
('Py K das Galaxias', 'Faz com que qualquer alvo se apaixone pelo usuário por até 24h', 1000.00, 1),
('Botas dos Ventos Alísios', 'Concede um bônus de agilidade e permite correr em superfícies instáveis', 110.00, 8);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção da Pele de Pedra', 'Endurece a pele, aumentando a defesa por 1 minuto', 38.00, 1),
('Anel da Estabilidade', 'Previne quedas e empurrões com magia de ancoragem', 140.00, 2),
('Martelo da Montanha', 'Arma pesada que causa tremores no impacto', 260.00, 5),
('Grimório de Geomancia', 'Contém feitiços de manipulação de rochas e solo', 290.00, 6),
('Cinturão do Guardião de Pedra', 'Aumenta a força física e resistência a ataques físicos', 115.00, 8),
('Totem da Terra Antiga', 'Cria uma barreira de pedra protetora ao ser ativado', 400.00, 7),
('Raiz Viva', 'Ingrediente mágico que pulsa com energia telúrica', 45.00, 3),
('Bastão do Terratremor', 'Canaliza ondas sísmicas que desestabilizam inimigos', 210.00, 4),
('Botas de Rocha Firme', 'Evita escorregões e concede vantagem em terrenos instáveis', 95.00, 8),
('Amuleto da Mãe Terra', 'Recupera lentamente pontos de vida enquanto estiver em contato com o solo', 170.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção da Fúria Ígnea', 'Aumenta o poder de ataque com dano de fogo por 30 segundos', 42.00, 1),
('Anel das Chamas Eternas', 'Envolve o usuário com uma aura flamejante que causa dano em área', 180.00, 2),
('Espada Vulcânica', 'Lâmina que incendeia inimigos com cada golpe', 270.00, 5),
('Livro do Inferno Rúnico', 'Contém rituais de invocação de chamas infernais', 310.00, 6),
('Manto do Salamandra', 'Reduz significativamente o dano de fogo recebido', 135.00, 8),
('Coração Ardente', 'Artefato que libera uma explosão flamejante ao comando', 480.00, 7),
('Cinza de Dragão', 'Ingrediente lendário usado em poções de fogo poderoso', 55.00, 3),
('Cajado do Sol Poente', 'Dispara projéteis de fogo concentrado', 230.00, 4),
('Botas de Cinza Viva', 'Deixam rastros de brasas ao andar, causando dano a perseguidores', 100.00, 8),
('Amuleto da Chama Sussurrante', 'Permite comunicação com entidades do fogo', 160.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção da Respiração Aquática', 'Permite respirar debaixo d\'água por 5 minutos', 37.00, 1),
('Anel da Correnteza', 'Aumenta a velocidade de movimento dentro da água', 150.00, 2),
('Tridente das Marés', 'Arma que invoca ondas e causa dano hídrico', 250.00, 5),
('Tomo das Profundezas', 'Contém feitiços de controle da água e invocação aquática', 290.00, 6),
('Manto da Névoa Marinha', 'Envolve o usuário em névoa que dificulta ser detectado', 120.00, 8),
('Frasco da Água Primordial', 'Artefato ancestral que purifica ou destrói com o toque', 470.00, 7),
('Alga Brilhante de Lúmen', 'Ingrediente raro que brilha ao contato com água', 48.00, 3),
('Cajado da Maré Alta', 'Conjura jatos e espirais de água contra os inimigos', 215.00, 4),
('Botas das Águas Calmas', 'Permite caminhar sobre a superfície da água por breves instantes', 98.00, 8),
('Amuleto da Lagrima Sagrada', 'Cura lentamente ferimentos enquanto o portador estiver molhado', 155.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção da Agilidade Elétrica', 'Aumenta a velocidade de reação e reflexos por 30 segundos', 40.00, 1),
('Anel da Faísca Contínua', 'Libera pequenas descargas elétricas contra inimigos próximos', 170.00, 2),
('Lança Trovejante', 'Arma que invoca um raio ao atingir o alvo', 265.00, 5),
('Grimório do Relâmpago Celeste', 'Contém feitiços de raio e invocação de tempestades', 300.00, 6),
('Manto da Tempestade', 'Dissipa eletricidade ao redor e reduz dano elétrico recebido', 125.00, 8),
('Orbe do Trovão', 'Explode em uma área com uma descarga devastadora', 490.00, 7),
('Cristal de Raio Concentrado', 'Ingrediente instável usado em poções e encantamentos elétricos', 52.00, 3),
('Bastão de Zeus', 'Conjura raios diretamente do céu com precisão mortal', 240.00, 4),
('Botas do Estalo Veloz', 'Aumenta drasticamente a velocidade ao correr em linha reta', 105.00, 8),
('Amuleto da Carga Estática', 'Acumula energia elétrica e a descarrega em ataques físicos', 160.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção do Toque Congelante', 'Faz com que ataques corpo a corpo causem dano de gelo por 30 segundos', 39.00, 1),
('Anel da Geada Silenciosa', 'Cria um campo gelado que reduz a velocidade de inimigos próximos', 165.00, 2),
('Machado Glacial', 'Causa dano físico e congela o alvo por alguns segundos', 255.00, 5),
('Tomo da Nevasca Arcana', 'Permite conjurar tempestades de neve e picos de gelo', 305.00, 6),
('Manto do Ártico', 'Concede resistência ao frio extremo e efeitos de congelamento', 128.00, 8),
('Estilhaço do Coração Invernal', 'Artefato raro que congela tudo ao redor quando ativado', 495.00, 7),
('Essência de Neve Eterna', 'Ingrediente mágico usado em encantamentos de gelo duradouros', 47.00, 3),
('Cajado do Inverno Profundo', 'Lança lanças de gelo e pode prender inimigos no lugar', 235.00, 4),
('Botas da Passagem Congelada', 'Permite caminhar sobre superfícies escorregadias sem perder equilíbrio', 92.00, 8),
('Amuleto da Tempestade Gélida', 'Libera uma rajada congelante quando o portador está em perigo', 155.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção da Luminância Interior', 'Energiza o corpo com luz pura, curando gradualmente por 1 minuto', 43.00, 1),
('Anel do Amanhecer', 'Emite um brilho sagrado que afasta criaturas das trevas', 175.00, 2),
('Espada Solar', 'Lâmina radiante que causa dano adicional a mortos-vivos e demônios', 285.00, 5),
('Tomo da Luz Celestial', 'Contém magias de cura, purificação e revelação de ilusões', 320.00, 6),
('Manto do Arcanjo', 'Cria uma aura de proteção luminosa ao redor do usuário', 140.00, 8),
('Cristal do Sol Nascente', 'Artefato que emite uma onda de luz purificadora ao ser ativado', 500.00, 7),
('Pétala de Flor Solar', 'Ingrediente raro usado em poções de cura e encantamentos de luz', 49.00, 3),
('Cajado da Aurora', 'Conjura feixes de luz que causam dano e curam aliados próximos', 245.00, 4),
('Botas da Luz Veloz', 'Permite movimentos rápidos e silenciosos em áreas escuras', 97.00, 8),
('Amuleto da Revelação', 'Revela criaturas ocultas e magias ilusórias nas proximidades', 160.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção da Invisibilidade Sombria', 'Oculta o usuário nas sombras por 20 segundos', 44.00, 1),
('Anel da Escuridão Fluida', 'Permite atravessar brevemente paredes finas em ambientes escuros', 185.00, 2),
('Lâmina do Eclipse', 'Arma que causa dano sombrio e pode cegar temporariamente o inimigo', 275.00, 5),
('Grimório das Sombras Profundas', 'Contém magias de ocultação, corrupção e controle da escuridão', 330.00, 6),
('Manto da Noite Infinda', 'Envolve o usuário em trevas, tornando difícil ser detectado', 138.00, 8),
('Olho de Tenebris', 'Artefato que permite enxergar e se comunicar com entidades do vazio', 520.00, 7),
('Semente do Crepúsculo', 'Ingrediente sombrio usado em rituais e alquimia de necromancia', 53.00, 3),
('Cajado do Véu Negro', 'Dispersa névoas negras que desorientam inimigos', 240.00, 4),
('Botas do Silêncio Absoluto', 'Anulam o som dos passos em qualquer terreno', 99.00, 8),
('Amuleto do Eclipse Total', 'Ativa uma aura de escuridão que reduz a precisão de ataques inimigos', 165.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção do Sangue Negro', 'Concede resistência a magia sombria e aumenta poder necromântico por 1 minuto', 48.00, 1),
('Anel do Lamento Eterno', 'Permite escutar sussurros dos mortos e encontrar cadáveres ocultos', 190.00, 2),
('Foice das Almas', 'Arma que coleta fragmentos de alma a cada inimigo derrotado', 295.00, 5),
('Grimório dos Mortos-Vivos', 'Contém feitiços de reanimação, comando de zumbis e invocação de esqueletos', 345.00, 6),
('Túnica do Cultista Esquecido', 'Reduz o custo de magia sombria e oculta o portador em cemitérios', 135.00, 8),
('Crânio de Lich Ancestral', 'Artefato que permite lançar uma magia necromântica extra por dia', 525.00, 7),
('Fêmur de Dragão Espectral', 'Ingrediente usado em rituais poderosos de ressurreição corrompida', 58.00, 3),
('Cajado da Morte Silenciosa', 'Libera uma aura de decadência que enfraquece todos ao redor', 255.00, 4),
('Botas do Cemitério Sombrio', 'Permite andar silenciosamente entre os mortos sem ser notado', 100.00, 8),
('Amuleto da Alma Fragmentada', 'Guarda uma alma presa, usada como foco para magias de controle e maldição', 170.00, 2);

INSERT INTO Produtos (nome, descricao, preco, id_categoria) VALUES
('Poção do Veneno Paralizante', 'Causa paralisia temporária no alvo por 15 segundos', 45.00, 1),
('Anel do Tóxico Silencioso', 'Libera uma névoa venenosa ao redor do usuário quando ativado', 180.00, 2),
('Adaga Venenosa', 'Arma com lâmina revestida de veneno letal, causando dano contínuo', 270.00, 5),
('Manual dos Toxins', 'Livro que ensina receitas e usos de venenos variados', 310.00, 6),
('Capa do Escorpião', 'Concede resistência a venenos e ataques tóxicos', 130.00, 8),
('Frasco do Veneno Mortal', 'Artefato que contém um veneno poderoso, capaz de matar em minutos', 490.00, 7),
('Folha de Belladona', 'Ingrediente venenoso usado em poções e armadilhas', 50.00, 3),
('Cajado do Venenoso', 'Projeta dardos envenenados que corroem a armadura inimiga', 220.00, 4),
('Botas da Passada Silenciosa', 'Permitem se mover sem fazer barulho e deixam um rastro venenoso', 100.00, 8),
('Amuleto da Cura Tóxica', 'Converte parte do dano recebido em energia vital', 160.00, 2);
  
---- Tabela de pedidos ---- 

INSERT INTO PedidosClientes (id_cliente, data_pedido, id_funcionario, valor_total) VALUES
(1, '2025-05-15', 1),
(2, '2025-05-16', 2);

INSERT INTO PedidosClientes (id_cliente, data_pedido, id_funcionario, valor_total) VALUES
(1, '2025-06-01', 1, 200.00),
(2, '2025-06-02', 2, 500.00),
(3, '2025-06-03', 3, 320.00),
(4, '2025-06-04', 1, 150.00),
(5, '2025-06-05', 2, 430.00),
(6, '2025-06-06', 3, 610.00);


---- Tabela Itens de Pedidos ---- 

INSERT INTO ItensDePedidos (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 2, 25.50),
(1, 3, 1, 40.00),
(2, 2, 1, 150.00);

INSERT INTO ItensDePedidos (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 2, 25.50),    -- Poção de Cura
(1, 6, 1, 150.00),   -- Anel da Invisibilidade
(2, 12, 3, 44.00),   -- Poção da Invisibilidade Sombria
(2, 14, 1, 275.00),  -- Lâmina do Eclipse
(5, 20, 2, 285.00),  -- Espada Solar
(5, 23, 1, 320.00),  -- Tomo da Luz Celestial
(6, 28, 4, 48.00),   -- Poção do Sangue Negro
(6, 31, 1, 295.00),  -- Foice das Almas
(7, 38, 2, 45.00),   -- Poção do Veneno Paralizante
(7, 40, 1, 270.00),  -- Adaga Venenosa
(9, 2, 5, 43.00),    -- Poção da Luminância Interior
(12, 5, 1, 175.00);  -- Anel do Amanhecer


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

INSERT INTO Receita (tipo, descricao, valor, data_movimentacao, forma_pagamento, categoria, observacao)
VALUES ('Saida', 'Compra de material', 150.00, CURDATE(), 'Cartão', 'Estoque', 'Compra de poções');


---- Tabela de agendamento de serviços ----

INSERT INTO AgendamentoDeServicos (id_cliente, tipo_servico, data_agendada, status, id_funcionario) VALUES
(1, 'Consulta de magia', '2025-05-20', 'Agendado', 2),
(3, 'Encantamento de objeto', '2025-05-21', 'Confirmado', 2);
