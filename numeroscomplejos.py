import math
from math import sqrt
def addcmplx(c1, c2):
    return (c1[0] + c2[0]), (c1[1] + c2[1])
def subtract (c1, c2):
    return (c1[0] - c2[0]), (c1[1] -c2[1])
def multcmplx(c1, c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    img = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return real, img
def divcmplx(c1, c2):
    real = ((c1[0] * c2[0]) + (c1[1] * (c2[1]))) / ((c2[0] ** 2) + (c2[1] ** 2))
    img = ((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    return real, img
def modulecmplx(c1):
    answer = sqrt((c1[0] ** 2) + (c1[1] ** 2))
    return answer
def conjucmplx(c1):
    return c1[0], -c1[1]
def polar2trig(a, b):
    p = sqrt((a ** 2) + (b ** 2))
    t = math.tan(b/a)
    return p, t
def cmplx2phase(c1):
    t = c1[1] % (2 * math.pi)
    return c1[0], t

x = 1 / sqrt(2)
y = 7 / sqrt(2)
Lista = []
Lista.append(x)
Lista.append(y)
print(multcmplx(Lista, Lista))
print("-----------------------------------------------------")
print(divcmplx([0,1],[1,2]))
print(divcmplx([2,1],[5,0]))
print('2+i5/5')
print(divcmplx([0,1],[5,0]))
print( 'i/5')
print(divcmplx([1,-2],[5,0]))
print('1−2i/5')
print('Error')
print( '2-i')
print(divcmplx([2,-1],[5,0]))
print('1−i/5')









