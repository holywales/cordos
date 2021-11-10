from tkinter import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from tkinter import filedialog
from pathlib import Path
import os.path
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

# from testy2 import dsong
# from VoiceAssistant import dsong

from test3 import LoadSong


root = Tk()
root.title('Johnson MP3 Player')
root.iconbitmap('./images/aurora.ico')
root.geometry("500x400")

# Initialize Pygame Mixer
pygame.mixer.init()

# Song directory
music_dir = r"C:\Users\Lamour\Music"


# grab song length and time info
def play_time():
    # check for double timing
    if stopped:
        return
    # Grab current song elapsed time
    current_time = pygame.mixer.music.get_pos() /1000

    # throw up temp label to get data
    # slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')

    # convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    
    # Get the current song tuple number
    # current_song = song_box.curselection()
    song = song_box.get(ACTIVE)

    # add directory structure to song
    song = reconsong(song)    

    # get song with mutagen
    song_mut =MP3(song)
    # get song length
    global song_length
    song_length = song_mut.info.length

    # convert to time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))    

    # increase current time by 1 second
    current_time +=1

    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length} of {converted_song_length}  ') 
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        # slider hasn't been moved
        # update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))        
    else:
        #slider has moved
        # update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        
        # convert to time format
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))        
        
        # output time to status bar
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')        
    
        # move this thing along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)


    # output time to status bar
    # status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')

    # update slide position value to current song position
    # my_slider.config(value=int(current_time))




    # update time
    status_bar.after(1000, play_time)

# add song fucntion from ai
def ai_add_song(song):
    # set global stopped variable to false so song can play
    global stopped
    stopped = False

    # Reset slider and stautus bar
    status_bar.config(text='')
    my_slider.config(value=0)    

    # strip out the directory info and .mp3 extension from the song path
    song = Path(song).stem

    # Add song to listbox
    song_box.insert(END,song)

    # song = reconsong(song)

    # pygame.mixer.music.load(song)
    # pygame.mixer.music.play(loops=0)




# Add Song function
def add_song():
    song = filedialog.askopenfilename(initialdir=r"C:\Users\Lamour\Music", title="Choose A song", filetypes=(("mp3 Files","*.mp3"),))
    # song = filedialog.askopenfilename(initialdir=r"C:\Users\Lamour\Music", title="Choose A song", filetypes=(("mp3 Files","*.mp3"),("wav Files","*.wav")))
    
    # strip out the directory info and .mp3 extension from the song path
    song = Path(song).stem

    # Add song to listbox
    song_box.insert(END,song)



# Add many song to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=r"C:\Users\Lamour\Music", title="Choose A song", filetypes=(("mp3 Files","*.mp3"),))
    # songs = filedialog.askopenfilenames(initialdir=r"C:\Users\Lamour\Music", title="Choose A song", filetypes=(("mp3 Files","*.mp3"),("wav Files","*.wav")))    

    # Loop through song list and replace directory info
    for song in songs:
        song = Path(song).stem
        # Insert songs to playlist
        song_box.insert(END,song)        

def reconsong(song):
    song = song+".mp3"
    resong = ""
    for root, dirs, files in os.walk(music_dir):
        for file in files:
            if file.endswith(".mp3"):
                name = os.path.join(root, file)
                if song in name:
                    resong = name
    return resong


def insert_song(song):
    song_box.insert(END,song)

# Play selected song
def play():
    # set global stopped variable to false so song can play
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = reconsong(song)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call the play_tim function to get song length
    play_time()

    # update slider to position
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)

    # get current volume
    current_volume = pygame.mixer.music.get_volume()
    # Times by 100 to make it easier to work with
    current_volume = current_volume * 100

    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <=25:
        volume_meter.config(image=vol1)    
    elif int(current_volume) > 25 and int(current_volume) <=50:
        volume_meter.config(image=vol2)  
    elif int(current_volume) > 50 and int(current_volume) <=75:
        volume_meter.config(image=vol3)  
    elif int(current_volume) > 75 and int(current_volume) <=100:
        volume_meter.config(image=vol4) 


# Stop playing current song
global stopped
stopped = False
def stop():
    # Reset slider and stautus bar
    status_bar.config(text='')
    my_slider.config(value=0)
    # stop song from playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # Clear the status bar
    status_bar.config(text='')

    # set sop variable to true
    global stopped
    stopped = True

# Play the next song in playlist
def next_song():
    # Reset slider and stautus bar
    status_bar.config(text='')
    my_slider.config(value=0)

    # get the number of song in playlist
    songlen = song_box.size()
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current tuple number
    next_one = next_one[0]+1
    # if the next song is not the last song run else do nothin
    if next_one<songlen:
        # Grab song title from playlist
        song = song_box.get(next_one)
        # add directory structure to song
        song = reconsong(song)
        # load and play song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Clear active bar in playlsit listbox
        song_box.selection_clear(0,END)

        # Activate new song bar
        song_box.activate(next_one)

        # st active bar to next song
        song_box.selection_set(next_one,last=None)

