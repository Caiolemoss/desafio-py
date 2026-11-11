# Caio: variáveis com os dados de identificação da execução, tirados do mock da Squad 4.
projeto = "LearnHub EdTech"
modulo = "Emissão de Certificados e Validação de Notas"
responsavel = "Gabriel Souza"
data_execucao = "10/11/2026"

# Caio: linha de separação guardada numa variável para reaproveitar no relatório.
linha = "=" * 40

# Caio: cabeçalho do relatório.
print(linha)
print("     RELATÓRIO DE EXECUÇÃO DE TESTES")
print(linha)

# Caio: mostro os dados usando f-strings para colocar as variáveis dentro do texto.
print(f"Projeto: {projeto}")
print(f"Módulo: {modulo}")
print(f"Responsável: {responsavel}")
print(f"Data da execução: {data_execucao}")

# Caio: rodapé indicando o fim da etapa.
print(linha)
print("       INICIALIZAÇÃO CONCLUÍDA")
print(linha)