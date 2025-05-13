num = int(input())
my_list = list(map(int, input().split()))

last_seen = {}
for i in range(num):
    last_seen[my_list[i]] = i  

unique_sorted_by_last = sorted(last_seen, key=lambda x: last_seen[x])

print(len(unique_sorted_by_last))
for i in unique_sorted_by_last:
    print(i, end=' ')
