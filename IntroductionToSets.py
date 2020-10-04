def average(array):
    # your code goes here
    l = {}
    l = set(l)
    n = len(array)
    for i in range(0,n):
        l.add(array[i])

    
    return (sum(l)/len(l))
