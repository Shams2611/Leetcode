def rps(p1, p2):
    outcomes = {
        ("scissors", "paper") : "Player 1 won!",
        ("rock", "scissors") : "Player 1 won!",
        ("paper", "rock") : "Player 1 won!"
    }
    
    if p1 == p2:
        return "Draw!"
    else:
        return outcomes.get((p1, p2), "Player 2 won!")

# very clever method 

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]