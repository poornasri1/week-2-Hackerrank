n = int(input())

arr = list(map(int, input().split()))

s=set(arr)

x=list(s)

x.sort(reverse=True)

print(x[1])
