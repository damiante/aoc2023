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
                curr_score += 1

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

    # score = [x.score() for x in cards]

    copies = dict()
    copies[1] = 1


    for card in cards:
        # next_card_num = int(card.card_num) + 1
        # if not next_card_num in copies.keys():
        #     try:
        #         copies[next_card_num] = 1
        #     except IndexError:
        #         break

        curr_card_num = int(card.card_num)
        score = card.score()

        if curr_card_num not in copies.keys():
            copies[curr_card_num] = 1

        for j in range(copies[curr_card_num]):
            if score > 0:
                for i in range(score):

                    try:
                        copies[curr_card_num + 1 + i] += 1
                    except KeyError:
                        copies[curr_card_num + 1 + i] = 2

    card_count = 0

    for val in copies.values():
        card_count += val


    for card_num,l in copies.items():
        print(str(card_num) + ":" + str(l))

    print(card_count)    



    pass



if __name__ == "__main__":
    main()