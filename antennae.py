from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()


freq = {0 : 'f1',1:'f2',2:'f3'}

at_1 = model.NewIntVar(0,2, 'at_1')
at_2 = model.NewIntVar(0,2, 'at_2')
at_3 = model.NewIntVar(0,2, 'at_3')
at_4 = model.NewIntVar(0,2, 'at_4')
at_5 = model.NewIntVar(0,2, 'at_5')
at_6 = model.NewIntVar(0,2, 'at_6')
at_7 = model.NewIntVar(0,2, 'at_7')
at_8 = model.NewIntVar(0,2, 'at_8')
at_9 = model.NewIntVar(0,2, 'at_9')


antenna1 = model.NewIntVar(0,2, "antenna1")

model.add(at_1 != at_2)
model.add(at_1 != at_3)
model.add(at_1 != at_4)
model.add(at_2 != at_3)
model.add(at_2 != at_5)
model.add(at_2 != at_6)
model.add(at_3 != at_6)
model.add(at_3 != at_9)
model.add(at_4 != at_5)
model.add(at_4 != at_2)
model.add(at_6 != at_7)
model.add(at_6 != at_8)
model.add(at_7 != at_8)
model.add(at_8 != at_9)


status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("at_1: %s" % freq[solver.Value(at_1)])
    print("at_2: %s" % freq[solver.Value(at_2)])
    print("at_3: %s" % freq[solver.Value(at_3)])
    print("at_4: %s" % freq[solver.Value(at_4)])
    print("at_5: %s" % freq[solver.Value(at_5)])
    print("at_6: %s" % freq[solver.Value(at_6)])
    print("at_7: %s" % freq[solver.Value(at_7)])
    print("at_8: %s" % freq[solver.Value(at_8)])
    print("at_9: %s" % freq[solver.Value(at_9)])
    print("antenna1: %s" % freq[solver.Value(antenna1)])