"""
Trying out iterators and generators to see how they work.
codebasics: https://www.youtube.com/watch?v=Fc1fLEk_Kr0
The iter does not need to be called necessarily.
"""
a_list = ["Hello", "World", "how", "are", "ya", "?"]
for i in a_list:
    print(i)
print(dir(a_list))
itr = iter(a_list)


print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(dir(itr))


class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "CNN", "ABC", "ESPN"]
        self.index = -1  # what channel we are on right now. In this case not 0, so -1.

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):  # when it reaches the end, it stops iteration.
            raise StopIteration
        return self.channels[self.index]



r = RemoteControl()
itr = iter(r)
for i in itr:
    print(next(r))
