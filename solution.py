# Guided Solution

def hourglassSum(arr):
    # we're only dealing with 6x6 matrices 
    # what's the deal with this hourglass shape? 
        # from some initial starting point, we the next three elements 
        # initial matrix position is arr[x][y]
        # we need arr[x][y+1] and arr[x][y+2]
        # we need the element that diagonally down from the initial element 
        # we need arr[x+1][y+1]
        # we also need the three elements in the current row + 2 
        # we need arr[x+2][y], arr[x+2][y+1], arr[x+2][y+2]
        # take all these and sum them up to get the hourglass sum 
        # we need to sum up the values in the hourglass 
        # need to figure out the maximum hourglass sum 
        
    current_max = float("-inf")
    # traverse through our entire matrix, calculating each hourglass sum
    # as we go 
    for row in range(len(arr)-2):
        for column in range(len(arr[0])-2):
            # find the hourglass sum from this current orientation point 
            current_sum = sum_hourglass(arr, row, column)
            # compare the sum to the largest sum we've seen so far
            if current_sum > current_max:
                current_max = current_sum
    # return the largest sum we've seen so far 
    return current_max
​
def sum_hourglass(arr, x, y):
    # does the work of calculating the hourglass sum values 
    # given a starting orientation point at the top left 
    # of the hourglass 
    # we need the position of the orientation point 
    # also need the matrix itself 
    total = arr[x][y]
    # sum up the other values 
    total += arr[x][y+1]
    total += arr[x][y+2]
    total += arr[x+1][y+1]
    total += arr[x+2][y]
    total += arr[x+2][y+1]
    total += arr[x+2][y+2]
​
    return total
