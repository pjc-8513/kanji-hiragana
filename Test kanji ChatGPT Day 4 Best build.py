import tkinter as tk
from random import shuffle, sample

class MatchingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Kanji Matching Game")

        # Read Kanji-Hiragana pairs from file
        self.kanji_hiragana_pairs = self.read_pairs_from_file("kanji_hiragana_pairs.txt")

        # Randomly select 8 pairs
        selected_pairs = sample(list(self.kanji_hiragana_pairs.items()), 8)
        self.selected_pairs = dict(selected_pairs)

        # Divide the window into two sections
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, padx=10)

        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(side=tk.RIGHT, padx=10)

        # Create shuffled lists of Kanji and Hiragana
        self.kanji_list = list(self.selected_pairs.keys())
        shuffle(self.kanji_list)

        self.hiragana_list = [self.selected_pairs[kanji] for kanji in self.kanji_list]
        shuffle(self.hiragana_list)

        # Assuming self.kanji_list and self.hiragana_list exist and contain at least 8 elements

        # Create Kanji buttons (limited to 8)
        self.kanji_buttons = []
        for i, kanji in enumerate(self.kanji_list):
            if i >= 8:  # Stop after creating 8 buttons
                break
            button = tk.Button(self.left_frame, text=kanji, command=lambda k=kanji: self.select_kanji(k), font=("Arial", 20))
            button.pack(pady=10, padx=20)
            self.kanji_buttons.append(button)

        # Create Hiragana buttons (limited to 8)
        self.hiragana_buttons = []
        for i, hiragana in enumerate(self.hiragana_list):
            if i >= 8:  # Stop after creating 8 buttons
                break
            button = tk.Button(self.right_frame, text=hiragana, command=lambda h=hiragana: self.select_hiragana(h), font=("Arial", 20))
            button.pack(pady=10, padx=20)
            self.hiragana_buttons.append(button)

        # Create a reset button
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack(side=tk.BOTTOM, pady=20)

        # Variables to keep track of selected Kanji and Hiragana
        self.selected_kanji = None
        self.selected_hiragana = None

    def read_pairs_from_file(self, filename):
        pairs = {}
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                kanji, hiragana = line.strip().split(",")
                pairs[kanji] = hiragana
        return pairs

    def select_kanji(self, kanji):
        self.selected_kanji = kanji
        self.check_match()

    def select_hiragana(self, hiragana):
        self.selected_hiragana = hiragana
        self.check_match()

    def check_match(self):
        if self.selected_kanji is not None and self.selected_hiragana is not None:
            pair = self.kanji_hiragana_pairs.get(self.selected_kanji)
            if pair == self.selected_hiragana:
                for button in self.kanji_buttons + self.hiragana_buttons:
                    if button["text"] == self.selected_kanji or button["text"] == self.selected_hiragana:
                        button.config(bg="green")
            self.selected_kanji = None
            self.selected_hiragana = None

    def reset_game(self):
        # Clear the left frame (containing Kanji buttons)
        for button in self.kanji_buttons:
            button.destroy()

        # Clear the right frame (containing Hiragana buttons)
        for button in self.hiragana_buttons:
            button.destroy()

        # Randomly select 8 pairs
        selected_pairs = sample(list(self.kanji_hiragana_pairs.items()), 8)
        self.selected_pairs = dict(selected_pairs)

        # Create shuffled lists of Kanji and Hiragana
        self.kanji_list = list(self.selected_pairs.keys())
        shuffle(self.kanji_list)

        self.hiragana_list = [self.selected_pairs[kanji] for kanji in self.kanji_list]
        shuffle(self.hiragana_list)

        # Assuming self.kanji_list and self.hiragana_list exist and contain at least 8 elements

        # Create Kanji buttons (limited to 8)
        self.kanji_buttons = []
        for i, kanji in enumerate(self.kanji_list):
            if i >= 8:  # Stop after creating 8 buttons
                break
            button = tk.Button(self.left_frame, text=kanji, command=lambda k=kanji: self.select_kanji(k), font=("Arial", 20))
            button.pack(pady=10, padx=20)
            self.kanji_buttons.append(button)

        # Create Hiragana buttons (limited to 8)
        self.hiragana_buttons = []
        for i, hiragana in enumerate(self.hiragana_list):
            if i >= 8:  # Stop after creating 8 buttons
                break
            button = tk.Button(self.right_frame, text=hiragana, command=lambda h=hiragana: self.select_hiragana(h), font=("Arial", 20))
            button.pack(pady=10, padx=20)
            self.hiragana_buttons.append(button)
        
        for button, kanji in zip(self.kanji_buttons, self.kanji_list):
            button.config(text=kanji, bg="SystemButtonFace")

        for button, hiragana in zip(self.hiragana_buttons, self.hiragana_list):
            button.config(text=hiragana, bg="SystemButtonFace")

            self.selected_kanji = None
            self.selected_hiragana = None

        # Reset matched pairs
        self.matched_pairs = set()

def main():
    root = tk.Tk()
    game = MatchingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
