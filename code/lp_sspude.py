from ssp import *
from pulp import *


def lp_sspude(ssp, penalty=1000):
	#declare variables

	Vars = {}

	for s in ssp.S:
		
		var_name = None
		#in vars

		var_name = "IN_"+s
		Vars[var_name] = LpVariable(var_name,0)

		#out vars
		var_name = "OUT_"+s
		Vars[var_name] = LpVariable(var_name,0)

		#occupation measure vars
		for a in ssp.App(s):
			var_name = s + a
			Vars[var_name] = LpVariable(var_name,0)



	print("=============================")
	print("====LP - SSPUDE =============")
	print("=============================")

	d = penalty

	problem = SSP = LpProblem("SSPUDE - LP", LpMinimize)

	#LP formulation with Dead Ends#

	#dead ends vars
	for s in ssp.S:
		var_name = "DE_"+s
		Vars[var_name] = LpVariable(var_name,0)


	#set objective

	r_side = None
	for s in ssp.S:
		for a in ssp.App(s):
			var_name = s + a
			r_side += Vars[var_name]*ssp.C(s,a)

	for s in ssp.S:
		r_side += Vars["DE_"+s]*d

	problem += r_side 


	#Add constraints

	#C1 - Done in declaration

	#C2
	for s in ssp.S:
		r_side = None
		for s1 in ssp.S:
			for a in ssp.App(s1):
				if ssp.P(s1,a,s) > 0:
					#add in var
					r_side += Vars[s1+a]*ssp.P(s1, a, s) 

		if r_side != None:
			problem += Vars["IN_"+s] == r_side

	#C3
	for s in ssp.S:
		if not (s==ssp.s0 or s in ssp.G):
			problem += Vars["OUT_"+s] - Vars["IN_"+s] == 0

	#C4
	problem += Vars["OUT_"+ssp.s0] - Vars["IN_"+ssp.s0] == 1

	#C7 - Done in declaration

	#C8

	for s in ssp.S:
		r_side = None
		if not (s in ssp.G):
			for a in ssp.App(s):
				r_side += Vars[s+a]
			r_side += Vars["DE_"+s]
			problem += Vars["OUT_"+s] == r_side


	#C9

	r_side = None
	for s in ssp.G:
		r_side += Vars["IN_"+s]

	for s in ssp.S:
		r_side += Vars["DE_"+s]

	problem += r_side == 1


	GLPK().solve(problem)

	for v in problem.variables():
		print(v.name, "=", v.varValue)

	    
	print("Objective =", value(problem.objective) )


	return problem