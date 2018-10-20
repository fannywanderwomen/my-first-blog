print('Hello, Django girls!')
if 3 > 2:
    print('It works!')
if 5 > 2:
    print('5 est effectivement plus grand que 2')
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')
if 5 > 2:
    print('5 est effectivement plus grand que 2')
else:
    print("5 n'est pas plus grand que 2")
if 5 > 7:
    print('5 est effectivement plus grand que 7')
else:
    print("5 n'est pas plus grand que 7")
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
elif name == 'Fanny':
    print('Salut Fanny!')
else:
    print('Hey anonymous!')
def hi():
    print('Hi there!')
    print('How are you?')
hi()
def hi(name):
    if name == 'Fanny':
        print('Hi Fanny!')
    elif name == 'Ornella':
        print('Hi Ornella!')
    else:
        print('Hi anonymous!')
hi("Ornella")
hi("Rec")
def hi(name):
    print('Hi ' + name + '!')

hi("Fanny")
hi("Rec")
girls = ['Fanny', 'Ornella', 'Caro', 'Ninie', 'You']
def hi(name):
    print('Hi ' + name + '!')

girls =['Fanny', 'Ornella', 'Caro', 'Ninie', 'You']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1, 6):
    print(i)
