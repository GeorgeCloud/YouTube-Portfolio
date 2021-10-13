from pytube import YouTube
from docstrings import *
from json import dump
from subprocess import call

data = {'videos': []}
resource_folder = f'../resources'
videos_file_path = f'{resource_folder}/my_videos'
video_text_file_path = f'{resource_folder}/video_data.txt'

def select(option):
    if option in '':
        print(f'{YELLOW}For help type: help{ENDC}')

    elif option == 'download':
        video_url, file_name = get_url_and_name()
        download_video(video_url, file_name)

    elif 'open' in option:
        print(f'{YELLOW}Opening your music library{ENDC}')
        call(['open', '../index.html'])

    elif option == 'exit':
        return 'exit'

    elif option in 'help':
        print(help)

    else:
        print(f'{RED}[*]Sorry that does not look like a command{ENDC}')

def append_video_to_json(youtube_video, date=''):
    file_name = youtube_video.title

    data['videos'].append({
        'file_name': file_name,
        'file_path': f'./images/{file_name}',
        'file_img_url': youtube_video.thumbnail_url,
        # 'date': 'time_stamp',
    })

    # TODO: Time box this without dump functionality
    with open(video_text_file_path, 'w') as file:
        dump(data, file)

    print(f'{YELLOW}Added video details to video.txt{ENDC}')

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

        append_video_to_json(youtube_video)
    except:
        print(f'{RED}[*] Video was not able to be downloaded{ENDC}')

# ------------------------------------------------------------------------------------------------------------------

print(intro_title)

def main():
    while True:
        option = input('\n-> ')

        if select(option) == 'exit':
            break

    print(f'{RED}[*]Program Closed{ENDC}')

main()