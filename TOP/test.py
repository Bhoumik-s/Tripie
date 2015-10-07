from data_class import Data
from constraints import status
from heuristic import heu1
from variables_class import Solution
from metaheuristic import metaN1,metaN2,metaN3
from plot import plotPlan
import numpy as np

file="data.xlsx"
m= int(raw_input("No. of days: "))
d=Data(file,m,230,50)

empty_route=np.array([[0,d.n+1]]*d.m)
rmvd=[[]]*d.m

sol=Solution(empty_route,d)
new_sol= heu1(sol,rmvd,d)
plotPlan(new_sol.R,d.points,d.m)