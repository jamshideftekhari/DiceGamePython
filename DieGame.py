import Die
class DieGame(object):
    def __init__(self):
        pass

    def Play(self):  
        self.D1 = Die.Die(0)
        self.D1.roll()
        self.D2 = Die.Die(0) 
        self.D2.roll()
         
    def PrintResult (self):
        fv1 = self.D1.GetFaceValue()
        fv2 = self.D2.GetFaceValue()
        result = fv1+fv2
        print("trace Die/printresult")
        print(fv1)
        print(fv2)
        print("result is: " + str(result))

    def GetResult(self):
        fv1 = self.D1.GetFaceValue()
        fv2 = self.D2.GetFaceValue()
        result = fv1+fv2
        return result


