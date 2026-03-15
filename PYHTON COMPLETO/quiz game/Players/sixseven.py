class sixseven:
    def __init__(self,out=0):
        self.s = []
        self.out = out
        
    def play(self):
        if len(self.s) > 50:
           if self.s == []:
            self.out = 0
           elif self.s[-1][1] == 0:
            self.out = 0
           else:
            self.out = 1
        else:
          mosse_avversario = [partita[1] for partita in self.s[:50]]
          percentuale_coop = (mosse_avversario.count(0) / 20) * 100
          if percentuale_coop > 75:
              self.out = 1
          if percentuale_coop >= 40:
              self.out = self.s[-1][1]
          else:
              self.out = 1
        
        return self.out
            
    
    def aggiorna_storico(self,partita):
        self.s.append(partita)

