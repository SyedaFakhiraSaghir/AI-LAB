# Imagine a game where two players, Max and Min, take turns picking coins from a row
# of numbers. Each player can only pick either the leftmost or rightmost coin from the
# remaining sequence.
# ● Max’s Goal: Collect coins with the highest total sum.
# ● Min’s Goal: Minimize Max’s total sum by making strategic choices.
# Since Max moves first, he wants to find the best sequence of picks that gives him the
# highest possible sum. This task uses the Alpha-Beta Pruning algorithm to optimize
# Max’s decision-making.
def max_turn(coins, left, right, alpha, beta, max_score, min_score):
  if left > right:
    return max_score, min_score, None  # Return None for best_pick when left > right

  # try picking left
  pick_left = coins[left]
  new_max, new_min, _ = min_turn(
      coins, left + 1, right, alpha, beta, max_score + pick_left, min_score, "left"
  )
  best_score = new_max
  best_pick = "left"

  # try picking right
  pick_right = coins[right]
  new_max2, new_min2, _ = min_turn(
      coins, left, right - 1, alpha, beta, max_score + pick_right, min_score, "right"
  )

  if new_max2 > best_score:
    best_score = new_max2
    best_pick = "right"
    new_max, new_min = new_max2, new_min2

  alpha = max(alpha, best_score)
  return new_max, new_min, best_pick


def min_turn(coins, left, right, alpha, beta, max_score, min_score, best_pick=None):
  if left > right:
    return max_score, min_score, best_pick  # Return best_pick as well

  # min just picks the smaller end
  if coins[left] <= coins[right]:
    new_max, new_min, _ = max_turn(
        coins, left + 1, right, alpha, beta, max_score, min_score + coins[left]
    )
    return new_max, new_min, best_pick  # Returning best_pick

  else:
    new_max, new_min, _ = max_turn(
        coins, left, right - 1, alpha, beta, max_score, min_score + coins[right]
    )
    return new_max, new_min, best_pick  # Returning best_pick

def play_game(coins):
  max_score = 0
  min_score = 0
  left = 0
  right = len(coins) - 1

  print(f"Initial Coins: {coins}")
  while left <= right:
    # max’s move
    _, _, move = max_turn(coins, left, right, float('-inf'), float('inf'), max_score, min_score)
    
    if move == 'left':
      picked = coins[left]
      left += 1
    else:
      picked = coins[right]
      right -= 1
    
    max_score += picked
    print(f"Max picks {picked}\n")
    print(f"Remaining Coins: {coins[left:right+1]}")

    if left <= right:
      # min’s move
      if coins[left] <= coins[right]:
        picked = coins[left]
        left += 1
      else:
        picked = coins[right]
        right -= 1
      
      min_score += picked
      print(f"Min picks {picked}\n")
      print(f"Remaining Coins: {coins[left:right+1]}")

  print(f"\nscores:\nMaximum {max_score}\nMinimum {min_score}")
  if max_score > min_score:
    print("Maximum Wins")
  elif max_score < min_score:
    print("Minimum wins")
  else:
    print("It's a tie!")

# run it
coins = [3, 9, 1, 2, 7, 5]
play_game(coins)
