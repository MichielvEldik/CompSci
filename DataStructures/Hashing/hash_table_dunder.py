"""
Code basics Hashing implementation

making the interaction with our HashTable object a little smoother.

1. __setitem__(self, key, value). called by self[key]
Changing your method to this special one will make it able to do this self['key'] = 130.
In this way, it's easy to set a value for a certain key in your array.

2. __getitem__ (self, key) called by self['key'].

This way, you can easily retrieve a value mapped to a certain key.
"""


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t['march 6'] = 130
print(t['march 6'])





