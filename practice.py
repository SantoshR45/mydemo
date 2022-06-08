"""
 x=[2,45,67]
x[1] =100
y=[45,2,60]
print(x[1]*y[0])

a=(2, 5,6)

print(a[1]*2)

s="santosh"
print(s[0:5])
print(len(s))

e=2+5
print(e.imag)
print(e.real)

p=-987
print(abs(p))

import math
print(math.pow(2,4))
print(math.sqrt(16))

print(max(x)*min(y)) """

p = [1, 2, 3, 4, 5]
r = [1, 2, "santosh", "is", "smart", 678, "rat"]
r.append(678)
r.extend(p)
r.insert(4, "waste")
r[4] = "great"
print(r)

var = [3, 8, 6, 1, 12, 100]
var.sort()
print(sum(var) * len(var))

l = ("mst", "pst", "est", "cst")
k = "gmt"
o = (k, l)
print(o)

um = ("santo",) * 5
print(um)

n = tuple("santosh")
print(n)
a, b, c, d = l
print(a, b)

x = ([1, 2, 3], [8, 9, 10])
print(x[1][2])

stg = "santosh"
for i in stg:
    print(i, end="")

p = "welcome to my practice session"
print(p.upper())
print(p.isupper())
print(p.replace("practice" , "hardwork"))
print(p.find("p"))
print(p.rpartition("my"))

stag1 ="hey"
stag2 = "there"
stag3 = "all"
stage4 = "{} {}, {}!".format(stag1,stag2,stag3)

print(stage4)
