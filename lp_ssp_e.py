from ssp import *
from pulp import *
from math import *


def lp_ssp_e(ssp, factor = 1):

	sign = lambda x: (1, -1)[x < 0]
	#declare variables
	Vars = {}

	s_a = {}

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
			s_a[var_name] = [s,a]



	problem = SSP = LpProblem("LP - SSP", LpMinimize)

	#Set objective
	r_side = 0
	for s in ssp.S:
		for a in ssp.App(s):
			var_name = s + a
			r_side += Vars[var_name]*exp(factor*ssp.C(s,a))
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
			problem += Vars["OUT_"+s] - Vars["IN_"+s] == 0
	
	#C5

	problem += Vars["OUT_"+ssp.s0] - Vars["IN_"+ssp.s0] == 1

	#C6
	r_side = None
	gl = -sign(factor)
	for s in ssp.G:

		r_side += Vars["IN_"+s]	
	problem += r_side == 1


	print("=============================")
	print("====LP SSP  =================")
	print("=============================")

	policy = {}

	GUROBI().solve(problem)

	for v in problem.variables():
		print(v.name, "=", v.varValue)
		if v.name in s_a:
			if v.varValue > 0:
				policy[s_a[v.name][0]] = s_a[v.name][1]

	    
	print("Objective =", value(problem.objective))

	print("=============policy==============")
	for key, v in policy.items():
		print(key, " ", v)


	return [problem, policy]



def lp_ssp2(ssp, factor = 1):

	sign = lambda x: (1, -1)[x < 0]
	#declare variables
	Vars = {}

	s_a = {}

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
			Vars[var_name] = 	LpVariable(var_name,0)
			s_a[var_name] = [s,a]



	problem = SSP = LpProblem("LP - SSP modified 2", LpMinimize)

	#Set objective
	r_side = 0
	for s in ssp.S:
		for a in ssp.App(s):
			var_name = s + a
			#r_side += Vars[var_name]*exp(factor*ssp.C(s,a))*ssp.P(s,a,ssp._G[0])
			r_side += Vars[var_name]*exp(factor*ssp.C(s,a))
	problem += r_side

	#Add Constraints

	#C1 - Done

	#C2 - modified 
	for s in ssp.S:
		r_side = None
		for s1 in ssp.S:
			for a in ssp.App(s1):
				if ssp.P(s1,a,s):
					#add in var
					r_side +=  Vars[s1+a]*ssp.P(s1, a, s)*exp(factor*ssp.C(s1,a))

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
			problem += Vars["OUT_"+s] - Vars["IN_"+s] == 0

	#C5

	problem += Vars["OUT_"+ssp.s0] - Vars["IN_"+ssp.s0] == 1

	#C6
	r_side = None
	gl = -sign(factor)
	for s in ssp.G:

		r_side += Vars["IN_"+s]	
	problem += r_side == exp(factor)


	print("=============================")
	print("====LP SSP  =================")
	print("=============================")

	policy = {}

	GUROBI().solve(problem)

	for v in problem.variables():
		print(v.name, "=", v.varValue)
		if v.name in s_a:
			if v.varValue > 0:
				policy[s_a[v.name][0]] = s_a[v.name][1]

	    
	print("Objective =", value(problem.objective))

	print("=============policy==============")
	for key, v in policy.items():
		print(key, " ", v)


	return [problem, policy]


	