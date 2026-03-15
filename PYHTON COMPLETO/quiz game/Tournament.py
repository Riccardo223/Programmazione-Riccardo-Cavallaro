from fplay import *
import os
import sys
import importlib
import itertools
import random

### First, lets import all the classes (Strategies) and create a list of objects form each class (a list of players)

# 1️ Make sure the Players folder is recognized
project_folder = os.path.dirname(__file__)
players_folder = os.path.join(project_folder, "Players")
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)


# 3️ Dynamically import all classes from Players
package = "Players"
modules_names = []
for filename in os.listdir(players_folder):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # strip .py
        module = importlib.import_module(f"{package}.{module_name}")
        modules_names.append(module_name)
        # map the class into the current namespace
        if hasattr(module, module_name):
            globals()[module_name] = getattr(module, module_name)

#create the list of players
players = [globals()[name]() for name in modules_names]

results = {p.__class__.__name__: {} for p in players}

for p in players:
    for op in players:
        if p != op:
            results[p.__class__.__name__][op.__class__.__name__] = None  # placeholder for result

# Generate all unique matches
matches = list(itertools.combinations(players, 2))

# Simulate matches and record results
rounds = 10

for p1, p2 in matches:
    points = []
    for i in range(rounds):
        game = [p1.play(),p2.play()]
        points.append(result(game))
        p1.aggiorna_storico(game)
        p2.aggiorna_storico(game[::-1]) #reverse order, such that the first elements of the game list corresponds to the player
    
    points = np.array(points)
    results[p1.__class__.__name__][p2.__class__.__name__] = np.sum(points[:,0])
    results[p2.__class__.__name__][p1.__class__.__name__] = np.sum(points[:,1])


totals = {name: sum(scores.values()) for name, scores in results.items()}

# Print results
print("Match results (individual):")
for player, scores in results.items():
    print(f"{player}: {scores}")

print("\n Total scores:")
sorted_scores = sorted(totals.items(), key=lambda x: x[1], reverse=True)
for player, total in sorted_scores:
    print(f"{player}: {total}")


'''print("\nTotal scores:")
for player, total in totals.items():
    print(f"{player}: {total}")'''



