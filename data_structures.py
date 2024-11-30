#!/bin/python3

import timeit
import tracemalloc

setup='''

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

def get_file_lines(num):
        lines = []
        for i in range(num):
                with open("list_files.txt", "r") as file:
                        for line in file:
                                lines.append(line)
        return lines

'''

def define_input_size(dataStrucName, extraSetup, instructions):
	item = 1
	iterator = 64
	if "(com insercao e delecao)" in dataStrucName:
		iterator = 8

	print("--- " + dataStrucName + " ---\n")
	while not item > iterator:
		tracemalloc.start()
		timeTaken = timeit.timeit(instructions, setup=setup + f"input = {item}\nfile = get_file_lines(input)\n{extraSetup}", number=10)
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

''', '''

hashTable.search(1)
hashTable.search(100)
hashTable.search(1000)
hashTable.search(5000)
hashTable.search(hashTable.getSize() - 1)

''')

define_input_size("Hashtable (com insercao e delecao)", hashtable_setup + '''

hashTable_ex = HashTable(len(file))

for idx, i in enumerate(file):
	hashTable_ex.insert(idx, file[idx])

''', '''

import csv

with open("insert_delete_files.txt", mode='r') as i_d_file:

	csvFile = csv.reader(i_d_file, delimiter=";")
	next(csvFile, None)

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
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
    	adj = self.head.next
    	out = ""
    	while adj:
    		out += str(adj.value) + " "
    		adj = adj.next
    	return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
    	return self.size == 0

    def peek(self):
        if self.isEmpty():
            return "Stack is empty."

        return self.head.next.value

    def push(self, value):
    	node = Node(value)
    	node.next = self.head.next
    	self.head.next = node
    	self.size += 1

    def pop(self):
    	if self.isEmpty():
    		raise Exception("Stack is already empty.")
    	remove = self.head.next
    	self.head.next = remove.next
    	self.size -= 1

    	return remove.value

'''

define_input_size("Pilha", stack_setup + '''

stack = Stack()

for i in file:
	stack.push(i)

''', '''

tempData = []

for i in range(stack.getSize() - 2):
	tempData.append(stack.peek())
	stack.pop()
stack.peek()

# tempData.reverse()

for i in tempData:
	stack.push(i)

tempData = []

for i in range(stack.getSize() - 101):
	tempData.append(stack.peek())
	stack.pop()
stack.peek()

# tempData.reverse()

for i in tempData:
	stack.push(i)

tempData = []

for i in range(stack.getSize() - 1001):
	tempData.append(stack.peek())
	stack.pop()
stack.peek()

# tempData.reverse()

for i in tempData:
	stack.push(i)

tempData = []

for i in range(stack.getSize() - 5001):
	tempData.append(stack.peek())
	stack.pop()
stack.peek()

# tempData.reverse()

for i in tempData:
	stack.push(i)

''')

define_input_size("Pilha (com insercao e delecao)", stack_setup + '''

stack_ex = Stack()

for i in file:
	stack_ex.push(i)

''', '''

import csv

with open("insert_delete_files.txt", mode='r') as i_d_file:
	csvFile = csv.reader(i_d_file, delimiter=";")
	next(csvFile, None)

	for lines in csvFile:
		# Removing last number of each index.
		indexAdd = lines[0][:-1]
		filenameAdd = lines[2]
		indexDel = lines[5][:-1]

		# Insert

		tempData = []
		
		for i in range((stack_ex.getSize() - 1) - (int(indexAdd) + 1)):
			tempData.append(stack_ex.peek())
			stack_ex.pop()
		stack_ex.push(indexAdd)

		# tempData.reverse()

		for i in tempData:
			stack_ex.push(i)

		# Delete

		tempData = []
		
		for i in range((stack_ex.getSize() - 1) - (int(indexAdd) + 1)):
			tempData.append(stack_ex.peek())
			stack_ex.pop()

		# tempData.reverse()

		for i in tempData:
			stack_ex.push(i)

''')

# Fila #

queue_setup='''

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, value):
    	new_node = Node(value)
    	if self.rear is None:
    		self.front = self.rear = new_node
    		self.length += 1
    		return
    	self.rear.next = new_node
    	self.rear = new_node
    	self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty."

        temp = self.front
        self.front = temp.next
        self.length -= 1

        if self.front is None:
        	self.rear = None

        return temp.value

    def peek(self):
        if self.isEmpty():
            return "Queue is empty."
        return self.front.value

    def getSize(self):
        return self.length

    def isEmpty(self):
    	return self.length == 0

    def display(self):
    	temp = self.front
    	while temp != None:
    		print(temp.value, end=" ")
    		temp = temp.next

'''

define_input_size("Fila", queue_setup + '''

queue = Queue()

for i in file:
	queue.enqueue(i)

''', '''

tempData = []

for i in range(1):
	tempData.append(queue.peek())
	queue.dequeue()
queue.peek()

for i in tempData:
	queue.enqueue(i)

tempData = []

for i in range(100):
	tempData.append(queue.peek())
	queue.dequeue()
queue.peek()

for i in tempData:
	queue.enqueue(i)

tempData = []

for i in range(1000):
	tempData.append(queue.peek())
	queue.dequeue()
queue.peek()

for i in tempData:
	queue.enqueue(i)

tempData = []

for i in range(5000):
	tempData.append(queue.peek())
	queue.dequeue()
queue.peek()

for i in tempData:
	queue.enqueue(i)

tempData = []

for i in range(queue.getSize() - 1):
	tempData.append(queue.peek())
	queue.dequeue()
queue.peek()

for i in tempData:
	queue.enqueue(i)

''')

define_input_size("Fila (com insercao e delecao)", queue_setup + '''

queue_ex = Queue()

for i in file:
	queue_ex.enqueue(i)

''', '''

import csv

with open("insert_delete_files.txt", mode='r') as i_d_file:
	csvFile = csv.reader(i_d_file, delimiter=";")
	next(csvFile, None)

	for lines in csvFile:
		# Removing last number of each index.
		indexAdd = lines[0][:-1]
		filenameAdd = lines[2]
		indexDel = lines[5][:-1]
		
		# Insert
		
		tempData = []
		
		for i in range(int(indexAdd) + 1):
			tempData.append(queue_ex.peek())
			queue_ex.dequeue()
		queue_ex.enqueue(filenameAdd)
		
		for i in tempData:
		    queue_ex.enqueue(i)
		
		# Delete
		
		tempData = []
		
		for i in range(int(indexDel) + 1):
			tempData.append(queue_ex.peek())
			queue_ex.dequeue()

		for i in tempData:
			queue_ex.enqueue(i)
			
''')