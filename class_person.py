import random

name_list = ['ato', 'john', 'smith', 'kendo', 'young', 'yujin', 'mee', 'yaker']

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say(self):
        print("안녕하세요, 내 이름은 {}이고, 내 나이는 {}입니다.".format(self.name, self.age))

    
if __name__ == '__main__':
    mans = []
    for x in range(100):
        n = random.sample(name_list, 1)[0]
        age = random.randint(10, 100)
        man = person(n, age)
        mans.append(man)

    for xman in mans:
        xman.say()
