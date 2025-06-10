# magic-item-shop

Sistema de Gestão Comercial

Descrição do Projeto

Este projeto consiste na modelagem de um banco de dados para um sistema de gestão comercial. Ele abrange funcionalidades como controle de clientes, produtos, pedidos, estoque, finanças, agendamentos de serviços, funcionários e fornecedores.

O objetivo é fornecer uma base sólida para sistemas de vendas, gerenciamento de estoque, agendamentos e controle financeiro.

Autores

* Nome: Ana Luzia Leão 
  Email: aninha_brasil1992@hotmail.com
- Nome: Arthur Arruda
  Email: arthur.arrudasait@gmail.com
- Nome: Meryellen G. Nascimento  
  Email: mgn5@discente.ifpe.edu.br

Estrutura do Projeto

Tabelas Principais

- Clientes: Informações dos clientes (nome, e-mail, telefone, endereço).
- Produtos: Dados dos produtos, preço e categoria.
- CategoriaProdutos: Classificação dos produtos por categoria.
- PedidosClientes: Registros de pedidos feitos por clientes.
- ItensDePedidos: Detalhes de cada item em um pedido (produto, quantidade, valor).
- Estoque: Quantidade disponível de cada produto.
- Funcionarios: Dados dos funcionários da empresa.
- Fornecedores: Cadastro de fornecedores.
- Receita: Controle financeiro (entradas e saídas).
- AgendamentoDeServicos: Serviços agendados por clientes, com data e responsável.

Relacionamentos Importantes

- Pedidos conectam clientes e funcionários.
- Itens de pedidos ligam produtos aos pedidos.
- Produtos pertencem a categorias e estão associados ao estoque.
- Agendamentos conectam clientes a funcionários responsáveis.

Tecnologias

- Banco de dados: MySQL
- Ferramentas recomendadas: MySQL Workbench, DBeaver, VS Code




