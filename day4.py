score = []
m = int(input("enter the size: "))
for  i in range(m) :
    n = int(input("enter the number: "))
    score = score + [n]
print(score)
reg = int(input("enter last digit of your registration number : "))
print(reg)

low = []
medium = []
high = []
critical = []

valid = 0
ignore = 0
removed = 0

for n in score :
    if n<0 :
        ignore = ignore +1
    else :
        valid = valid+1
        if n>=0 and n <= 30:
            low = low +[n]
        elif n >=31 and n<=60 :
            medium = medium + [n]
        elif n >=61 and n<=100 :
            high = high + [n]
        else :
            critical = critical + [n]
print("Low Risk : ",low)
print("Medium Risk : ",medium)
print("High Risk : ",high)
print("Critical Risk : ", critical)

