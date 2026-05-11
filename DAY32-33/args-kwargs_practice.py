def create_player(*args, **kwargs):
    print('player info:')
    print('nickname: ', kwargs.get('nickname', 'Not found'))
    print('level: ', kwargs.get('level', 'Not found'))
    print('vip_status: ', kwargs.get('vip_status', 'Not found'))
    print('items: ', *args)
create_player('melon', 'poison',nickname='oleg', level=32, vip_status='vip')


def describe_person(*args, **kwargs):
    for name, age in kwargs.items():
        print(name,age)
    print('skills: ', *args)
describe_person('python developer','backend',name='German', age=18)

describe = {'name': 'German',
            'skills': 'python developer',
            'age': 18
            }

print(*describe)

def describe_person_two(**describe):
    for name, age in describe.items():
        print(name, age)
describe_person_two(**describe)

def hero_state(nickname, *skills, **clan):
    print('nickname:', nickname)
    for skill in skills:
        print('skills:', skill)

    for c in clan.items():
        print(*c)
hero_state('Mage', 'fireball', 'fire', clan='Dragons')