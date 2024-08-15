import random
import customtkinter as ctk
import tkinter as tk

class HangmanGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hangman Game")
        self.geometry('800x600')  

        self.word = ""
        self.guessed_letters = set()
        self.attempts_left = 6
        self.game_over = False 

        self.create_widgets()
        self.bind_keys()
        self.new_game()

        # Fullscreen setup
        self.fullscreen = True
        self.bind('<F11>', self.toggle_fullscreen)  
        self.bind('<Escape>', self.exit_fullscreen)  

    def get_random_word(self):
        words = ['code', 'alpha', 'python', 'project', 'hangman', 'dog', 'elephant']
        return random.choice(words)
    
    def display_word(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def create_widgets(self):
        self.word_label = ctk.CTkLabel(self, text=self.display_word(), font=('Arial', 24))
        self.word_label.pack(pady=20)

        self.guess_entry = ctk.CTkEntry(self)
        self.guess_entry.pack(pady=10)
        
        self.guess_button = ctk.CTkButton(self, text="Submit", command=self.make_guess)
        self.guess_button.pack(pady=10)
        
        self.message_label = ctk.CTkLabel(self, text=f"Attempts left: {self.attempts_left}")
        self.message_label.pack(pady=20)
        
        self.hangman_canvas = ctk.CTkCanvas(self, bg='black')
        self.hangman_canvas.pack(fill='both', expand=True)
        
        self.restart_button = ctk.CTkButton(self, text="Restart Game", command=self.new_game)
        self.restart_button.pack(pady=10)

        self.draw_hangman()

    def bind_keys(self):
        self.bind('<Return>', lambda event: self.make_guess())

    def make_guess(self):
        if self.game_over:
            return  # Ignore guesses if the game is over

        guess = self.guess_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.configure(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.configure(text="You've already guessed that letter.")
            return

        self.guessed_letters.add(guess)
        self.guess_entry.delete(0, 'end')  # Clear the entry field

        if guess in self.word:
            self.message_label.configure(text="Good guess!")
        else:
            self.attempts_left -= 1
            self.message_label.configure(text=f"Wrong guess! Attempts left: {self.attempts_left}")
            self.draw_hangman()

        current_display = self.display_word()
        self.word_label.configure(text=current_display)

        if '_' not in current_display:
            self.message_label.configure(text="Congratulations! You've guessed the word!")
            self.guess_button.configure(state='disabled')
            self.show_confetti()  # Trigger confetti
            self.game_over = True  # End game
        elif self.attempts_left <= 0:
            self.message_label.configure(text=f"Game Over! The word was '{self.word}'")
            self.guess_button.configure(state='disabled')
            self.game_over = True  # End game

    def draw_hangman(self):
        self.hangman_canvas.delete('all')
        self.hangman_canvas.configure(bg='black')  

        width = self.hangman_canvas.winfo_width()
        height = self.hangman_canvas.winfo_height()

        if self.attempts_left <= 5:
            self.hangman_canvas.create_line(width * 0.2, height * 0.8, width * 0.8, height * 0.8, fill='white')  # Base
        if self.attempts_left <= 4:
            self.hangman_canvas.create_line(width * 0.5, height * 0.1, width * 0.5, height * 0.8, fill='white')  # Pole
        if self.attempts_left <= 3:
            self.hangman_canvas.create_line(width * 0.3, height * 0.1, width * 0.7, height * 0.1, fill='white')  # Top Bar
        if self.attempts_left <= 2:
            self.hangman_canvas.create_line(width * 0.5, height * 0.1, width * 0.5, height * 0.2, fill='white')  # Rope
        if self.attempts_left <= 1:
            self.hangman_canvas.create_oval(width * 0.47, height * 0.2, width * 0.53, height * 0.28, outline='white')  # Head
        if self.attempts_left == 0:
            self.hangman_canvas.create_line(width * 0.5, height * 0.28, width * 0.5, height * 0.4, fill='white')  # Body
            self.hangman_canvas.create_line(width * 0.4, height * 0.35, width * 0.5, height * 0.3, fill='white')  # Left Arm
            self.hangman_canvas.create_line(width * 0.6, height * 0.35, width * 0.5, height * 0.3, fill='white')  # Right Arm
            self.hangman_canvas.create_line(width * 0.4, height * 0.45, width * 0.5, height * 0.4, fill='white')  # Left Leg
            self.hangman_canvas.create_line(width * 0.6, height * 0.45, width * 0.5, height * 0.4, fill='white')  # Right Leg

    def new_game(self):
        self.word = self.get_random_word()
        self.guessed_letters = set()
        self.attempts_left = 6
        self.word_label.configure(text=self.display_word())
        self.message_label.configure(text=f"Attempts left: {self.attempts_left}")
        self.guess_button.configure(state='normal')
        self.game_over = False  # Reset game state
        self.draw_hangman()

    def show_confetti(self):
        colors = ['red', 'green', 'blue', 'yellow', 'purple']
        width = self.hangman_canvas.winfo_width()
        height = self.hangman_canvas.winfo_height()
        
        for _ in range(100):  # Number of confetti pieces
            x = random.randint(0, width)
            y = random.randint(0, height)
            color = random.choice(colors)
            self.hangman_canvas.create_oval(x, y, x+10, y+10, fill=color, outline=color)
        self.update_idletasks()  # Ensure all drawing is updated

    def toggle_fullscreen(self, event):
        self.fullscreen = not self.fullscreen
        self.attributes('-fullscreen', self.fullscreen)
        self.bind('<F11>', self.toggle_fullscreen)
        self.bind('<Escape>', self.exit_fullscreen)

    def exit_fullscreen(self, event):
        self.attributes('-fullscreen', False)
        self.geometry('800x600')  # Reset size when exiting fullscreen
        self.bind('<F11>', self.toggle_fullscreen)  # Bind F11 to toggle fullscreen

if __name__ == "__main__":
    app = HangmanGame()
    app.mainloop()
