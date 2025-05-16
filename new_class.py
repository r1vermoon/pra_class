class Car:
    def __init__(self,color,tires_num,gas_num,cost):
        self.color=color
        self.glass_num=6
        self.tires_num=tires_num
        self.gas_num=gas_num
        self.cost=cost
        
    def show_color(self):
        print(self.color)

    def get_howlong(self):
        howlong=self.gas_num/self.cost
        return howlong
    
    def weight(self):
        weight=self.gas_num*10
        return weight
    
class Trunk(Car):
    def __init__(self, color, tires_num, gas_num, cost,load):
        super().__init__(color, tires_num, gas_num, cost)
        color
        color
        color
        self.load=load
    
    def get_howlong(self):
        if (self.load<=0):
            howlong=self.gas_num/self.cost
        else:
            howlong=(self.gas_num/self.cost)/2
        return howlong
    
    def full_weight(self):
        full_weight=self.weight()+self.load
        return full_weight