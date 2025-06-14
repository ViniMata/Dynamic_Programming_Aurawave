# Controle de Estoque Laboratorial

## Objetivo
Este projeto simula o controle de estoque de insumos em laboratórios com base no consumo por funcionários e visitantes.
Calcula o estoque ideal, compara com o atual, e estima a duração dos insumos.

## Algoritmos Aplicados
- **Selection Sort**: ordena os materiais pela duração do estoque (complexidade O(n²)).
- **Busca Binária**: localiza um insumo específico após ordenação (complexidade O(log n)).

## Como Executar
Este projeto roda com Python 3.9 ou superior.

Para executar, utilize:

```
python main.py
```

**Grupo:**

1. Nome: Fabiano 	RM: 555524
2. Nome: Lorran 	RM: 558982
3. Nome: Maria 		RM: 557478
4. Nome: Pedro 		RM: 556268
5. Nome: Vinícius RM: 555200

**Turma:** 2ESPX 

## Hipóteses Consideradas

- Cada funcionário consome 1 unidade de EPI por dia útil (22 dias por mês).
- Cada visitante consome 1 unidade por visita.
- Um estoque recomendado possui 5% a mais do que o mínimo necessário.
- Os dados são simulados para fins acadêmicos.

## Justificativa dos Dados

Os dados utilizados foram criados com base em situações realistas de consumo de materiais laboratoriais.
A proposta visa exercitar a aplicação de estruturas de dados e algoritmos clássicos para tomada de decisão.

# Referências

- Matéria: Dynamic programming
- Professor: Lucas Mendes
- Algoritmos aplicados:
  - Selection Sort
  - Busca Binária
- Python 3.9+