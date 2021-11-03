class Buscaminas():
    def __init__(self, rows, cols, bombs):
        self.board = []
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
        for row in self.board:
               print(row)
    def win(self):
        bombs_found = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "F" and self.show[i][j] == "B":
                    bombs_found += 1
        if bombs_found == self.num_bombs:
            return True
        return False
    def lose(self):
        for row in self.show:
            if "B" in row:
                return True
        return False