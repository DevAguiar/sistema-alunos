from funcoes.adicionaraluno import adicionar_aluno # importa a função adicionar_aluno do arquivo adicionaraluno.py
from funcoes.listaralunos import listar_alunos 
from funcoes.buscaraluno import buscar_aluno 

alunos = {} # Dicionário de alunos que será utilizada nos códigos

def mostrarmenu():
    print("           -------------")
    print("1. Adicionar aluno\n2. Listar todos os alunos\n3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Mostrar menu novamente\n7. Sair")
    print("           -------------")

mostrarmenu()

while True:
    menu = input("Escolha uma opção: ")
    match menu:
        case '1': adicionar_aluno(alunos) # Utiliza a função como se fosse própria, pois ela foi diretamente importada, e não o arquivo. 
        case '2': listar_alunos(alunos) # Lista os nomes dos alunos já adicionados na lista
        case '3': buscar_aluno(alunos)
        # case '4': remover_aluno()
        # case '5': media_alunos
        case '6': mostrarmenu()
        case '7': break
        case _: print("Digite uma opção válida\n") 

