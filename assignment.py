
#!/usr/bin/python
import sys
import math
import csv
from operator import attrgetter


class node(object):

    goal = None

    def __init__(self, state, children = None):
        self.state = state
        self.depth = 0
        self.children = []
        self.parent = None
        self.cost = 0
        for child in self.children:
            child.parent = self

    def add_goal(self, target):
        self.goal = target

    def add_children(self, successors):
        self.children = successors

    def add_parent(self, parent):
        self.parent = parent

    def increment_depth(self):
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

    def set_cost(self, goal):
        g = self.depth
        h = ((goal[0][0] - self.state[0][0]) + (goal[0][1] - self.state[0][1])) / 2
        self.cost = g+h




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
    if (state in explored_set):
        isValid = False

    # print("~~~~~~~~~~~~~~~~Let's validate the checking function~~~~~~~~~~~~~")
    # print("This is the state to check: ", state)
    # print("This is the explored set: ", explored_set)
    # print("Do we find it valid? ", isValid)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return isValid

def generateSuccessors(nodeObject, goal = []):
    print("Generating Successors...")
    global expansionCounter

    successors = []
    #Get current state from node object
    nodeState = nodeObject.state
    if (nodeState in explored_set):
        return []
    #First we have to find out which side the boat is on
    #node[0] is left bank
    #node[1] is right bank

    #Find where boat is
    is_boat_right_bank = True


    if nodeState[1][2] == 1:
        is_boat_right_bank = True
        boat_bank = nodeState[1]
        destination_bank = nodeState[0]
    else:
        is_boat_right_bank = False
        boat_bank = nodeState[0]
        destination_bank = nodeState[1]

    #Get chicken and wolves from boat bank
    boat_bank_chickens = boat_bank[0]
    boat_bank_wolves = boat_bank[1]

    #Get chicken and wolves from destination bank
    destination_bank_chickens = destination_bank[0]
    destination_bank_wolves = destination_bank[1]

    #print("Boat is in Right Bank:", is_boat_right_bank, " Boat:", boat_bank)
    #print("Current state: ", nodeState)
    explored_set.append(nodeState)
    #print("Explored set: ", explored_set)
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
    if (check_valid_state(successor_final)):
        print("Condition 1 Successor: ", successor_final)
        successor_node = node(successor_final)
        #Increments depth of node for use in iddfs
        successor_node.add_parent(nodeObject)
        successor_node.increment_depth()

        successor_node.set_cost(goal)
        print("Successor Cost: ", successor_node.cost)
        print("Successor Depth in function: ", successor_node.depth)
        successors.append(successor_node)

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
    if (check_valid_state(successor_final)):
        print("Condition 2 Successor: ", successor_final)
        successor_node = node(successor_final)
        #Increments depth of node for use in iddfs
        successor_node.add_parent(nodeObject)
        successor_node.increment_depth()
        successor_node.set_cost(goal)
        print("Successor Cost: ", successor_node.cost)
        successors.append(successor_node)

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
    if (check_valid_state(successor_final)):
        print("Condition 3 Successor: ", successor_final)
        successor_node = node(successor_final)
        #Increments depth of node for use in iddfs
        successor_node.add_parent(nodeObject)
        successor_node.increment_depth()
        successor_node.set_cost(goal)
        print("Successor Cost: ", successor_node.cost)
        successors.append(successor_node)

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
    if (check_valid_state(successor_final)):
        print("Condition 4 Successor: ", successor_final)
        successor_node = node(successor_final)
        #Increments depth of node for use in iddfs
        successor_node.add_parent(nodeObject)
        successor_node.increment_depth()
        successor_node.set_cost(goal)
        print("Successor Cost: ", successor_node.cost)
        successors.append(successor_node)


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
    if (check_valid_state(successor_final)):
        print("Condition 5 Successor: ", successor_final)
        successor_node = node(successor_final)
        #Increments depth of node for use in iddfs
        successor_node.add_parent(nodeObject)
        successor_node.increment_depth()
        successor_node.set_cost(goal)
        print("Successor Cost: ", successor_node.cost)
        successors.append(successor_node)

    #print("What is successors: ", successors)
    nodeObject.add_children(successors)
    #Should be a bunce of Node objects
    #print("Successors: ", successors)
    expansionCounter += 1
    return successors

