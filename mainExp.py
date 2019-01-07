import argparse
import ssp
import vi
import lpSolver

parser = argparse.ArgumentParser()


parser.add_argument("p" , help="file path of the problem", type=str)
parser.add_argument("l" , help="lambda factor: [l>0: risk adverse], [l<0 : risk prone]", type=float)
parser.add_argument("s" , help="solution: [0:vi], [1:dualLP]", type=int)


parser.add_argument("-v","--verbose",help="increase verbosity output")
parser.add_argument("-log","--logFile",help="save time in a file", type=str)
parser.add_argument("-t","--time_limit",help="limit time for the solver in seconds", type=float)



args = parser.parse_args()


factor = args.l
filename = args.p
solution = args.s
maxtime = args.time_limit

solutions = { 0 : vi.vi_e, 1: lpSolver.lp_ssp_e}

ssp = ssp.SSP()
ssp.readJSON(filename)

R = None

n_states = len(ssp._S)
time_sol = 0

if solution == 0:
	R = vi.vi_e(ssp,factor,0,time_limit=maxtime)
	time_sol = R['time']

if solution == 1:
	R = lpSolver.lp_ssp_e(ssp,factor, max_time=maxtime)
	time_sol = R['time']


print("#STATES")
print(n_states)
print("#LAMBDA")
print(factor)
print("#TIME")
print(time_sol)


