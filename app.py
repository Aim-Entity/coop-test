import random


class GridGame:
    def __init__(self):
        self.moves = 0

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

    def displayMapNeatly(self, gameMap):
        for i in gameMap:
            print(i)

    def piecePosition(self, piece, gameMap):
        for i in range(len(gameMap)):
            for j in range(len(gameMap[i])):
                if gameMap[i][j] == piece:
                    return i, j

        return (7, 0)

    def playerMove(self):
        xTransformation = int(
            input("Enter number of tiles to move right(+) or left(-): "))
        yTransformation = int(
            input("Enter number of tiles to move down(+) or up(-):"))

        currentY, currentX = self.piecePosition("Player", self.hiddenMap)

        while(xTransformation < -8 or xTransformation > 8)or(yTransformation < -8 or yTransformation > 8):
            print("\nInvalid input")
            xTransformation = int(
                input("Enter number of tiles to move right(+) or left(-): "))
            yTransformation = int(
                input("Enter number of tiles to move down(+) or up(-):"))

        while True:
            newY = currentY + yTransformation
            newX = currentX + xTransformation

            if (newY < 0 or newY > 7) or (newX < 0 or newX > 7):
                print("\nCoordinates fall out of range of map", (newY, newX))
                xTransformation = int(
                    input("Enter number of tiles to move right(+) or left(-): "))
                yTransformation = int(
                    input("Enter number of tiles to move down(+) or up(-):"))

            else:
                break

        self.hiddenMap[currentY][currentX] = ""
        self.hiddenMap[newY][newX] = "Player"

        newPiece = self.gameMap[newY][newX]

        if newPiece == "":
            self.gameMap[newY][newX] = "Player"
        else:
            self.gameMap[newY][newX] = f"{newPiece}|Player"

        if len(self.gameMap[newY][newX].split("|")) == 2:
            if self.gameMap[newY][newX].split("|")[0] != "":
                currentPiece = self.gameMap[newY][newX].split("|")[0]
            else:
                currentPiece = ""
        else:
            currentPiece = ""

        print(self.gameMap[newY][newX].split("|"))
        print(currentPiece)
        print(newPiece)

        self.gameMap[currentY][currentX] = currentPiece
        self.moves += 1

    def gameinit(self):
        self.generateMap()

        while True:
            self.displayMapNeatly(self.gameMap)
            self.playerMove()


G1 = GridGame()
G1.menu()
