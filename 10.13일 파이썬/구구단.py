#-*-coding:utf-8-*-

print "구구단 몇단을 계산할까요(1~9)?"
x=1
while(x<>0):
    x=int(raw_input())
    if x==0: break
    if not(1 <= x <=9):
        print "잘못 입력하셨습니다","1부터 9사이 숫자를 입력해주세요"
        continue
    else:
        print"구구단" +str(x) +"단을 계산합니다."
        for i in range(1,10):
            print str(x) +" X" +str(i) + "=" +str(x*i)
        print "구구단 몇단을 계산할까요(1~9)?"
print"구구단 게임을 종료합니다"
                                                
