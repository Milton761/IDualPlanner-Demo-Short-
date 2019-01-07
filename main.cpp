
#include "types.h"
#include "algorithms.h"

using namespace std;
using namespace namespace_MDP;

int sign(int f);
tuple<V,Policy> vi_e(vector<state> S,vector<action> A, P p,C c,vector<state> G, App app, lambda f, error e);
void load_ssp(string filename);

int main()
{

	

	cout<<"Hello world"<<endl;
	load_ssp("FIRSTSSP.ssp");
	
	
	return 0;
}




int sign(int f)
{
	if(f<0)
		return 1;
	return -1;
}

tuple<V,Policy> vi_e(vector<state> S,vector<action> A, P p,C c,vector<state> G, App app, lambda f, error e)
{
	V v;
	Policy policy;
	BellmanResidual BR;

	cout<<"TEST"<<endl;
	for(auto s: S)
	{
		v[s] = 2;
	}

	int counter = 0;

	bool flag = true;

	while(flag)
	{

		error errorBelman = 0.0;
		cout<<counter<<endl;
		counter++;
		auto v1 = v;

		for(auto s: S)
		{

			vector<value> tmpVal;
			vector<action> tmpAct;

			for(auto a: app[s])
			{
				auto s_a = make_tuple(s,a);
				double acc = 0;
				for(auto s1: S)
				{
					if(find(G.begin(),G.end(),s1)==G.end())
					{

						
						auto s_a_s1 = make_tuple(s,a,s1);
						acc += exp(f*c[s_a])*p[s_a_s1]*v1[s1];
					}
				}
				auto g  = G[0];
				auto s_a_g = make_tuple(s,a,g);
				acc += exp(f*c[s_a])*p[s_a_g] * sign(f);

				tmpVal.push_back(acc);
				tmpAct.push_back(a);

			}

			if(tmpVal.size()==0){
				v[s] = 0;
				policy[s] = "None";
			}else{
				double minV = numeric_limits<double>::infinity();

				for(int i=0; i<tmpVal.size(); i++)
				{
					if(tmpVal[i]<minV)
					{
						policy[s] = tmpAct[i];
						v[s] = tmpVal[i];
						minV = tmpVal[i];
					}
				}
			}
		}


		for(auto s_v: v)
		{
			state s = s_v.first;
			cout<<s<<" "<<v[s]<<" "<<v1[s]<<endl;
		}

		string a;
		cin>>a;

		if(v1==v)
		{
			flag = false;
		}

	}

	cout<<"counter "<<counter<<endl;
	return forward_as_tuple(v,policy);
}


void load_ssp(string filename)
{
	ifstream file;
	file.open(filename);

	string key;

	
	vector<state> S;
	vector<action> A;
	C c;
	P p;
	App app;
	int n_states;
	int n_actions;
	int p_function;
	int app_function;
	int c_function;
	state s;
	action a;
	state s0;
	state sg;

	

	while(file>>key)
	{


		if(key=="#STATES")
		{
			cout<<key<<endl;
			file>>n_states;
		}
		if(key=="#LIST-STATES")
		{
			cout<<key<<endl;
			for(int i=0; i<n_states; i++)
			{
				file>>s;
				S.push_back(s);
			}
		}
		if(key=="#ACTIONS")
		{
			cout<<key<<endl;
			file>>n_actions;
		}
		if(key=="#LIST-ACTIONS")
		{
			cout<<key<<endl;
			for(int i=0; i<n_actions; i++)
			{
				file>>a;
				A.push_back(a);
			}

		}
		if(key=="#INIT-STATE")
		{
			cout<<key<<endl;
			file>>s0;
		}
		if(key=="#GOAL-STATES")
		{
			cout<<key<<endl;
			file>>sg;
			
		}
		if(key=="#PROBABILITY-TRANSITION-FUNCTION")
		{
			cout<<key<<endl;
			file>>p_function;
			for(int i=0; i<p_function; i++)
			{
				state s,s1;
				action a;
				probability pr;

				file>>s>>a>>s1>>pr;

				auto s_a_s1 = make_tuple(s,a,s1);

				p[s_a_s1] = pr;
			}

		}
		if(key=="#COST-FUNCTION")
		{
			cout<<key<<endl;
			file>>c_function;
			for(int i=0; i<c_function; i++)
			{
				state s;
				action a;
				cost ct;
				
				file>>s>>a>>ct;

				auto s_a = make_tuple(s,a);

				c[s_a] = ct;

			}
		}
		if(key=="#APP-FUNCTION")
		{
			cout<<key<<endl;
			file>>app_function;

			for(int i=0;i<app_function;i++)
			{
				int aps;
				file>>aps;

				for(int j=0; j<aps; j++)
				{
					state s;
					action a;

					file>>s>>a;
					app[s].push_back(a);
				}


			}

		}

	}

	cout<<"STATES"<<endl;
	for(int i=0; i<S.size(); i++)
	{
		cout<<S[i]<<endl;
	}

	cout<<"------------------"<<endl;

	for(int i=0; i<A.size(); i++)
	{
		cout<<A[i]<<endl;
	}

	cout<<"-------------------"<<endl;
	cout<<s0<<" "<<sg<<endl;

	for(auto s_a_s1: p)
	{
		state s = get<0>(s_a_s1.first);
		state a = get<1>(s_a_s1.first);
		state s1 = get<2>(s_a_s1.first);
		probability pr = s_a_s1.second;
		cout<<s<<" "<<a<<" "<<s1<<" "<<pr<<endl;
	}

	for(auto s_a: c)
	{
		state s = get<0>(s_a.first);
		state a = get<1>(s_a.first);
		//state s1 = get<2>(s_a_s1.first);
		cost ct = s_a.second;
		cout<<s<<" "<<a<<" "<<ct<<endl;
	}

	vector<state> G;
	G.push_back(sg);

	auto R = vi_e(S,A,p,c,G,app,0.5,0);

	V value= get<0>(R);
	Policy policy= get<1>(R);

	cout<<"Policy"<<endl;
	for(auto p: policy)
	{
		state s = get<0>(p);
		action a = get<1>(p);

		cout<<s<<" "<<policy[s]<<endl;
	}

}

