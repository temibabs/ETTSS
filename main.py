from collections import defaultdict


# In a CSP, 3 things are taken into consideration:

# (1) Variables (Examination Courses) => A list representing all the courses
variables = []
 
# (2) Domains (Time slices) => We will represent this as a dictionary
# Initially, all variables are assigned all possible values
# Mapping to be put into consideration:
# 1 = 8 - 10
# 2 = 10 - 12
# ...

Assuming there are only 6 time slices
temp = map(str, [1, 2, 3, 4, 5, 6])
domains = defaultdict(list)
for i in range(variables):
  domains[variables[i]].append(temp[i])
 
 
# (3) Costraints
# First, we define a constraint function.
# But because the constraints are not yet well-defined, we will skip this for now.
constraints = 