def bfs(startNode, outputFile):
    print("Running bfs...")
    print("Starting State:", startNode.state)
    print("Goal:", startNode.goal)
    #Establishes a queue of nodes
    currentNode = startNode
    nodes_to_explore = [startNode]
    dead_end = False
    print("final state is: ", startNode.goal)

    #Keep searching the graph if we don't find the final state
    while (currentNode.state != startNode.goal):
        nodes_to_explore += generateSuccessors(currentNode, startNode.goal)
        #Check if we've reached a dead end
        if (len(nodes_to_explore) == 0):
            dead_end = True
            break
        next_to_check = nodes_to_explore.pop(0)
        currentNode = next_to_check

    if(dead_end):
        print("Reached the end of the graph and could not find a solution")
    else:
        print("We were successful!")
        print("We expanded ", expansionCounter, "nodes")
        printSolution(currentNode, outputFile)


#Function to solve depth-first search
def dfs(startNode, outputFile):
    currentNode = startNode
    nodes_to_explore = [startNode]
    dead_end = False
    print("final state is: ", startNode.goal)

    #Keep searching the graph if we don't find the final state
    while (currentNode.state != startNode.goal):
        nodes_to_explore += generateSuccessors(currentNode, startNode.goal)
        #Check if we've reached a dead end
        if (len(nodes_to_explore) == 0):
            dead_end = True
            break
        next_to_check = nodes_to_explore.pop()
        currentNode = next_to_check

    if(dead_end):
        print("Reached the end of the graph and could not find a solution")
    else:
        print("We were successful!")
        print("We expanded ", expansionCounter, "nodes")
        printSolution(currentNode, outputFile)


def iddfs(startNode, outputFile):
    depth_limit = 2
    found_goal = False
    while (not found_goal):
        currentNode = startNode
        nodes_to_explore = [startNode]
        global explored_set
        explored_set = []
        dead_end = False

        #print("final state is: ", startNode.goal)

        #Keep searching the graph if we don't find the final state
        while (currentNode.state != startNode.goal):
            next_nodes = generateSuccessors(currentNode, startNode.goal)
            for item in next_nodes:
                if (item.depth <= depth_limit):
                    nodes_to_explore.append(item)

            #Check if we've reached a dead end
            if (len(nodes_to_explore) == 0):
                print("reached the end of this depth limit")
                dead_end = True
                break
            next_to_check = nodes_to_explore.pop()
            currentNode = next_to_check
            if (currentNode.state == startNode.goal):
                dead_end = False
                found_goal = True
                break
        depth_limit += 1
    if(dead_end):
        print("Reached the end of the graph and could not find a solution")
    else:
        print("We were successful!")
        print("We expanded ", expansionCounter, "nodes")
        printSolution(currentNode, outputFile)


def astar(initialState, finalState, outputFile):
    currentNode = startNode
    nodeList = [startNode]
    dead_end = False
    nodes_to_check = []
    while (currentNode.state != startNode.goal):
        nodes_to_check += generateSuccessors(currentNode, finalState)
        #Check if we've reached a dead end
        if (len(nodes_to_check) == 0):
            dead_end = True
            break
        min_cost_node_index = nodes_to_check.index(min(nodes_to_check, key=attrgetter('cost')))
        print("min_cost_node_index", min_cost_node_index)
        next_to_check = nodes_to_check.pop(min_cost_node_index)
        #print("The min cost node is ", next_to_check)
        currentNode = next_to_check

    if(dead_end):
        print("Reached the end of the graph and could not find a solution")
    else:
        print("We were successful!")
        print("We expanded ", expansionCounter, "nodes")
        printSolution(currentNode, outputFile)



def printSolution(finalNode, ourputFile):

    print("Solution: ", finalNode.state)

    parent = finalNode.parent

    while parent is not None:
        print("Solution: ", parent.state)
        parent = parent.parent


if __name__ == '__main__':

    if(len(sys.argv) != 5):
        print("Err: Missing arguments")
        quit()
    #Here we will parse the files to get the proper input
    initialState, finalState, outputFile = entry()

    startNode = node(initialState)

    startNode.add_goal(finalState)

    #Here we get the mode that we want to run each number represents an algorithm
    # 1 = bfs (breadth first search)
    # 2 = dfs (depth first search)
    # 3 = iddfs (for iterative deepening depth-first search)
    # 4 = astar (A-Star search)

    algo_mode = sys.argv[3]

    if algo_mode == "1":
        #bfs(initialState, finalState, outputFile)
        bfs(startNode, outputFile)
    elif algo_mode == "2":
        #dfs(initialState, finalState, outputFile)
        dfs(startNode, outputFile)
    elif algo_mode == "3":
        iddfs(startNode, outputFile)
    elif algo_mode == "4":
        astar(initialState, finalState, outputFile)
    else:
        print("Invalid Mode")
