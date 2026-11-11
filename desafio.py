# Caio: variáveis com os dados de identificação da execução, tirados do mock da Squad 4.
projeto = "LearnHub EdTech"
modulo = "Emissão de Certificados e Validação de Notas"
responsavel = "Gabriel Souza"
data_execucao = "10/11/2026"

# Caio: quantidades de testes do mock, guardadas como int porque são números inteiros.
testes_aprovados = 28
testes_reprovados = 14
testes_nao_executados = 8

# Caio: total de testes previstos, somando todos os resultados.
total_testes = testes_aprovados + testes_reprovados + testes_nao_executados

# Caio: testes que realmente rodaram, que são só os aprovados e os reprovados.
testes_executados = testes_aprovados + testes_reprovados

# Caio: taxas de aprovação e reprovação, calculadas sobre os testes executados.
taxa_aprovacao = round(testes_aprovados / testes_executados * 100, 2)
taxa_reprovacao = round(testes_reprovados / testes_executados * 100, 2)

# Caio: taxa de não executados, calculada sobre o total de testes previstos.
taxa_nao_executados = round(testes_nao_executados / total_testes * 100, 2)

# Caio: linhas de separação guardadas em variáveis para reaproveitar no relatório.
linha = "=" * 40
linha_fina = "-" * 40

# Caio: cabeçalho do relatório.
print(linha)
print("     RELATÓRIO DE EXECUÇÃO DE TESTES")
print(linha)

# Caio: mostro os dados de identificação usando f-strings.
print(f"Projeto: {projeto}")
print(f"Módulo: {modulo}")
print(f"Responsável: {responsavel}")
print(f"Data da execução: {data_execucao}")
print()

# Caio: seção com as quantidades de testes registradas.
print(linha_fina)
print("        RESULTADOS REGISTRADOS")
print(linha_fina)
print(f"Testes aprovados: {testes_aprovados}")
print(f"Testes reprovados: {testes_reprovados}")
print(f"Testes não executados: {testes_nao_executados}")
print()

# Caio: seção com as métricas calculadas pelo programa.
print(linha_fina)
print("         MÉTRICAS DA EXECUÇÃO")
print(linha_fina)
print(f"Total de testes: {total_testes}")
print(f"Testes executados: {testes_executados}")
print()
print(f"Taxa de aprovação: {taxa_aprovacao}%")
print(f"Taxa de reprovação: {taxa_reprovacao}%")
print(f"Taxa de não executados: {taxa_nao_executados}%")
print()

# Caio: rodapé indicando o fim da etapa de cálculos.
print(linha_fina)
print("         CÁLCULOS CONCLUÍDOS")
print(linha_fina)