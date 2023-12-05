#!/usr/bin/python3


class Card():
    def __init__(self, card_num, winners, vals):
        self.card_num = card_num
        self.winners = winners
        self.vals = vals

    def __repr__(self):
        return f"<card_num={self.card_num},winners={self.winners},vals={self.vals}"
    

    def score(self):
        curr_score = 0
        for winner in self.winners:
            if winner in self.vals:
                if curr_score == 0:
                    curr_score = 1
                else:
                    curr_score *= 2

        return curr_score

def parse_line(line):
    card, rest = line.split(":")

    card_num = card.split(" ")[-1]

    winners, vals = rest.split("|")

    winners = winners.strip().split(" ")
    winners = [x for x in winners if bool(x)]

    vals = vals.strip().split(" ")
    vals = [x for x in vals if bool(x)]

    return Card(card_num, winners, vals)


def main():

    cards = []

    with open("./input", "r") as f:
        for line in f:
            cards.append(parse_line(line))

    score = [x.score() for x in cards]

    print(sum(score))



    pass



if __name__ == "__main__":
    main()