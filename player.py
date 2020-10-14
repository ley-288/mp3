from tkinter import *
from tkinter import filedialog
import pygame

root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

#initialize pygame
pygame.mixer.init()

#function to add one song
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    #strip directory strucure and .mp3 from title
    song = song.replace("/Users/leytonnightingale/Documents/VisualStudioCode/mp3/audio/", "")
    song = song.replace(".mp3", "")

    playlist_box.insert(END, song)


#function to add many songs
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    #loop through songlist and replace structure and mp3 from name
    for song in songs:
        #strip directory strucure and .mp3 from title
        song = song.replace("/Users/leytonnightingale/Documents/VisualStudioCode/mp3/audio/", "")
        song = song.replace(".mp3", "")
        #Add to end of playlist
        playlist_box.insert(END, song)

#Create delete single song function
def delete_song():
    playlist_box.delete(ANCHOR) #anchor = highlighted song in mp3 text box

#Create all songs function
def delete_all_songs():
    playlist_box.delete(0, END)


#Create play function
def play():
    song = playlist_box.get(ACTIVE)
    my_label.config(text=song)


#Create playlist box
playlist_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
playlist_box.pack(pady=20)

#Define button images
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png', command=play)
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

#Create buttons frame
control_frame = Frame(root)
control_frame.pack(pady=20)

#Create buttons
back_button = Button(control_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create add song dropdown
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
#add single song
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)
#add many songs
add_song_menu.add_command(label="Add Many Songs to Playlist", command=add_many_songs)

#Create delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a Song from Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs from Playlist", command=delete_all_songs)



#Temporary label
my_label = Label(root, text='')
my_label.pack(pady=20)


root.mainloop()