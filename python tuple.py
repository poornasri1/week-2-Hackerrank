if __name__ == '__main__':
    n=int(input())
    t=tuple(int(x) for x in input().split())
    t=tuple(t)
    print(hash(t))
