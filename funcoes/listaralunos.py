# def listar_alunos(alunos):
#     if alunos: # Verificação se a lista não está vazia
#         nomes = [aluno['nomealuno'].title() for aluno in alunos] # Cria outra lista contendo os nomes dos alunos na lista principal, formatados.
#         print(" - ".join(nomes)) # Utiliza join para formatar o print dos nomes: nome1 - nome2 - nome3
#     else:
#         print("Ainda não há nenhum aluno na lista!") 

# ---------------------- Acima, forma inicial de listar alunos.
# ---------------------- Abaixo, forma atualizada de listar alunos.

def listar_alunos(alunos):
    if alunos: # Verificação se a lista não está vazia    
        print("Lista de alunos: ")
        nomes = list(alunos) # Cria uma lista contendo os nomes dos alunos no dicionário principal, formatados.
        print(" - ".join(nomes).title()) # Utiliza join para formatar o print dos nomes: nome1 - nome2 - nome3
    else:
        print("Ainda não há nenhum aluno na lista!!!")

# ---------------------- Abaixo, forma de listar a idade de cada aluno.


# def listar_alunos(alunos):
#     if alunos: # Verificação se a lista não está vazia
        
#         nomes = [str(alunos[aluno]['idadealuno']) for aluno in alunos] # Cria uma lista contendo as idades dos alunos transformados em str para formatar com join.
#         print(" - ".join(nomes)) 
#     else:
#         print("Ainda não há nenhum aluno na lista!")

        
