from ssp import *
from pulp import *
from lp_maxprob import *
from lp_mincost import *
from lp_sspude import *


def lp_hsearch(lp_formulation, ssp, penalty = None):

	counter = 0

	x = None
	print("========================================")
	print("==== LP - Heuristic Search =============")
	print("========================================")

	policy = {}

	#[ line 1 ] -------------
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

	#INIT#

	with open("0.dot", 'w') as out:

			var = "digraph {"
			out.write(var+'\n')

			var = "node [ fontname = Helvetica fontsize = 10 shape=circle style=filled ]"
			out.write('\t' + var + '\n')
			var = "edge [ fontname = Helvetica fontsize = 10 ]"
			out.write('\t' + var + '\n')

			

			for s in ssp._S:
				label 	  = "label = \""+s+"\""
				color     = ", color = \"#E0E0E0\""
				fillcolor = ", fillcolor = \"#E0E0E0\""
				var = s + "["+label+color+fillcolor+"]"
				out.write('\t' + var + '\n')
				for a in ssp.App(s):

					for s1 in ssp._S:
						if ssp.P(s,a,s1) > 0:
							label = "label = <"+ str(ssp.P(s,a,s1)) +"<SUB>"+ a +"</SUB>>"
							color = ",color = \"#E0E0E0\""
							var = s + " -> " + s1 + "["+label+color+"]"
							out.write('\t' + var + '\n')


			
			#animation phase

			for s in S:
				label 	  = "label = \""+s+"\""
				color     = ", color = \"#99FFFF\""
				fillcolor = ", fillcolor = \"#99FFFF	\""
				var = s + "["+label+color+fillcolor+"]"
				out.write('\t' + var + '\n')

			var = "}"
			out.write(var+'\n')
	#INIT#

	#[ line 6 ] -------------
	while not (len(Fr) == 0):

		counter += 1 
		print("ITERATION : " , counter)

		#print
		ssp1 = SSP()
		
		ssp1._s0 = ssp._s0

	#[ line 7 ] -------------
		N = set()
		for s in Fr:
			for a in ssp.App(s):
				for s1 in ssp.S:
					if ssp.P(s,a,s1) > 0 and not s1 in S:
						N = N.union([s1])
		print("\tN :: ",N)
	#[ line 8 ] -------------
		S = S.union(N)
		print("\tS :: ",S)

		for s in S:
			ssp1.S.append(s)

	#[ line 9 ] -------------
		F = (F.difference(Fr)).union(N.difference(G))
		print("\tF :: ",F)

	#[ line 10 ] -------------
		G1 = F.union(G.intersection(S))
		print("\tG1 :: ",G1)

		for g in G1:
			ssp1.G.append(g)

	#[ line 11 ] -------------
		tempS = S.difference(F)

		for s in tempS:
			for a in ssp.App(s):
				A.add(a)
				ssp1.A.append(a)
				ssp1.App(s,a)

		App = ssp._App
		print("App : ",ssp1._App)

		print(ssp1)
		ssp1._P = ssp._P
		ssp1._C = ssp._C
		ssp1._App = ssp._App


	#[ line 12 ] -------------
		#solve LP:

		with open(str(counter)+".dot", 'w') as out:

			var = "digraph {"
			out.write(var+'\n')

			var = "node [ fontname = Helvetica fontsize = 10 shape=circle style=filled]"
			out.write('\t' + var + '\n')
			var = "edge [ fontname = Helvetica fontsize = 10 ]"
			out.write('\t' + var + '\n')

			

			for s in ssp._S:
				label 	  = "label = \""+s+"\""
				color     = ", color = \"#E0E0E0\""
				fillcolor = ", fillcolor = \"#E0E0E0\""
				var = s + "["+label+color+fillcolor+"]"
				out.write('\t' + var + '\n')
				for a in ssp.App(s):

					if s in ssp1._S:

						for s1 in ssp._S:
							if ssp.P(s,a,s1) > 0:
								if s1 in ssp1._S:
									label = "label = <"+ str(ssp.P(s,a,s1)) +"<SUB>"+ a +"</SUB>>"
									color = ",color = \"#99FF99	\""
									var = s + " -> " + s1 + "["+label+color+"]"
									out.write('\t' + var + '\n')
								else:
									label = "label = <"+ str(ssp.P(s,a,s1)) +"<SUB>"+ a +"</SUB>>"
									color = ",color = \"#E0E0E0\""
									var = s + " -> " + s1 + "["+label+color+"]"
									out.write('\t' + var + '\n')

					else:
						for s1 in ssp._S:
							if ssp.P(s,a,s1) > 0:
								label = "label = <"+ str(ssp.P(s,a,s1)) +"<SUB>"+ a +"</SUB>>"
								color = ",color = \"#E0E0E0\""
								var = s + " -> " + s1 + "["+label+color+"]"
								out.write('\t' + var + '\n')



			
			#animation phase

			for s in ssp1._S:
				label 	  = "label = \""+s+"\""
				color     = ", color = \"#99FFFF\""
				fillcolor = ", fillcolor = \"#99FFFF\""
				var = s + "["+label+color+fillcolor+"]"
				out.write('\t' + var + '\n')

			var = "}"
			out.write(var+'\n')



		x = lp_formulation(ssp1)

		

		#for var in x.variables():
		#	print(var.name, "\t:", var.varValue)

	#[ line 13 ] -------------
		print("[LINE 13]")
		Fr = set()
		for s in F:
			var_name = "IN_"+s
			print(var_name)
			for var in x.variables():
				if var.name == var_name:
					if var.varValue > 0:
						Fr = Fr.union([s])
						
		print("\tFr :: ",Fr)

		



	return x
#	for var in x:
#		for s in S:
#			for a in ssp1.App(s):
#				var_name = s + a
#				policy(s,a) = 



