from ssp import *
from pulp import *
from lp_maxprob import *
from lp_mincost import *
from lp_sspude import *
from lp_sspude_e import *
from lp_hsearch import *
from lp_ssp import *


ssp = SSP()


ssp.S.append("A")
ssp.S.append("B")
ssp.S.append("C")
ssp.S.append("D")

ssp._s0 = "A"

ssp.G.append("D")

ssp.A.append("a0")
ssp.A.append("a1")

#probability

ssp.P("A", "a0", "B", 1)

ssp.P("A", "a1", "C", 0.7)
ssp.P("A", "a1", "D", 0.3)

ssp.P("B", "a1", "D", 1)

ssp.P("C", "a0", "D", 1)


#cost

ssp.C("A","a0", 3)
ssp.C("A","a1", 1)

ssp.C("B","a1", 1)
ssp.C("C","a0", 1)

#app

ssp.App("A","a0")
ssp.App("A","a1")

ssp.App("B","a1")

ssp.App("C","a0")

problem = lp_ssp(ssp)



#problem = lp_maxprob(ssp)

#problem = lp_mincost(ssp, 0.33)

#problem = lp_sspude(ssp, 1000)



#problem = lp_hsearch(lp_sspude,ssp)



