def media_alunos(alunos):
    soma = float(0)
    media = float(0)
    if alunos:
        print("Calculando soma e média das notas de todos alunos!!!")
        for aluno in alunos:
            soma += (alunos[aluno]['notaaluno'])
        soma_formatada = f"{soma:.2f}".replace('.', ',')
        media = (soma/len(alunos))
        media_formatada = f"{media:.2f}".replace('.', ',')
        print(f"--- A soma de todas as notas é: {soma_formatada}. Já a média é: {media_formatada}.")
    else:
        print("Não existem alunos o suficiente para calcular a média!")