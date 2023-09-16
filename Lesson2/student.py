class Student:
    def __init__(self, name:str, age:float, group:str, money:float):
        self.Name = name
        self.Age = age
        self.Group = group
        self.Money = money
    def showInfo(self):
        print(f"Name: \t{self.Name}\n"
              f"Age: \t{self.Age}\n"
              f"Group: \t{self.Group}\n"
              f"Money: \t{self.Money}\n")
    def Buy(self, price:float):
        if(self.Money >= price):
            self.Money -= price
        else:
            print("Not enough money!\n"
                  f"Your bugget:\t{self.Money}")
