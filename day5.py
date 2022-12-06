#skipped day 4 temporarily. 6/12/22
#part 1, maybe make every stack in a list?
stack1 = ['Q', 'H', 'C', 'T', 'N', 'S', 'V', 'B']
stack2 = ['G', 'B', 'D', 'W']
stack3 = ['B', 'Q', 'S', 'T', 'R', 'W', 'F']
stack4 = ['N', 'D', 'J', 'Z', 'S', 'W', 'G', 'L']
stack5 = ['F', 'V', 'D', 'P', 'M'] 
stack6 = ['J', 'W', 'F']
stack7 = ['V', 'J', 'B', 'Q', 'N', 'L']
stack8 = ['N', 'S', 'Q', 'J', 'C', 'R', 'T', 'G']
stack9 = ['M', 'D', 'W', 'C', 'Q', 'S', 'J']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

with open("day5input.txt", 'r') as readfile:
    for line in readfile.readlines()[10:]:
        values = line.split()
        x, y, z = int(values[1]), int(values[3]), int(values[5])
        def moveCrate(noOfCrates: int, stackMovedFrom: int, stackMovedTo: int):
            stackToRemoveFrom = stacks[(stackMovedFrom - 1)]
            del stackToRemoveFrom[2:stackMovedFrom]
            stackToAddTo = stacks[(stackMovedTo - 1)]
            stackToAddTo.insert(0, (range(0, noOfCrates)))
        def printTopCrate():
            for x in stacks:
                print(stacks[x][0])
        moveCrate(x, y, z)
        printTopCrate()