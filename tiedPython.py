class tiedPython:

    def __init__(self, snake_data):
        self.snake_data = snake_data
        self.next_snake = None
    
    def hasNextSnake(self):
        if (self.next_snake == None):
            return False
        else:
            return True

    def setNextSnake(self, next_snake):
        self.next_snake = next_snake
    
    def getNextSnake(self):
        return self.next_snake
    
    def setSnakeData(self, snake_data):
        self.snake_data = snake_data

    def getSnakeData(self):
        return self.snake_data
