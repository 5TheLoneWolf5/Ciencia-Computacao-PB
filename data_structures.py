#!/bin/python3

import timeit
import tracemalloc

setup='''
def get_file_lines(num):
        lines = []
        for i in range(num):
                with open("list_files.txt", "r") as file:
                        for line in file:
                                lines.append(line)
        return lines
'''

def define_input_size(dataStrucName, instructions):
	item = 1

	print("--- " + dataStrucName + " ---\n")
	while not item > 8:
		tracemalloc.start()
		timeTaken = timeit.timeit(instructions, setup=setup + f"input = {item}\nfile = get_file_lines(input)", number=10)
		print("Memoria: ", tracemalloc.get_traced_memory())
		tracemalloc.stop()
		print(f"Tempo (AVG): {timeTaken} - {item}x a entrada.")
		item = item * 2
	print()

# Hashtable #

hashtable_setup='''

class HashTable:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def hash(self, key):
        return hash(key) % self.capacity

    def getSize(self):
        return self.size

    def insert(self, key, value):
        idx = self.hash(key)

        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[idx].append([key, value])
        self.size += 1

    def search(self, key):
        idx = self.hash(key)

        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        idx = self.hash(key)

        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                del self.table[idx][i]
                self.size -= 1
                return True

        return False

    def __str__(self):
        result = []

        for listTable in self.table:
            for pair in listTable:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{ " + ", ".join(result) + " }"

'''

define_input_size("Hashtable", hashtable_setup + '''

hashTable = HashTable(len(file))

for idx, i in enumerate(file):
	hashTable.insert(idx, file[idx])

hashTable.search(1)
hashTable.search(100)
hashTable.search(1000)
hashTable.search(5000)
hashTable.search(hashTable.getSize() - 1)

''')

define_input_size("Hashtable (com insercao e delecao)", hashtable_setup + '''

import csv

with open("insert_delete_files.txt", mode='r') as i_d_file:
	csvFile = csv.reader(i_d_file, delimiter=";")
	next(csvFile, None)

	hashTable_ex = HashTable(len(file))
	for idx, i in enumerate(file):
		hashTable_ex.insert(idx, file[idx])

	for lines in csvFile:
		# Removing last number of each index.
		indexAdd = lines[0][:-1]
		filenameAdd = lines[2]
		indexDel = lines[5][:-1]
		hashTable_ex.insert(indexAdd, filenameAdd)
		hashTable_ex.remove(indexDel)

''')

# Pilha #

stack_setup='''

class Stack:
    def __init__(self, size_limit):
        self.size_limit = size_limit
        self.stack = [None] * size_limit
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.size_limit <= self.size()

    def size(self):
        if self.is_empty():
            return -1

        return self.top + 1

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")

        return self.stack[self.top]

    def push(self, item):
        if self.is_full():
            return "Stack is full."

        self.top += 1
        self.stack[self.top] = item

        return self.stack[self.top]

    def pop(self):
        if self.is_empty():
            return "Stack is already empty."
        self.stack[self.top] = None
        self.top -= 1

        return self.stack[self.top]

'''

define_input_size("Pilha", stack_setup + '''

stack_1 = Stack(len(file))
stack_2 = Stack(len(file))
stack_3 = Stack(len(file))
stack_4 = Stack(len(file))
stack_5 = Stack(len(file))

for i in file:
	stack_1.push(i)
	stack_2.push(i)
	stack_3.push(i)
	stack_4.push(i)
	stack_5.push(i)

for i in range(1):
	stack_1.pop()
stack_1.peek()

for i in range(100):
	stack_2.pop()
stack_2.peek()

for i in range(1000):
	stack_3.pop()
stack_3.peek()

for i in range(5000):
	stack_4.pop()
stack_4.peek()

for i in range(stack_5.size() - 1):
	stack_5.pop()
stack_5.peek()

''')

define_input_size("Pilha (com insercao e delecao)", stack_setup + '''

import csv

with open("insert_delete_files.txt", mode='r') as i_d_file:
	csvFile = csv.reader(i_d_file, delimiter=";")
	next(csvFile, None)

	stack_ex = Stack(len(file))
	for i in file:
		stack_ex.push(i)

	for lines in csvFile:
		# Removing last number of each index.
		indexAdd = lines[0][:-1]
		filenameAdd = lines[2]
		indexDel = lines[5][:-1]
		for i in range(int(indexAdd) + 1):
			stack_ex.pop()
		stack_ex.push(indexAdd)

		for i in range(int(indexDel) + 1):
			stack_ex.pop()

''')

# Fila #

queue_setup='''

class Queue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):

        if self.is_full():
            print("Fila cheia.")
            return

        self.items[self.end] = item
        self.end += 1
        self.size += 1

        if self.end == self.capacity:
            self.end = 0

    def dequeue(self):
        # if self.is_empty():
           #  print("Fila vazia.")
           #  return

        item = self.items[self.start]
        self.items[self.start] = None
        self.start += 1
        self.size -= 1

        if self.start == self.capacity:
            self.start = 0

        return item

    def peek(self):
        # if self.is_empty():
            # print("Fila vazia")
            # return None
        return self.items[self.start]

    def getSize(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Fila vazia.")
            return
        else:
            for i in range(self.size):
                index = (self.start + i) % self.capacity
                print(self.items[index], end=" ")
'''

define_input_size("Fila", queue_setup + '''

queue_1 = Queue(len(file))
queue_2 = Queue(len(file))
queue_3 = Queue(len(file))
queue_4 = Queue(len(file))
queue_5 = Queue(len(file))

for i in file:
	queue_1.enqueue(i)
	queue_2.enqueue(i)
	queue_3.enqueue(i)
	queue_4.enqueue(i)
	queue_5.enqueue(i)

for i in range(1):
	queue_1.dequeue()
queue_1.peek()

for i in range(100):
	queue_2.dequeue()
queue_2.peek()

for i in range(1000):
	queue_3.dequeue()
queue_3.peek()

for i in range(5000):
	queue_4.dequeue()
queue_4.peek()

for i in range(queue_5.getSize() - 1):
	queue_5.dequeue()
queue_5.peek()

''')

define_input_size("Fila (com insercao e delecao)", queue_setup + '''

import csv

with open("insert_delete_files.txt", mode='r') as i_d_file:
	csvFile = csv.reader(i_d_file, delimiter=";")
	next(csvFile, None)

	queue_ex = Queue(len(file))
	for i in file:
		queue_ex.enqueue(i)

	for lines in csvFile:
		# Removing last number of each index.
		indexAdd = lines[0][:-1]
		filenameAdd = lines[2]
		indexDel = lines[5][:-1]
		for i in range(int(indexAdd) + 1):
			queue_ex.dequeue()
		queue_ex.enqueue(indexAdd)

		for i in range(int(indexDel) + 1):
			queue_ex.dequeue()
''')
