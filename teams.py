from pyomo.environ import *
import math


model = AbstractModel()

I = 17
G = 4
N = 98
model.I = RangeSet(1, I)
model.G = RangeSet(1, G)
model.N = RangeSet(1, N)

model.f = Param(model.I, within=Binary)
model.gpa = Param(model.I, model.I)
model.m = Param(model.I, model.I, within=Binary)
model.a = Param(model.I, within=Binary)
model.s = Param(model.I, model.I, model.N, within=Binary)

model.x = Var(model.I, model.G, domain=Binary)
model.p = Var(model.I, model.I, model.G, domain=Binary)
model.y = Var(model.G, domain=Binary)
model.r = Var(model.G, domain=Binary)


def Obj(model):
    return sum(sum(sum(model.p[i, t, g] * (model.gpa[i, t] + model.m[i, t] - sum(model.s[i, t, n] for n in model.N)) for t in model.I) for i in model.I) for g in model.G)
model.objfc = Objective(rule=Obj, sense=minimize)




#math.ceil(I/G) rounds up
#math.floor(I/G) rounds down

# Constraint (b)
def group_size_bounds(model,g):
    math.floor(I/G) <= sum(model.X[i,g] for i in model.I)
qa

def log1(model, i, t, g):
    if t > i:
        return model.x[t,g] >= model.p[i,t,g]
    else:
        return model.p[i,t,g] == 0
model.log1c = Constraint(model.I, model.I, model.G, rule = log1)


def log2(model, i, t, g):
    if t > i:
        return model.x[i,g] >= model.p[i,t,g]
    else:
        return model.p[i,t,g] == 0
model.log2c = Constraint(model.I, model.I, model.G, rule = log2)