from pytube import YouTube
from docstrings import *

downloads_folder = "../my_music"

def select(option):
    if option in "":
        print(f"{YELLOW}For help type: help{ENDC}")

    elif option == "download":
        video_url, file_name = get_url_and_name()
        download_video(video_url, file_name)

    elif "open" in option:
        print(f"{YELLOW}Opening index.html{ENDC}")
        # TODO: LOAD FILE HERE

    elif option == "exit":
        return "exit"

    elif option in "help":
        print(help)

    else:
        print(f"{RED}[*]Sorry that doesn't look like a command{ENDC}")

def get_url_and_name():
    print("\nYoutube Music Downloader")
    print(medium_line)

    video_url = input(f"\n{YELLOW}Enter a Youtube link: {ENDC}")

    file_name = input(f"{YELLOW}Custom video title(enter to give default title): {ENDC}")

    return (video_url, file_name)


def download_video(video_url, file_name):
    try:
        youtube_video = YouTube(video_url)
        import pdb; pdb.set_trace()

        if file_name:
            youtube_video.title = file_name

        youtube_video.streams.first().download(output_path=downloads_folder)
    except:
        print(f"{RED}[*] Video was not able to be downloaded{ENDC}")

# ------------------------------------------------------------------------------------------------------------------

print(intro_title)

def main():
    while True:
        option = input("\n-> ")

        if select(option) == "exit":
            break

    print(f"{RED}[*]Program Closed{ENDC}")

main()
