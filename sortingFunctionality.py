def mergeSort(ratings, left, right):
    if left < right:
        middle = left + (right-left) // 2
        mergeSort(ratings, left, middle)
        mergeSort(ratings, middle+1, right)
        merge(ratings, left, middle, right)

def merge(ratings, left, middle, right):
    n1 = middle-left+1
    n2 = right-middle
    X = [0] * n1
    Y = [0] * n2
    for i in range(n1):
        X[i] = ratings[left+i]
    for i in range(n2):
        Y[i] =  ratings[middle+1+i]
    i=0
    j=0
    k=left
    while i < n1 and j < n2:
        if X[i] <= Y[j]:
            ratings[k] = X[i]
            i+=1
            k+=1
        else:
            ratings[k] = Y[j]
            j+=1
            k+=1
    while i < n1:
        ratings[k] = X[i]
        i+=1
        k+=1
    while j < n2:
        ratings[k] = Y[j]
        j+=1
        k+=1