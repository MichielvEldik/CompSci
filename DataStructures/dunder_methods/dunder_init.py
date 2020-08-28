"""
This will only output the memory address of a string object.
That's because we have not provided a __rep__ yet!
"""


# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    # Driver Code


if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)
