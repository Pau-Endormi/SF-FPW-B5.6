"""Игра «Крестики-нолики»
Размер поля: 3x3.
Пример печати поля в консоль:
_ 0 1 2
0 x x o
1 o x -
2 - o -
"""
def greet():
  print("---------x--o---------")
  print("Игра «Крестики-нолики»")
  print(" ввод: ширина и длина ")

def show_space(space):
  print("--------")
  print("_ 0 1 2 ")
  for i in range(3):
    for j in range(1):
      print(i, space[i][j], space[i][j+1], space[i][j+2])
  print("--------")

def request_coordinates():
  while True:
    coordinates = input("Введите координаты: ").split()
    if len(coordinates) != 2:
      print("Требуются 2 координаты!")
      continue
    
    width, depth = coordinates
    if not(width.isdigit()) or not(depth.isdigit()):
      print("Требуются числа!")
      continue
    
    width, depth = int(width), int(depth)
    if (0 > width) or (width > 2) or (0 > depth) or (depth > 2):
      print("Требуется диапазон от 0 до 2!")
      continue

    if space[depth][width] != "-":
      print("Ход на указанной клетке был уже произведён!")
      continue
    
    return width, depth

def check_win():
  # check horizontal
  for i in range(3):
    symbols = []
    for j in range(3):
      symbols.append(space[i][j])
    if symbols == ["x", "x", "x"]:
      print("Выиграл «крестик»!")
      return True
    elif symbols == ["o", "o", "o"]:
      print("Выиграл «нолик»!")
      return True

  # check vertical
  for i in range(3):
    symbols = []
    for j in range(3):
      symbols.append(space[j][i])
    if symbols == ["x", "x", "x"]:
      print("Выиграл «крестик»!")
      return True
    elif symbols == ["o", "o", "o"]:
      print("Выиграл «нолик»!")
      return True
  
  # check diagonal
  symbols = []
  for i in range(3):
    symbols.append(space[i][i])
  if symbols == ["x", "x", "x"]:
    print("Выиграл «крестик»!")
    return True
  elif symbols == ["o", "o", "o"]:
    print("Выиграл «нолик»!")
    return True
  
  # check diagonal
  symbols = []
  for i in range(3):
    symbols.append(space[i][2-i])
  if symbols == ["x", "x", "x"]:
    print("Выиграл «крестик»!")
    return True
  elif symbols == ["o", "o", "o"]:
    print("Выиграл «нолик»!")
    return True

  return False

greet()
space = [["-"] * 3 for i in range(3)]
count = 0
while True:
  count += 1
  show_space(space)
  if count % 2 == 1:
    print(f"Ход {count}. Ходит «крестик»!")
  else:
    print(f"Ход {count}. Ходит «нолик»!")
  
  width, depth = request_coordinates()
  
  # write simbol
  if count % 2 == 1:
    space[depth][width] = "x"
  else:
    space[depth][width] = "o"
  
  if check_win():
    show_space(space)
    print("конец игры...")
    break
  
  # all cells are filled
  if count == 9:
    show_space(space)
    print("Ничья!")
    break

