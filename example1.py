from ssp import *
from lpSolver import *

p1 = 0.01

ssp = SSP()


ssp.S.append("s1")
ssp.S.append("sg")


ssp._s0 = "s1"

ssp.G.append("sg")

ssp.A.append("a1")


#probability

ssp.P("s1", "a1", "s1", p1)
ssp.P("s1", "a1", "sg", 1-p1)

#cost

ssp.C("s1","a1", 1)


#app

ssp.App("s1","a1")

ssp.toDot("text.dot")

F = search_lambda2(ssp,verbose = 1)
print(F['value'])
print(F['problem'])


