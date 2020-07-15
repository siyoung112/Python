

an_salary=int(input("연봉을 입력하세요 : ")) #연금은 x 라 한다

#an_salary=format(an_salary,',')
fund=an_salary * 0.05

heal_fund=an_salary * 0.06
hire_fund=an_salary * 0.01
retire_fund=an_salary * 0.08

mo_salary=(an_salary-fund-heal_fund-hire_fund-retire_fund)/12
"{:0,.2f}".format(mo_salary)
print('당신의 월 수령액은 {:,} 원 입니다.'.format(round(mo_salary,2)))
print('국민 연금 : {:,} 원, 건강 보험 : {:,} 원, 고용 보험 : {:,} 원, 퇴직 연금 : {:,} 원'.format(an_salary,heal_fund,hire_fund,retire_fund))

