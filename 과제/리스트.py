g = 0
while(g != 1):
    n=int(input("리스트 크기를 입력해주세 :"))
    if(n == 0):
        print("종료합니다")
        break
    ma=[0]*n
    import random


    i = 0
    m = 1
    e = 1
    while(i < n):
    
        ma[i] += e
        i += 1
        e += 1
    random.shuffle(ma)
    print(ma)
    s = 0
    c = 0
    while(s < n):
        b = 0
        while(b < n-1):
            if(ma[b] > ma[b+1]):
                ma[b], ma[b+1] = ma[b+1], ma[b]
                c += 1
            b += 1  
        s += 1
    print("정렬된숫자",ma, "바뀐 횟수" ,c)
