def listar_alunos(alunos):
    if alunos: # Verificação se a lista não está vazia
        nomes = [aluno['nomealuno'].title() for aluno in alunos] # Cria outra lista contendo os nomes dos alunos na lista principal, formatados.
        print(" - ".join(nomes)) # Utiliza join para formatar o print dos nomes: nome1 - nome2 - nome3
    else:
        print("Ainda não há nenhum aluno na lista!")