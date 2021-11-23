import math
sqr_num=input('enter a number: ')
sqr_num=int(sqr_num)
sqr=math.sqrt(sqr_num)
#print(sqr)
if sqr*sqr != sqr_num:
    print('your number is not a square number')
else:
    print('the square number of your number is:',sqr)
