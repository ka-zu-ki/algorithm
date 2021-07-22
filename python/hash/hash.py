import hashlib


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self):
        for index in range(self.size):
            print(index, end='\n')
            for data in self.table[index]:
                print(data, end='\n')

    def get(self, key):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return print(data[1])


hash_table = HashTable()
hash_table.add('car', 'Tesla')
hash_table.add('car', 'Toyota')
hash_table.add('pc', 'Mac')
hash_table.add('sns', 'Youtube')
hash_table.print()
hash_table.get('car')
hash_table.get('sns')