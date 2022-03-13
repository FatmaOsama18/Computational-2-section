#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra


# In[2]:


from cobra import Model, Reaction, Metabolite


# In[10]:


model = Model('Test')

r1 = Reaction('r1')
r1.name = 'R1'
r1.lower_bound=0
r1.upper_bound=1000

r2=Reaction('r2')
r2.name = 'R2'
r2.lower_bound=0
r2.upper_bound=1000


# In[11]:


rr = Reaction('rr')
rr.name = 'RR'
rr.lower_bound=1
rr.upper_bound=1


# In[12]:


y = Reaction('y')
y.name = 'Y'
y.lower_bound=0
y.upper_bound=1000


# In[13]:


ATP_T = Reaction('ATP_T')
ATP_T.name = 'ATP_T'
ATP_T.lower_bound=0
ATP_T.upper_bound=1000


# In[28]:


r3 = Reaction('r3')
ATP_T.name = 'r3'
ATP_T.lower_bound=.7
ATP_T.upper_bound=.7


# In[16]:


A= Metabolite(
    'A',compartment='c')
B=Metabolite(
    'B',compartment='c')
C= Metabolite(
    'C',compartment='c')


# In[17]:


ATP= Metabolite(
    'ATP',compartment='c')


# In[18]:


r1.add_metabolites({A:-1,B:1})

r2.add_metabolites({B:-1,C:1})


# In[19]:


rr.add_metabolites({A:1})


# In[20]:


y.add_metabolites({C:-1})


# In[21]:


ATP_T.add_metabolites({A:-1,ATP:1})


# In[22]:


r3.add_metabolites({ATP:-1})


# In[23]:


model.add_reactions([rr,r1,ATP_T,r2,r3,y])


# In[26]:


model.objective = 'y'


# In[29]:


model.optimize()


# In[30]:


model.summary()

