#Brandon Jarvis, 2024

from pytube import YouTube
import os
import customtkinter

#Sets the download directory to the user's downloads folder (by default)
downloadDirectory = os.path.join(os.path.expanduser("~"), "Downloads")

def downloadVideo():
    """
    Downloads the video given the link in the entry box and saves it to the download directory (by default the user's downloads folder). Saves as mp4 file
    """
    try:
        yt = YouTube(linkEntry.get())
        video = yt.streams.get_highest_resolution()
        video.download(downloadDirectory)
        print("Download complete!")
        downloadedLabel.configure(text="Download complete! ", text_color="green")
    except:
        downloadedLabel.configure(text="Error Downloading Video!", text_color="red")

def downloadAudio():
    """
    Downloads the audio of video given the link in the entry box and saves it to the download directory (by default the user's downloads folder). Saves as mp4 file
    """
    try:
        yt = YouTube(linkEntry.get())
        audio = yt.streams.get_audio_only()
        audio.download(downloadDirectory)
        downloadedLabel.configure(text="Download complete!", text_color="green")
    except:
        downloadedLabel.configure(text="Error Downloading Audio!", text_color="red")

def changeDownloadDirectory():
    """
    Changes the download directory to the directory entered in the entry box. Currently does not recognize if entered directory does not exist. 
    """
    global downloadDirectory
    try:
        downloadDirectory = os.path.join(os.path.expanduser("~"), downloadDirectVar.get())
        downloadedLabel.configure(text="Download Directory Changed!", text_color="green")
    except:
        downloadedLabel.configure(text="Error Changing Download Directory!", text_color="red")

#GUI Setup
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Audio/Video Downloader")

#GUI UI Elements
title = customtkinter.CTkLabel(app, text="YouTube Audio/Video Downloader", font=("Arial", 24))
title.pack(padx=20, pady=20)

urlVar = customtkinter.StringVar()
linkEntry = customtkinter.CTkEntry(app, width=500, height=40, textvariable=urlVar, font=("Arial", 18))
linkEntry.pack()

downloadedLabel = customtkinter.CTkLabel(app, text="", font=("Arial", 18))
downloadedLabel.pack()

videoDownloadButton = customtkinter.CTkButton(app, text="Download Video", font=("Arial", 18), command=downloadVideo)
videoDownloadButton.pack(side="left")

audioDownloadButton = customtkinter.CTkButton(app, text="Download Audio", font=("Arial", 18), command=downloadAudio)
audioDownloadButton.pack(side="right")

downloadDirectVar = customtkinter.StringVar()
changeDownloadDirectoryEntry = customtkinter.CTkEntry(app, textvariable=downloadDirectVar, font=("Arial", 18))
changeDownloadDirectoryEntry.pack(side="bottom")

changeDirectoryButton = customtkinter.CTkButton(app, text="Change Download Directory", font=("Arial", 18), command=changeDownloadDirectory)
changeDirectoryButton.pack(side="bottom")

app.mainloop()
