"""
Binary search Python.

Binary search is basically splitting an ordered list through half and throwing half of the list away.
This saves time because that part you throw out, you don't need to look at it!
It's important that the list is sorted of course, else it won't work.
"""

DATA = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
TARGET = 28


def linear_search(data, target):
    """
    It's going to perform linear time. It's not great.
    """
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


def binary_search(data, target):
    """
    log(n) instead of linear time.
    """
    low = 0
    high = len(data) - 1

    while low <= high: # while low is smaller or equal to high
        mid = (low + high) // 2 # middle element of the list
        
        if target == data[mid]: # we found it!
            return True 

        elif target < data[mid]: # if it's in the lower part of the array
            high = mid - 1 # we can throw out the current higher half and reposition our 'high'
        
        else: # other way around. We reposition our low and chuck out current lower portion.
            low = mid + 1
        
    return False


def binary_search_recursive(data, target, low, high):
    """
    We are going to do the exact same thing but with recursion.
    """ 
    if low > high: # if this is true, we know that the target is not in the data
        return False
    else:
        mid = (low + high) // 2
        
        if target == data[mid]:
            return True
        
        elif target < data[mid]: # when we recall again, we have a new high, being mid -1.
            return binary_search_recursive(data, target, low, mid-1) 
        
        else:
            return binary_search_recursive(data, target, mid + 1, high)


print(binary_search(DATA, TARGET))
print(binary_search_recursive(DATA, TARGET, 0, len(DATA) - 1))
