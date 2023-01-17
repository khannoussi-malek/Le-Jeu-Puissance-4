class Player():
    """
    player is just a conter start at 0
    and if player is even it's player 1
    and if player is odd it's player 2
    """
    def __init__(self, playerPlay=0):
        self.playerPlay =playerPlay
    def __str__(self):
        return self.playerPlay
    def getPlayer(self):
        return self.playerPlay%2+1
    def nextPlayer(self):
        self.playerPlay+=1
        return self.playerPlay
    def resetPlayer(self):
        self.playerPlay=0
        return self.playerPlay