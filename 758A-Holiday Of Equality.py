num = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse=True)
Result = 0
for i in range(num):
    if arr[0] == arr[i]:
        continue    
    elif arr[0] > arr[i]:
        Result = Result + (arr[0] - arr[i])

print(Result)        


    