
# generates all possible connections that are possible for a 2d grid of cells
import math
from typing import Dict, List

# Code UDLR
# 0000 -> None  (0)
EMPTY = 0
# 0001 -> Right (1)
RIGHT = 1
# 0010 -> Left  (2)
LEFT = 2
# 0100 -> Down  (4)
DOWN = 4
# 1000 -> Up    (8)
UP = 8

Connections = {
  RIGHT: [
    LEFT, 
    LEFT + RIGHT, 
    LEFT + UP, 
    LEFT + DOWN,
    LEFT + UP + DOWN,
    LEFT + UP + RIGHT,
    LEFT + DOWN + RIGHT,
    LEFT + UP + DOWN + RIGHT,
  ],
  LEFT: [
    RIGHT, 
    RIGHT + LEFT, 
    RIGHT + UP, 
    RIGHT + DOWN,
    RIGHT + UP + DOWN,
    RIGHT + UP + LEFT,
    RIGHT + DOWN + LEFT,
    RIGHT + UP + DOWN + LEFT,
  ],
  UP: [
    DOWN, 
    DOWN + UP, 
    DOWN + LEFT, 
    DOWN + RIGHT,
    DOWN + LEFT + UP, 
    DOWN + RIGHT + UP,
    DOWN + LEFT + RIGHT, 
    DOWN + LEFT + RIGHT + UP, 
  ],
  DOWN: [
    UP, 
    UP + DOWN, 
    UP + LEFT, 
    UP + RIGHT,
    UP + LEFT + DOWN, 
    UP + RIGHT + DOWN,
    UP + LEFT + RIGHT, 
    UP + LEFT + RIGHT + DOWN, 
  ],
}

def Unconnections(code: int) -> List[int]:
  return [x for x in range(16) if x not in Connections[code]];

class Node:
  def __init__(self, code):
    self.code = code
    self.connections = {
      RIGHT: Connections[RIGHT] if code & RIGHT != 0 else Unconnections(RIGHT), 
      LEFT: Connections[LEFT] if code & LEFT != 0 else Unconnections(LEFT), 
      DOWN: Connections[DOWN] if code & DOWN != 0 else Unconnections(DOWN), 
      UP: Connections[UP] if code & UP != 0 else Unconnections(UP)
    }

  def Connections(self, side: int) -> List[int]:
    result = []
    if side & RIGHT != 0:
      result.extend(self.connections[RIGHT])
    if side & LEFT != 0:
      result.extend(self.connections[LEFT])
    if side & DOWN != 0:
      result.extend(self.connections[DOWN])
    if side & UP != 0:
      result.extend(self.connections[UP])
    return result

def generateBoard(boardWidth: int, boardHeight: int) -> List[List[Node]]:
  result = []
  for index in range(boardWidth * boardHeight):
    x = index % boardWidth
    y = math.floor(index / boardWidth)
    if x == 0:
      if y == 0:
        result.append([1, 4, 5])
      elif y == boardHeight - 1:
        result.append([1, 8, 9])
      else:
        result.append([1, 4, 5, 8, 9, 12, 13])
    elif x == boardWidth - 1:
      if y == 0:
        result.append([2, 4, 6])
      elif y == boardHeight - 1:
        result.append([2, 8, 10])
      else:
        result.append([2, 4, 6, 8, 10, 12, 14])
    else:
      if y == 0:
        result.append([1, 2, 3, 4, 5, 6, 7])
      elif y == boardHeight - 1:
        result.append([1, 2, 3, 8, 9, 10, 11])
      else:
        result.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
  return [[Node(code) for code in possibilities] for possibilities in result]

def printSubCell(code: int, subRow: int):
  layout: Dict[int, List[str]] = {
    0: ['   ', '   ', '   '],
    1: ['╭──', '│██', '╰──'],
    2: ['──╮', '██│', '──╯'],
    3: ['───', '███', '───'],
    4: ['╭─╮', '│█│', '│█│'],
    5: ['╭──', '│██', '│█╭'],
    6: ['──╮', '██│', '╮█│'],
    7: ['───', '███', '╮█╭'],
    8: ['│█│', '│█│', '╰─╯'],
    9: ['│█╰', '│██', '╰──'],
    10: ['╯█│', '██│', '──╯'],
    11: ['╯█╰', '███', '───'],
    12: ['│█│', '│█│', '│█│'],
    13: ['│█╰', '│██', '│█╭'],
    14: ['╯█│', '██│', '╮█│'],
    15: ['╯█╰', '███', '╮█╭'],
  }
  print(layout[code][subRow], end='')

def printBoard(board: List[List[Node]], boardWidth: int, boardHeight: int):
  for y in range(boardHeight):
    for subRow in range(3):
      for x in range(boardWidth):
        val = board[y * boardWidth + x]
        if len(val) != 1:
          print('???', end='')
        else:
          printSubCell(val[0].code, subRow)
      print()

def printLengthBoard(board: List[List[Node]], boardWidth: int, boardHeight: int):
  for y in range(boardHeight):
    for x in range(boardWidth):
      val = board[y * boardWidth + x]
      if len(val) == 1:
        l = str(val[0].code).rjust(2, ' ') 
        print(f' {l} ', end = '')
      else:
        l = str(len(val)).rjust(2, ' ')
        print(f'#{l} ', end = '')
    print()
