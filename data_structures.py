#!/bin/python3

"""
import tracemalloc

tracemalloc.start()

print("Memory: ", tracemalloc.get_traced_memory())

tracemalloc.stop()

"""

import timeit

setup='''
def get_file_lines(num):
        lines = []
        for i in range(num):
                with open("list_files.txt", "r") as file:
                        for line in file:
                                lines.append(line)
        print(len(lines))
        return lines
'''

def define_input_size(algName, instructions):
        item = 1

        print("--- " + algName + " ---\n")
        while not item > 8:
                timeTaken = timeit.timeit(instructions, setup=setup + f"input = {item}\nfile = get_file_lines(input)", number=10)
                print(f"Tempo (AVG): {timeTaken} - {item}x a entrada.")
                item = item * 2
        print()

# Hashtable #

define_input_size("Bubble Sort", '''

def bubble_sort(list):
        size = len(list)
        for i in range(size):
                for j in range(0, size-i-1):
                        if list[j] > list[j+1]:
                                list[j], list[j+1] = list[j+1], listj]

bubble_sort(file)

''')

# Pilha #

define_input_size("Selection Sort", '''

def selection_sort(list):
        size = len(list)

        for i in range(size - 1):
                smallest_idx = i
                for j in range(i + 1, size):
                        if list[j] < list[smallest_idx]:
                                smallest_idx = j

                list[i], list[smallest_idx] = list[smallest_idx], list[i]

selection_sort(file)

''')

# Fila #

define_input_size("Fila", '''

def insertion_sort(list):
        size = len(list)

        for i in range(1, size):
                key = list[i]
                j = i - 1

                while j >= 0 and key < list[j]:
                        list[j + 1] = list[j]
                        j -= 1
                list[j + 1] = key

insertion_sort(file)

''')
