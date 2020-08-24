"""
Checking out Big-O
"""
import timeit


def get_squared_numbers(numbers):
    """
    O(n) linear time complexity.
    If we increase n with 100, it will do 100 more computations.

    """
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers



def find_first_pe(prices, eps, index):
    """
    O(1) big-O complexity.
    When you supply an index, you will be doing a constant operation. 
    So it does not matter how HUGE your dataset is, you will only look at one item.
    """
    pe = prices[index]/eps[index]
    return pe



def find_duplicate(numbers):
    """
    O(n^2) because time = a* n^2 + b.
    When n grows, it will grow for both lists!
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers [i] == numbers[j]:
                print(numbers[i], " is a duplicate.")
                break

numbers = [2, 5, 8, 9]
numbers = get_squared_numbers(numbers)
print(numbers)

# print(timeit.timeit(get_squared_numbers, number=100))

more_numbers = [3, 6, 2, 4, 3, 6, 8, 9]
find_duplicate(more_numbers)

