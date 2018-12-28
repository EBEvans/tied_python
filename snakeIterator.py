from tiedPython import tiedPython

class snakeIterator:

    def __init__(self, snake):
        self.currentSnake = snake

    def iterate(self):
        self.currentSnake = self.getSnake().getNextSnake()
    
    def hasNext(self):
        if (self.currentSnake.hasNextSnake() == True):
            return True
        else:
            return False

    def getSnake(self):
        return self.currentSnake
