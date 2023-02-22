#write a program tha calculates 16% 
#ranging between 100k-150k


#19%tax invome is above 150k-300k
#30% tax income is above 300k
#5% tax income is less 100k

#print gross income, net income


gross_income = input("what is your gross income")
tax_group_1 = (gross_income * 0.05)
tax_group_2 = (gross_income * 0.16)
tax_group_3 = (gross_income * 0.19)
tax_group_4 = (gross_income * 0.30)

if gross_income <=100000:
    print("gross_income:", gross_income)
    print("net_income:",gross_income - tax_group_1)
elif (gross_income >=100000) & (gross_income <= 150000):
    print("gross_income:", gross_income)
    print("net_income:",gross_income - tax_group_2)
elif (gross_income >=150001) & (gross_income<=300000):
     print("gross_income:", gross_income)
     print("net_income:",gross_income - tax_group_3)
else:
     print("gross_income:", gross_income)
     print("net_income:",gross_income - tax_group_4)
     







