import random


class Hand:
    def __init__(self):
        """Start with an empty hand."""
        self.cards = []

    def add_card(self):
        """Deal one card into this hand."""
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards.append(random.choice(deck))

    def score(self):
        """Return the Blackjack score for this hand."""
        total = sum(self.cards)

        # Blackjack
        if total == 21 and len(self.cards) == 2:
            return 0

        # Convert aces from 11 to 1 when needed
        while total > 21 and 11 in self.cards:
            ace_index = self.cards.index(11)
            self.cards[ace_index] = 1
            total = sum(self.cards)

        return total


def compare(user_score, dealer_score):
    """Return the result of the game."""

    if user_score == dealer_score:
        return "Draw"

    if dealer_score == 0:
        return "You lose. Dealer has Blackjack."

    if user_score == 0:
        return "You win with Blackjack!"

    if user_score > 21:
        return "You went over. You lose."

    if dealer_score > 21:
        return "Dealer went over. You win!"

    if user_score > dealer_score:
        return "You win!"

    return "You lose."


def main():
    user_hand = Hand()
    dealer_hand = Hand()

    # Initial deal
    for _ in range(2):
        user_hand.add_card()
        dealer_hand.add_card()

    game_over = False

    while not game_over:
        user_score = user_hand.score()
        dealer_score = dealer_hand.score()

        print("\nYour cards:", user_hand.cards)
        print("Your score:", user_score)

        print("Dealer first card:", dealer_hand.cards[0])

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to hit, 'n' to stand: ").lower()

            if choice == "y":
                user_hand.add_card()
            else:
                game_over = True

    # Dealer draws to 17
    while dealer_hand.score() != 0 and dealer_hand.score() < 17:
        dealer_hand.add_card()

    user_score = user_hand.score()
    dealer_score = dealer_hand.score()

    print("\n===== FINAL RESULT =====")
    print("Your hand  :", user_hand.cards)
    print("Your score :", user_score)
    print("Dealer hand:", dealer_hand.cards)
    print("Dealer score:", dealer_score)

    print(compare(user_score, dealer_score))


if __name__ == "__main__":
    main()