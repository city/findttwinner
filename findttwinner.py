nner in tic tac toe
from random import randint
class Board:

    a = ['','','','','','','','','']

    def makeMove(self, location, compOrPlayer):
        self.a[location] = compOrPlayer

    def findNextMove(self):
        #find somewhere the player/comp can go
        rand = randint(0,8)
        print(rand)
        while self.a[rand] is not '':
            rand = randint(0,8)

        return rand

    def isWinner(self, compOrPlayer):

        #if three across are 'player#' or 'comp'
        #[0],[1],[2]
        #[3],[4],[5]
        #[6],[7],[8]

        if(self.a[0] == compOrPlayer and self.a[1] == compOrPlayer and self.a[2] == compOrPlayer):
            return True

        return False

    def print(self):
        print(self.a)

b = Board()
pWinner = False
compWinner = False
while(pWinner is False and compWinner is False):

    move = b.findNextMove()
    b.makeMove(move, 'player')
    pWinner = b.isWinner('player')


b.print()
print(pWinner)


