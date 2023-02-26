import functools
import random
from typing import List
from connections import DOWN, LEFT, RIGHT, UP, Node, generateBoard, printBoard, getPossibilities

def collapsed(board: List[List[Node]]) -> bool:
  return functools.reduce(lambda x, y: x and y, [len(x) == 1 for x in board])

def contradicted(board: List[List[Node]]) -> bool:
  return functools.reduce(lambda x, y: x and y, [len(x) < 1 for x in board])

def valid(board: List[List[Node]]) -> bool:
  return functools.reduce(lambda x, y: x and y, [len(x) == 1 and x[0].code in [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] for x in board])

def choices(board: List[List[Node]]) -> List[int]:
  return [idx for idx, val in enumerate(board) if len(val) > 1]

def match(board: List[List[Node]], index: int, direction: int, code: int) -> List[Node]:
  results = []
  for node in board[index]:
    if code in node.Connections(direction):
      results.append(node)
  return results

def propagate(board: List[List[Node]], boardSize: int, index: int) -> List[List[Node]]:
  x = index % boardSize
  y = index // boardSize
  result = board
  idx = y * boardSize + x
  code = result[idx][0].code

  if x > 0:
    result[idx - 1] = match(result, idx - 1, RIGHT, code)
  if x < boardSize - 1:
    result[idx + 1] = match(result, idx + 1, LEFT, code)  
  if y > 0:
    result[idx - boardSize] = match(result, idx - boardSize, DOWN, code)
  if y < boardSize - 1:
    result[idx + boardSize] = match(result, idx + boardSize, UP, code)  
  return result

def collapse(board: List[List[Node]], boardSize: int) -> List[List[Node]]:
  if collapsed(board):
    return board

  if contradicted(board):
    raise RecursionError

  possibleIndex = choices(board)
  random.shuffle(possibleIndex)
  possibleIndex.sort(key=lambda x: len(board[x]))
  for idx in possibleIndex:
    possibleNodes = board[idx]
    random.shuffle(possibleNodes)
    for possibleNode in possibleNodes:
      try:
        result = board
        result[idx] = [possibleNode]
        return collapse(propagate(result, boardSize, idx), boardSize)
      except:
        continue

  return board

def invalidate(board: List[List[Node]], boardWidth: int, boardHeight: int) -> List[List[Node]]:
  result = board
  for idx in range(len(result)):
    x = idx % boardWidth
    y = idx // boardWidth
    if len(result[idx]) == 0 or len(result[idx]) == 1 and result[idx][0].code not in [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]:
      result[idx] = [Node(i) for i in getPossibilities(x, y, boardWidth, boardHeight)]
  for idx in range(len(result)):
    if len(board[idx]) == 1:
      result = propagate(result, boardWidth, idx)
  return result

boardWidth = 10
boardHeight = 10
result = collapse(generateBoard(boardWidth, boardHeight), boardWidth)
print("collapsed:", collapsed(result))
print("valid: ", valid(result))
print("contradicted: ", contradicted(result))
printBoard(result, boardWidth, boardHeight)
while not valid(result):
  result = collapse(invalidate(result, boardWidth, boardHeight), boardWidth)
  print("collapsed:", collapsed(result))
  print("valid: ", valid(result))
  print("contradicted: ", contradicted(result))
  printBoard(result, boardWidth, boardHeight)




