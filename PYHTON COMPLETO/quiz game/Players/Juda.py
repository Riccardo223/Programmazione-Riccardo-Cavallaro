class Juda:
    def __init__(self,out=0):
        self.s = []
        self.out = out
        
    def play(self):
        self.out = 1
        return self.out
    
    def aggiorna_storico(self,partita):
        self.s.append(partita)