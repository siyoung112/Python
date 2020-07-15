name=input("이름을 입력하세요 : ")
height=int(input("키를 입력하세요 : "))
weight=int(input("몸무게를 입력하세요 : "))

standweight=(height-100) * 0.9 
value= weight/standweight * 100 

#print(round(value,2)) 셋째자리에서
print('{} 님의 비만도는 {} % 입니다.'.format(name,round(value,2)))