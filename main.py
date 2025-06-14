# Dicionário com informações dos insumos (materiais), incluindo preço unitário
# e dados como validade, tipo e fornecedor
materiais = {
    "MAT001": {
        "nome": "Agulha hipodérmica 25x7mm",
        "tipo": "Descartável",
        "categoria": "Uso clínico",
        "validade": "2027-01-15",
        "lote": "L2023A1",
        "custo_unitario": 0.45,
        "fornecedor": "MedEquip Ltda"
    },
    "MAT002": {
        "nome": "Luva de látex M",
        "tipo": "Proteção individual",
        "categoria": "EPI",
        "validade": "2025-12-20",
        "lote": "L2022L5",
        "custo_unitario": 0.60,
        "fornecedor": "SafeLab Distribuidora"
    },
    "MAT003": {
        "nome": "Tubo de coleta a vácuo",
        "tipo": "Vidraria",
        "categoria": "Coleta",
        "validade": "2026-09-01",
        "lote": "L2024T8",
        "custo_unitario": 1.25,
        "fornecedor": "LabPlus Equipamentos"
    },
    "MAT004": {
        "nome": "Máscara cirúrgica descartável",
        "tipo": "Descartável",
        "categoria": "EPI",
        "validade": "2025-08-15",
        "lote": "L2023M3",
        "custo_unitario": 0.35,
        "fornecedor": "Higienix Fornecimentos"
    }
}

# Dicionário com os dados de cada laboratório, incluindo número de visitantes,
# funcionários e o estoque atual de materiais
laboratorios = {
    "Lab Clínico A": {
        "visitantes_mensais": 200,
        "funcionarios": 60,
        "materiais": {
            "MAT001": 300,
            "MAT002": 500
        }
    },
    "Lab Biomédico B": {
        "visitantes_mensais": 150,
        "funcionarios": 40,
        "materiais": {
            "MAT003": 150,
            "MAT004": 900
        }
    },
    "Lab Pesquisa C": {
        "visitantes_mensais": 80,
        "funcionarios": 25,
        "materiais": {
            "MAT001": 200,
            "MAT004": 800
        }
    }
}

# Dicionário que define o tipo de consumo de cada material (por visitante ou funcionário),
# além da quantidade usada por mês
taxa_consumo = {
    "MAT001": {"por": "visitante", "quantidade": 1},
    "MAT002": {"por": "funcionario", "quantidade": 1},
    "MAT003": {"por": "visitante", "quantidade": 1},  
    "MAT004": {"por": "funcionario", "quantidade": 1} 
}

dados_duracao = []

# Função que analisa o estoque de cada laboratório
# Calcula o consumo mensal esperado com base nos dados de entrada
# Compara o estoque atual com o ideal mínimo e recomendado (com margem de segurança)
# Informa a duração estimada do estoque (em meses)
# Armazena os dados de duração para posterior ordenação
# Complexidade: O(n*m) considerando n = laboratórios e m = materiais
def calcular_estoque_ideal(laboratorios, materiais, taxa_consumo):
    for nome_lab, dados_lab in laboratorios.items():
        print(f"\nAnalisando {nome_lab}:")
        for material_id, qtd_estoque in dados_lab["materiais"].items():
            tipo_uso = taxa_consumo[material_id]["por"]
            qtd = taxa_consumo[material_id]["quantidade"]
            if tipo_uso == "visitante":
                consumo = dados_lab["visitantes_mensais"] * qtd
            elif tipo_uso == "funcionario":
                consumo = dados_lab['funcionarios'] * qtd * 22 #22 dias úteis por mês
            else:
                continue

            ideal_minimo = consumo
            ideal_recomendado = consumo * 1.05
            meses_duracao = qtd_estoque / consumo if consumo else 0

            print(f"Material {material_id} ({materiais[material_id]['nome']}):")
            print(f"Estoque atual: {qtd_estoque}")
            print(f"Ideal mínimo mensal: {ideal_minimo:.0f}")
            print(f"Ideal recomendado (20% a mais): {ideal_recomendado:.0f}")
            print(f"Duração estimada: {meses_duracao:.2f} meses")

            dados_duracao.append((nome_lab,materiais[material_id]["nome"], meses_duracao))

            if qtd_estoque < ideal_minimo:
                print("Estoque abaixo do mínimo!")
            elif qtd_estoque < ideal_recomendado:
                print("Estoque abaixo do recomendado.")
            else:
                print("Estoque adequado.")
    
