# Sistema de Gerenciamento de Vendas

Tendo em vista o problema relatado pelo cliente, Miguel, nós do grupo Celacanto provoca maremoto desenvolvemos um sistema que centraliza seus anúncios em diversos marketplaces, permitindo que o Miguel tenha facilidade para realizar as seguintes tarefas:

1. Visualizar sua base de produtos de todos os marketplaces em um único lugar;
2. Poder cadastrar seus produtos nos marketplaces pelo SGV (Sistema de Gerenciamento de Vendas);
3. Visualizar a situação atual do estoque de seus produtos, tanto em sua base de produtos, quanto nos anúncios nos marketplaces;
4. Repor o estoque de um determinado produto, mediante um alerta emitido pelo SGV.

## Especificação de Requisitos

Tendo essa demanda em vigência, o nosso sistema deverá atender os seguintes requisitos básicos:

1. Centralizar a comiunicação entre o ERP e os marketplaces;
2. Permitir o cadastro dos produtos a serem anunciados;
3. Gerenciar e atualizar o estoque dos produtos cadastrados.

## Pré-requisitos

Miguel possui um sistema ERP já instalado e contas em diferentes Marketplaces.

## Instalação

Para rodar o projeto, utilize o Docker Compose:
>docker compose build
>docker compose up

## Implementação

Com o objetivo de permitir a expansão da empresa de Miguel, o SGV permitirá que ele anuncie seus produtos em diversos marketplaces sem se preocupar com o gereciamento de cada um em particular, pois o sistema irá centralizar todos os anúncios.
Para tal, basta que o Miguel cadastre seus produtos.

## Construído com
Bibliotecas python:
  [Flask](https://flask.palletsprojects.com/) - Biblioteca para construção de APIs
  [time] - Controlar intervalo de tempo entre requisições.
  [threading] - Gerar threads de monitores e updates
  [json] - Manipular arquivos json
  [os] - Recursos do sistema operacional
  
[PlantText](https://www.planttext.com/) - Editor UML

[Google Docs](https://docs.google.com/?hl=pt-BR) - Editor de Texto para a [documentação formal do projeto](https://docs.google.com/document/d/1_n_Y9VzPirSi8xGHPFUpLFhRByi0lGL5/edit?usp=sharing&ouid=106651746525604779290&rtpof=true&sd=true)

[Pyhton](https://www.python.org/) - Linguagem de programação

[Docker](https://www.docker.com/) - Conteinerização

[Docker Compose](https://docs.docker.com/compose/) - Orquestração de contêiner

## Autores

- **Desenvolvedores** - 
1. João Pedro Rodrigues Martins
2. Eduardo Neves Paschoal
3. André Mendonça Morato Pupin

- **Documentação** - 
1. Jeferson Patrick Dietrich Filho
2. Thiago César Castilho Almeida
3. João Pedro Bastasini Garcia de Souza
4. Pedro Bruce de Lima

- **Design** - 
1. Mariana Ferreira Kenworthy

- **Assistência** - 
1. Edgar Auler Galvão de França
2. Gil de Almeida ALves

## Gratidão
