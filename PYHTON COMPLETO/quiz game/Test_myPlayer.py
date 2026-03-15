from fplay import *
from Players.Goku import *
from Players.Juda import *
from Players.Random import *
from Players.Tit_for_Tat import *
from Players.sixseven import*

p1 = sixseven()
p2 = Random()
points = []
for i in range(100):
    game = [p1.play(),p2.play()]
    points.append(result(game))
    p1.aggiorna_storico(game)
    p2.aggiorna_storico(game[::-1]) #reverse order, such that the first elements of the game list corresponds to the player

points = np.array(points)

print(
    f"player {str(p1).split('.')[1].split(' ')[0]}: {points[:,0].sum()} points"
    f"\n player {str(p2).split('.')[1].split(' ')[0]}: {points[:,1].sum()} points")