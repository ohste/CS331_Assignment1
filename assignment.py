
#!/usr/bin/python
import sys
import math
import csv

#Global Counters 
expansionCounter = 0

#Generic file handling function to read the two state files
def fileStuff(filepath):
    f = open(filepath,"r")
    reader = csv.reader(f)
    left = next(reader)
    leftBank = [int(left[0]), int(left[1]), int(left[2])]
    right = next(reader)
    rightBank = [int(right[0]), int(right[1]), int(right[2])]
    f.close()
    return leftBank, rightBank

#Gets the initial and final states and stores them in named variables
def entry():
    initialLeft, initialRight = fileStuff(sys.argv[1])
    initialState = [initialLeft, initialRight]
    finalLeft, finalRight = fileStuff(sys.argv[2])
    finalState = [finalLeft, finalRight]
    outputFile = sys.argv[4]
    return initialState, finalState, outputFile


def generateSuccessors(node):
    print("Generating Successors...")
    global expansionCounter
    successors = []

    
    #First we have to find out which side the boat is on
    #node[0] is left bank
    #node[1] is right bank

    #node[0][0] is left bank chickens
    left_chickens = node[0][0]
    #node[1][0]is right bank chickens
    right_chickens = node[1][0]
    #node[0][1] is left bank wolves
    left_wolves = node[0][1]
    #node [1][1] is right bank wolves
    right_wolves = node[1][1]

    #Find where boat is
    is_boat_right_bank = True
    

    if node[1][2] == 1:
        is_boat_right_bank = True
        boat_bank = node[1]
    else:
        is_boat_right_bank = False
        boat_bank = node[0]

            
    print("Boat is in Right Bank:", is_boat_right_bank, " Boat:", boat_bank)
    #1)Put one chicken in the boat

    #2)Put two chickens in the boat

    #3)Put one wolf in the boat

    #4)Put one wolf and one chicken in the boat

    #5)Put two wolves in the boat

    expansionCounter += 1
    return successors

def bfs(initialState, finalState, outputFile):
    print("Running bfs...")
    print("Starting State:", initialState)

    #Establishes a queue of nodes
    nodeList = [initialState]
    currentNode = initialState

    while True:
        if currentNode == finalState:
            #Break out of the infinite loop because we have reached the solution
            break
        else:
            newNode = nodeList.pop(0)

            successors = generateSuccessors(newNode)
            
            break


def dfs(initialState, finalState, outputFile):
    print("Running dfs...")
    

def iddfs(initialState, finalState, outputFile):
    print("Running iddfs...")

def astar(initialState, finalState, outputFile):
    print("Running astar...")


if __name__ == '__main__':

    if(len(sys.argv) != 5):
        print("Err: Missing arguments")
        quit()
    #Here we will parse the files to get the proper input
    initialState, finalState, outputFile = entry()

    #Here we get the mode that we want to run each number represents an algorithm
    # 1 = bfs (breadth first search)
    # 2 = dfs (depth first search)
    # 3 = iddfs (for iterative deepening depth-first search)
    # 4 = astar (A-Star search)

    algo_mode = sys.argv[3]

    if algo_mode == "1":
        bfs(initialState, finalState, outputFile)
    elif algo_mode == "2":
        dfs(initialState, finalState, outputFile)
    elif algo_mode == "3":
        iddfs(initialState, finalState, outputFile)
    elif algo_mode == "4":
        astar(initialState, finalState, outputFile)
    else:
        print("Invalid Mode")
