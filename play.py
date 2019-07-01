from player import Player


def main():
    print('Welcome to rock, paper, scissors. ')
    player1 = Player()
    player1.kind = input('Is player 1 a human or computer? ')
    player1.name = input("What is player 1's name? ")

    player2 = Player()
    player2.kind = input('Is player 2 a human or computer? ')
    player2.name = input("What is player 2's name? ")

    turns = int(input('How many turns do you want to play? '))

    game_loop(player1, player2, turns)


def game_loop(player1, player2, turns):
    for turn in range(1, turns + 1):
        print(player1.play(player2))


if __name__ == '__main__':
    main()
