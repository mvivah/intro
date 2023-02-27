class Hero:
    def __init__(self):
        self.level = 1
        self.hp = 0
        self.msg = ""

    def kill(self):
        self.level += 500
        print(f'kiled! hp: {self.hp}')
        if self.hp > 1000 and self.level == 1:
            print('level up by one')
            self.level += 1
        if self.hp > 2000 and self.level == 2:
            print('level up by two!')
            self.level += 1
        if self.hp > 3000 and self.level == 3:
            print('level up by three!')
            self.level += 1

    def fly(self):
        self.hp += 1
        print(f'I can fly without wings: {self.hp}')


chan = Hero()
for i in range(10):
    chan.kill()
    print(chan.level)
    chan.fly()
    
