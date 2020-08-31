"""
Code basics Hashing implementation.
1. create an array with all Nones for range 100.
2. mod-hash so any key value is turned into something between 0 and n-1. <- max range for modulo operation. (99)
3. result from the hash (e.g., 9) is the index number that will be used for our array full of Nones.
4. at index 9 (9 being the hash result of march 6), a value can now be placed to fill out the None (130)
"""


class HashTable:
    def __init__(self):
        """
        set size of bucket array.
        Use list comprehension to turn each value into None.
        """
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        """
        Input: key (string)
        ord(char) will find an ASCII value for a character.
        Output: Mod 100 of sum all ASCII values.
        """
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add_key_value(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)  # create a hash function for the key 'March 6'. h: 9
        return self.arr[h]  # return the value in our bucket array for index 9.


t = HashTable()
print(t.get_hash('march 6'))

# we add a key value
t.add_key_value('march 6', 130)

# on the 9th place, there will be 130.
print(t.arr)

# how to get key value
print(t.get('march 6'))




