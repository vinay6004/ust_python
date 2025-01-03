'''amount =120
bonus=10
amount +=bonus  #amount = amount +bonus
print(amount)

#identity operators
year = input("enter year")
if (type(year) is int):
    age =2025-year
else:
    print(type(year))
    age=0
print(age)
year = input("enter year")


year = int(year)
if(type(year)is not int):
    print("convert year into integer")
else:
    age =2025-year
    print(age)'''
#=========tuple=========

'''cars = ("BMW","VOLVO","TOYOTA","MARUTHI","BMW")
print(type(cars))
print(len(cars))
for x in range(len(cars)):
    print(cars[x])

for car in cars:
    print(car)
print("1st 2 cars",cars[:2])
print("all cars except last one:",cars[:-1])
print("all cars skiping 2 cars:",cars[2:])
print("only the last car:",cars[-1:])
print("cars b/w 2nd and 3rd position:",cars[1:3])
print("count of bmw for cars",cars.count("BMW"))
print("existence of model renaut"in cars)
print("theb index of btoyota cars is",cars.index("TOYOTA"))
trucks=("VOLVO",)
vehicles = cars +trucks
print(vehicles)'''
#=============list========
score=[100,23,56,87,81,21]
print(type(score))
score.append(0)
score.insert(2,0)
score_ipl=[64,22,10]
score.extend([64,22,10])
score[5]=123
print(score)
user_details=[("vinay",21),("neelu",18),("rakesh",6),("asish",7)]
for user in user_details:
    print(user[0],"roll number",user[1])
score.pop()
print(score)
score.remove(87)
print(score)
score.sort()
print("scorted in ascending",score)
score.reverse()
print("scorted in descending",score)












