import sys, csv

def fileStuff(filepath):
    f = open(filepath,"r")
    reader = csv.reader(f)
    left = next(reader)
    leftBank = [int(left[0]), int(left[1]), int(left[2])]
    right = next(reader)
    rightBank = [int(right[0]), int(right[1]), int(right[2])]
    f.close()
    return leftBank, rightBank

def entry():
    initialLeft, initialRight = fileStuff(sys.argv[1])
    print("Left Bank", initialLeft)
    print("Right Bank", initialRight)
    finalLeft, finalRight = fileStuff(sys.argv[2])
    print("Left Bank", finalLeft)
    print("Right Bank", finalRight)
    algToUse = sys.argv[3]
    outputFile = sys.argv[4]

if __name__ == '__main__':
    print("Yo")
    entry()
