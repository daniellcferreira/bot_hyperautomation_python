# Automação de Cadastro de Produtos no Fakturama

![Python](https://img.shields.io/badge/Python-Linguagem-3776AB?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Manipula%C3%A7%C3%A3o%20de%20Dados-150458?style=flat-square&logo=pandas)
![BotCity](https://img.shields.io/badge/BotCity-Automa%C3%A7%C3%A3o-FFD700?style=flat-square&logo=botcity)
![Fakturama](https://img.shields.io/badge/Fakturama-Gest%C3%A3o%20ERP-0A0A0A?style=flat-square&logo=data)

## Descrição

Este projeto visa automatizar o processo de cadastro de produtos no sistema **Fakturama**, um ERP (Enterprise Resource Planning) utilizado para gestão de negócios. Através do uso da biblioteca **BotCity Desktop**, o script preenche automaticamente os campos necessários para cadastrar um produto, com base em um arquivo Excel contendo os dados dos produtos.

O script é projetado para reduzir o tempo gasto na inserção manual de dados, tornando o processo mais eficiente e preciso. Além disso, ele é totalmente automatizado, sem a necessidade de intervenção humana após o início da execução.

## Funcionalidade

O processo de automação é realizado em algumas etapas principais:

- **Leitura de dados**: O script lê os dados de uma planilha Excel (`produtos.xlsx`) que contém informações sobre os produtos a serem cadastrados.
- **Abertura do sistema Fakturama**: O sistema é aberto automaticamente.
- **Preenchimento dos campos**: Para cada produto, os seguintes campos são preenchidos automaticamente:
  - **Nome do Produto**
  - **Descrição do Produto**
  - **Preço do Produto**
  - **Categoria**
  - **Código do Produto**
  - **Quantidade/Estoque**
- **Salvamento**: Após preencher os dados, o produto é salvo no sistema.
- **Repetição**: O processo é repetido para todos os produtos listados na planilha Excel.

O script utiliza o **BotCity** para simular a interação do usuário com o sistema, clicando nos campos certos, preenchendo os dados e interagindo com a interface do software de forma autônoma.

## Tecnologias Abordadas

- **Python**: Linguagem de programação principal utilizada no projeto para implementar a lógica de automação.
- **Pandas**: Biblioteca utilizada para manipulação e processamento de dados. É responsável por ler o arquivo Excel e transformar os dados em um formato adequado para ser usado na automação.
- **BotCity**: Framework para automação de tarefas no desktop e web. Usado para controlar o sistema operacional e simular interações com o software Fakturama.
- **Fakturama**: Sistema ERP utilizado para gerenciamento de produtos e estoque. O projeto interage com o sistema Fakturama para cadastrar os produtos.



