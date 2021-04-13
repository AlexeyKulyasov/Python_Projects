import random
import time
from itertools import cycle
from typing import Optional, Union


class GameBoard:
    lst_cells = []
    COUNT_CELLS = 9
    win_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self, mark_user: str, mark_comp: str):
        self.mark_user = mark_user
        self.mark_comp = mark_comp
        self.win_line = None

    def new_board(self):
        self.lst_cells = list(range(1, self.COUNT_CELLS + 1))
        self.show_board()

    def print_value_cell(self, number_cell: int):
        if self.win_line and number_cell in self.win_line:
            print(f'\033[32m\033[1m{self.lst_cells[number_cell]}\033[0m', end=' ')
        elif self.lst_cells[number_cell] == 'X':
            print(f'\033[33m{self.lst_cells[number_cell]}\033[0m', end=' ')
        elif self.lst_cells[number_cell] == '0':
            print(f'\033[35m{self.lst_cells[number_cell]}\033[0m', end=' ')
        else:
            print(self.lst_cells[number_cell], end=' ')

    def show_board(self):
        print()
        for row in range(3):
            print('\t', end=' ')
            for col in range(3):
                self.print_value_cell(col + row * 3)
                print('|', end=' ') if col != 2 else print()
            print('\t', '-' * 10) if row != 2 else None
        print()

    def is_valid_move(self, number_cell: int) -> bool:
        number_cell -= 1
        if number_cell < self.COUNT_CELLS and isinstance(self.lst_cells[number_cell], int):
            return True
        return False

    def user_move(self, number_cell: int):
        self.lst_cells[number_cell - 1] = self.mark_user

    def check_win(self) -> Optional[bool]:
        for cells in self.win_combs:
            cell1, cell2, cell3 = cells
            if self.lst_cells[cell1] == self.lst_cells[cell2] == self.lst_cells[cell3]:
                self.win_line = cells
                return self.lst_cells[cell1]
        if len(set(self.lst_cells)) == 2:
            return False
        return None

    def computer_move(self):
        buffer_val = None
        for cells in self.win_combs:
            cell1, cell2, cell3 = cells
            can_win_cells = {self.lst_cells[cell1], self.lst_cells[cell2], self.lst_cells[cell3]}
            if len(can_win_cells) == 2 and ''.join(map(str, can_win_cells)) not in 'X00X':
                cell_number = (can_win_cells - {'X', '0'}).pop()
                if (can_win_cells - {cell_number}).pop() == self.mark_comp:
                    break
                else:
                    buffer_val = cell_number
                    continue
        else:
            cell_number = buffer_val if buffer_val else \
                random.choice([el for el in self.lst_cells if isinstance(el, int)])

        self.lst_cells[cell_number - 1] = self.mark_comp


class GameAct:
    mark_winner: Union[str, bool]

    def __init__(self, board: "GameBoard", first_player: tuple[str, str],
                 sec_player: tuple[str, str]):
        self.board = board
        self.first_player = first_player
        self.sec_player = sec_player
        self.dict_player_mark = {first_player[0]: first_player[1], sec_player[0]: sec_player[1]}

    def start_game(self):
        self.board.new_board()
        players = cycle([self.first_player[1], self.sec_player[1]])
        winner = None
        while winner is None:
            player_turn = next(players)
            if player_turn == 'user':
                while True:
                    answer_user = input(f'Ваш ход (вы ходите {self.board.mark_user}), введите номер клетки [1-9]: ')
                    if not answer_user.isdigit() or not self.board.is_valid_move(int(answer_user)):
                        print('Некорректный ввод. Проверьте, что это число от 1 до 9 и эта клетка свободна.')
                    else:
                        break
                self.board.user_move(int(answer_user))
            else:
                print('Ход компьютера...')
                time.sleep(1)
                self.board.computer_move()
            winner = self.board.check_win()
            self.board.show_board()
        self.mark_winner = winner

    def return_winner(self):
        return self.dict_player_mark.get(self.mark_winner, False)


def main():
    while True:
        mark_user = input('\n\033[0mБудете играть крестиками или ноликами (крестики ходят первые) [X/0] ? ')
        mark_user = mark_user.upper()
        if mark_user in 'X0':
            break
        else:
            print('\033[31mНекорректный ввод. Нужно ввести X или 0.')

    mark_comp = ({'X', '0'} - {mark_user}).pop()
    sec_move, first_move = sorted({mark_user: 'user', mark_comp: 'comp'}.items())

    board = GameBoard(mark_user=mark_user, mark_comp=mark_comp)
    game = GameAct(board, first_move, sec_move)
    game.start_game()
    winner = game.return_winner()

    print('Игра закончена')
    if winner == 'user':
        print('Вы выиграли!')
    elif winner == 'comp':
        print('Вы проиграли.')
    else:
        print('Ничья.')


if __name__ == "__main__":
    main()
