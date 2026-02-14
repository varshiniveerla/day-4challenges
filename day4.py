score = []
m = int(input("enter the size: "))
for  i in range(m) :
    n = int(input("enter the number: "))
    score = score + [n]
print(score)
D = int(input("enter last digit of your registration number : "))
print(D)

low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

valid = 0
ignore = 0
removed = 0

for n in score :
    if n<0 :
        ignore = ignore +1
    else :
        valid = valid+1
        if n>=0 and n <= 30:
            low_risk = low_risk +[n]
        elif n >=31 and n<=60 :
            medium_risk = medium_risk + [n]
        elif n >=61 and n<=100 :
            high_risk = high_risk + [n]
        else :
            critical = critical + [n]
print("Low Risk : ",low_risk)
print("Medium Risk : ",medium_risk)
print("High Risk : ",high_risk)
print("Critical Risk : ", critical_risk)
if D%2 == 0 :
    print("My registration number ends with EVEN -> removing low risks")
    removed = removed + 1
    low_risk =[]

print("After Personalized Filtering: ")
print("Low Risk : ",low_risk)
print("Medium Risk : ",medium_risk)
print("High Risk : ",high_risk)
print("Critical Risk : ", critical_risk)

print("Total Valid Entries : ",valid)
print("Ignored Entries : ",ignore)
print("Removed Due Personalization : ",removed)




