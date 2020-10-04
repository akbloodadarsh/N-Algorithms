if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr2 = list(arr)

    k = max(arr2)

    while k in arr2:
        arr2.remove(max(arr2))

    print(max(arr2))

