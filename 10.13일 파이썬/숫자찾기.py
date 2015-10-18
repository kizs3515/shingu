#-*-coding:utf-8-*-
import random
guess_number=random.randint(1,100)
print "숫자를 맞춰보세요(1~100)"
users_input = int(raw_input())
while(users_input <> guess_number):
    if users_input>guess_number:
        print "숫자가 너무 큽니다"
    else:
        print "숫자가 너무 작습니다"
    users_input = int(raw_input())
else: print"정답입니다.","입력한숫자는",users_input,"입니다"
