m = "Y"
while(m == "Y"):
    n = 0
    n=int(input("마방진 크기를 입력해주세요 :"))
    if(n <= 2):
        print("2보다 커야합니다")
    elif(n % 2 == 1):
        print( n,"크기의 마방진은 아래와 같습니다")
     
        x = n * n
        b = n
        d = n//2
        g = n - 1
        a = n - 1
        ma=[[0]*n for i in range(n)]
        if(ma[a][d] == 0):
            ma[a][d] += 1
            c = 2
            while(c <= x):
                if(a < g):
                    a += 1
                elif(a == g):
                    a = 0
                if(d < g):
                    d += 1
                elif(d == g):
                    d = 0
                if(ma[a][d] == 0):
                    ma[a][d] += c
                elif(ma[a][d] != 0):
                    a = a - 2
                    d = d - 1
                    if(ma[a][d] == 0):
                        ma[a][d] += c        
                
                c += 1
    
        i = 0
        while(i < b):
            print(ma[i])
            i += 1
    elif(n % 2 == 0):
        print( n, "크기의 마방진은 아래와 같습니다")
        ma=[[0]*n for i in range(n)]
        b = n
        x = n * n
        j = 0
        k = 0
        a = n -1
        c = 1
        i = 1
        while(c <= x):
            while(j < n):
                k = 0
                while(k < n):
                    if(ma[j][k] == 0):
                        if(k == j):
                            ma[j][k] = c
                    
                        elif(k != j):
                            e = 0
                            h = a
                            while(e <= a):
                                if(j == e and k == h):
                                    ma[j][k] = c
                                e += 1
                                h -= 1
                    c += 1
                    k += 1
                j += 1
            c += 1
            i += 1
        c = 1
        while(c <= x):
            p = a
            while(0 <= p):
                o = a
                while(0 <= o):
                    if(ma[p][o] == 0):
                        ma[p][o] = c
                    o -= 1
                    c += 1
                p -= 1
            c += 1
    


    
        i = 0
        while(i < b):
            print(ma[i])
            i += 1
    print("또 하시겟습니까 Y,N")
    m = input()
    m = m.upper()
    if(m == "Y"):
        print ("다시시작합니다")
    elif(m == "N"):
        print ("종료합니다")
        break










        
