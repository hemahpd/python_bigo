#An algorithm is said to have a factorial time complexity when it grows
# in a factorial way based on the size of the input data

#EX: Heap permutations

def heap_permutation(data, n):
    if n == 1:
        print(data)
        return

    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]


if __name__ == '__main__':
    data = [1, 2, 3]
    heap_permutation(data, len(data))
