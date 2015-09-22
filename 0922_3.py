print "당신이 태어난 년도를 입력하세요"
a= int(raw_input())
b = (2015 - a)+1 
if 26 > b >=20:
    print "대학생"
elif 20 > b >=17:
    print "고등학생"
elif  17 > b >=14:
    print "중학생"
elif 14 > b >=8:
    print "초등학생"
else:
    print "학생이 아닙니다"


