#An algorithm is said to have a quadratic time complexity when it needs
# to perform a linear time operation for each value in the input data

#Bubble sort
#   Best O(n^2); Average O(n^2); Worst O(n^2)

def bubbleSort(List):
    for i in range(len(List)):
        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                List[j], List[j - 1] = List[j - 1], List[j]
    return List

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print('Sorted List:',bubbleSort(List))