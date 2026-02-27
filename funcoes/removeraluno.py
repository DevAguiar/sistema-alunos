def remover_aluno(alunos):
    print("Iniciando remoção de aluno!!!")
    nome = input("--- Qual o nome do aluno que você deseja remover? ").title()
    if nome in alunos:
        del alunos[nome]
        print(f"O aluno {nome} foi deletado com sucesso!")
    else:
        print(f"O aluno {nome} não foi encontrado!")