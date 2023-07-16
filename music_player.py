import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("400x150")

        # Initialize pygame mixer
        pygame.mixer.init()

        # Create a label to display the current playing file
        self.current_file_label = tk.Label(self, text="No file loaded")
        self.current_file_label.pack(pady=10)

        # Create buttons
        self.load_button = tk.Button(self, text="Load", command=self.load_file)
        self.load_button.pack(pady=5)

        self.play_button = tk.Button(self, text="Play", command=self.play_music)
        self.play_button.pack(padx=5)

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

    def load_file(self):
        # Open a file dialog to choose a music file
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Music File",
                                               filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")))

        if file_path:
            # Update the current file label
            self.current_file_label["text"] = os.path.basename(file_path)

            # Load the selected music file
            pygame.mixer.music.load(file_path)

    def play_music(self):
        # Play the loaded music file
        pygame.mixer.music.play()

    def stop_music(self):
        # Stop the music playback
        pygame.mixer.music.stop()
        self.current_file_label["text"] = "No file loaded"


if __name__ == "__main__":
    app = MusicPlayerApp()
    app.mainloop()
