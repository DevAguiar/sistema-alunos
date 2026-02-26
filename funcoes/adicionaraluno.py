def adicionar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))

    aluno = {
        'nomealuno': nome,
        'idadealuno': idade,
        'notaaluno': nota
    }

    alunos.append(aluno)
