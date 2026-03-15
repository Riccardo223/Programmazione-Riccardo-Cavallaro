from fplay import *
import os
import sys
import importlib

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

rounds = int(input("how many rounds do you want to play?"))

p1 = sixseven()
points = []
for i in range(rounds):
    round_gamer = int(input("cooperate=0 or defect=1   "))
    game = [p1.play(),round_gamer]
    points.append(result(game))
    p1.aggiorna_storico(game)
    print(result(game))
    if result(game)[0] > result(game)[1]:
        print('\033[31m You lose \033[0m')
    elif result(game)[0] < result(game)[1]:
        print("\033[32m You win \033[0m")
    else:
        print("\033[33mIt's a tie \033[0m")
    
    
points = np.array(points)
print(f"\n \n Totale partite: {points} \n \n Il tuo punteggio totale è {np.sum(points[:,1])} \t mentre quello del tuo avversario è {np.sum(points[:,0])}")