import math
#only works for proper fractions and doesn't work 

numerator = int(input("Numerator: "))
denominator = int(input("Denominator: "))
print("The decimal equivalent of this fraction is ", +numerator/denominator)
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
commondivisor = gcd(numerator, denominator)
(reducednum, reducedden) = (numerator / commondivisor, denominator / commondivisor)
nonrepeat = 0
while reducedden%2 == 0 or reducedden%5 == 0 or reducedden%10 == 0:
    while reducedden%2 == 0 and reducedden%5 == 0:
        if reducedden%10 == 0:
            reducedden = reducedden/10
            nonrepeat += 1
    if reducedden%5 == 0:
        reducedden = reducedden/5
        nonrepeat += 1
    if reducedden%2 == 0:
        reducedden = reducedden/2
        nonrepeat += 1
remainder = 0
numerator = 1
repeating = 0
refernum = numerator
lister = []
if numerator%reducedden != 0:
    numerator = numerator*10
    remainder = numerator%reducedden
    lister.append(remainder)
    repeating +=1
    while refernum not in lister:
        numerator = numerator*10
        remainder = numerator%reducedden
        lister.append(remainder)
        repeating +=1
print("Non-repeating digits: ", +nonrepeat)
if remainder in lister:
    print("Repeating digits: ",+repeating)


