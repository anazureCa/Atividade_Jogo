import Cadastro_dinossauros
class Funcionarios():
    def __init__(self,nome,ID,idade,tempo_servico,funcao,partes_perdidas,senha):
        self._nome = nome
        self._ID = ID
        self._senha = senha
        self._idade = idade
        self._tempo_servico = tempo_servico
        self._funcao = funcao
        self._partes_perdidas = partes_perdidas

    @property
    def nome(self):  
        return self._nome
    @nome.setter
    def nome(self, nome_novo):
        self._nome = nome_novo
    
    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self, novo_ID):
        self._ID = novo_ID

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self,nova_senha):
        self._senha = nova_senha

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):  
        if nova_idade < 0:
            print("Idade não pode ser negativa.")   
        else:
            self._idade = nova_idade

    @property
    def tempo_servico(self):
        return self._tempo_servico
    
    @tempo_servico.setter
    def tempo_servico(self, tempo_servico_atual):
        if tempo_servico_atual < 0:
            print('O tempo de serviço não pode ser negativo')
        if tempo_servico_atual == 0:
            print('Novo funcionário')
            self._tempo_servico = tempo_servico_atual
        else:
            print('Tempo de serviço atualizado')
            self._tempo_servico = tempo_servico_atual
    @property
    def funcao(self):
        return self._funcao
    
    @funcao.setter
    def funcao(self,nova_funcao):
        self._funcao = nova_funcao

    @property
    def partes_perdidas(self):
        return self._partes_perdidas
    
    @partes_perdidas.setter
    def partes_perdidas(self,novas_partes_perdidas):
        self._partes_perdidas = novas_partes_perdidas

    def exibir_dados(self):
        print("=== Lista de Funcionários Cadastrados ===")
        print(f'Nome: {self._nome}')
        print(f'ID: {self._ID}')
        print(f'Idade: {self._idade}')
        print(f'Tempo de serviço: {self._tempo_servico}')
        print(f'Função: {self._funcao}')
        print(f'Partes perdidas: {self._partes_perdidas}')

    def get_dados_formatados(self):
        return (
            "\n" + "="*40 +
        f"\n Funcionário: {self._nome} (ID: {self._ID})" +
        "\n" + "="*40 +
        f"\n Idade:             {self._idade} anos" +
        f"\n Tempo de serviço:  {self._tempo_servico} meses" +
        f"\n Função:            {self._funcao}" +
        f"\n Partes perdidas:  {self._partes_perdidas if self._partes_perdidas else 'Nenhuma'}" +
        "\n" + "="*40
        )

    def get_dados(self):
        return {
            "Nome": self._nome,
            "ID": self._ID,
            "Idade": f"{self._idade} anos",
            "Tempo de serviço": f"{self._tempo_servico} meses",
            "Função": self._funcao,
            "Partes perdidas": self._partes_perdidas if self._partes_perdidas else "Nenhuma"
        }
funcionarios = []

def cadastrar_funcionario():
    print("\n=== Cadastro de Funcionário ===")
    nome = input("Nome: ")
    while True:
        try:
            ID = input("ID: ")
            if ID.strip():
                break
            else:
                print("ID não pode ficar vazio.")
        except ValueError:
            print('Erro: O ID deve ser um número. Tente novamente.')
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                break
            else:
                print('Idade inválida.')
        except ValueError:
            print('Erro: Digite um número maior que zero')
    while True:
        try:
            tempo_servico = int(input("Tempo de serviço (em meses): "))
            if tempo_servico > 0:
                break
            else:
                print('Tempo de serviço inválido.')
        except ValueError:
            print('Erro: Digite um número maior que zero')
    funcao = input("Função: ")
    partes_perdidas = input("Partes perdidas no trabalho (ou deixe vazio): ")
    senha = input("Crie uma senha para esse funcionário: ")

    f = Funcionarios(nome, ID, idade, tempo_servico, funcao, partes_perdidas, senha)
    funcionarios.append(f)
    print(f"\nFuncionário {nome} cadastrado com sucesso!")
#lucas
tratamentos = {}

def agendar_tratamento():
    print("\n=== Agendar Tratamento Médico ===")
    while True:
        try:
            id_dino = int(input("ID do dinossauro: "))
            if any(dino.ID == id_dino for dino in Cadastro_dinossauros.dinossauros):
                break
            else:
                print('ID inválido')
        except ValueError:
            print("Erro: Digite um número inteiro válido para o ID do dinossauro.")
    data = input("Data do tratamento (dd/mm/aaaa): ")
    descricao = input("Descrição do tratamento: ")
    if id_dino not in tratamentos:
        tratamentos[id_dino] = []
    tratamentos[id_dino].append((data, descricao))
    print("Tratamento agendado com sucesso!")

def listar_tratamentos():
    print("\n=== Tratamentos Agendados ===")
    if not tratamentos:
        print("Nenhum tratamento agendado.")
        return
    for id_dino, lista_tratamentos in tratamentos.items():
        print(f"ID Dinossauro: {id_dino}")
        for i, (data, descricao) in enumerate(lista_tratamentos, start=1):
            print(f" Tratamento {i}:")
            print(f"  Data: {data}")
            print(f"  Descrição: {descricao}")
#lucas
def Menu_funcionario():
    while True:
        print('\n=== Menu de Funcionário===')
        print('1 - Cadastrar Dinossauro')
        print('2 - Consultar Dinossauro')
        print('3 - Agendar Tratamento Médico')
        print('4 - Listar Tratamentos')
        print('5 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            Cadastro_dinossauros.cadastro_dinossauro()
        elif opcao == "2":
            id_busca = int(input("\nDigite o ID do dinossauro que deseja consultar: "))
            encontrado = False
            for d in Cadastro_dinossauros.dinossauros:
                if d.ID == id_busca:
                    print("\nDinossauro encontrado:")
                    d.exibir_dados()
                    encontrado = True
                    break
            if not encontrado:
                print("\nNenhum dinossauro encontrado com esse ID.")
        elif opcao == "3":
            agendar_tratamento()
        elif opcao == "4":
            listar_tratamentos()
        elif opcao == "5":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def login():
    print("\n=== Login ===")
    IDL = input("Digite o ID: ")
    senhaL = input("Digite a senha: ")

    for f in funcionarios:
        if f.ID == IDL and f.senha == senhaL:
            print(f"\nLogin bem-sucedido! Bem-vindo, {f.nome}.")
            Menu_funcionario()
            return

    print("\nID ou senha incorretos.")

def Menu():
    print("\n=== Menu Principal ===")
    print("1 - Cadastrar funcionário")
    print("2 - Fazer login")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Encerrando o sistema. Até mais!")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
        Menu()