class Buscaminas():
    def __init__(self, rows, cols, bombs):
        #self.board = [["" for j in range(cols)] for i in range(rows)]}
        self.board = [['2', 'B', '2', ' ', '1', 'B', 'B', '1'],
                      ['3', 'B', '3', ' ', '1', '3', '3', '2'],
                      ['3', 'B', '3', ' ', ' ', '1', 'B', '1'],
                      ['4', 'B', '3', ' ', ' ', '1', '1', '1'],
                      ['B', 'B', '2', ' ', ' ', ' ', ' ', ' '],
                      ['2', '2', '1', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', '1', '1', '1', ' ', ' ', ' '],
                      [' ', ' ', '1', 'B', '1', ' ', ' ', ' ']]
        self.show = [["" for j in range(cols)] for i in range(rows)]
        self.num_bombs = bombs
    def question(self, movs):
        mov = input("¿Qué movimiento desea realizar?" + str(movs))
        row = int(input("Ingrese fila: "))
        col = int(input("Ingrese columna: "))
        if mov not in movs:
            raise Exception
        return mov, row, col
    def play(self, mov, row, col):
        if mov == "uncover":
            self.show[row][col] = self.board[row][col]
        elif mov == "flag":
            self.show[row][col] = "F"
    def show_board(self):
        for row in self.show:
               print(row)
    def win(self):
        bombs_found = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "B" and self.show[i][j] == "F":
                    bombs_found += 1
        if bombs_found == self.num_bombs:
            return True
        return False
    def lose(self):
        for row in self.show:
            if "B" in row:
                return True
        return False