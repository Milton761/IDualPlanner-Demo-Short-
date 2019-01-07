from ssp import *
from pulp import *
from genProblem import *
from lpSolver import *
from vi import *
import jsonpickle
from river import *


x = 4
y = 100
f = 2.3


# for i in range(5,1000,10):
# 	print("Generation problem size " + str(x) + " - " + str(i)
#   ssp = genRiv(x,i)
# 	ssp.writeJSON("problems/"+str(x)+"_"+str(i)+".json")


ssp = genRiv2(x,y)
#ssp = genRivDE(x,y)
#ssp = genNav(x,y)
#ssp.printFullSSP()
#print(ssp)
#ssp.writeFile("FIRSTSSP.ssp")

#F = search_lambda(ssp,top=3,verbose=1)
# F = search_lambda2(ssp,verbose = 1)
# print(F['value'])
# R = lp_ssp_e(ssp,F['value'])

R = lp_ssp_e(ssp,f)
#printValues(R['problem'])


plotRiv(ssp, x, y, "expRiv", R['policy'])

#[problem, policy] = lp_sspude(ssp1,1000)
#R = lp_ssp_e_l(ssp,f,0,60)
#R = lp_sspude_e(ssp,f)

#[V,policy] = vi_e(ssp,-f,0)


#[problem, policy] = lp_sspude(ssp,0.8, 1000)
# [problem, policy] = lp_sspude_D(ssp,0.95)
# plotRiv(ssp, x, y, "expRivD_DE", policy)

# print("Value Function")
# print(V)
#print(problem)
#print("Policy")
#print(policy)

#print(problem)

#printValues(problem)
#print(R['policy'])


#print(R['time'])
#plotNav(ssp, x, y, "expNav", policy)
#plotRiv(ssp, x, y, "expRiv", R['policy'])


# for v in problem.variables():
# 	print(v.name, "=", v.varValue)

#-----------------------------


#ssp = genDr()
#ssp.printFullSSP()

#[problem, policy] = lp_ssp_e(ssp,0.5)
#printPolicy(policy)

#print(ssp.toJSON())

