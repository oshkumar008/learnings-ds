import tkinter as tk
import pygame
from PIL import Image, ImageTk
from tkinter import ttk, filedialog, Frame, Label
r = tk.Tk()
#Get the current screen width and height
screen_width = int(r.winfo_screenwidth()/2)
screen_height = int(r.winfo_screenheight()/2)
top = screen_width//2
left = screen_height//2
r.title('Counting Seconds')
r.geometry(f"{screen_width}x{screen_height}+{top}+{left}")
r.configure(bg='#856ff8')
button = tk.Button(r, text='Stop click', width=25,height=1, background="red", foreground="yellow", command=r.destroy)
button.pack()
r.mainloop()


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("600x200+400+200")
        self.playlist = []
        self.current_index = 0

        pygame.mixer.init()

        self.create_ui()

    def create_ui(self):
        self.song_label = tk.Label(self.root, text="Select a song")
        self.song_label.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load Song", command=self.load_song)
        self.load_button.config(fg="red", bg="blue")
        self.load_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()
        self.play_button["state"] = "disabled"

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack()
        self.pause_button["state"] = "disabled"

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()
        self.stop_button["state"] = "disabled"

    def load_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])

        if file_path:
            self.playlist.append(file_path)
            self.song_label.config(text=file_path.split("/")[-1])
            if len(self.playlist) == 1:
                self.play_button["state"] = "active"
                self.pause_button["state"] = "active"
                self.stop_button["state"] = "active"

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.song_label.config(text="Now Playing: " + self.playlist[self.current_index])

    def pause(self):
        pygame.mixer.music.pause()
        self.song_label.config(text="Paused: " + self.playlist[self.current_index])

    def stop(self):
        pygame.mixer.music.stop()
        self.song_label.config(text="Stopped")
        self.current_index = 0

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Frame.Style().configure("TFrame", background="#333")

        bard = Image.open("img.png")
        bardejov = ImageTk.PhotoImage(bard)
        label1 = tk.Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)

        rot = Image.open("img.png")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = tk.Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)

        minc = Image.open("img.png")
        mincol = ImageTk.PhotoImage(minc)
        label3 = tk.Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()