from ssp import *
import os


def prNav(i,x):

	maxP = 0.8
	minP = 0.2	
	step = (maxP-minP)/(x-1)

	return minP + i*step


def st(i,j):
	return str(i)+"_"+str(j)


def genDr():


	A=[0,1,2,3,4]

	S=[]

	for i in range(11):
		S.append(str(i))

	S.append("PASS")
	S.append("INIT")

	ssp = SSP()


	for state in S:
		ssp.S.append(state)

	ssp._s0 = "INIT"
	ssp.G.append("PASS")

	for a in A:
		ssp.A.append(str(a))

	detAct = "detAct"
	ssp.A.append(detAct)
	for s in range(11):

		state = "INIT"
		state1 = str(s)
		ssp.P(state,detAct,state1,1)
		ssp.C(state,detAct,0)
		ssp.App(state, detAct)

	
	for s in range(11):
		for a in A:
			action = str(a)
			for state1 in S:

				state = str(s)
				p=0
				if state1=="PASS":
					p = (0.08*float(s))+(0.04*float(a))
					ssp.P(state, action, state1, p) 
					ssp.C(state, action, 2+a)
					ssp.App(state, action)
				else:
					if state1 == str(min(s+a,10)):

						p = 1 - (0.08*float(s))+(0.04*float(a))
						ssp.P(state, action, state1, p) 
						ssp.C(state, action, 2+a)
						ssp.App(state, action)
				
				

	return ssp
		
def genNav2(x,y):
	A = ['U','D','R','L','abs']

	ssp = SSP()


	for j in range(y):
		for i in range(x):
			state = st(i,j)
			ssp.S.append(state)

	# ssp.S.append("DE")

	ssp._s0 = st(0,0)
	ssp.G.append(st(0,y-1))

	#add actions:
	for a in A:
		ssp.A.append(a)



	# goal abs state
	state = st(0,y-1)
		
	# action absorbing action
	
	ssp.P(state, A[4], state, 1) 
	ssp.C(state, A[4], 0)
	ssp.App(state, A[4])

	#[TOP] - define probability transiction function
	j = y-1
	for i in range(1,x):
		state = st(i,j)
		
		#action UP 	  NORTH
		if j < y-1:
			state1 = st(i,j+1)
			ssp.P(state, A[0], state1, 1) 
			ssp.C(state, A[0], 1)
			ssp.App(state, A[0])

		#action DOWN  SOUTH
		if j > 0:
			state1 = st(i,j-1)
			ssp.P(state, A[1], state1, 1)
			ssp.C(state, A[1], 1)
			ssp.App(state, A[1])

		#action RIGHT EAST
		if i < x-1:
			state1 = st(i+1,j)
			ssp.P(state, A[2], state1, 1)
			ssp.C(state, A[2], 1)
			ssp.App(state, A[2])

		#action LEFT  WEST
		if i > 0:
			state1 = st(i-1,j)
			ssp.P(state, A[3], state1, 1)
			ssp.C(state, A[3], 1)
			ssp.App(state, A[3])


	#[BOT] - define probability transiction function
	j = 0
	for i in range(x):
		state = st(i,j)

		#action UP 	  NORTH
		if j < y-1:
			state1 = st(i,j+1)
			ssp.P(state, A[0], state1, 1) 
			ssp.C(state, A[0], 1)
			ssp.App(state, A[0])

		#action DOWN  SOUTH
		if j > 0:
			state1 = st(i,j-1)
			ssp.P(state, A[1], state1, 1)
			ssp.C(state, A[1], 1)
			ssp.App(state, A[1])

		#action RIGHT EAST
		if i < x-1:
			state1 = st(i+1,j)
			ssp.P(state, A[2], state1, 1)
			ssp.C(state, A[2], 1)
			ssp.App(state, A[2])

		#action LEFT  WEST
		if i > 0:
			state1 = st(i-1,j)
			ssp.P(state, A[3], state1, 1)
			ssp.C(state, A[3], 1)
			ssp.App(state, A[3])

	#[MID] - define probability transiction function
	for j in range(1,y-1):
		for i in range(x):

			state = st(i,j)
			stateDE = st(0,0)

			#action UP 	  NORTH
			if j < y-1:
				state1 = st(i,j+1)
				ssp.P(state, A[0], state1, prNav(i,x)) 
				ssp.P(state, A[0], stateDE, 1-prNav(i,x)) 

				ssp.C(state, A[0], 1)
				ssp.App(state, A[0])

			#action DOWN  SOUTH
			if j > 0:
				state1 = st(i,j-1)
				ssp.P(state, A[1], state1, prNav(i,x)) 
				ssp.P(state, A[1], stateDE,1- prNav(i,x)) 
				ssp.C(state, A[1], 1)
				ssp.App(state, A[1])

			#action RIGHT EAST
			if i < x-1:
				state1 = st(i+1,j)
				ssp.P(state, A[2], state1, prNav(i,x)) 
				ssp.P(state, A[2], stateDE, 1-prNav(i,x)) 
				ssp.C(state, A[2], 1)
				ssp.App(state, A[2])

			#action LEFT  WEST
			if i > 0:
				state1 = st(i-1,j)
				ssp.P(state, A[3], state1, prNav(i,x)) 
				ssp.P(state, A[3], stateDE, 1-prNav(i,x)) 
				ssp.C(state, A[3], 1)
				ssp.App(state, A[3])




	return ssp


