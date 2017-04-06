'''
Created on Mar 6, 2017

@author: Stanislav Petrov
'''

import sys, io

def inplace_sort(input_string):
    number_index, string_index, output_string, number_list, string_list = 0, 0,"",[],[]
    for item in input_string.split(' '):
        if item.isdigit():
            number_list.append(int(item))
        else:
            string_list.append(item)
    
    number_list = sorted(number_list)
    string_list = sorted(string_list)
    
    for item in input_string.split():
        if item.isdigit():
            output_string += str(number_list[number_index]) + " "
            number_index += 1
        else:
            output_string += string_list[string_index] + " "
            string_index += 1

    return "\nOutput:\n"+output_string

sys.stdin = io.StringIO(input("Input:"))
test_string = inplace_sort(input())
sys.stdout.write(test_string)
