Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))
if answer == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif answer == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong input")

print('Q2) When I’m dead, I want people to remember me as:')

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter answer (1-4): '))
if answer == 1:
  Hufflepuff = Hufflepuff + 2
elif answer == 2:
  Slytherin = Slytherin + 2
elif answer == 3:
  Ravenclaw = Ravenclaw + 2
elif answer == 4:
  Gryffindor = Gryffindor + 2
else:
  print("Wrong input")

print('Q3) Which kind of instrument most pleases your ear?')

print('  1) The Violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
  Slytherin = Slytherin + 3
elif answer == 2:
  Hufflepuff = Hufflepuff + 3
elif answer == 3:
  Ravenclaw = Ravenclaw + 3
elif answer == 4:
  Gryffindor = Gryffindor + 3
else:
  print("Wrong input")

print("Gryffindor", Gryffindor)
print("Ravenclaw", Ravenclaw)
print("Slytherin", Slytherin)
print("Huffle puff", Hufflepuff)