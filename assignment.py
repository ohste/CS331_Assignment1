
#!/usr/bin/python
import sys
import math
import csv

#Global Counters
expansionCounter = 0
explored_set = []

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

def check_valid_state(state):
    isValid = True
    for bank in state:
        if (bank[1]>bank[0] and bank[0] != 0):
            isValid = False
        if (bank[0] < 0 or bank[1] < 0):
            isValid = False
    return isValid

def generateSuccessors(node, successors = []):
    print("Generating Successors...")
    global expansionCounter


    #First we have to find out which side the boat is on
    #node[0] is left bank
    #node[1] is right bank

    #Find where boat is
    is_boat_right_bank = True


    if node[1][2] == 1:
        is_boat_right_bank = True
        boat_bank = node[1]
        destination_bank = node[0]
    else:
        is_boat_right_bank = False
        boat_bank = node[0]
        destination_bank = node[1]

    #Get chicken and wolves from boat bank
    boat_bank_chickens = boat_bank[0]
    boat_bank_wolves = boat_bank[1]

    #Get chicken and wolves from destination bank
    destination_bank_chickens = destination_bank[0]
    destination_bank_wolves = destination_bank[1]

    #print("Boat is in Right Bank:", is_boat_right_bank, " Boat:", boat_bank)
    print("Current state: ", node)
    explored_set.append(node)
    #1) Conditions: Put one chicken in the boat, more chickens than wolves

    #For Right Banks
    if is_boat_right_bank:
        successor_left = destination_bank.copy()
        successor_left[0] += 1
        successor_right = boat_bank.copy()
        successor_right[0] -= 1
        successor_left[2] = 1
        successor_right[2] = 0
    else: #For Left Bank
        successor_left = boat_bank.copy()
        successor_left[0] -= 1
        successor_right = destination_bank.copy()
        successor_right[0] += 1
        successor_right[2] = 1
        successor_left[2] = 0

    #Make sure our successor is a valid state
    successor_final = [successor_left, successor_right]
    if (check_valid_state(successor_final) and successor_final not in explored_set):
        print("Condition 1 Successor: ", successor_final)
        successors.append(successor_final)

    #2)Conditions: Put two chickens in the boat, At least 2 chickens at Boat bank, Destination wolves - destination chickens <= 2, destination chickens > destination wolves + 1 OR boat bank chickens == 2

    if is_boat_right_bank:
        successor_left = destination_bank.copy()
        successor_left[0] += 2
        successor_right = boat_bank.copy()
        successor_right[0] -= 2
        successor_left[2] = 1
        successor_right[2] = 0
    else: #For Left Bank
        successor_left = boat_bank.copy()
        successor_left[0] -= 2
        successor_right = destination_bank.copy()
        successor_right[0] += 2
        successor_right[2] = 1
        successor_left[2] = 0

    #Make sure our successor is a valid state
    successor_final = [successor_left, successor_right]
    if (check_valid_state(successor_final) and successor_final not in explored_set):
        print("Condition 2 Successor: ", successor_final)
        successors.append(successor_final)

    #3)Conditions: Put one wolf in the boat, Destination bank chickens must be greater than wolves + incoming wolf.

    if is_boat_right_bank:
        successor_left = destination_bank.copy()
        successor_left[1] += 1
        successor_right = boat_bank.copy()
        successor_right[1] -= 1
        successor_left[2] = 1
        successor_right[2] = 0
    else: #For Left Bank
        successor_left = boat_bank.copy()
        successor_left[1] -= 1
        successor_right = destination_bank.copy()
        successor_right[1] += 1
        successor_right[2] = 1
        successor_left[2] = 0

    #Make sure our successor is a valid state
    successor_final = [successor_left, successor_right]
    if (check_valid_state(successor_final) and successor_final not in explored_set):
        print("Condition 3 Successor: ", successor_final)
        successors.append(successor_final)

    #4)Condtions: Put one wolf and one chicken in the boat, Destination bank needs wolves <= chickens, Boat bank needs wolves >=1 & chickens >= 1

    if is_boat_right_bank:
        successor_left = destination_bank.copy()
        successor_left[0] += 1
        successor_left[1] += 1
        successor_right = boat_bank.copy()
        successor_right[0] -= 1
        successor_right[1] -= 1
        successor_left[2] = 1
        successor_right[2] = 0
    else: #For Left Bank
        successor_left = boat_bank.copy()
        successor_left[0] -= 1
        successor_left[1] -= 1
        successor_right = destination_bank.copy()
        successor_right[0] += 1
        successor_right[1] += 1
        successor_right[2] = 1
        successor_left[2] = 0

    #Make sure our successor is a valid state
    successor_final = [successor_left, successor_right]
    if (check_valid_state(successor_final) and successor_final not in explored_set):
        print("Condition 4 Successor: ", successor_final)
        successors.append(successor_final)


    #5)Conditions: Put two wolves in the boat, Destination bank chickens == 0 OR Destination bank wolves <= chickens -1, Boat bank wolves >= 2

    if is_boat_right_bank:
        successor_left = destination_bank.copy()
        successor_left[1] += 2
        successor_right = boat_bank.copy()
        successor_right[1] -= 2
        successor_left[2] = 1
        successor_right[2] = 0
    else: #For Left Bank
        successor_left = boat_bank.copy()
        successor_left[1] -= 2
        successor_right = destination_bank.copy()
        successor_right[1] += 2
        successor_right[2] = 1
        successor_left[2] = 0

    #Make sure our successor is a valid state
    successor_final = [successor_left, successor_right]
    if (check_valid_state(successor_final) and successor_final not in explored_set):
        print("Condition 5 Successor: ", successor_final)
        successors.append(successor_final)


    print("Successors: ", successors)
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

#Function to solve depth-first search
def dfs(initialState, finalState, outputFile):
    currentNode = initialState
    explored_set.append(initialState)

    dead_end = False
    print("final state is: ", finalState)

    #Keep searching the graph if we don't find the final state
    while (currentNode != finalState):
        successors = generateSuccessors(currentNode)
        #Check if we've reached a dead end
        if (len(successors) == 0):
            dead_end = True
            break
        next_to_check = successors.pop()
        currentNode = next_to_check

    if(dead_end):
        print("Reached the end of the graph and could not find a solution")
    else:
        print("We were successful!")
        print("We expanded ", expansionCounter, "nodes")

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
