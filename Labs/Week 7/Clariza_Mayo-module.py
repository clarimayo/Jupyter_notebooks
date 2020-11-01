from random import randint

class GuessingColors:
    def __init__(self):
        self.max_guesses = 3
        self.guesses = 0
        self.colors = ["green", "blue", "white"]     
        
    @staticmethod    
    def welcome_message():
        print("Welcome to the Guessing colors' game!")
        
    def start(self):
        GuessingColors.welcome_message()
        win = self.handle_guess()
        if win:
            print(f"you won!")
        else:
            print(f"you lost")
               
    def handle_guess(self):
        random_index = randint(0, len(self.colors) - 1)
        random_color = self.colors[random_index]
        while self.guesses < self.max_guesses:
            user_guess = input("Take a guess of a color between 'green', 'blue', 'white': ")
            if random_color == user_guess:   
                  return True 
            self.guesses +=1
        return False
    
if __name__ == '__main__': #letting me call the name of file    
    new_game = GuessingColors()
    new_game.start()