#!/usr/bin/env python
# coding: utf-8

# In[1]:


python -m pip install gurobipy


# In[4]:


conda install -c gurobi gurobi


# In[3]:


import gurobipy as gp
from gurobipy import GRB


# In[5]:


# Model definiton
m=gp.Model('Optimization Model')


# In[11]:


# Define variables          
x1=m.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2=m.addVar(vtype=GRB.CONTINUOUS, name='x2')
x3=m.addVar(vtype=GRB.CONTINUOUS, name='x3')


# # set objective
# m.setObjective(2x1+1.5x2+3x3,GRB.MINIMIZE)

# In[13]:


m.addConstr(x1+x2+x3>=8000)
m.addConstr(2*x1+3*x2+5*x3<=4000000)
m.addConstr(3*x1+5*x2+2*x3>=20000)
m.addConstr(2*x1+7*x2+9*x3>=20000)
m.addConstr(x1>=0)
m.addConstr(x2>=0)
m.addConstr(x3>=0)



# m.optimize()

# In[ ]:




