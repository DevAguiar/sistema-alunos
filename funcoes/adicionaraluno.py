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
# ---------------------- Abaixo, nova forma de adicionar alunos, utilizando um dicionário onde a key é o nome do aluno e os valores são outro dicionário, que guarda idade e nota, facilitando buscas e manuseio. Subrotinas separadas para que a função adicionar_aluno não faça todas as partes.

def adicionar_aluno(alunos):
    print("Adicionando novo aluno!!!")

    nome = obter_nome(alunos)

    if nome is None:
        print("--- Cancelando cadastro do novo aluno!!!")
        return

    idade = obter_idade()
    nota = obter_nota()

    alunos[nome] = {
        'idadealuno': idade,
        'notaaluno': nota
    }

    print(f"Aluno {nome} foi adicionado com sucesso!!!")


# Cadastro nome -------
def obter_nome(alunos):
    while True:
        nome = input("--- Digite o nome do aluno: ").strip().title()

        if nome == "0":
            return None

        if not nome.replace(" ", "").isalpha():
            print("Digite apenas letras no nome.")
            continue

        if nome in alunos:
            print("Este nome não está disponível, digite outro nome ou 0 para voltar ao menu.")
            continue

        return nome


# Cadastro idade ------
def obter_idade():
    while True:
        try:
            idade = int(input("--- Digite a idade do aluno: "))

            if idade < 1 or idade > 100:
                print("A idade deve estar entre 1 e 100.")
                continue

            return idade  # sai do loop se tudo estiver correto

        except ValueError:
            print("Digite um número inteiro válido!")


# Cadastro nota -------
def obter_nota():
    while True:
        try:
            nota = float(input("--- Digite a nota do aluno: "))

            if nota < 0 or nota > 10:
                print("A nota deve estar entre 0 e 10.")
                continue

            return nota  # sai do loop se tudo estiver correto

        except ValueError:
            print("Digite uma nota válida!!!")