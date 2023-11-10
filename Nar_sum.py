x = list(range(500))

for y in x:
    if y%2==1 and y%3==2 and y%6==5 and y%5==4 and y%7==0:
        print(y)
