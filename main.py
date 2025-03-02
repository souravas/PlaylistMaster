import subprocess

def fetch_playlist(url):
    command = ["yt-dlp", "--flat-playlist", "--print", "%(artist)s ----- %(title)s", url]
    result = subprocess.run(command, capture_output=True, text=True)
    output_lines = result.stdout.splitlines()
    return output_lines

def write_to_file(filename, lines):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


def fetch_duplicates(playlist):
    song_set = set()
    duplicate_list = []
    for song in playlist:
        if song in song_set:
            duplicate_list.append(song)
        else:
            song_set.add(song)
    return duplicate_list

playlist = fetch_playlist("https://www.youtube.com/playlist?list=PL5mKbkRfXiOqTzlagO60Sk-EKBWTre-YU")
write_to_file("everything.txt", playlist)
write_to_file("duplicate.txt",fetch_duplicates(playlist))