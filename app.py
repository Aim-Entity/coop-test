import random


class GridGame:
    def __init__(self):
        self.gameMap = [["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["Player", "", "", "", "", "", "", ""], ]

        self.hiddenMap = [["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", "", ""],
                          ["Player", "", "", "", "", "", "", ""], ]

    def menu(self):
        while True:
            play = input("1) Play Game\n2) Quit Game\nSelect 1 | 2: ")
            if play == "1":
                return self.gameinit()
            elif play == "2":
                break

    def generateMap(self):
        chestDeplete = 10
        while chestDeplete != 0:
            x = random.randint(0, 7)
            y = random.randint(0, 7)

            if self.gameMap[y][x] != "" or (x == 0 and y == 7):
                pass
            else:
                self.gameMap[y][x] = "Chest"
                chestDeplete -= 1

        banditDeplete = 5
        while banditDeplete != 0:
            x = random.randint(0, 7)
            y = random.randint(0, 7)

            if self.gameMap[y][x] != "" or (x == 0 and y == 7):
                pass
            else:
                self.gameMap[y][x] = "Bandit"
                banditDeplete -= 1

    def displayMapNeatly(self):
        for i in gameMap:
            print(i)

    def piecePosition(self, piece):
        for i in range(len(gameMap)):
            for j in range(len(gameMap[i])):
                if gameMap[i][j] == piece:
                    return i, j

        return False

    def playerMove(self):
        xTransformation = int(
            input("Enter number of tiles to move right(+) or left(-): "))
        yTransformation = int(
            input("Enter number of tiles to move up(+) or down(-):"))
        realY, realX = piecePosition("player", gameMap)

        while (xTransformation < 1 or xTransformation > 8) or (yTransformation < 1 or yTransformation > 8):
            print("\nInvalid input")
            xTransformation = int(
                input("Enter number of tiles to move right(+) or left(-): "))
            yTransformation = int(
                input("Enter number of tiles to move up(+) or down(-):"))

    def gameinit(self):
        hidden_map = [["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["Player", "", "", "", "", "", "", ""], ]
        generated_map = self.generateMap()
        print(self.piecePosition("Player", hidden_map))
