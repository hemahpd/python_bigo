#Polynomial running is represented as O(nc), when c > 1.
# As you already saw, two inner loops almost translate to O(n2)
# since it has to go through the array twice in most cases.
# Are three nested loops cubic? If each one visit all elements, then yes!
# Usually, we want to stay away from polynomial running times (quadratic, cubic, nc, etc.)
# since they take longer to compute as the input grows fast.

#EX : Multi variable equation solver
#In the below case, it is 3 variable solver.So it takes cubic time


def findXYZ(n):

    for x in range(n):
        for y in range(n):
            for z in range(n):
                if (3*x + 9*y +8*z ==79):
                    print("x:",x,"y:",y,"z:",z)



findXYZ(10)
