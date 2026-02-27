# Cadastro de Alunos - Projeto Python

## 📋 Descrição

Sistema simples de cadastro e gerenciamento de alunos desenvolvido em Python. O programa permite adicionar, listar, buscar, remover alunos e calcular a média geral das notas.

## 🎯 Funcionalidades

1. **Adicionar Aluno** - Registra um novo aluno com nome, idade e nota
2. **Listar Todos os Alunos** - Exibe a lista de todos os alunos cadastrados
3. **Buscar Aluno** - Procura um aluno específico pelo nome
4. **Remover Aluno** - Deleta um aluno do cadastro
5. **Média Geral** - Calcula a média de notas de todos os alunos
6. **Menu** - Exibe o menu de opções novamente

## 📁 Estrutura do Projeto

```
Cadastro de Alunos_Projeto/
├── main.py                 # Arquivo principal com o menu do programa
└── funcoes/
    ├── adicionaraluno.py    # Função para adicionar alunos
    ├── buscaraluno.py       # Função para buscar aluno por nome
    ├── listaralunos.py      # Função para listar todos os alunos
    ├── mediaalunos.py       # Função para calcular a média de notas
    └── removeraluno.py      # Função para remover aluno
```

## 💾 Estrutura de Dados

Os alunos são armazenados em um dicionário com a seguinte estrutura:

```python
alunos = {
    "Nome do Aluno": {
        "idadealuno": 20,
        "notaaluno": 8.5
    }
}
```

## 🚀 Como Usar

1. Execute o arquivo `main.py`
2. Escolha uma opção do menu
3. Siga as instruções na tela
4. Digite '6' para visualizar o menu novamente
5. Digite '0' para encerrar o programa

## 📝 Exemplo de Uso

```
Inicializando o programa!!!
           -------------
1. Adicionar aluno
2. Listar todos os alunos
3. Buscar aluno pelo nome
4. Remover aluno
5. Mostrar média geral das notas
0. Sair
           -------------

Digite 6 para rever o menu!
Escolha uma opção: 1
Adicionando novo aluno!!!
--- Digite o nome do aluno: João Silva
--- Digite a idade do aluno: 20
--- Digite a nota do aluno: 8.5
Aluno João Silva foi adicionado com sucesso!!!
```

## 🔧 Tecnologias

- **Python 3.x** - Linguagem de programação utilizada

## 📚 Conceitos Utilizados

- Dicionários em Python
- Funções e importação de módulos
- Estruturas condicionais (match/case)
- Loops (while)
- Manipulação de strings
- Tratamento de entrada de dados
