class Tit_for_Tat:
    def __init__(self,out=0):
        self.s = []
        self.out = out
        
    def play(self):
        if self.s == []:
            self.out = 0
        elif self.s[-1][1] == 0:
            self.out = 0
        else:
            self.out = 1
        return self.out
    
    def aggiorna_storico(self,partita):
        self.s.append(partita)