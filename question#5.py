# Write a Python program to generate an infinite cycle of elements from an iterable.
list = [1,2,3,4,5]
def infinite_func(list):
    for i in list:
        return infinite_func(list)

print(infinite_func(list))
