# wap to print good morning good evening good afternoon according to the time using time module


import time
timestamp=time.strftime('%H:%M:%S')
print("THE CURRENT TIME IS : ", timestamp)      # here time module returns the time instring so we have to typecaste it into time
h=int(time.strftime('%H'))
m=int(time.strftime('%M'))
s=int(time.strftime('%S'))

if(h>=5 and h<=12):
    print("GOOD MORNING SIR")
elif(h>12 and h<=18):
    print("GOOD AFTERNOON SIR")
else:
    print("GOOD EVENING SIR")




