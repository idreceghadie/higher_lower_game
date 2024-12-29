from art import logo
from art import vs
import random
from game_data import data

# choose a random dictionary entry from game_data and compare it to another
# change the random entry each time they get it right
print(logo)
current_score = 0

def score_ticker(answer):
    global current_score
    if answer:
        current_score += 1
    return current_score

def answer_check(user_answer,A,B):
    if (user_answer == 'A' and A['follower_count']>B['follower_count']) or (user_answer == 'B' and A['follower_count']<B['follower_count']):
        return f"You're right! Current score: {score_ticker(True)}"

    elif (user_answer == 'A' and A['follower_count']<B['follower_count']) or (user_answer == 'B' and A['follower_count']>B['follower_count']):
        return f"Sorry, that's wrong. Final score: {current_score}"

    else:
        print("Invalid input. Please enter 'A' or 'B'.")


A = random.choice(data)

B = random.choice(data)

# determining the correct guess

while True:
    print('Compare A:', A['name'] + ',', 'a', A['description'], 'from', A['country'] + '.')
    print(vs)
    print('Against B:', B['name'] + ',', 'a', B['description'], 'from', B['country'] + '.')
    user_answer = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

    result = answer_check(user_answer,A,B)
    print(result)

    if 'Final score' in result:
        break

    if A['follower_count'] < B['follower_count']:
        A = A
        B = random.choice(data)
    elif B['follower_count'] < A['follower_count']:
        A = B
        B = random.choice(data)









    # ask the user for an input about who has more instagram followers, A or B
# use the one w the lower number of followers for the next comparison, "A", if they get it right
# display score count if they get it right
# end the game if they choose wrong
# display final score when they lose
