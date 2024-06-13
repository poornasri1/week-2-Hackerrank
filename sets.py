def average(array):
    sumheight=sum(set(arr))
    numberofheight=len(set(arr))
    avg=float(sumheight/numberofheight)
    return avg
 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
