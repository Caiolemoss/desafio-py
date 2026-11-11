# Caio: variáveis com os dados de identificação da execução, tirados do mock da Squad 4.
projeto = "LearnHub EdTech"
modulo = "Emissão de Certificados e Validação de Notas"
responsavel = "Gabriel Souza"
data_execucao = "10/11/2026"

# Caio: quantidades de testes do mock, guardadas como int porque são números inteiros.
testes_aprovados = 28
testes_reprovados = 14
testes_nao_executados = 8

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

# Caio: rodapé indicando o fim da etapa de registro.
print(linha_fina)
print("          REGISTRO CONCLUÍDO")
print(linha_fina)