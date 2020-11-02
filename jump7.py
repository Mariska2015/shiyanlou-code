a=0
while a<100:
    a=a+1
    if a%7==0:
        continue
    elif a%10==7:
        continue
    elif a>70 and a<80:
        continue
    else:
        print(a)
