from ssp import *
from pulp import *

def lp_maxprob(ssp):

#declare variables

	Vars = {}

	for s in ssp.S:
		
		var_name = None
		#in vars

		var_name = "IN_"+s
		Vars[var_name] = LpVariable(var_name,0,1)

		#out vars
		var_name = "OUT_"+s
		Vars[var_name] = LpVariable(var_name,0)

		#occupation measure vars
		for a in ssp.App(s):
			var_name = s + a
			#print("VARNAME : ",var_name)
			Vars[var_name] = LpVariable(var_name,0)


	#===============================#
	#------ MAX PROBLEM ------------#
	#===============================#
	problem = SSP = LpProblem("SSP-MaxProb", LpMaximize)

	#set objective
	r_side = None
	for s in ssp.G:
		r_side += Vars["IN_"+s]

	problem += r_side


	#C2
	for s in ssp.S:
		r_side = None
		for s1 in ssp.S:
			for a in ssp.App(s1):
				if ssp.P(s1,a,s) > 0:
					#add in var
					r_side += Vars[s1+a]*ssp.P(s1, a, s) 

		if r_side != None:
			#print("[C2]: IN_"+s, "=", str(r_side))
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


	#C7
	for s in ssp.S:
		if not (s==ssp.s0 or s in ssp.G):
			#print("[C7]: OUT_"+s, " - ","OUT_"+s, " = ",str(r_side))
			problem += Vars["OUT_"+s] - Vars["IN_"+s] == 0

	#C8
	problem += Vars["OUT_"+ssp.s0] - Vars["IN_"+ssp.s0] == 1
	#print("[C8]: OUT_"+ssp.s0, " - ","IN_"+ssp.s0, " = 1")




	GLPK().solve(problem)
	p_max = value(problem.objective)

	print("=============================")
	
	for v in problem.variables():
		print(v.name,"\t",v.varValue)

	print("p_max = ", p_max)
	print("=============================")

	return problem