def genNav(x,y):

	A = ['U','D','R','L','abs']

	ssp = SSP()


	for j in range(y):
		for i in range(x):
			state = st(i,j)
			ssp.S.append(state)

	ssp.S.append("DE")

	ssp._s0 = st(0,0)
	ssp.G.append(st(0,y-1))

	#add actions:
	for a in A:
		ssp.A.append(a)



	#goal abs state
	#state = st(0,y-1)
		
	#action absorbing action
	
	#ssp.P(state, A[4], state, 1) 
	#ssp.C(state, A[4], 1)
	#ssp.App(state, A[4])

	#[TOP] - define probability transiction function
	j = y-1
	for i in range(1,x):
		state = st(i,j)
		
		#action UP 	  NORTH
		if j < y-1:
			state1 = st(i,j+1)
			ssp.P(state, A[0], state1, 1) 
			ssp.C(state, A[0], 1)
			ssp.App(state, A[0])

		#action DOWN  SOUTH
		if j > 0:
			state1 = st(i,j-1)
			ssp.P(state, A[1], state1, 1)
			ssp.C(state, A[1], 1)
			ssp.App(state, A[1])

		#action RIGHT EAST
		if i < x-1:
			state1 = st(i+1,j)
			ssp.P(state, A[2], state1, 1)
			ssp.C(state, A[2], 1)
			ssp.App(state, A[2])

		#action LEFT  WEST
		if i > 0:
			state1 = st(i-1,j)
			ssp.P(state, A[3], state1, 1)
			ssp.C(state, A[3], 1)
			ssp.App(state, A[3])


	#[BOT] - define probability transiction function
	j = 0
	for i in range(x):
		state = st(i,j)

		#action UP 	  NORTH
		if j < y-1:
			state1 = st(i,j+1)
			ssp.P(state, A[0], state1, 1) 
			ssp.C(state, A[0], 1)
			ssp.App(state, A[0])

		#action DOWN  SOUTH
		if j > 0:
			state1 = st(i,j-1)
			ssp.P(state, A[1], state1, 1)
			ssp.C(state, A[1], 1)
			ssp.App(state, A[1])

		#action RIGHT EAST
		if i < x-1:
			state1 = st(i+1,j)
			ssp.P(state, A[2], state1, 1)
			ssp.C(state, A[2], 1)
			ssp.App(state, A[2])

		#action LEFT  WEST
		if i > 0:
			state1 = st(i-1,j)
			ssp.P(state, A[3], state1, 1)
			ssp.C(state, A[3], 1)
			ssp.App(state, A[3])

	#[MID] - define probability transiction function
	for j in range(1,y-1):
		for i in range(x):

			state = st(i,j)
			stateDE = "DE"

			#action UP 	  NORTH
			if j < y-1:
				state1 = st(i,j+1)
				ssp.P(state, A[0], state1, prNav(i,x)) 
				ssp.P(state, A[0], stateDE, 1-prNav(i,x)) 

				ssp.C(state, A[0], 1)
				ssp.App(state, A[0])

			#action DOWN  SOUTH
			if j > 0:
				state1 = st(i,j-1)
				ssp.P(state, A[1], state1, prNav(i,x)) 
				ssp.P(state, A[1], stateDE,1- prNav(i,x)) 
				ssp.C(state, A[1], 1)
				ssp.App(state, A[1])

			#action RIGHT EAST
			if i < x-1:
				state1 = st(i+1,j)
				ssp.P(state, A[2], state1, prNav(i,x)) 
				ssp.P(state, A[2], stateDE, 1-prNav(i,x)) 
				ssp.C(state, A[2], 1)
				ssp.App(state, A[2])

			#action LEFT  WEST
			if i > 0:
				state1 = st(i-1,j)
				ssp.P(state, A[3], state1, prNav(i,x)) 
				ssp.P(state, A[3], stateDE, 1-prNav(i,x)) 
				ssp.C(state, A[3], 1)
				ssp.App(state, A[3])




	return ssp






