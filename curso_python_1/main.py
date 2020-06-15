from game import jogar, ler_arquivo

def menu():
    while True:
        print('-- Jogo da Forca --')
        print('1 - Ver Placar')
        print('2 - Jogar')
        print('3 - Sair')
        escolha = input('Digite a opção selecionada:')
        if escolha == '1':
            placar()
        elif escolha == '2':
            jogar()
        elif escolha == '3':
            break
        else:
            print('Opção inválida')


def placar():
    jogadores = ler_arquivo('jogadores.txt')
    for j in jogadores:
        if j == '':
            continue
        print(j)

if __name__ == '__main__':
    menu()
