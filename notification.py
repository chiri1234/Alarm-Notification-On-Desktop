import pygame
import threading
import time
from plyer import notification
import tkinter as tk
# Declare display_time as a global variable
display_time = 0

def sound(duration):
    pygame.init()
    audio_file = r"C:\python virtual env\venv\cosy-prigida-main-version-02-58-17021.mp3"
    # r string should be created to delete all the empty space present in the path
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio_file)

    # Play the sound on channel 0
    channel = pygame.mixer.Channel(0)
    channel.play(sound, loops=-1)  # '-1' means to play the sound indefinitely, it will be playing repeatedly until having any interpretation
#  channel are like audo levels you have in video editing where their are different audio levels
    # Wait for the specified duration
    time.sleep(duration)

    # Stop the sound after the specified duration
    channel.stop()
    pygame.mixer.quit()
    pygame.quit()

def alarm():
    
    notification.notify(
        
        title="alarm",
        message="Your timer has completed",
        app_icon=r"C:\python virtual env\venv\alarm-bell_icon-icons.com_68596.ico",
        app_name="chirilarm",
        timeout=4
    )
  
# Ask for the sound duration and time to display on the desktop
sound_duration = int(input("Enter the duration you want your alarm to ring (in seconds): "))
display_time = int(input("Enter the time (in seconds) to display on the desktop: "))

# Create a thread for the timer
def update_time():
    global display_time
    time_str = f"Time left: {display_time} seconds"
    time_label.config(text=time_str)
# here time_label is being used to display text and image in the window and messages apart from that 
    if display_time > 0:
        display_time -= 1
        root.after(1000, update_time)
        # update_time is responsible for changing the time_label which works as a loop which goes continuously until it stop and escape for it and then it when 
        # execute sound and notification using thread.
# Update the time every 1000 milliseconds (1 second)

    else:
        sound_thread = threading.Thread(target=sound, args=(sound_duration,))
        sound_thread.start()
        notification_thread = threading.Thread(target=alarm)
        notification_thread.start()

root = tk.Tk()
# tinker module is responsible for the GUI in python 
root.attributes('-topmost', True)  # Make the tkinter window always on top
root.geometry('300x50+800+500')  # Set the window size and position on the screen

time_label = tk.Label(root, font=('Helvetica', 18))
time_label.pack()
update_time()
root.mainloop()
print("Your timer has completed")


