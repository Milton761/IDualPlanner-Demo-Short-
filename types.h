#ifndef UTIL_H
#define UTIL_H

#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <string>
#include <random>
#include <fstream>
#include <chrono>
#include <algorithm>
#include <deque>
#include <cmath>
#include <iomanip>
#include <stack>

using namespace std;


namespace namespace_MDP
{
	typedef string state;
	typedef string action;
	typedef double probability;
	typedef double cost;
	typedef double value;

	typedef map<tuple<state, action>, cost > C;
	typedef map<tuple<state, action, state>, probability> P;
	typedef map<state, vector<action>> App;

	typedef map<state, value> V;
	typedef map<state, action> Policy;
	
	typedef double lambda;
	typedef double error;
	typedef map<state, probability> BellmanResidual;

} 



#endif