def plotNav(ssp, x, y, filename, policy = {}):


	#print(policy)

	symbol = {} 
	symbol['L'] = "&#x2190;"
	symbol['U'] = "&#x2191;"
	symbol['R'] = "&#x2192;"
	symbol['D'] = "&#x2193;"
	symbol['water'] = ""
	symbol['goal'] = "&#x2690;"
	symbol['abs'] = "&#x21ba;"


	with open(filename+".dot", 'w') as out:

		var = "digraph {"
		out.write(var+'\n')

		var = "\tnode [shape=plaintext]"
		out.write(var+'\n')

		var = "\ta[label=<<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
		out.write(var+'\n')

		for j in range(y):

			var = "\t<TR>"
			out.write(var+'\n')

			for i in range(x):

				s_a = str(i)+"_"+str(y-j-1)
				
				if s_a in policy:
					

					color = " BGCOLOR=\"darkslategray1\""

					if i==0 and j==y-1:
						color = " BGCOLOR=\"deepskyblue\""

					sign = symbol[policy[s_a]]
					var = "\t\t<TD width=\"35\" height=\"35\" fixedsize=\"true\""+color+">"+sign+"</TD>"
				else:

					color = " BGCOLOR=\"gray\""
					sign = symbol['water']

					if j == 0 and i == 0:
						color = " BGCOLOR=\"chartreuse2\""
						sign = symbol['goal']

					var = "\t\t<TD width=\"35\" height=\"35\" fixedsize=\"true\""+color+">"+sign+"</TD>"

				out.write(var+'\n')

			var = "\t</TR>"
			out.write(var+'\n')

		var = "\t</TABLE>>];"
		out.write(var+'\n')
		var = "}"
		out.write(var+'\n')
		out.close()

		os.system("convert "+ filename+".dot " + filename+".png")



