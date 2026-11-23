import json
import random
import time

ARQUIVO = "leads.json"

def carregar_leads():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_leads(leads):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(leads, arquivo, ensure_ascii=False, indent=2)

def mostrar_menu():
    print("\n===== SISTEMA DE GESTÃO DE LEADS =====")
    print("1 - Cadastrar lead")
    print("2 - Listar leads")
    print("3 - Buscar lead")
    print("4 - Ordenar leads")
    print("5 - Fila de retorno")
    print("6 - Relatório")
    print("7 - Experimento")
    print("0 - Sair")

def ler_inteiro(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto.isdigit():
            return int(texto)
        print("Digite apenas números.")

def ler_decimal(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(texto)
        except ValueError:
            print("Digite um número válido (ex.: 12.5).")
            continue
        if valor < 0:
            print("O valor não pode ser negativo.")
        else:
            return valor

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Este campo não pode ficar vazio.")

def cadastrar_lead(leads):
    print("\n--- Novo lead ---")
    codigo = ler_inteiro("Código: ")
    nome = ler_texto("Nome: ")
    tipo_seguro = ler_texto("tipo_seguro: (auto, vida, saúde, residencial)  ")
    status = ler_texto("status): (novo, em negociação, fechado, perdido) ")
    valor_da_proposta = ler_decimal("Valor da proposta(R$): ")
    data = ler_texto("Data (dd/mm/aaaa): ")
    lead = {"codigo": codigo, "nome": nome, "tipo_seguro": tipo_seguro,
            "status": status, "valor_da_proposta": valor_da_proposta, "data": data}
    leads.append(lead)
    salvar_leads(leads)
    print("Lead cadastrado e salvo!")

def listar_leads(leads):
    if len(leads) == 0:
        print("Nenhum lead cadastrado.")
        return
    print("\n--- Leads cadastrados ---")
    for lead in leads:
        print(f"{lead['codigo']} | {lead['nome']} | {lead['tipo_seguro']} | {lead['status']} | R$ {lead['valor_da_proposta']:.2f} | {lead['data']}")

leads = carregar_leads()
fila=[]
def calcular_estatisticas(leads):
    total = 0
    maior = leads[0]["valor_da_proposta"]
    menor = leads[0]["valor_da_proposta"]
    for lead in leads:
        total = total + lead["valor_da_proposta"]
        if lead["valor_da_proposta"] > maior:
            maior = lead["valor_da_proposta"]
        if lead["valor_da_proposta"] < menor:
            menor = lead["valor_da_proposta"]
    media = total / len(leads)
    return media, maior, menor

def ordenar_por(leads, campo):
    lista = leads.copy()
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j][campo] > lista[j + 1][campo]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def busca_sequencial(leads, codigo):
    comparacoes = 0
    for lead in leads:
        comparacoes = comparacoes + 1
        if lead["codigo"] == codigo:
            return lead, comparacoes
    return None, comparacoes

def busca_binaria(leads_ordenados, codigo):
    comparacoes = 0
    inicio = 0
    fim = len(leads_ordenados) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes = comparacoes + 1
        if leads_ordenados[meio]["codigo"] == codigo:
            return leads_ordenados[meio], comparacoes
        elif leads_ordenados[meio]["codigo"] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None, comparacoes

def mostrar_lead(lead):
    print(f"{lead['codigo']} | {lead['nome']} | {lead['tipo_seguro']} | {lead['status']} | R$ {lead['valor_da_proposta']:.2f} | {lead['data']}")

def buscar_lead(leads):
    if len(leads) == 0:
        print("Nenhum lead cadastrado.")
        return
    codigo = ler_inteiro("Código do lead: ")
    lead, comp_seq = busca_sequencial(leads, codigo)
    ordenados = ordenar_por(leads, "codigo")
    lead, comp_bin = busca_binaria(ordenados, codigo)
    if lead is None:
        print("Lead não encontrado.")
    else:
        mostrar_lead(lead)
    print(f"Comparações -> sequencial: {comp_seq} | binária: {comp_bin}")

def ordenar_leads(leads):
    if len(leads) == 0:
        print("Nenhum lead cadastrado.")
        return
    print("\n--- Leads do mais baixo ao mais alto ---")
    for lead in ordenar_por(leads, "valor_da_proposta"):
        mostrar_lead(lead)

def relatorio(leads):
    if len(leads) == 0:
        print("Nenhum lead cadastrado.")
        return
    media, maior, menor = calcular_estatisticas(leads)
    print("\n--- Relatório ---")
    print(f"Total de leads: {len(leads)}")
    print(f"Valor médio da proposta: R$ {media:.2f}")
    print(f"Maior valor da proposta: R$ {maior:.2f}")
    print(f"Menor valor da proposta: R$ {menor:.2f}")

def menu_fila(leads, fila):
    while True:
        print("\n--- Fila de retornos ---")
        print("1 - Colocar lead na fila de retorno")
        print("2 - Retornar o próximo lead")
        print("3 - Ver a fila")
        print("0 - Voltar")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            codigo = ler_inteiro("Código do lead: ")
            lead, comparacoes = busca_sequencial(leads, codigo)
            if lead is None:
                print("Lead não encontrado.")
            else:
                fila.append(lead)
                print(f"{lead['nome']} entrou na fila. Posição: {len(fila)}")
        elif opcao == "2":
            if len(fila) == 0:
                print("A fila está vazia.")
            else:
                lead = fila.pop(0)
                print(f"Atendendo agora: {lead['nome']}")
        elif opcao == "3":
            if len(fila) == 0:
                print("A fila está vazia.")
            else:
                posicao = 1
                for lead in fila:
                    print(f"{posicao}º - {lead['nome']}")
                    posicao = posicao + 1
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")

def gerar_leads(quantidade):
    leads = []
    for i in range(quantidade):
        lead = {"codigo": i + 1, "nome": f"Lead {i + 1}", "email": f"lead{i + 1}@email.com", "valor_da_proposta": round(random.uniform(1000, 10000), 2)}
        leads.append(lead)
    return leads

def experimento():
    print("\n--- Experimento: busca sequencial x busca binária ---")
    print("Média de 100 buscas para cada quantidade de leads\n")
    print("Quantidade | Comp. seq. | Comp. bin. | Tempo seq. (ms) | Tempo bin. (ms)")
    for quantidade in [100, 1000, 10000]:
        leads = gerar_leads(quantidade)
        buscas = 100
        total_comp_seq = 0
        total_comp_bin = 0
        tempo_seq = 0
        tempo_bin = 0
        for repeticao in range(buscas):
            codigo = random.randint(1, quantidade)

            inicio = time.perf_counter()
            lead, comparacoes = busca_sequencial(leads, codigo)
            tempo_seq = tempo_seq + (time.perf_counter() - inicio)
            total_comp_seq = total_comp_seq + comparacoes

            inicio = time.perf_counter()
            lead, comparacoes = busca_binaria(leads, codigo)
            tempo_bin = tempo_bin + (time.perf_counter() - inicio)
            total_comp_bin = total_comp_bin + comparacoes

        media_comp_seq = total_comp_seq / buscas
        media_comp_bin = total_comp_bin / buscas
        media_tempo_seq = tempo_seq / buscas * 1000
        media_tempo_bin = tempo_bin / buscas * 1000
        print(f"{quantidade:>10} | {media_comp_seq:>10.1f} | {media_comp_bin:>10.1f} | {media_tempo_seq:>15.4f}| {media_tempo_bin:>15.4f}")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":   
        cadastrar_lead(leads)
    elif opcao == "2":
        listar_leads(leads)
    elif opcao == "3":
        buscar_lead(leads)
    elif opcao == "4":
        ordenar_leads(leads)
    elif opcao == "5":
        menu_fila(leads, fila)
    elif opcao in ["6"]:
        relatorio(leads)
    elif opcao == "7":
        experimento()
    elif opcao in ["0"]: 
        print("Encerrando o sistema. Até Logo!")
        break
    else:
        print("Opção invalida")