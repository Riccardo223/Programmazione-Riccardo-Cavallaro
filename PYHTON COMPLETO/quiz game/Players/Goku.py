class Goku:
    def __init__(self,out=0):
        self.s = []
        self.out = out
        
    def play(self):
        self.out = 0
        return self.out
    
    def aggiorna_storico(self,partita):
        self.s.append(partita)