from pytube import YouTube
from docstrings import *

downloads_folder = "../my_music"

def select(option):
    if option in "":
        print("You have to enter a valid command")

    elif option in "download":
        video_url, file_name = get_url_and_name()
        download_video(video_url, file_name)

    elif option in "open load website":
        print("Opening index.html")

    elif option in "exit quit close finish":
        return "exit"

    elif option in "help":
        print(help)

    else:
        print("Sorry that doesn't look like a command")

def get_url_and_name():
    print("\nYoutube Music Downloader")
    print(medium_line)

    video_url = input("\nEnter a Youtube link: ")

    file_name = input("Custom video title(enter to give default title): ")

    return (video_url, file_name)


def download_video(video_url, file_name):
    try:
        youtube_video = YouTube(video_url)

        if file_name:
            youtube_video.title = file_name

        youtube_video.streams.first().download(output_path=downloads_folder)
    except:
        print("Something Went Wrong, please try again.")

# ------------------------------------------------------------------------------------------------------------------

print(intro_title)

def main():
    while True:
        option = input("-> ")

        if select(option) == "exit":
            break

    print("Program Closed")

main()
