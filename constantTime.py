#An algorithm is said to have a constant time when it is not dependent on the input data (n).
# No matter the size of the input data, the running time will always be the same

#Ex1: ODD/EVEN program
def oddeven(a):
    if a % 2==0:
        return True #Odd
    else:
        return False #Even

#Ex2:function get_first which returns the first element of a list:
def get_first(data):
    return data[0]

if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(get_first(data))

#No matter how many elements in the list, it is only going to print the first element