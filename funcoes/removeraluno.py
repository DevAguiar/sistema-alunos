def remover_aluno(alunos):
    nome = input("Qual aluno você deseja remover? ").title()
    if nome in alunos:
        del alunos[nome]
        print(f"O aluno {nome} foi deletado com sucesso!")
    else:
        print(f"O aluno {nome} não foi encontrado!")