# Função que calcula o valor total em reais dos insumos disponíveis em cada laboratório
# Compara o valor real (baseado no estoque atual) com o valor ideal (baseado no consumo ideal)
# Útil para análise de custo-benefício e planejamento de reposição de materiais
# Complexidade: O(n*m) considerando n = laboratórios e m = materiais
def calcular_valor_estoque(laboratorios, materiais, taxa_consumo):
    for nome_lab, dados_lab in laboratorios.items():
        print(f"\nCalculando o estoque do {nome_lab}:")
        for material_id, qtd_estoque in dados_lab["materiais"].items():
            tipo_uso = taxa_consumo[material_id]["por"]
            qtd = taxa_consumo[material_id]["quantidade"]
            if tipo_uso == "visitante":
                consumo = dados_lab["visitantes_mensais"] * qtd
            elif tipo_uso == "funcionario":
                consumo = dados_lab['funcionarios'] * qtd * 22 #22 dias úteis por mês
            else:
                continue

            valor_total_atual = consumo * materiais[material_id]["custo_unitario"]
            consumo_ideal = consumo * 1.05
            valor_total_ideal = consumo_ideal * materiais[material_id]["custo_unitario"]
            
            print(f"Material {material_id} ({materiais[material_id]['nome']}):")
            print(f"Valor de estoque atual: {valor_total_atual:.2f}")
            print(f"Valor de estoque ideal: {valor_total_ideal:.2f}")
            


# Algoritmo de ordenação Selection Sort aplicado sobre a duração estimada dos materiais
# Ordena os materiais em ordem crescente de tempo de duração em estoque
# Complexidade: O(n²)       
def ordenar_por_duracao(lista):
    tamanho_lista = len(lista)
    for i_preencher in range(tamanho_lista):
        menor = i_preencher
        for i_verificando in range(i_preencher + 1, tamanho_lista):
            if lista[i_verificando][2] < lista[menor][2]:
                menor = i_verificando
        lista[i_preencher], lista[menor] = lista[menor], lista[i_preencher]
    return lista

# Algoritmo de busca binária aplicado sobre a lista de materiais ordenada por nome
# Retorna a tupla com nome e duração do material procurado
# Pré-requisito: lista deve estar ordenada
# Complexidade: O(log n)
def busca_binaria_nome(lista_ordenada, nome_procurado):
    inicio = 0
    fim = len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_meio = lista_ordenada[meio][1]
        if nome_meio == nome_procurado:
            return lista_ordenada[meio]
        elif nome_procurado < nome_meio:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None


# Execução da análise de estoque
# Execução do calculo do valor do estoque
# Ordenação dos materiais com base na duração do estoque
# Aplicação da busca binária para localizar um insumo específico
calcular_estoque_ideal(laboratorios, materiais, taxa_consumo)

calcular_valor_estoque(laboratorios, materiais, taxa_consumo)

print("\nMateriais ordenados por duração de estoque (Selection Sort):")
ordenados = ordenar_por_duracao(dados_duracao.copy())
for laboratorio, nome, duracao in ordenados:
    print(f"{laboratorio} - {nome}: {duracao:.2f} meses")


nome_procurado = "Máscara cirúrgica descartável"
resultado = busca_binaria_nome(ordenados, nome_procurado)
print(f"\nResultado da busca por '{nome_procurado}':")
if resultado:
    print(f"Material encontrado: {resultado[1]} - duração de {resultado[2]:.2f} meses")
else:
    print("Material não encontrado.")