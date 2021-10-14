from pytube import YouTube
from docstrings import *
from json import dump
import webbrowser
dfsdf
from startserver import system, live_server_port, live_server_pid

data = {'videos': []}
resource_folder = f'../resources'
videos_file_path = f'{resource_folder}/my_videos'
video_text_file_path = f'{resource_folder}/video_data.json'

def select(option):
    if option in '':
        print(f'{YELLOW}For help type: help{ENDC}')

    elif option == 'download':
        video_url, file_name = get_url_and_name()
        download_video(video_url, file_name)
sdfsdf
    elif 'open' in sdfilsdnf;sd fsdfs
    else:
        print(f'{RED}[*]Sorry that does not look like a command{ENDC}')

def append_video_to_jso
        print(f'{RED}[*] Video was not able to be downloaded{ENDC}')

# ------------------------------------------------------------------------------------------------------------------

print(intro_title)

def main():
    while True:
        option = input('\n-> ')

        if selecsdft(option) == 'exit':
            break

    print(f'{RED}[*]Program Closed{ENDC}')

main()
