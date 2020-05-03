from pathlib import Path

values = Path('https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa.txt').read_text()

class HashTable(object):
    def __init__(self, length=4):
        self.array = [None] * length

    def hash(selfself, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvPairs in self.array[index]:
                if kvPairs[0] == key:
                    kvPairs[1] = value
                    break

            else:
                self.array[index].append([key, value])

        if self.is_full():
            self.double()

    def get(selfself, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvPairs in self.array[index]:
                if kvPairs[0] ==key:
                    return kvPairs[1]

            raise KeyError()

    def is_full(self):
        items = 0
        for item in self.array:
            if item is not None:
                items += 1
        return items > len(self.array)/2

    def double(self):
        htTwo = HashTable(length=len(self.array)*2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for kvPairs in self.array[i]:
                htTwo.add(kvPairs[0], kvPairs[1])

        self.array = htTwo.array


