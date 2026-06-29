


#Task-1
import random
import math

def strength(x):
  finalStrength = math.log2(x + 1) + (x / 10)   #Strength calculation.
  return finalStrength

def utility(maxV, minV):
  randomval = random.randint(1, 10)
  i = random.randint(0, 1)
  return strength(maxV) - strength(minV) + (((-1) ** i) * (randomval/10))     #Utility calculation.

def minimax(maxV, minV, depth, alpha, beta, maximizingPlayer):
  if depth == 0:                    #Base case
    return utility(maxV, minV)

  if maximizingPlayer:          # MAX's turn
    maxEval = float('-inf')
    for branchingFactor in range(2):
      eval = minimax(maxV, minV, depth - 1, alpha, beta, False)  # Recursively call minimax for MIN
      maxEval = max(maxEval, eval)   # Choose the maximum value
      alpha = max(alpha, eval)  # Update alpha
      if beta <= alpha:    # Alpha-beta pruning condition
        break
    return maxEval
  else:                      # MIN's turn (opponent's move)
    minEval = float('inf')
    for branchingFactor in range(2):
      eval = minimax(maxV, minV, depth - 1, alpha, beta, True)  # Recursively call minimax for MAX
      minEval = min(minEval, eval)  # Choose the minimum value
      beta = min(beta, eval)  # Update beta
      if beta <= alpha:  # Alpha-beta pruning condition
        break
    return minEval

inputs1 = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
baseStrength_Carlsen = float(input("Enter base strength for Carlsen: "))
baseStrength_Caruana = float(input("Enter base strength for Caruana: "))

Carlsen = 0
Caruana = 0
draw = 0

for gamenum in range(1, 5):
  if (gamenum % 2 == 1 and inputs1 == 0) or (gamenum % 2 == 0 and inputs1 == 1):
    maxV = baseStrength_Carlsen    # Carlsen plays as MAX
    minV = baseStrength_Caruana    # Caruana plays as MIN
    max_name = "Magnus Carlsen"
    min_name = "Fabiano Caruana"
    maximizingPlayer = True
  else:
    maxV = baseStrength_Caruana    # Caruana plays as MAX
    minV = baseStrength_Carlsen    # Carlsen plays as MIN
    max_name = "Fabiano Caruana"
    min_name = "Magnus Carlsen"
    maximizingPlayer = True

  alpha = float('-inf')
  beta = float('inf')
  utility_val = minimax(maxV, minV, 5, alpha, beta, maximizingPlayer)

  if utility_val > 0:
    winner = max_name
    if maximizingPlayer:
      gameGoal = "Max"
    else:
      gameGoal = "Min"
    if max_name == "Magnus Carlsen":
      Carlsen += 1
    else:
      Caruana += 1

  elif utility_val < 0:
    winner = min_name
    if maximizingPlayer:
      gameGoal = "Min"
    else:
      gameGoal = "Max"
    if min_name == "Magnus Carlsen":
      Carlsen += 1
    else:
      Caruana += 1
  else:
    winner = "Draw"
    gameGoal = "Draw"
    draw += 1

  print(f"Game {gamenum} Winner: {winner} ({gameGoal}) (Utility value: {utility_val:.2f})")

print("Overall Results:")
print(f"Magnus Carlsen Wins: {Carlsen}")
print(f"Fabiano Caruana Wins: {Caruana}")
print(f"Draws: {draw}")

if Carlsen > Caruana:
    print("Overall Winner: Magnus Carlsen")
elif Caruana > Carlsen:
    print("Overall Winner: Fabiano Caruana")
else:
    print("Overall Winner: Draw")

#Task-2 

def minimax(maxV, minV, depth, alpha, beta, maximizingPlayer, withMindControl):
  if depth == 0:   #Base case
    return utility(maxV, minV)

  if maximizingPlayer:     # MAX's turn
    maxEval = float('-inf')
    for branchingFactor in range(2):
      eval = minimax(maxV, minV, depth - 1, alpha, beta, False,  withMindControl)
      maxEval = max(maxEval, eval)  # Choose the maximum value
      alpha = max(alpha, eval) # Update alpha value
      if beta <= alpha:    # Alpha-beta pruning condition
        break
    return maxEval
  else:                  # MIN's turn
    if withMindControl:
      badMove = float('-inf')  # Track the worst move for MIN (best for MAX)
      for branchingFactor in range(2):
        eval = minimax(maxV, minV, depth - 1, alpha, beta, True, withMindControl)
        badMove = max(badMove, eval)  # MIN picks the worst move (best for MAX)
      return badMove  # Return worst move (best for MAX)
    else:
      minEval = float('inf')
      for branchingFactor in range(2):
        eval = minimax(maxV, minV, depth - 1, alpha, beta, True, withMindControl)
        minEval = min(minEval, eval)  # Choose the minimum value
        beta = min(beta, eval)  # Update beta value
        if beta <= alpha:   # Alpha-beta pruning condition
          break
      return minEval

inputs2 = int(input("Enter who goes first (0 for Light, 1 for L): "))
cost_c = float(input("Enter the cost of using Mind Control: "))
baseStrength_Light = float(input("Enter base strength for Light: "))
baseStrength_L = float(input("Enter base strength for L: "))

if inputs2 == 0:
    maxV = baseStrength_Light
    minV = baseStrength_L
    max_name = "Light"
    min_name = "L"
    maximizingPlayer = True              # Light is MAX
else:
    maxV = baseStrength_L
    minV = baseStrength_Light
    max_name = "L"
    min_name = "Light"
    maximizingPlayer = True              # L is MAX

alpha = float('-inf')
beta = float('inf')

utility_without_mind_control = minimax(maxV, minV, 5, alpha, beta, True, False)   # Without Mind Control
utility_with_mind_control = minimax(maxV, minV, 5, alpha, beta, True, True)    # With Mind Control
utility_with_mind_control_cost = utility_with_mind_control - cost_c  # Deduct cost from utility

print(f"Minimax value without Mind Control: {utility_without_mind_control:.2f}")
print(f"Minimax value with Mind Control: {utility_with_mind_control:.2f}")
print(f"Minimax value with Mind Control after incurring the cost: {utility_with_mind_control_cost:.2f}")

if utility_with_mind_control_cost > utility_without_mind_control:
    print("Light should use Mind Control.")
else:
    print("Light should NOT use Mind Control as the position is already winning.")