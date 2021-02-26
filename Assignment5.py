# Assignment 5 for CS 411
# Author: Matthew Alvero
# NetID: malver2
# UIN: 663738906
# Created on 02/25/21


# Any imports needed go under here


# Board class that stores the game board (state)
class State:
    
    # constructor
    def __init__(self, grid):
        self.grid = grid
        self.emptySpaceIdx = grid.index('0')
    
    # get the state after a left move
    def getLeftState(self):
        # check if we can even move left
        if self.emptySpaceIdx == 0 or self.emptySpaceIdx % 4 == 0:
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid[:]
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx-1]
            newState[self.emptySpaceIdx - 1] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            return State(newState)
            

    # get the state after a right move
    def getRightState(self):
        # check if we can even move right
        if self.emptySpaceIdx % 3 == 0:
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid[:]
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx+1]
            newState[self.emptySpaceIdx + 1] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            return State(newState)

    # get the state after a up move
    def getUpState(self):
        # check if we can even move up
        if self.emptySpaceIdx in range (0,5):
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid[:]
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx - 4]
            newState[self.emptySpaceIdx - 4] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            return State(newState)
    
    # get the state after a down move
    def getDownState(self):
        # check if we can even move down
        if self.emptySpaceIdx in range (12,16):
            pass
        # otherwise, get the left state
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.grid[:]
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx + 4]
            newState[self.emptySpaceIdx + 4] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            return State(newState)

# Node class that stores information of nodes
class Node:
    
    # constructor
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
    
    # return a string representation of the state
    def __repr__(self):
        return str(self.state.grid)
    
    # comparing nodes
    def __eq__(self, other):
        return self.state.grid == other.state.grid

    # hash
    def __hash__(self):
        return hash(tuple(self.state.grid))
    
    # add children to the node
    def add_children(self):
        left = self.state.getLeftState()
        right = self.state.getRightState()
        up = self.state.getUpState()
        down = self.state.getDownState()
        if left is not None:
            self.children.append(Node(left, self, 'L', self.depth+1))
        if right is not None:
            self.children.append(Node(right, self, 'R', self.depth+1))
        if up is not None:
            self.children.append(Node(up, self, 'U', self.depth+1))
        if down is not None:
            self.children.append(Node(down, self, 'D', self.depth+1))
        return self.children

# Function to back track from current node to the root node
def backtrack(node):
    path = []
    while(node.parent is not None):
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path

# utility function to test if we have the desired goal
def goal_test(grid):
    return grid == ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']

# main a star search function


# main function
def main():
    board = str(input("Enter initial board: "))
    initial_list = board.split(" ")
    root = Node(State(initial_list), None, None)
    print
# run main
if __name__ == '__main__':
    main()
