`main.py`
 - Run the game with 200 turns and 4 players
 - Options can be modified in this file

`test_probabilities.py`
 - Runs a game with one player and a million dice rolls
 - Prints the probabilities of ending a turn on each spot
 - Graphical representation (chart.js):
![](images/probability_distribution.png)


# Decisions
 - Buys a property that has been landed on when one of these two requirements is met:
    - Player has over £600
    - Player has over double the cost of the property
 - Building houses and hotels (check every turn):
    - Needs to be in a complete set (All cards in the set are owned by this player)
    - If the property has 0 houses,
        - Build 3 houses or fewer if there are less left in the bank and the player will have at least £200 left after building
    - If the property has houses,
        - Build a hotel if there's one in the bank and the player will have at least £200 left after building
 - If the player is in jail, they will always use any existing get out of jail free cards first
    - If the player doesn't have any, but the player has over $150, the player will pay $50 to get out of jail
    - Otherwise, the player will wait out the three turns

# TBD
 - Add chance cards: `street repairs`, `general repairs`, `birthday`
 - Trading?
