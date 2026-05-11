fruits = ['apple',
          'banana',
          'lime']

admins = {'alex': 43}


#Распаковка
print(*fruits)


def all_fruits(*fruits):
    print(*fruits)

def all_admins(**all_admins):
    print(all_admins)

all_admins(name='Alex', age=43)
all_fruits(1,2,3,4)