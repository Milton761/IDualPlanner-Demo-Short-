from ssp import *
from vi import *
from lpSolver import *
from genProblem import *
from util import *
from tireworld import *

from lpSolverG import *




def exp07():
	# TireWorld Domain
	print('#{0:10} {1:10} {2:10} {3:10} {4:10} {5:10} {5:10} {6:10}'.format('instante','states','time1','f1','time2','f2','time3','f3'))

	for tam in range(2,22,2):
		R = genTire(tam)
		ssp = R['ssp']
		s_states = len(ssp._S)
		instance = str(tam)
		
		R1 = search_lambda2(ssp)

		factor = 0.1
		error = 0.001
		R2 = riskAdverse(ssp, error + 0.000001, error, factor, initPolicy(ssp))

		R3 = riskAdverse2(ssp, error + 0.000001, error, factor, initPolicy(ssp))

		print('{0:3} {1:5} {2:10.3f} {3:10.3f} {4:10.3f} {5:10.3f} {6:10.3f} {7:10.3f}'.format(instance,s_states,R1['time'],R1['factor'],R2['time'],R2['factor'],R3['time'],R3['factor']))


# Navigation Domain
def exp06():
	
	print('#{0:10} {1:10} {2:10} {3:10} {4:10} {5:10} {6:10} {7:10}'.format('instante','states','time1','f1','time2','f2','time2','f2'))

	x = 4
	for j in range(6,22,2):
		y = j

		ssp = genNav2(x,y)
		s_states = len(ssp._S)
		instance = str(x) +" X "+str(y)
		# print(s_states)
		
		# print(R1['time'],R1['factor'])
		R1 = search_lambda2(ssp)
		factor = -0.1
		error = 0.001
		R2 = riskAdverse(ssp, error + 0.000001, error, factor, initPolicy(ssp))
		R3 = riskAdverse2(ssp, error + 0.000001, error, factor, initPolicy(ssp))
		print('{0:3} {1:5} {2:10.3f} {3:10.3f} {4:10.3f} {5:10.3f} {6:10.3f} {7:10.3f}'.format(instance,s_states,R1['time'],R1['factor'],R2['time'],R2['factor'],R3['time'],R3['factor']))


# River Domain
def exp05():
	
	print('#{0:10} {1:10} {2:10} {3:10} {4:10} {5:10} {6:10} {7:10}'.format('instante','states','time1','f1','time2','f2','time2','f2'))

	x = 5
	for j in range(6,22,2):
		y = j
		ssp = genRiv2(x,y)

		s_states = len(ssp._S)
		instance = str(x) +" X "+str(j)
		
		# print(s_states)
		R1 = search_lambda2(ssp)
		factor = -0.1
		error = 0.001
		R2 = riskAdverse(ssp, error + 0.000001, error, factor, initPolicy(ssp))
		R3 = riskAdverse2(ssp, error + 0.000001, error, factor, initPolicy(ssp))
		print('{0:3} {1:5} {2:10.3f} {3:10.3f} {4:10.3f} {5:10.3f} {6:10.3f} {7:10.3f}'.format(instance,s_states,R1['time'],R1['factor'],R2['time'],R2['factor'],R3['time'],R3['factor']))


def exp03():
	

	print('#{0:10} {1:10} {2:10} {3:10} {4:10}'.format('instante','states','variables','lambda','time'))

	for i in range(10,100,10):
		
		x = i
		ssp = genRiv(x,i)
		R = search_lambda(ssp)

		s_states = len(ssp._S)
		instance = str(x) +" X "+str(i)
		n_variables = R['n_variables']
		if R['factor']==0:
			break
		print('{0:10} {1:10} {2:10} {3:10.4f} {4:10.4f}' .format(instance,s_states, n_variables,R['factor'],R['time']))

def exp02():
	
	x = 5

	print('#{0:10} {1:10} {2:10} {3:10} {4:10}'.format('instante','states','variables','lambda','time'))

	for i in range(10,1000,10):
		
		ssp = genRiv(x,i)
		R = search_lambda(ssp)

		s_states = len(ssp._S)
		instance = str(x) +" X "+str(i)
		n_variables = R['n_variables']
		if R['factor']==0:
			break
		print('{0:10} {1:10} {2:10} {3:10.4f} {4:10.4f}' .format(instance,s_states, n_variables,R['factor'],R['time']))

def exp04():
	
	y = 5

	print('#{0:10} {1:10} {2:10} {3:10} {4:10}'.format('instante','states','variables','lambda','time'))

	for i in range(10,1000,10):
		
		ssp = genRiv(i,y)
		R = search_lambda(ssp)

		s_states = len(ssp._S)
		instance = str(i) +" X "+str(y)
		n_variables = R['n_variables']
		if R['factor']==0:
			break
		print('{0:10} {1:10} {2:10} {3:10.4f} {4:10.4f}' .format(instance,s_states, n_variables,R['factor'],R['time']))

def exp01():
	x = 5 

	error = 0.0001

	print('#{0:10} {1:10} {2:10} {3:10}'.format('states','factor','time-vi','time-2lp'))
	f = open("logTest.dat",'w')

	for y in range(50,1000,10):
		

		ssp = genRiv2(x,y)
		s_states = len(ssp._S)

		factor = -1
		stop = 1
		step = 0.01

		while factor <= stop:
			
			factor = factor + step

			#Rvi = vi_e(ssp, factor, error, 0, 60)
			R2lp = lp_ssp_e(ssp,factor,0,60)
					
			#print('{0:10} {1:10.2f} {2:10.5f} {3:10.5f}'.format(s_states,factor,Rvi['time'],R2lp['time']))
			print('{0:10} {1:10.2f} {2:10.5f}'.format(s_states,factor,R2lp['time']))

def test():

	tam = 2
	R = genTire(tam)
	ssp = R['ssp']
	md = R['metadata'] 
	am = R['actMap']

	e = 0.00001
	factor = 0.1
	R = riskAdverse(ssp,e+0.00000001,e, factor, initPolicy(ssp))
	print(R['factor'])

	R1 = search_lambda2(ssp)
	print('SEARCH LAMBDA', R1['factor'])

	#0.6 0.7 0.8
	R = lp_ssp_e(ssp, 0.7)
	plotTire(ssp, tam, "tire-2[0-7]", R['policy'], md, am);


test()
# exp07()