def genRiv2(x,y):
	
	A = ['U','D','R','L']

	ssp = SSP()

	for j in range(y):
		for i in range(x):
			state = str(i)+"_"+str(j)
			ssp.S.append(state)


		

	#ssp.S.append("DE")

	ssp._s0 = str(0)+"_"+str(0)
	ssp.G.append(str(x-1)+"_"+str(0))

	#add actions
	for a in A:
		ssp.A.append(a)

	ssp.A.append('abs')

	#[1] - define probability transiction function
	for j in range(1,y):
		for i in range(x):
	
			state = str(i)+"_"+str(j)
			if i==0 or i==x-1 or j==y-1:

				#action UP 	  NORTH
				if j < y-1:
					state1 = str(i)+"_"+str(j+1)
					ssp.P(state, A[0], state1, 0.9) 
					ssp.P(state, A[0], state, 0.1) 
					ssp.C(state, A[0], 1)
					ssp.App(state, A[0])

				#action DOWN  SOUTH
				if j > 0:
					state1 = str(i)+"_"+str(j-1)
					ssp.P(state, A[1], state1, 0.9)
					ssp.P(state, A[1], state, 0.1)
					ssp.C(state, A[1], 1)
					ssp.App(state, A[1])

				#action RIGHT EAST
				if i < x-1:
					state1 = str(i+1)+"_"+str(j)
					ssp.P(state, A[2], state1, 0.9)
					ssp.P(state, A[2], state, 0.1)
					ssp.C(state, A[2], 1)
					ssp.App(state, A[2])

				#action LEFT  WEST
				if i > 0:
					state1 = str(i-1)+"_"+str(j)
					ssp.P(state, A[3], state1, 0.9)
					ssp.P(state, A[3], state, 0.1)
					ssp.C(state, A[3], 1)
					ssp.App(state, A[3])


	state = str(0)+"_"+str(0)


	#action UP 	  NORTH

	state1 = str(0)+"_"+str(1)
	ssp.P(state, A[0], state1, 0.9) 
	ssp.P(state, A[0], state, 0.1) 
	ssp.C(state, A[0], 1)
	ssp.App(state, A[0])

	#action RIGHT EAST
	#state1 = "DE"
	#ssp.P(state, A[2], state1, 1)
	#ssp.C(state, A[2], 1)
	#ssp.App(state, A[2])



	rangeP = []
	maxP = 0.8
	minP = 0.2
	step = (maxP-minP)/(x-3)

	for i in range(x-2):
		rangeP.append(0.2)
	# print("HEREEEEEEEEEEEEEEE=============")
	# print(rangeP)


	for j in range(2,y-1):
		for i in range(1,x-1):

			state = str(i)+"_"+str(j)

			#action UP 	  NORTH
			if j < y-1:
				state1 = str(i)+"_"+str(j+1)
				state2 = str(i)+"_"+str(j-1)
				ssp.P(state, A[0], state1, 1-rangeP[i-1]) 
				ssp.P(state, A[0], state2, rangeP[i-1]) 

				ssp.C(state, A[0], 1)
				ssp.App(state, A[0])

			#action DOWN  SOUTH
			if j > 0:
				state1 = str(i)+"_"+str(j-1)
				ssp.P(state, A[1], state1, 1)
				
				ssp.C(state, A[1], 1)
				ssp.App(state, A[1])

			#action RIGHT EAST
			if i < x-1:
				state1 = str(i+1)+"_"+str(j)
				state2 = str(i)+"_"+str(j-1)
				ssp.P(state, A[2], state1, 1-rangeP[i-1])
				ssp.P(state, A[2], state2, rangeP[i-1]) 

				ssp.C(state, A[2], 1)
				ssp.App(state, A[2])

			#action LEFT  WEST
			if i > 0:
				state1 = str(i-1)+"_"+str(j)
				state2 = str(i)+"_"+str(j-1)
				ssp.P(state, A[3], state1, 1-rangeP[i-1])
				ssp.P(state, A[3], state2, rangeP[i-1]) 

				ssp.C(state, A[3], 1)
				ssp.App(state, A[3])

	for i in range(1,x-1):
		j = 1
		state = str(i)+"_"+str(j)

		#action UP 	  NORTH
		if j < y-1:
			state1 = str(i)+"_"+str(j+1)
			state2 = str(i)+"_"+str(j-1)
			ssp.P(state, A[0], state1, 1-rangeP[i-1]) 
			ssp.P(state, A[0], state2, rangeP[i-1]) 

			ssp.C(state, A[0], 1)
			ssp.App(state, A[0])

		#action DOWN  SOUTH
		if j > 0:
			#state1 = "DE"
			state1 = str(i)+"_"+str(j-1)

			ssp.P(state, A[1], state1, 1)
			
			ssp.C(state, A[1], 1)
			ssp.App(state, A[1])

		#action RIGHT EAST
		if i < x-1:
			state1 = str(i+1)+"_"+str(j)
			state2 = str(i)+"_"+str(j-1)
			ssp.P(state, A[2], state1, 1-rangeP[i-1])
			ssp.P(state, A[2], state2, rangeP[i-1]) 

			ssp.C(state, A[2], 1)
			ssp.App(state, A[2])

		#action LEFT  WEST
		if i > 0:
			state1 = str(i-1)+"_"+str(j)
			state2 = str(i)+"_"+str(j-1)
			ssp.P(state, A[3], state1, 1-rangeP[i-1])
			ssp.P(state, A[3], state2, rangeP[i-1]) 

			ssp.C(state, A[3], 1)
			ssp.App(state, A[3])

	stateGoal = str(x-1)+"_"+str(0)

	ssp.P(stateGoal,'abs',stateGoal,1)
	ssp.C(stateGoal,'abs',0)
	ssp.App(stateGoal,'abs')


	for i in range(1,x-1):
		state = str(i)+"_"+str(0)
		init = str(i-1)+"_"+str(0)
		#ssp.P(state, A[0], init, 1)
		#ssp.P(state, A[1], init, 1)
		#ssp.P(state, A[2], init, 1)
		ssp.P(state, A[3], init, 1)

		#ssp.C(state, A[0], 1)
		#ssp.C(state, A[1], 1)
		#ssp.C(state, A[2], 1)
		ssp.C(state, A[3], 1)

		#ssp.App(state, A[0])
		#ssp.App(state, A[1])
		#ssp.App(state, A[2])
		ssp.App(state, A[3])


	return ssp




