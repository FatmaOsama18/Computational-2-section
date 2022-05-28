#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[2]:


M = nx.Graph()
M.add_nodes_from(['m', 'c', 'y', 'k','r','g','b'])
M.add_edges_from([('m','c'), ('c','k'), ('r','b'), ('y','g'),('k','g'),('y','r'),('k','b')])
nx.draw(M, with_labels = True)


# In[3]:


list(M.neighbors('k'))


# In[4]:


for neighbor in M.neighbors('y'):
    print(neighbor)


# In[5]:


M.has_node('a')


# In[6]:


M.has_node('y')


# In[7]:


nx.is_tree(M)


# In[8]:


nx.is_connected(M)


# In[9]:


M.degree('k')


# In[10]:


DI = nx.DiGraph()
DI.add_edges_from([('m','c'), ('c','y'), ('y','g'),('g','k'),('y','r'),('r','m')])
nx.draw(DI, with_labels = True, node_size = 550)


# In[11]:


dict(DI.degree())


# In[12]:


nx.to_numpy_matrix(DI)


# In[14]:


graph=nx.read_edgelist('NX.txt',nodetype=str,create_using=nx.DiGraph())
nx.draw(graph,with_labels=True,node_size=600)

