# YouTube Downloader

**Author**: Brandon Jarvis, 2024

This is a python script that allows you to enter a YouTube link and download the video or audio to your machine. Uses a basic GUI developed upon customtkinter and uses pytube to access/download YouTube content. Current functionality also allows the user to change the directory they are downloading output to - at this time limited to preexisting directories on the users PC. 

Please note that this is not finished - it currently overwrites previous files of the same name (so you cannot download a video and audio version of the same titled video). There are plans to edit this to allow the user to change what files are being saved as, as well as create new directories that are not yet on the user's PC.

You can view current issues and planned functionality on the Projects bored. 

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Run the script by executing `python3 YouTubeDownloader.py`.
2. Use on screen GUI to enter YouTube link, download video, download audio, and edit directory downloaded output is stored in (by default it is the users Downloads folder).
