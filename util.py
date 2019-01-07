
from numpy import linalg as LA
import numpy as np
import time
from copy import deepcopy
from ssp import *
from pulp import *
from genProblem import *
from lpSolver import *
from vi import *

from river import *
from math import *

# from tireworld import *
# FIRST VERSION RISK ADVERSE POLICY TO FIND MAX LAMBDA ADMISIBLE


def initPolicy(ssp):
    currentP = {}
    for s in ssp._S:
        currentP[s] = ssp.App(s)[0]

    return currentP


def foo(ssp, beta, error, factor, p0):

    R = {}
    link = {}
    linkT = {}

    for i in range(len(ssp._S)):
        link[i] = ssp._S[i]
        linkT[ssp._S[i]] = i

    T = []

    tamM = len(ssp._S)

    for i in range(tamM):
        T.append([])
        for j in range(tamM):
            T[i].append(0)

    for j in range(tamM):
        for i in range(tamM):
            state1 = link[i]
            state2 = link[j]
            if state2 == ssp._G[0]:
                T[i][j] = 0
            else:
                T[i][j] = ssp.P(state1, p0[state1], state2)

    D = []

    for i in range(tamM):
        D.append([])
        for j in range(tamM):
            D[i].append(0)

    for j in range(tamM):
        for i in range(tamM):
            if i == j:
                state1 = link[i]
                D[i][j] = exp(factor*ssp.C(state1, p0[state1]))

    T1 = np.array(T)
    D1 = np.array(D)

    def specR(ssp, factor, policy):

        for j in range(tamM):
            for i in range(tamM):
                state1 = link[i]
                state2 = link[j]

                if state2 == ssp._G[0]:
                    T[i][j] = 0
                else:
                    T[i][j] = ssp.P(state1, policy[state1], state2)

        for j in range(tamM):
            for i in range(tamM):
                if i == j:
                    state1 = link[i]
                    D[i][j] = exp(factor*ssp.C(state1, policy[state1]))
                    print("VALUE", D[i][j])

        T1 = np.array(T)
        D1 = np.array(D)
        M = D1.dot(T1)
        w, v = LA.eig(M)
        for i in range(len(w)):
            w[i] = abs(w[i])
        initSR = max(w)

        return initSR.real

    flag = True

    R = vi_e(ssp, factor, p0)
    #R = vi_e(ssp,factor,p0)
    p1 = R['policy']

    p1[ssp._G[0]] = 'abs'

    counter = 0

    t0 = time.clock()
    tp = 0

    while p0 != p1:
        tp = time.clock()-t0

        counter = counter + 1
        p0 = deepcopy(p1)
        # print("deepcopy")

        try:
            initSR = specR(ssp, factor, p1)
        except:
            print('problem here')
            break
        # print("before inner while")
        # print("INIT SR", initSR)
        while initSR < (1-beta):
            # counter +=1
            factor = factor + (np.log(1-error) - np.log(initSR))
            # print("factor",factor)
            initSR = specR(ssp, factor, p1)

        # 	print("afterINITSR")
        # print("exit inner while")

        # R = vi_e(ssp,factor,p0)
        try:
            R = lp_ssp_e(ssp, factor)
        except:
            break

        p1 = R['policy']
        p1[ssp._G[0]] = 'abs'
        # plotRiv(ssp, x, y, "expRiv2", p1)

    time2 = time.clock()-t0

    R['factor'] = factor
    R['policy'] = p1
    R['time'] = time2
    R['tlast'] = tp
    R['counter'] = counter
    return R


# x = 4
# y = 4

# factor = -0.1
# error = 0.001


# ssp = tt3()
# ssp = genRiv2(5, 20)

# R = foo(ssp, error + 0.000001, error, -0.1, initPolicy(ssp))
# # print(R)
# print(R['time'],R['tlast'],R['factor'])
# print(R['policy'])

# R = search_lambda2(ssp)
# print(R['time'], R['factor'])
# R = lp_ssp_e(ssp, 0.66)
# print(R['policy'])
