# Sistema de Gestão de Leads para Corretoras de Seguros

Projeto Integrador da disciplina **Laboratório de Programação**, do curso de Análise e Desenvolvimento de Sistemas da **Universidade Santo Amaro (Unisa)**.

## Sobre o projeto
Corretores de seguros recebem leads pela página de captação e pelo WhatsApp, mas ainda enfrentam dois problemas no dia a dia: a demora para retornar o contato e a falta de organização dos leads. Este sistema ajuda na organização dos leads, permitindo que o corretor saiba qual lead precisa de retorno mais rápido.

O projeto nasceu da minha experiência criando sistemas e painéis de gestão para corretores.

## Para quem é
Corretores de seguros de todas as áreas, autônomos ou corretoras.

## Funcionalidades
| Opção | Funcionalidade | O que faz |
|---|---|---|
| 1 | Cadastrar lead | Registra código, nome, tipo de seguro, status, valor da proposta e data, com validação das entradas |
| 2 | Listar leads | Mostra todos os leads cadastrados |
| 3 | Buscar lead | Encontra um lead pelo código e mostra as comparações da busca sequencial e da binária |
| 4 | Ordenar leads | Organiza os leads do menor para o maior valor de proposta |
| 5 | Fila de retorno | Organiza os leads que aguardam contato, por ordem de chegada |
| 6 | Relatório | Mostra o total de leads e o valor médio, maior e menor das propostas |
| 7 | Experimento | Compara a busca sequencial e a binária com 100, 1.000 e 10.000 leads |

## Validações
- Nome e demais campos de texto não podem ficar vazios
- O código aceita apenas números
- O código não pode se repetir
- O valor da proposta não pode ser negativo

## Como os dados são salvos
Os leads ficam no arquivo `leads.json`, criado automaticamente no primeiro cadastro. Exemplo de um lead:

```json
{
  "codigo": 10,
  "nome": "Ana Souza",
  "tipo_seguro": "saúde",
  "status": "novo",
  "valor_da_proposta": 1200.0,
  "data": "24/11/2026"
}
```

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

## Resultado do experimento
Média de comparações em 100 buscas:

| Quantidade de leads | Busca sequencial | Busca binária |
|---|---|---|
| 100 | 51,3 | 5,8 |
| 1.000 | 526,1 | 9,0 |
| 10.000 | 4.855,3 | 12,3 |

Quanto maior a quantidade de leads, maior a vantagem da busca binária.

## Como executar
1. Instale o Python 3 ([python.org](https://www.python.org))
2. Baixe o arquivo `leads.py`
3. No terminal, dentro da pasta do arquivo, execute:
   ```
   python3 leads.py
   ```

## Vídeo de demonstração
[link do vídeo no YouTube]

## Autora
**Talia S. Xavier Lourenço**
Análise e Desenvolvimento de Sistemas – Unisa
Projeto Integrador: Laboratório de Programação – 2026
Orientador: Prof. Me. Patrick Araujo
