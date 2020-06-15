class Jogador:
    jogadores = []

    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
        type(self).jogadores.append(self)

    @classmethod
    def importar_jogadores(cls):
        cls.jogadores = []

        try:
            with open('jogadores.txt', 'rt') as file:
                data = file.read()
        except IOError:
            print('não foi possivel abrir o arquivo')

        lista = data.split('\n')
        for j in lista:
            if j == '':
                continue
            nome, pontuacao = j.split('=')
            Jogador(nome, int(pontuacao))

    @classmethod
    def salvar_jogadores(cls):
        file = open('jogadores.txt', 'w')
        for j in cls.jogadores:
            file.write(j.nome + "=" + str(j.pontuacao) + "\n")

    @classmethod
    def buscar_jogador(cls, nome):
        for j in cls.jogadores:
            if j.nome == nome:
                return j

    @classmethod
    def buscar_jogadores(cls):
        return cls.jogadores
