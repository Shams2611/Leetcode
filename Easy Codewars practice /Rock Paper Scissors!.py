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