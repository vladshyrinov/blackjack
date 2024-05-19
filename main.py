from logo import logo
import random

ACE = 11
cards = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def choose_card():
    return random.choice(cards)

def replace_ace(cards):
    ace_index = cards.index(ACE)
    cards[ace_index] = 1

def collect_pc_cards(pc_cards, my_cards):
    if sum(my_cards) <= 21:
        while sum(pc_cards) < sum(my_cards):
            pc_cards.append(choose_card())
            if sum(pc_cards) > 21 and ACE in pc_cards:
                replace_ace(pc_cards)
    else:
        pc_cards.append(choose_card())


def show_my_cards(cards, is_final):
    if is_final:
        print(f'Your final hand: {cards}, final score: {sum(cards)}')
    else:
        print(f'Your cards: {cards}, current score {sum(cards)}')

def show_pc_cards(cards):
    if len(cards) == 1:
        print(f'Computer\'s first card: {cards[0]}')
    else:
        print(f'Computer\'s final hand: {cards}, final score: {sum(cards)}')

def show_game_result(my_cards, pc_cards):
    my_cards_sum = sum(my_cards)
    pc_cards_sum = sum(pc_cards)

    show_my_cards(my_cards, True)
    show_pc_cards(pc_cards)

    if my_cards_sum > 21:
        print('You went over. You lose 😤')
    elif pc_cards_sum > 21:
        print('Opponent went over. You win 😁')
    elif my_cards_sum > pc_cards_sum:
        if my_cards_sum == 21:
            print('You win with Blackjack 😃')
        else:
            print('You win 😃')
    elif my_cards_sum < pc_cards_sum:
        if pc_cards_sum == 21:
            print('Lose, opponent has Blackjack 😱')
        else:
            print('You lose 😤')
    else:
        print("Draw 🙃")

def start_game():
    my_cards = [choose_card(), choose_card()]
    pc_cards = [choose_card()]
    is_game_running = True

    while is_game_running:
        show_my_cards(my_cards, False)
        show_pc_cards(pc_cards)

        is_take_more_cards = input('Type \'y\' to get another card, type \'n\' to pass: ')

        if is_take_more_cards.lower() == 'y':
            my_cards.append(choose_card())
            if sum(my_cards) > 21:
                if ACE in my_cards:
                    replace_ace(my_cards)
                else:
                    collect_pc_cards(pc_cards, my_cards)
                    is_game_running = False
        else:
            collect_pc_cards(pc_cards, my_cards)
            is_game_running = False

        if not is_game_running:
            show_game_result(my_cards, pc_cards)

def run_games():
    is_run_games = True

    while is_run_games:
        start_game()
        play_blackjack = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
        if play_blackjack.lower() != 'y':
            is_run_games = False

def main():
    print(logo)
    run_games()


if __name__ == "__main__":
    main()
