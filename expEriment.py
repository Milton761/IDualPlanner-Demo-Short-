from ssp import *
from pulp import *
from genProblem import *
from lpSolver import *
import os


x = 10
y = 4

ssp = genNav(x,y)


stop = 2
step = 0.02
lamd = 0.01

code = 0

name_folder = "nav-"+str(x)+"-"+str(y)
os.system("mkdir " + name_folder)


while lamd<=stop:

    

    [problem, policy,result] = lp_ssp_e(ssp,lamd)
    if result==1:
        plotNav(ssp, x, y, name_folder+"/expNav_"+str(code), policy)
    else:
        break

    lamd = lamd+step
    code = code+1

"GIF-nav-"+str(x)+"-"+str(y)
os.system("convert -delay 30 '"+ name_folder+ "/expNav_%d.png[0-50]' output.gif")