def genRiv(x,y):


	A = ['U','D','R','L']

	ssp = SSP()

	for j in range(y):
		for i in range(x):
			state = str(i)+"_"+str(j)
			ssp.S.append(state)


		

	#ssp.S.append("DE")

	ssp._s0 = str(0)+"_"+str(0)
	ssp.G.append(str(x-1)+"_"+str(0))

	#add actions
	for a in A:
		ssp.A.append(a)

	ssp.A.append('abs')

	#[1] - define probability transiction function
	for j in range(1,y):
		for i in range(x):

			state = str(i)+"_"+str(j)


			#action UP 	  NORTH
			if j < y-1:
				state1 = str(i)+"_"+str(j+1)
				ssp.P(state, A[0], state1, 1) 
				ssp.C(state, A[0], 1)
				ssp.App(state, A[0])

			#action DOWN  SOUTH
			if j > 0:
				state1 = str(i)+"_"+str(j-1)
				ssp.P(state, A[1], state1, 1)
				ssp.C(state, A[1], 1)
				ssp.App(state, A[1])

			#action RIGHT EAST
			if i < x-1:
				state1 = str(i+1)+"_"+str(j)
				ssp.P(state, A[2], state1, 1)
				ssp.C(state, A[2], 1)
				ssp.App(state, A[2])

			#action LEFT  WEST
			if i > 0:
				state1 = str(i-1)+"_"+str(j)
				ssp.P(state, A[3], state1, 1)
				ssp.C(state, A[3], 1)
				ssp.App(state, A[3])


	state = str(0)+"_"+str(0)


	#action UP 	  NORTH

	state1 = str(0)+"_"+str(1)
	ssp.P(state, A[0], state1, 1) 
	ssp.C(state, A[0], 1)
	ssp.App(state, A[0])

	#action RIGHT EAST
	#state1 = "DE"
	#ssp.P(state, A[2], state1, 1)
	#ssp.C(state, A[2], 1)
	#ssp.App(state, A[2])



	rangeP = []
	maxP = 0.8
	minP = 0.2
	step = (maxP-minP)/(x-3)

	for i in range(x-2):
		rangeP.append(minP+i*step)
	# print("HEREEEEEEEEEEEEEEE=============")
	# print(rangeP)


	for j in range(2,y-1):
		for i in range(1,x-1):

			state = str(i)+"_"+str(j)

			#action UP 	  NORTH
			if j < y-1:
				state1 = str(i)+"_"+str(j+1)
				state2 = str(i)+"_"+str(j-1)
				ssp.P(state, A[0], state1, 1-rangeP[i-1]) 
				ssp.P(state, A[0], state2, rangeP[i-1]) 

				ssp.C(state, A[0], 1)
				ssp.App(state, A[0])

			#action DOWN  SOUTH
			if j > 0:
				state1 = str(i)+"_"+str(j-1)
				ssp.P(state, A[1], state1, 1)
				
				ssp.C(state, A[1], 1)
				ssp.App(state, A[1])

			#action RIGHT EAST
			if i < x-1:
				state1 = str(i+1)+"_"+str(j)
				state2 = str(i)+"_"+str(j-1)
				ssp.P(state, A[2], state1, 1-rangeP[i-1])
				ssp.P(state, A[2], state2, rangeP[i-1]) 

				ssp.C(state, A[2], 1)
				ssp.App(state, A[2])

			#action LEFT  WEST
			if i > 0:
				state1 = str(i-1)+"_"+str(j)
				state2 = str(i)+"_"+str(j-1)
				ssp.P(state, A[3], state1, 1-rangeP[i-1])
				ssp.P(state, A[3], state2, rangeP[i-1]) 

				ssp.C(state, A[3], 1)
				ssp.App(state, A[3])

	for i in range(1,x-1):
		j = 1
		state = str(i)+"_"+str(j)

		#action UP 	  NORTH
		if j < y-1:
			state1 = str(i)+"_"+str(j+1)
			state2 = str(i)+"_"+str(j-1)
			ssp.P(state, A[0], state1, 1-rangeP[i-1]) 
			ssp.P(state, A[0], state2, rangeP[i-1]) 

			ssp.C(state, A[0], 1)
			ssp.App(state, A[0])

		#action DOWN  SOUTH
		if j > 0:
			#state1 = "DE"
			state1 = str(i)+"_"+str(j-1)

			ssp.P(state, A[1], state1, 1)
			
			ssp.C(state, A[1], 1)
			ssp.App(state, A[1])

		#action RIGHT EAST
		if i < x-1:
			state1 = str(i+1)+"_"+str(j)
			state2 = str(i)+"_"+str(j-1)
			ssp.P(state, A[2], state1, 1-rangeP[i-1])
			ssp.P(state, A[2], state2, rangeP[i-1]) 

			ssp.C(state, A[2], 1)
			ssp.App(state, A[2])

		#action LEFT  WEST
		if i > 0:
			state1 = str(i-1)+"_"+str(j)
			state2 = str(i)+"_"+str(j-1)
			ssp.P(state, A[3], state1, 1-rangeP[i-1])
			ssp.P(state, A[3], state2, rangeP[i-1]) 

			ssp.C(state, A[3], 1)
			ssp.App(state, A[3])

	stateGoal = str(x-1)+"_"+str(0)

	ssp.P(stateGoal,'abs',stateGoal,1)
	ssp.C(stateGoal,'abs',0)
	ssp.App(stateGoal,'abs')


	for i in range(1,x-1):
		state = str(i)+"_"+str(0)
		init = str(i-1)+"_"+str(0)
		#ssp.P(state, A[0], init, 1)
		#ssp.P(state, A[1], init, 1)
		#ssp.P(state, A[2], init, 1)
		ssp.P(state, A[3], init, 1)

		#ssp.C(state, A[0], 1)
		#ssp.C(state, A[1], 1)
		#ssp.C(state, A[2], 1)
		ssp.C(state, A[3], 1)

		#ssp.App(state, A[0])
		#ssp.App(state, A[1])
		#ssp.App(state, A[2])
		ssp.App(state, A[3])


	return ssp



