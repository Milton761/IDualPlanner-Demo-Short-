from ssp import *
from pulp import *
from lp_maxprob import *
from lp_mincost import *
from lp_sspude import *
from lp_sspude_e import *
from lp_hsearch import *
from river import *
from lp_ssp_e import *
from lp_ssp import *

ssp = SSP()


ssp.S.append("d0")
ssp.S.append("d1")
ssp.S.append("d2")
ssp.S.append("d3")
ssp.S.append("g")
#ssp.S.append("D1")

ssp._s0 = "d0"

ssp.G.append("g")

ssp.A.append("a1")
ssp.A.append("a2")
ssp.A.append("a3")
ssp.A.append("a4")
ssp.A.append("ag")

#probability

ssp.P("d0", "a2", "d2", 1)
ssp.P("d0", "a1", "d1", 1)

ssp.P("d2", "a4", "d3", 1)

ssp.P("d1","a3","d1", 0.2)
ssp.P("d1","a3","d2", 0.4)
ssp.P("d1","a3","d3", 0.4)

ssp.P("d3","ag","g", 1)

#cost

ssp.C("d0","a1", 0)
ssp.C("d0","a2", 0)

ssp.C("d1","a3", 1)

ssp.C("d2","a4", 1)
ssp.C("d3","ag", 0)

#app

ssp.App("d0","a1")
ssp.App("d0","a2")

ssp.App("d1","a3")


ssp.App("d2","a4")

ssp.App("d3","ag")

ssp.toDot("text.dot")

problem = lp_ssp(ssp)



print(">>>>>>>>>>>>>>>>>> 1")

#-----------------------------------------



ssp = SSP()


ssp.S.append("d0")
ssp.S.append("d1")
ssp.S.append("d3")
ssp.S.append("g")
#ssp.S.append("D1")

ssp._s0 = "d0"

ssp.G.append("g")

ssp.A.append("a1")
ssp.A.append("a2")
#ssp.A.append("a3")
ssp.A.append("a4")
ssp.A.append("ag")

#probability

ssp.P("d0", "a2", "d1", 1)
ssp.P("d0", "a1", "d3", 1)

ssp.P("d1", "a4", "d3", 1)

ssp.P("d3","a3","d3", 0.6)
ssp.P("d3","a3","d1", 0.4)

ssp.P("d3","ag","g", 1)

#cost

ssp.C("d0","a1", 1)
ssp.C("d0","a2", 0)

ssp.C("d1","a4", 1)

ssp.C("d3","a3", 1)
ssp.C("d3","ag", 0)

#app

ssp.App("d0","a1")
ssp.App("d0","a2")

ssp.App("d1","a4")


#ssp.App("d2","a4")

ssp.App("d3","a3")
ssp.App("d3","ag")

ssp.toDot("text.dot")

problem = lp_ssp(ssp)

print(">>>>>>>>>>>>>>>>>>>>>>>>>> 2")



#------------------SSPUDE-----------------------

print(":::::::::::::::::::::H_POM _ MAXPROB TEST ::::::::::::::::::::::")

ssp = SSP()


ssp.S.append("d0")
ssp.S.append("d1")
ssp.S.append("d2")
ssp.S.append("d3")
ssp.S.append("g")

#ssp.S.append("D1")

ssp._s0 = "d0"

ssp.G.append("g")

ssp.A.append("a1")
ssp.A.append("a2")
ssp.A.append("a3")
ssp.A.append("a4")


#probability

ssp.P("d0", "a2", "d2", 1)
ssp.P("d0", "a1", "d1", 1)


ssp.P("d1","a3","d1", 0.2)
ssp.P("d1","a3","d2", 0.4)
ssp.P("d1","a3","d3", 0.4)

ssp.P("d3","ag","g", 1)

#cost

ssp.C("d0","a1", 1)
ssp.C("d0","a2", 1)

ssp.C("d1","a3", 1)

ssp.C("d3","ag", 0)

#app

ssp.App("d0","a1")
ssp.App("d0","a2")

ssp.App("d1","a3")


ssp.App("d3","ag")

ssp.toDot("pro1.dot")

problem = lp_ssp(ssp)
problem = lp_sspude(ssp,5)
problem = lp_maxprob(ssp)


#----------------------------------------



ssp = SSP()


ssp.S.append("d0")
ssp.S.append("d1")
ssp.S.append("d3")
ssp.S.append("g")
#ssp.S.append("D1")

ssp._s0 = "d0"

ssp.G.append("g")

ssp.A.append("a1")
ssp.A.append("a2")
#ssp.A.append("a3")
ssp.A.append("ag")

#probability

ssp.P("d0", "a2", "d1", 1)
ssp.P("d0", "a1", "d3", 1)


ssp.P("d3","a3","d3", 0.6)
ssp.P("d3","a3","d1", 0.4)

ssp.P("d3","ag","g", 1)

#cost

ssp.C("d0","a1", 0)
ssp.C("d0","a2", 0)


ssp.C("d3","a3", 0)
ssp.C("d3","ag", 1)

#app

ssp.App("d0","a1")
ssp.App("d0","a2")


#ssp.App("d2","a4")

ssp.App("d3","a3")
ssp.App("d3","ag")

ssp.toDot("pro2.dot")

#problem = lp_sspude(ssp,10)
problem = lp_maxprob(ssp)



