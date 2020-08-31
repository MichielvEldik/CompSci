class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False  # by default set it to not found a.k.a. found = False
        for idx, element in enumerate(self.arr[h]):  # [('march 54', 130), ('march 81', 459)]
            if len(element) == 2 and element[0] == key:  # if you wanted to update march 54 from value 6 to e.g. 130
                self.arr[h][idx] = (key, val)  # the original value (6) will be replaced while the key stays the same
                found = True  # break from the sequence
                break
        if not found:
            self.arr[h].append((key, val))  # if there were no matches, we want to append our NESTED list.

    def __getitem__(self, key):
        h = self.get_hash(key)  # 60 in this case, which grants us access to the nested list.
        for element in self.arr[h]:  # arr[h] being at index 60 in this case
            if element[0] == key:  # element zero being the ('march 54', ...) or ('march 81', ...)
                return element[1]  # return the second element when key matches element[0], 130 or 459

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]


t = HashTable()
y = HashTable()
t['march 54'] = 130
t['march 81'] = 459


print(t['march 54'])
print(t['march 81'])

# the problem: for march 54 and march 81, there is a collision. Both make for the same index so it is overwritten.
print(t.get_hash('march 54'))
print(t.get_hash('march 81'))

print(t.arr)