# Plat previous song in playlist
def previous_song():
    # Reset slider and stautus bar
    status_bar.config(text='')
    my_slider.config(value=0)

    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current tuple number
    next_one = next_one[0]-1
    if next_one>-1:
        # Grab song title from playlist
        song = song_box.get(next_one)
        # add directory structure to song
        song = reconsong(song)
        # load and play song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Clear active bar in playlsit listbox
        song_box.selection_clear(0,END)

        # Activate new song bar
        song_box.activate(next_one)

        # st active bar to next song
        song_box.selection_set(next_one,last=None)

# Delete a song
def delete_song():
    stop()
    # delete curently selected song
    song_box.delete(ANCHOR)
    # stop music if it's playing
    pygame.mixer.music.stop()

# Delete All songs from playlist
def delete_all_songs():
    stop()
    # delete curently selected song
    song_box.delete(0,END)
    # stop music if it's playing
    pygame.mixer.music.stop()


# Create Global pause
global paused
paused = False

# Pause and Unpause the current song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

# create slider function
def slide(x):
    # slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')    
    song = song_box.get(ACTIVE)
    song = reconsong(song)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))    


def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())

    # get current volume
    current_volume = pygame.mixer.music.get_volume()
    # Times by 100 to make it easier to work with
    current_volume = current_volume * 100

    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <=25:
        volume_meter.config(image=vol1)    
    elif int(current_volume) > 25 and int(current_volume) <=50:
        volume_meter.config(image=vol2)  
    elif int(current_volume) > 50 and int(current_volume) <=75:
        volume_meter.config(image=vol3)  
    elif int(current_volume) > 75 and int(current_volume) <=100:
        volume_meter.config(image=vol4)                          



# create Master frame
master_frame = Frame(root)
master_frame.pack(pady=20)

#  Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.grid(row=0, column=0)

def to_raw(string):
    return fr"{string}"

# a = 'hello\nbobby\nsally\n'
# a.encode('unicode-escape').decode().replace('\\\\', '\\')
# print(a)

# print(r"{}".format(LoadSong))
# print(to_raw(LoadSong))




# Define Player Control Buttons Images
back_btn_img = PhotoImage(file='./images/back50.png')
forward_btn_img = PhotoImage(file='./images/forward50.png')
play_btn_img = PhotoImage(file='./images/play50.png')
pause_btn_img = PhotoImage(file='./images/pause50.png')
stop_btn_img = PhotoImage(file='./images/stop50.png')


# defne volume control images
global vol0
global vol1
global vol2
global vol3
global vol4

vol0 = PhotoImage(file='./images/volume0.png')
vol1 = PhotoImage(file='./images/volume1.png')
vol2 = PhotoImage(file='./images/volume2.png')
vol3 = PhotoImage(file='./images/volume3.png')
vol4 = PhotoImage(file='./images/volume4.png')

# Cretae Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# create volume meter
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)

# create volume label frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=30)

#  Create Player Control Buttons
back_button =  Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img , borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0,column=0, padx=10)
forward_button.grid(row=0,column=1, padx=10)
play_button.grid(row=0,column=2, padx=10)
pause_button.grid(row=0,column=3, padx=10)
stop_button.grid(row=0,column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#  Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

# Add Many Songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# cretae Delete song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song from Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs from Playlist", command=delete_all_songs)

# Create status bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# create music position slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

# crevoeate volume slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

# create slider label
# slider_label = Label(root, text="0")
# slider_label.pack(pady=10)

# play song from voice assistant
def play_song(song):
    # set global stopped variable to false so song can play
    global stopped
    stopped = False

    # song = reconsong(song)
    print(song)

    # strip out the directory info and .mp3 extension from the song path
    song = Path(song).stem

    # Add song to listbox
    song_box.insert(END,song)

    # pygame.mixer.music.load(song)
    # pygame.mixer.music.play(loops=0)

    # # Call the play_tim function to get song length
    # play_time()

    # # update slider to position
    # # slider_position = int(song_length)
    # # my_slider.config(to=slider_position, value=0)

    # # get current volume
    # current_volume = pygame.mixer.music.get_volume()
    # # Times by 100 to make it easier to work with
    # current_volume = current_volume * 100

    # if int(current_volume) < 1:
    #     volume_meter.config(image=vol0)
    # elif int(current_volume) > 0 and int(current_volume) <=25:
    #     volume_meter.config(image=vol1)    
    # elif int(current_volume) > 25 and int(current_volume) <=50:
    #     volume_meter.config(image=vol2)  
    # elif int(current_volume) > 50 and int(current_volume) <=75:
    #     volume_meter.config(image=vol3)  
    # elif int(current_volume) > 75 and int(current_volume) <=100:
    #     volume_meter.config(image=vol4) 

# play song from ai
def play_the_song():
    song = song_box.select_set(0)
    # song = reconsong(song)
    play()
    
if LoadSong != "":
    print("mp3" + LoadSong)
    # LoadSong = r"{}".format(LoadSong)
    # song = r"{}".format(LoadSong)
    # song =to_raw(LoadSong)
    # raw_string = r"{}".format(string)
    # strip out the directory info and .mp3 extension from the song path
    song = Path(LoadSong).stem

    # Add song to listbox
    insert_song(song)
    play_the_song()

root.mainloop()

# from VoiceAssistant import dsong
# if dsong != "":
#     print("mp3 "+dsong)
#     ai_add_song(dsong)    