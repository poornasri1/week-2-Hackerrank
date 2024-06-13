N=input()
a=set(map(int,input().split()))
for i in range(int(input())):
    command=input().split()
    try:
        if "pop" in command:
            a.pop()
        elif "remove" in command:
            a.remove(int(command[1]))
        elif "discard" in command:
            a.discard(int(command[1]))
    except KeyError:
        pass
print(sum(a))
