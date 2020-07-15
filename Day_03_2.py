a=10.0
print(type(a))

p1,p2,p3='010','8888','9999'

pp1=int(p1)
pp1=pp1+10
print(pp1)

num1=10
num2=20
#num1,num2=10,20
#num3=num1+num2

name='시영'
age=32

english,math,korean=100,80,50
tot=english+math+korean
avg=tot/len('tot')

print('{}+{}={}'.format(num1,num2,num1+num2))
print('이름 : {}\n나이 : {}'.format(name,age))
print('합계 : {}\n평균 : {:.2f}'.format(tot,avg))


