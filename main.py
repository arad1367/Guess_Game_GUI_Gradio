import random
import gradio as gr

# Game constants
LIVES = 5
BOUND = 100
IS_CONTINUE = True
COMPUTER_RANDOM_NUMBER = random.randint(1, BOUND)

def play_guess_game(user_name, user_guess):
    global LIVES, IS_CONTINUE, COMPUTER_RANDOM_NUMBER

    # Initialize game result
    game_result = ""

    if IS_CONTINUE:
        try:
            user_guess = int(user_guess)
            if user_guess == COMPUTER_RANDOM_NUMBER:
                game_result = f"You win! Congratulations, {user_name}! You saved {LIVES} lives."
                IS_CONTINUE = False
            else:
                LIVES -= 1
                if LIVES == 0:
                    game_result = f"Sorry! Game Over, {user_name}! You have 0 lives left. Correct guess was {COMPUTER_RANDOM_NUMBER}."
                    IS_CONTINUE = False
                elif user_guess > COMPUTER_RANDOM_NUMBER:
                    game_result = f"Oops! You have {LIVES} Lives left, {user_name}. Guess smaller number :)"
                else:
                    game_result = f"Oops! You have {LIVES} Lives left, {user_name}. Guess bigger number :)"
        except ValueError:
            game_result = "Invalid input! Please enter a number."
    else:
        # Reset game variables for a new game
        LIVES = 5
        IS_CONTINUE = True
        COMPUTER_RANDOM_NUMBER = random.randint(1, BOUND)
        game_result = "Game has restarted. Please enter your name to start a new game."

    return game_result

# Gradio GUI
iface = gr.Interface(
    fn=play_guess_game, 
    inputs=["text", "text"],
    outputs="text",
    title="Guess Game",
    description="Welcome to the Guess Game! Enter your name and your guess to start playing."
)

iface.launch(share=True)  # Launch the interface on web