def plotRiv(ssp, x, y, filename, policy = {}):


	#print(policy)

	symbol = {} 
	symbol['L'] = "&#8592;"
	symbol['U'] = "&#8593;"
	symbol['R'] = "&#8594;"
	symbol['D'] = "&#8595;"
	symbol['water'] = "&#x2248;"
	symbol['goal'] = "&#71;"
	symbol['None'] = "&#10540;"
	symbol['abs'] = "&#x21ba;"


	with open(filename+".dot", 'w') as out:

		var = "digraph {"
		out.write(var+'\n')

		var = "\tnode [shape=plaintext]"
		out.write(var+'\n')

		var = "\ta[label=<<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
		out.write(var+'\n')

		for j in range(y):

			var = "\t<TR>"
			out.write(var+'\n')

			for i in range(x):

				s_a = str(i)+"_"+str(y-j-1)
				
				if s_a in policy:
					
					color = " BGCOLOR=\"darkgoldenrod1\""
					sign = symbol[policy[s_a]]
					var = "\t\t<TD width=\"35\" height=\"35\" fixedsize=\"true\""+color+">"+sign+"</TD>"
				else:



					color = " BGCOLOR=\"dodgerblue\""
					sign = symbol['water']

					if j == y-1 and i == x-1:
						color = " BGCOLOR=\"chartreuse3\""
						sign = symbol['goal']

					var = "\t\t<TD width=\"35\" height=\"35\" fixedsize=\"true\""+color+">"+sign+"</TD>"

				out.write(var+'\n')

			var = "\t</TR>"
			out.write(var+'\n')

		var = "\t</TABLE>>];"
		out.write(var+'\n')
		var = "}"
		out.write(var+'\n')
		out.close()

		os.system("convert "+ filename+".dot " + filename+".png")