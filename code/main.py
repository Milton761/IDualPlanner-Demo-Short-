from ssp import *
from pulp import *

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

ssp.P("S2","a1","S0", 0.25)
ssp.P("S2","a1","Sg", 0.25)
ssp.P("S2","a1","D2", 0.5)

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
		problem += Vars["IN_"+s] == r_side


#C3
for s in ssp.S:
	r_side = None
	for a in ssp.App(s):
		r_side += Vars[s+a]
	if r_side != None:
		problem += Vars["OUT_"+s] == r_side


#C7
for s in ssp.S:
	if not (s==ssp.s0 or s in ssp.G):
		problem += Vars["OUT_"+s] - Vars["IN_"+s] == 0

#C8
problem += Vars["OUT_"+ssp.s0] - Vars["IN_"+ssp.s0] == 1


GLPK().solve(problem)
p_max = value(problem.objective)

print("=============================")
print("p_max = ", p_max)
print("=============================")


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
	r_side = None
	for a in ssp.App(s):
		r_side += Vars[s+a]
	if r_side != None:
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



print("=============================")
print("====LP - SSPUDE =============")
print("=============================")

d = penalty = 1000

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


print("========================================")
print("==== LP - Heuristic Search =============")
print("========================================")




S = set()
F = set()
Fr = set()
N = set()
G = set()
G1 = set()
A = set()
App = None

S.add(ssp.s0)
F.add(ssp.s0)
Fr.add(ssp.s0)

for g in ssp.G:
	G.add(g)



while not (len(Fr) == 0):
	for s in Fr:
		for a in ssp.App(s):
			for s1 in ssp.S:
				if ssp.P(s,a,s1) > 0 and not s1 in S:
					N.union(s1)
	S = S.union(N)
	F = (F.difference(Fr)).union(N.difference(G))
	G1 = F.union(G.intersection(S))
	
	tempS = S.difference(F)

	for s in tempS:
		for a in ssp.App(s):
			A.add(a)

	App = ssp._App


	#solve LP:





	