import json


arquivo_json = 'dados.json'


with open(arquivo_json, 'r') as file:
    dados = json.load(file)


faturamento_diario = [dia['valor'] for dia in dados]


faturamento_completo = [faturamento for faturamento in faturamento_diario if faturamento > 0]


menor_faturamento = min(faturamento_completo)


maior_faturamento = max(faturamento_completo)


media_faturamento = sum(faturamento_completo) / len(faturamento_completo)


dias_acima_da_media = len([faturamento for faturamento in faturamento_completo if faturamento > media_faturamento])


print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
