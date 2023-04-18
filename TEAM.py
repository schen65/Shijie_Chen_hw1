from pyomo.environ import *
import math


model = AbstractModel()

I = 17
G = 4
N = 98
model.i = RangeSet(1, I)
model.g = RangeSet(1, G)
model.n = RangeSet(1, N)

model.f = Param(model.i, within=Binary)
model.gpa = Param(model.i, model.i)
model.m = Param(model.i, model.i, within=Binary)
model.a = Param(model.i, within=Binary)
model.s = Param(model.i, model.i, model.n, within=Binary)

model.x = Var(model.i, model.g, domain=Binary)
model.p = Var(model.i, model.i, model.g, domain=Binary)
model.y = Var(model.g, domain=Binary)
model.r = Var(model.g, domain=Binary)

def Obj(model):
    return sum(sum(sum(model.p[i, t, g] * (model.gpa[i, t] + model.m[i, t] - sum(model.s[i, t, n] / N for n in model.n)) for t in model.i) for i in model.i) for g in model.g)
model.objfc = Objective(rule=Obj, sense=minimize)



# Constraint (a)
def group_ASSI(model,i):
    return sum(model.x[i,g] for g in model.g) == 1
model.group_ASSIFC = Constraint(model.i, rule = group_ASSI)

#math.ceil(I/G) rounds up
#math.floor(I/G) rounds down
# Constraints (b)
def group_size_LOW(model,g):
    return  math.floor(I/G) <= sum(model.x[i,g] for i in model.i)
model.group_size_LOWFC = Constraint(model.g, rule = group_size_LOW)

def group_size_HI(model,g):
    return  math.floor(I/G) >= sum(model.x[i,g] for i in model.i)
model.group_size_HIFC = Constraint(model.g, rule = group_size_HI)

# Constraints (c)
def group_females1(model,g):
    return  2 - sum(model.x[i,g] * model.f[i] for i in model.i) - model.y[g] <= 0
model.group_females1fc = Constraint(model.g, rule = group_females1)

def group_females2(model,g):
    return sum(model.x[i, g] * model.f[i] for i in model.i) - 1 * (1 - model.y[g]) <= 0
model.group_females2fc = Constraint(model.g, rule = group_females2)

# Constraints (d)
def group_minority1(model,g):
    return 2 - sum(model.x[i,g] * model.a[i] for i in model.i) - model.r[g] <= 0
model.group_minority1fc = Constraint(model.g, rule =group_minority1)

def group_minority2(model,g):
    return sum(model.x[i,g] * model.a[i] for i in model.i) - 1 * (1 - model.r[g]) <= 0
model.group_minority2fc = Constraint(model.g, rule = group_minority2)

# Constraints(e)
def log1(model, i, t, g):
    if t > i:
        return model.x[t,g] >= model.p[i,t,g]
    else:
        return model.p[i,t,g] == 0
model.log1c = Constraint(model.i, model.i, model.g, rule = log1)


def log2(model, i, t, g):
    if t > i:
        return model.x[i,g] >= model.p[i,t,g]
    else:
        return model.p[i,t,g] == 0
model.log2c = Constraint(model.i, model.i, model.g, rule = log2)

def log3(model,i,t,g):
    return model.x[i,g] + model.x[t,g] - model.p[i,t,g] <= 1
model.log3c = Constraint(model.i, model.i, model.g, rule = log3)

def log4(model,i,t,g):
    if t <= i:
        return model.p[i,t,g] == 0
    else:
        return Constraint.Skip
model.log4c = Constraint(model.i, model.i, model.g, rule = log4)