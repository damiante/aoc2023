#!/usr/bin/python3

from functools import cmp_to_key

HAND_RANKS = (
    [5],       # Five-of-a-kind
    [4, 1],         # Four-of-a-kind
    [3, 2],         # Full House
    [3, 1, 1],      # Three-of-a-kind
    [2, 2, 1],      # Two-pair
    [2, 1, 1, 1],    # One-pair
    [1, 1, 1, 1, 1] # High-card
)

CARD_ORDER = (
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2"
)


def identify_rank_pattern(hand):
    unique_cards = dict()

    for card in hand:
        try:
            unique_cards[card] += 1
        except KeyError:
            unique_cards[card] = 1
    
    
    return [x for x in sorted(unique_cards.values(), reverse=True)]

# return 1 if hand1 is better than hand2, -1 if hand2 is better, and 0 if they are the same
def better_hand(hand1, hand2):
    rank1_pattern, rank2_pattern = identify_rank_pattern(hand1), identify_rank_pattern(hand2)



    for i in range(len(HAND_RANKS)):
        if HAND_RANKS[i] == rank1_pattern:
            rank1 = i
        if HAND_RANKS[i] == rank2_pattern:
            rank2 = i

    
    if rank1 > rank2:
        return -1
    elif rank2 > rank1:
        return 1

    
    for curr_card1, curr_card2 in zip(hand1, hand2):
        if curr_card1 == curr_card2:
            continue

        for card in CARD_ORDER:
            if card == curr_card1:
                return 1
            elif card == curr_card2: 
                return -1

    return 0




def main():

    game = []
    
    with open("./input", "r") as f:
        for line in f:
            hand, bid = line.split(" ")
            game.append([hand, int(bid)])


    game = sorted(game, key=cmp_to_key(lambda x,y: better_hand(x[0], y[0])))



    total_winnings = 0

    for i in range(len(game)):
        total_winnings += game[i][1] * (i + 1)

    print(total_winnings)
    




if __name__ == "__main__":
    main()