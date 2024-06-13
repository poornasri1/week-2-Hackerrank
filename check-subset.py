values=[]
for i in range(int(input())):
    set_A_no=int(input())
    set_A=map(int, (input().split())) 
    
    set_B_no=int(input())
    set_B=map(int, (input().split())) 
    
    values.append(set(set_A).issubset(set(set_B)))
    
for value in values:
    print(value)
