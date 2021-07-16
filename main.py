# import models
import art
import game_data
import random

#To pick up a person from game_data.data
def pick_up():
  info = game_data.data[random.randint(0, 49)]
  return info
  # print(info)
  
# Define the Main function
def game():
    print(art.logo)
    person_a = pick_up()
    print(f"Compare A: {person_a['name']}, {person_a['description']}, from {person_a['country']}")
    print(art.vs)
    person_b = pick_up()
    print(f"Against B: {person_b['name']}, {person_b['description']}, from {person_b['country']}")

    is_correct = True
    while is_correct:
        choice = input("Who has more followers? Type 'A' or 'B':")
        score = 0
        if choice == 'A' and person_a['follower_count'] > person_b['follower_count']:
            score += 1
            print(f"Yes, that's right. Your score: {score}")
        elif choice == 'B' and person_a['follower_count'] < person_b['follower_count']:
            score += 1
            print(f"Yes, that's right. Your score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_correct = False




# Run the main function
game()