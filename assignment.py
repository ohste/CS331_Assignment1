#!/usr/bin/python

import sys
import math

def bfs():
    print("Running bfs...")

def dfs():
    print("Running dfs...")   

def iddfs():
    print("Running iddfs...")

def astar():
    print("Running astar...")


def main():

    #Here we will parse the files to get the proper input


    #Here we get the mode that we want to run each number represents an algorithm
    # 1 = bfs (breadth first search)
    # 2 = dfs (depth first search)
    # 3 = iddfs (for iterative deepening depth-first search)
    # 4 = astar (A-Star search)

    algo_mode = sys.argv[3]

    if algo_mode == "1":
        bfs()
    elif algo_mode == "2":
        dfs()
    elif algo_mode == "3":
        iddfs()
    elif algo_mode == "4":
        astar()
    else:
        print("Invalid Mode")


main()

