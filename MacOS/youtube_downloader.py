from pytube import YouTube
from docstrings import *
from json import dump
import webbrowser

data = {'videos': []}
resource_folder = f'../resources'
videos_file_path = f'{resource_folder}/my_videos'
video_text_file_path = f'{resource_folder}/video_data.json'

live_server_port = 9999

def select(option):
    if option in '':
        print(f'{YELLOW}For help type: help{ENDC}')

    elif option == 'download':
        video_url, file_name = get_url_and_name()
        download_video(video_url, file_name)

    elif 'open' in option:
        print(f'{YELLOW}Opening your music library{ENDC}')
        webbrowser.open(f'http://127.0.0.1:{live_server_port}')

    elif option in 'help':
        print(help)

    else:
        print(f'{RED}[*]Sorry that does not look like a command{ENDC}')

def append_video_to_json(youtube_video, date=''):
    file_name = youtube_video.title

    data['videos'].append({
        'file_name': file_name,
        'file_path': f"./resources/my_videos/{''.join([c for c in file_name if c.isalpha() or c.isdigit() or c in '-()[]'])}.mp4",
        'file_img_url': youtube_video.thumbnail_url, # make available offline | stretch
        # 'date': 'time_stamp',
    })

    # TODO: Time box this without dump functionality
    with open(video_text_file_path, 'w') as file:
        dump(data, file)

    print(f'{YELLOW}Added video details to video_data.json{ENDC}')

def get_url_and_name():
    print('\nYoutube Music Downloader')
    print(medium_line)

    video_url = input(f'\n{YELLOW}Enter a Youtube link: {ENDC}')

    file_name = input(f'{YELLOW}Custom video title(enter to give default title): {ENDC}')

    return (video_url, file_name)

def download_video(video_url, file_name):
    try:
        youtube_video = YouTube(video_url)

        if file_name:
            youtube_video.title = file_name

        youtube_video.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=videos_file_path)

        # Swap to different live-server; refresh should happen after this
        append_video_to_json(youtube_video)
    except:
        print(f'{RED}[*] Video was not able to be downloaded{ENDC}')

# ------------------------------------------------------------------------------------------------------------------

print(intro_title)

def main():
    while True:
        option = input('\n-> ')

        if option == 'exit':
            # safely kill live-server
            print(f'{RED}[*] Do not forget to close your live-server{ENDC}')
            break
        else:
            select(option)

    print(f'{RED}[*]Program Closed{ENDC}')

main()
