from collections import namedtuple
Album = namedtuple('Album', 'id artist title year songs')
Song = namedtuple('Song', 'track title length play_count')


def get_song_input():
    """Create tuple for each song."""
    song_track = int(input('Enter the song\'s track:\n'))
    song_title = input('Enter the song\'s title:\n')
    song_length = int(input('Enter the song\'s length:\n'))
    song_count = int(input('Enter the song\'s play_count:\n'))
    song = Song(song_track, song_title, song_length, song_count)
    return song


def get_album_input():
    """Create tuple for each album."""
    album_id = input('Enter the album\'s id:')
    album_artist = input('Enter the album\'s artist:')
    album_title = input('Enter the album\'s title:')
    album_year = int(input('Enter the album\'s year:'))
    album_num = int(input('Enter the number of songs in this album:'))
    song_list = []
    for _ in range(album_num):
        song_list.append(get_song_input())
    album = Album(album_id, album_artist, album_title, album_year, song_list)
    return album


def add_album(music_col):
    """Add album to music collection."""
    music_col.append(get_album_input())
    return music_col


def remove_album(music_col, ID):
    """Remove an album from music collection."""
    foundAlbum = False

    for item in music_col:
        if ID == item.id:
            foundAlbum = True
            music_col.remove(item)

    if not foundAlbum:
        print('Album not found.')

    return music_col


def favorite_song(music_col, ID):
    """Output favorite song using album ID."""
    foundAlbum = False

    for item in music_col:
        if ID == item.id:
            foundAlbum = True
            max_play = 0
            max_song = None

            for song in item.songs:
                play_count = 0
                if song.play_count:
                    play_count = song.play_count
                playing_time = play_count * song.length
                if playing_time > max_play:
                    max_play = playing_time
                    max_song = song

    if not foundAlbum:
        return 'Album not found.'

    return max_song


def unplayed_songs(music_col, ID):
    """Output a list of songs that have a play count of 0 using album ID."""
    foundAlbum = False
    
    for item in music_col:
        if ID == item.id:
            foundAlbum = True
            unplay_songs = []
            
            for song in item.songs:
                if song.play_count == 0:
                    unplay_songs.append(song)

    if not foundAlbum:
        return 'Album not found.'
        
    return unplay_songs


def favorite_album(music_col):
    """Output favorite song."""
    max_album_time = 0
    max_album = None
    for album in music_col:
        albumTime = 0

        for song in album.songs:
            play_count = 0
            if song.play_count:
                play_count = song.play_count
            playing_time = play_count * song.length
            albumTime += playing_time
            
        if albumTime > max_album_time:
            max_album_time = albumTime
            max_album = album

    return max_album


def unplayed_albums(music_col):
    """Output a list of albums that have a total play count of 0."""
    unplay_albums = []
    for album in music_col:
        counter = 0
        
        for song in album.songs:
            if song.play_count and song.play_count > 0:
                counter += 1

        if counter == 0:
            unplay_albums.append(album)
            
    return unplay_albums


def print_menu():
    """Print the collection manager menu and save user choice."""
    print('''MUSIC COLLECTION MANAGER

    add - Add a new album
    del - Remove an album
    fav_a - Print favorite album
    fav_s - Print favorite song
    not_a - Print not played albums
    not_s - Print not played songs
    exit - Exit the application\n''')

    answerList = ['add', 'del', 'fav_a', 'fav_s', 'not_a', 'not_s', 'exit']

    option = input('Choose an option:\n')

    while option not in answerList:
        option = input('Choose an option:\n')
    
    return option


if __name__ == '__main__':

    answer = print_menu()
    music_collection = []
444
    while answer != 'exit':
        if answer == 'add':
            add_album(music_collection)
        if answer == 'del':
            removeID = input('Enter the Album ID:')
            remove_album(music_collection, removeID)
        if answer == 'fav_a':
            print(favorite_album(music_collection))
        if answer == 'fav_s':
            favSongAlbumID = input('Enter the Album ID:')
            print(favorite_song(music_collection, favSongAlbumID))
        if answer == 'not_a':
            print(unplayed_albums(music_collection))
        if answer == 'not_s':
            notSongAlbumID = input('Enter the Album ID:')
            print(unplayed_songs(music_collection, notSongAlbumID))

        answer = print_menu()
