#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra


# In[2]:


from cobra import Model,Reaction,Metabolite


# In[3]:


model = Model('Test')


# In[4]:


#======>glc
r0 = Reaction('r0') 
r0.name ='r0'
r0.lower_bound = 1
r0.upper_bound = 1


# In[5]:


#glc=======>AA
r1 = Reaction('r1')
r1.name ='r1'
r1.lower_bound = 0
r1.upper_bound = 1000


# In[6]:


#AA=======>Biomass
r2 = Reaction('r2')
r2.name ='r2'
r2.lower_bound = 0
r2.upper_bound = 1000


# In[7]:


#Biomass=======>
M = Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[8]:


glc=Metabolite('glc',compartment='c')
AA=Metabolite('AA',compartment='c')
Biomass=Metabolite('Biomass',compartment='c')


# In[9]:


r0.add_metabolites({glc:1})


# In[10]:


r1.add_metabolites({glc:-1,AA:1})


# In[11]:


r2.add_metabolites({AA:-9.09,Biomass:1})


# In[12]:


M.add_metabolites({Biomass:-1})


# In[13]:


model.add_reactions([r0,r1,r2,M])


# In[14]:


model.objective='M'


# In[15]:


model.optimize()


# In[16]:


model.summary()


# In[22]:


cobra.io.save_json_model(model,"Testing1.json")


# In[23]:


import escher


# In[24]:


from escher import Builder


# In[25]:


builder = Builder()


# In[26]:


builder


# In[ ]:




