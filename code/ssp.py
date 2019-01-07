from collections import defaultdict
from typing import overload


class SSP:

	#SSP is a Tuple M = <S, s0, G, A, P, C>



	def __init__(self):

		self._S = []
		self._s0 = ""
		self._G = []
		self._A = []

		self._P = {}
		self._C = {}
		self._App = defaultdict(list)


	def foo(self):
		print("FOO")

	def App(self, state, action = None):

		if action is None:
			return self._App[state]
		else:
			self._App[state].append(action)

	def P(self, s, action, s1, probability = None):

		if probability is None:
			return self._P.get((s,action,s1),0)
		else:
			self._P[s, action, s1] = probability

	def C(self, s, a, cost = None):
		if cost is None:
			return self._C.get((s,a),0)
		else:
			self._C[s,a] = cost


	@property
	def S(self):
		return self._S

	@property
	def s0(self):
		return self._s0

	@property
	def G(self):
		return self._G

	@property
	def A(self):
		return self._A
		
	def __str__(self):


		limit = "==========================="
		varS = "Stat : " + str(self._S)
		actA = "Acts : " + str(self._A)
		init = "Init : " + self._s0
		goal = "Goal : " + str(self._G)

		return limit + "\n" + varS + "\n" + actA + "\n" + init + "\n" + goal + "\n" + limit
	

	def toDot(self, filename):
		with open(filename, 'w') as out:
			var = "digraph {"
			out.write(var+'\n')

			var = "node [ fontname = Helvetica fontsize = 10 shape=circle style=filled]"
			out.write('\t' + var + '\n')
			var = "edge [ fontname = Helvetica fontsize = 10 ]"
			out.write('\t' + var + '\n')



			for s in self._S:
				label 	  = "label = \""+s+"\""
				color     = ", color = \"#E0E0E0\""
				fillcolor = ", fillcolor = \"#E0E0E0\""
				var = s + "["+label+color+fillcolor+"]"
				out.write('\t' + var + '\n')
				for a in self.App(s):

					for s1 in self._S:
						if self.P(s,a,s1) > 0:
							label = "label = <"+ str(self.P(s,a,s1)) +"<SUB>"+ a +"</SUB>>"
							color = ",color = \"#E0E0E0\""
							var = s + " -> " + s1 + "["+label+color+"]"
							out.write('\t' + var + '\n')

			var = "}"
			out.write(var+'\n')