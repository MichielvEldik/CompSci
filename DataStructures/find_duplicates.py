"""
Code inspired by...
https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
"""


def duplicates_check_1(input_list):
    """
    comparing len of listofelements with len of set of listofelements.
    Not the best way to do this.
    Complexity will be n(log(n)) as we are creating a set from a list.
    Even in the best case scenario it will be n(log(n)) because we are adding all elements from list to set.
    It has to make an entire set first before we can start comparing, that may be unnecessary since maybe the match is
    found early on!
    """
    if len(input_list) == len(set(input_list)):
        return False
    else:
        return True


def duplicates_check_2(input_list):
    """
    This time we get around the problem of solution 1.
    We iteratively add elements to our set while checking if it is already part of the set.
    This way, if we had 1_000_000 list items and the match was between item 3 and 4, we find it early on!

    Worst case is n(log(n))
    Best case is much lesser than n(log(n))
    """
    setOfElems = set()
    for elem in input_list:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False


def duplicates_check_3(input_list):
    """
    Here we are iterating over all the elements of list and check count of each element in the list. If count > 1,
    then it means this element has duplicate entries.
    The absolute worst way to do it.

    Time complexity is O(n^2). We are squaring the amount of data!
    """
    for elem in input_list:
        if input_list.count(elem) > 1:
            return True
    return False


def main():
    elements_list = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
    print(duplicates_check_1(elements_list))
    print(duplicates_check_2(elements_list))
    print(duplicates_check_3(elements_list))


if __name__ == '__main__':
    main()