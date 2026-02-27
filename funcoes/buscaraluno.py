def buscar_aluno(alunos):
    nome = input("Qual aluno você quer buscar? ").title()
    if nome in alunos:
        print(f"Aluno: {nome} | Idade: {alunos[nome]['idadealuno']} | Nota: {alunos[nome]['notaaluno']}")
    else:
        print(f"O aluno {nome} não foi encontrado!")