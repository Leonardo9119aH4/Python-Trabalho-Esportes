class MembroEquipe: # Base que a profe deu
    def __init__(self, nome, idade, posicao, numero_camisa, equipe):
        self.nome = nome # Nome do membro da equipe
        self.idade = idade # Idade do membro
        self.posicao = posicao # Posição que o membro ocupa (ex: atacante, defensor)
        self.numero_camisa = numero_camisa # Número da camisa
        self.equipe = equipe # Nome da equipe ou time ao qual pertence
class SistemaCadastro:
    def __init__(self):
        self.alunos = []
    def cadastrarAluno(self):
        nome=input("Digite o nome do aluno: ")
        idade=int(input("Digite a idade do aluno: "))
        posicao=input("Digite a posição em que o membro ocupa: ")
        numero_camisa=int(input("Digite o número da camisa: "))
        equipe=input("Digite o nome da equipe que o aluno pertence: ")
        self.alunos.append(MembroEquipe(nome, idade, posicao, numero_camisa, equipe))
    def listarAlunos(self):
        for aluno in self.alunos:
            print(f"Aluno: {aluno.nome}, idade: {aluno.idade} anos, poisção: {aluno.posicao}, número da camisa: {aluno.numero_camisa}, equipe: {aluno.equipe}.")
        if len(self.alunos)==0:
            print("Não há alunos cadastrados")
    def atualizarAluno(self):
        while True:
            alterName = input("Digite o nome do aluno a ser atualizado: ")
            foundAluno = False
            for x in range(0, len(self.alunos)):
                if self.alunos[x].nome == alterName:
                    foundAluno = True
                    while True:
                        opc = int(input("Digite o atributo a ser alterado:\n1 - Nome\n2 - Idade\n3 - Posição\n4 - Número da camisa\n5 - Equipe\n\nSua opção: "))
                        match (opc):
                            case 1:
                                self.alunos[x].nome = input("Digite o novo nome: ")
                                break
                            case 2:
                                self.alunos[x].idade = input("Digite a nova idade: ")
                                break
                            case 3:
                                self.alunos[x].posicao = input("Digite a nova posição: ")
                                break
                            case 4:
                                self.alunos[x].numero_posicao = input("Digite o novo número: ")
                                break
                            case 5:
                                self.alunos[x].equipe = input("Digite a nova equipe: ")
                                break
                            case _:
                                print("Opção inválida!")
            if not foundAluno:
                print("Aluno não encontrado!")
                continue
            break
    def deletarAluno(self):
        nome=input("Digite o nome do aluno a ser deletado: ")
        for i in range(len(self.alunos)):
            if self.alunos[i].nome==nome:
                del self.alunos[i] # não sei se está certo
                break
sistema = SistemaCadastro()
while True:
    opc = int(input("1. Cadastrar aluno\n2. Listar alunos\n3. Atualizar aluno\n4. Deletar aluno\n5. Sair\nEscolha uma opção: "))
    match(opc):
        case 1:
            sistema.cadastrarAluno()
        case 2:
            sistema.listarAlunos()
        case 3:
            sistema.atualizarAluno()
        case 4:
            sistema.deletarAluno()
        case 5:
            break
        case _:
            print("Opção inválida!")
