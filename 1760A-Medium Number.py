num = int(input())

Result = []

for i in range(num):
    arr = list(map(int,input().split()))
    arr.sort()
    Result.append(arr[1])

for i in Result:
    print(i)
    