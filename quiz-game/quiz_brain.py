class Qbrain:

    def __init__(self,qlist):
        self.qnum=0
        self.qlist=qlist
        self.c=0
        
    def stillhasqns(self):
        return self.qnum < len(self.qlist)
    
    def nextqn(self):
        self.currentqn=self.qlist[self.qnum]
        self.qnum+=1
        b=input(f"Q{self.qnum}: {self.currentqn.text} (True/False) ?: ")
        return b
    
    def check(self,a):    
        if a==self.currentqn.answer:
            self.c+=1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"You got {self.c}/{self.qnum} right so far!\n\n")
        
        
        