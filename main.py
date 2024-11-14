class MembroEquipe: # Base que a profe deu
    def __init__(self, nome, idade, posicao, numero_camisa, equipe):
        self.nome = nome # Nome do membro da equipe
        self.idade = idade # Idade do membro
        self.posicao = posicao # Posição que o membro ocupa (ex: atacante, defensor)
        self.numero_camisa = numero_camisa # Número da camisa
        self.equipe = equipe # Nome da equipe ou time ao qual pertence

alunos=[]
while True:
    opc = int(input("1. Cadastrar aluno\n2. Listar alunos\n3. Atualizar aluno\n4. Deletar aluno\n5. Sair\nEscolha uma opção: "))
    match(opc):
        case 1:
            nome=input("Digite o nome do aluno: ")
            idade=int(input("Digite a idade do aluno: "))
            posicao=input("Digite a posição em que o membro ocupa: ")
            numero_camisa=int(input("Digite o número da camisa: "))
            equipe=input("Digite o nome da equipe que o aluno pertence: ")
            alunos.append(MembroEquipe(nome, idade, posicao, numero_camisa, equipe))
        case 4:
            nome=input("Digite o nome do aluno a ser deletado: ")
            for i in range(len(alunos)):
                if alunos[i].nome==nome:
                    alunos.remove(i) # não sei se está certo
        case 5:
            break
        case _:
            print("Opção inválida!")