from cocoex import Suite

suite = Suite('bbob-constrained', '', '')


for f in suite:
    print(f.initial_solution)
    print(f.number_of_objectives)