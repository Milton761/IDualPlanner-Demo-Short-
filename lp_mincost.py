from ssp import *
from pulp import *

def lp_mincost(ssp, p_max):
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



	#===============================#
	#------ MIN COST    ------------#
	#===============================#


	problem = SSP = LpProblem("SSP-MinCost", LpMinimize)

	#Set objective
	r_side = None
	for s in ssp.S:
		for a in ssp.App(s):
			var_name = s + a
			r_side += Vars[var_name]*ssp.C(s,a)
	problem += r_side

	#Add Constraints

	#C1 - Done

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
		if not s in ssp.G:
			r_side = None
			for a in ssp.App(s):
				r_side += Vars[s+a]
			if r_side != None:

				#print("[C3]: OUT_"+s, "=", str(r_side))
				problem += Vars["OUT_"+s] == r_side

	#C4
	for s in ssp.S:
		if not (s==ssp.s0 or s in ssp.G):
			problem += Vars["OUT_"+s] - Vars["IN_"+s] <= 0

	#C5

	problem += Vars["OUT_"+ssp.s0] - Vars["IN_"+ssp.s0] <= 1

	#C6
	r_side = None
	for s in ssp.G:

		r_side += Vars["IN_"+s]	
	problem += r_side == p_max


	print("=============================")
	print("====MIN-COST=================")
	print("=============================")

	GLPK().solve(problem)

	for v in problem.variables():
		print(v.name, "=", v.varValue)

	    
	print("Objective =", value(problem.objective) )

	return problem