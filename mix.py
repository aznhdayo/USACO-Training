"""
ID: azha0561
LANG: PYTHON3
PROG: milk
"""

class Farmer:
    lstpi = []
    def __init__(self, pia):
        self.price, self.amount = pia

        Farmer.lstpi.append((self.price, self.amount))
        Farmer.lstpi.sort()

    def min_cost_to_reach(lst, goal):
        cost = 0
        for price, amount in lst:
            if goal > amount:
                goal -= amount
                cost += price * amount
            else:
                cost += price * goal
                goal = 0
                break
        return cost

with open("milk.in", "r") as inp:
    inp_data = inp.read()

lines = inp_data.splitlines()
milk_needed = int(lines[0].split()[0])

for line in lines[1:]:
    i = line.split()
    pia = (int(i[0]), int(i[1]))
    farmer = Farmer(pia)

min_cost = Farmer.min_cost_to_reach(Farmer.lstpi, milk_needed)

with open("milk.out", "w") as out:
    out.write(str(min_cost) + "\n")
