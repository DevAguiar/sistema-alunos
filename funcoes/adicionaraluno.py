# def adicionar_aluno(alunos):
#     nome = input("Digite o nome do aluno: ")
#     idade = int(input("Digite a idade do aluno: "))
#     nota = float(input("Digite a nota do aluno: "))

#     aluno = {
#         'nomealuno': nome,
#         'idadealuno': idade,
#         'notaaluno': nota
#     }

#     alunos.append(aluno)

# ---------------------- Acima, forma inicial de adicionar alunos, utilizando uma lista de dicionários.
# ---------------------- Abaixo, nova forma de adicionar alunos, utilizando um dicionário onde a key é o nome do aluno e os valores são outro dicionário, que guarda idade e nota, facilitando buscas e manuseio.

def adicionar_aluno(alunos):
    nome = input("Digite o nome do aluno: ").strip().title()
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))

    alunos[nome] = {
        'idadealuno': idade,
        'notaaluno': nota
    }
    
    print(f"Aluno {nome} foi adicionado com sucesso!")
