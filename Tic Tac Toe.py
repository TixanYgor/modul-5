playing_field = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 9]

winnings_moves = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8],
                  [0, 3, 6],
                  [1, 4, 7],
                  [2, 5, 8],
                  [0, 4, 8],
                  [2, 4, 6]]


def print_field():
    print("-" * 13)
    for i in range(3):
        print("|", playing_field[0 + i * 3], "|", playing_field[1 + i * 3], "|", playing_field[2 + i * 3], "|")
        print("-" * 13)


def step_field(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + " ? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(playing_field[player_answer - 1]) not in "XO":
                playing_field[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def get_result():
    win = ""

    for i in winnings_moves:
        if playing_field[i[0]] == "X" and playing_field[i[1]] == "X" and playing_field[i[2]] == "X":
            win = "X"
        if playing_field[i[0]] == "O" and playing_field[i[1]] == "O" and playing_field[i[2]] == "O":
            win = "O"

    return win


def main():
    counter = 0
    win = False
    while not win:
        print_field()
        if counter % 2 == 0:
            step_field("X")
        else:
            step_field("O")
        counter += 1

        tmp = get_result()
        if tmp:
            print(" Победитель !", tmp)
            break
        if counter == 9:
            print("Ничья!")
            break

    print_field()


main()
