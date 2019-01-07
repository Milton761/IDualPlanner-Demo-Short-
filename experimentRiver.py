from ssp import *
from pulp import *
from genProblem import *
from lpSolver import *
import os


x = 4
y = 8

ssp = genRiv(x,y)


stop = 1
step = 0.01
lamd = 0.01 

code = 0

name_folder = "riv-"+str(x)+"-"+str(y)
os.system("mkdir " + name_folder)


while lamd<=stop:

    

    [problem, policy,result] = lp_ssp_e(ssp,lamd)
    if result==1:
        plotRiv(ssp, x, y, name_folder+"/expRiv_"+str(code), policy)
    else:
        break

    lamd = lamd+step
    code = code+1

"GIF-riv-"+str(x)+"-"+str(y)
os.system("convert -delay 30 '"+ name_folder+ "/expRiv_%d.png[0-50]' output.gif")