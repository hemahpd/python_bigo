#An algorithm is said to have a linear time complexity when the running time increases at most linearly with the size of the input data.
# This is the best possible time complexity when the algorithm must examine all values in the input data.

#Ex: Linear Search

def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')


if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(linear_search(data, 7))


#Note that in this example, we need to look at all values in the list to find the value we are looking for.
