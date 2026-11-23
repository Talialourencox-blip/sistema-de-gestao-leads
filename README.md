# Sistema de Gestão de Leads para Corretoras de Seguros

## Sobre o projeto
Corretores de seguros recebem leads pela página de captação e pelo WhatsApp, mas ainda enfrentam dois problemas no dia a dia: a demora para retornar o contato e a falta de organização dos leads. Este sistema ajuda na organização dos leads, permitindo que o corretor saiba qual lead precisa de retorno mais rápido.

O projeto nasceu da minha experiência criando sistemas e painéis de gestão para corretores, e foi desenvolvido como Projeto Integrador da disciplina Laboratório de Programação.

## Para quem é
Corretores de seguros de todas as áreas, autônomos ou corretoras.

## Funcionalidades
- **Cadastrar lead:** registra código, nome, tipo de seguro, status, valor da proposta e data
- **Listar leads:** mostra todos os leads cadastrados
- **Buscar lead:** encontra um lead pelo código, comparando a busca sequencial e a busca binária
- **Ordenar leads:** organiza os leads do menor para o maior valor de proposta
- **Fila de retorno:** organiza os leads que aguardam contato, por ordem de chegada
- **Relatório:** mostra o total de leads e o valor médio, maior e menor das propostas
- **Experimento:** compara o desempenho da busca sequencial e da busca binária com 100, 1.000 e 10.000 leads

## Conceitos aplicados
- Registros (dicionários) e listas de registros
- Laços, decisões, contadores e acumuladores
- Funções com parâmetros e retorno
- Validação das entradas do usuário
- Gravação e leitura de dados em JSON
- Ordenação feita à mão (Bubble Sort)
- Busca sequencial e busca binária
- Fila (o primeiro a entrar é o primeiro a ser atendido)
- Média, maior e menor valor

## Como executar
1. Instale o Python 3 (python.org)
2. Baixe o arquivo `leads.py`
3. No terminal, dentro da pasta do arquivo, execute:
   `python3 leads.py`

## Autora
Talia Lourenço - Análise e Desenvolvimento de Sistemas - Unisa
Projeto Integrador: Laboratório de Programação - 2026
Orientador: Prof. Patrick Araujo
