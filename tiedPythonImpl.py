#!/usr/bin/python3

# This program was written to give an example of
#   A) linked lists and how they work, generally, and
#   B) linked lists, specifically implimented in the python language
# This program was written to run in a linux environment on python3

from tiedPython import tiedPython
from snakeIterator import snakeIterator
import time

def appendSnake(firstSnake, snake):
    print("Creating an iterator to help move across the snake list")
    tempIterator = snakeIterator(firstSnake)
    while (tempIterator.hasNext()):
        tempIterator.iterate()
    tempIterator.getSnake().setNextSnake(snake)
    print("Appended snake ", snake.getSnakeData(), " to the list")

def insertSnake(firstSnake, newSnake, insertionPoint):
    if (insertionPoint == 1):
        newSnake.setNextSnake(firstSnake)
        return newSnake
    index = 1
    #If we want to insert newSnake as the 2nd snake, we need to be currently
    # looking at the first snake (or look at the 3rd snake to insert as 4th),
    # etc. Therefore, we need to stop iterating when (index < insertionPoint -1)
    tempIterator = snakeIterator(firstSnake)
    while (tempIterator.hasNext() and (index < insertionPoint - 1)):
        index += 1
        tempIterator.iterate()
    newSnake.setNextSnake(tempIterator.getSnake().getNextSnake())
    tempIterator.getSnake().setNextSnake(newSnake)
    return firstSnake

def listAllSnakes(firstSnake):
    print("Creating an iterator to help move across the snake list")
    tempIterator = snakeIterator(firstSnake)
    if (firstSnake == None):
        return
    while (tempIterator.hasNext()):
        print("A ", tempIterator.getSnake().getSnakeData(), " snake.")
        #if (tempIterator.hasNext() == False):
        #    break
        tempIterator.iterate()
    print("A ", tempIterator.getSnake().getSnakeData(), " snake.")
    return    

def main():
    firstSnake = None
    
    print("This program was written to give an example of\n",
          "  A) linked lists and how they work, generally, and\n",
          "  B) linked lists, specifically implimented in"
          " the python language\n")
    time.sleep(2)
        
    firstSnake = tiedPython(input(
        "What type of snake is your fist snake? (ex. Python) "))
    print("Created first snake, ", firstSnake.getSnakeData())
    time.sleep(1)
    
    firstSnake.setNextSnake(tiedPython(input(
        "What type of snake is the second snake? (ex. Rattle-Snake) ")))
    print("Created second snake, ", firstSnake.getNextSnake().getSnakeData())
    time.sleep(1)    

    print("Appending a snake to the end of the list")
    appendSnake(firstSnake, tiedPython(input(
        "What type of snake is your third snake? (ex. Copperhead) ")))
    time.sleep(1)

    print("So far, we have created the following snakes: ")
    listAllSnakes(firstSnake)
    time.sleep(2)
    
    print("We can add a snake to the middle of the list")
    tempSnake = tiedPython(input("What type of snake do you want to insert? "))
    firstSnake = insertSnake(firstSnake, tempSnake, int(input(
        "What place in the list do you want to add the snake? ")))
    time.sleep(1)
    
    print("Now we have the following snakes: ")
    listAllSnakes(firstSnake)

main()
