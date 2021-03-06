from ssp import *
from pulp import *
from lp_maxprob import *
from lp_mincost import *
from lp_sspude import *
from lp_hsearch import *


ssp = SSP()


ssp.S.append("S0")
ssp.S.append("S1")
ssp.S.append("S2")
ssp.S.append("Sg")
ssp.S.append("D1")
ssp.S.append("D2")
ssp.S.append("D3")

ssp._s0 = "S0"

ssp.G.append("Sg")

ssp.A.append("a0")
ssp.A.append("a1")

#probability

ssp.P("S0", "a1", "S2", 1)
ssp.P("S0", "a0", "S1", 0.5)
ssp.P("S0", "a0", "D1", 0.5)

ssp.P("S1","a0","S0", 0.5)
ssp.P("S1","a0","Sg", 0.5)

ssp.P("S2","a1","S0", 0.4)
ssp.P("S2","a1","Sg", 0.4)
ssp.P("S2","a1","D2", 0.2)

ssp.P("D2","a1","D3", 1)

ssp.P("D3","a1","D2", 1)

#cost

ssp.C("S0","a0", 1)
ssp.C("S0","a1", 1)

ssp.C("S1","a0", 3)

ssp.C("S2","a1", 2)

#app

ssp.App("S0","a0")
ssp.App("S0","a1")

ssp.App("S1","a0")

ssp.App("S2","a1")

ssp.App("D2","a1")

ssp.App("D3","a1")

ssp.toDot("text.dot")


problem = lp_maxprob(ssp)



#problem = lp_mincost(ssp, 0.33)

#problem = lp_sspude(ssp, 1000)



problem = lp_hsearch(lp_sspude,ssp)


