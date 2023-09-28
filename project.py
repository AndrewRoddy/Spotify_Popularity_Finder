import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tabulate import tabulate
import datetime
import re
import copy
import tkinter as tk


def ascii_art():
    """
    Returns ascii art created for the Spotify Popularity Finder made by Andrew Roddy

    :return: Ascii Art
    :rtype: str

    """

    """
        ____  ____   __  ____  __  ____  _  _                            ⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀
        / ___)(  _ \\ /  \\(_  _)(  )(  __)( \\/ )                        ⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀
        \\___ \\ ) __/(  O ) )(   )(  ) _)  )  /                        ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
        (____/(__)   \\__/ (__) (__)(__)  (__/ by Andrew Roddy       ⢀⣾⣿⡿⠿⠛⠛⠛⠉⠉⠉⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣷⡀
        ____   __  ____  _  _  __     __   ____  __  ____  _  _    ⣾⣿⣿⣇⠀⣀⣀⣠⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠈⠙⠻⣿⣿⣷⠀
        (  _ \\ /  \\(  _ \\/ )( \\(  )   / _\\ (  _ \\(  )(_  _)( \\/ )  ⢠⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠛⠛⠻⠿⢿⣿⣶⣤⣀⣠⣿⣿⣿⡄
        ) __/(  O )) __/) \\/ (/ (_/\\/    \\ )   / )(   )(   )  /   ⢸⣿⣿⣿⣿⣇⣀⣀⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠉⠛⢿⣿⣿⣿⣿⡇
        (__)   \\__/(__)  \\____/\\____/\\_/\\_/(__\\_)(__) (__) (__/    ⠘⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠛⠿⠿⣿⣶⣦⣤⣾⣿⣿⣿⣿⠃
        ____  __  __ _  ____  ____  ____                          ⠀⢿⣿⣿⣿⣿⣤⣤⣤⣤⣶⣶⣦⣤⣤⣄⡀⠈⠙⣿⣿⣿⣿⣿⡿⠀
        (  __)(  )(  ( \\(    \\(  __)(  _ \\                          ⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠁⠀⠀
        ) _)  )( /    / ) D ( ) _)  )   /                            ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀
        (__)  (__)\\_)__)(____/(____)(__\\_)                             ⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀
                                                                        ⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
    """

    return " ____  ____   __  ____  __  ____  _  _                            ⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀\n/ ___)(  _ \\ /  \\(_  _)(  )(  __)( \\/ )                        ⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀\n\\___ \\ ) __/(  O ) )(   )(  ) _)  )  /                        ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀\n(____/(__)   \\__/ (__) (__)(__)  (__/ by Andrew Roddy       ⢀⣾⣿⡿⠿⠛⠛⠛⠉⠉⠉⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣷⡀\n ____   __  ____  _  _  __     __   ____  __  ____  _  _    ⣾⣿⣿⣇⠀⣀⣀⣠⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠈⠙⠻⣿⣿⣷⠀\n(  _ \\ /  \\(  _ \\/ )( \\(  )   / _\\ (  _ \\(  )(_  _)( \\/ )  ⢠⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠛⠛⠻⠿⢿⣿⣶⣤⣀⣠⣿⣿⣿⡄\n ) __/(  O )) __/) \\/ (/ (_/\\/    \\ )   / )(   )(   )  /   ⢸⣿⣿⣿⣿⣇⣀⣀⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠉⠛⢿⣿⣿⣿⣿⡇\n(__)   \\__/(__)  \\____/\\____/\\_/\\_/(__\\_)(__) (__) (__/    ⠘⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠛⠿⠿⣿⣶⣦⣤⣾⣿⣿⣿⣿⠃\n ____  __  __ _  ____  ____  ____                          ⠀⢿⣿⣿⣿⣿⣤⣤⣤⣤⣶⣶⣦⣤⣤⣄⡀⠈⠙⣿⣿⣿⣿⣿⡿⠀\n(  __)(  )(  ( \\(    \\(  __)(  _ \\                          ⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠁⠀⠀\n ) _)  )( /    / ) D ( ) _)  )   /                            ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀\n(__)  (__)\\_)__)(____/(____)(__\\_)                             ⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀\n                                                                  ⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀"


def setup_spotipy(c_id, c_secret):
    """
    Creates a global variable that contains the client id and client secret needed to run the spotipy library.

    :param c_id: The user's client id
    :type c_id: str
    :param c_secret: The user's client secret
    :type c_secret: str
    """
    # Creates a global variable for the spotipy
    global spotify

    # Instalizes the spotipy library
    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
            client_id=c_id, client_secret=c_secret
        )
    )


def length_limit(name, length):
    """
    Limits the length of strings input and adds three dots to the end.

    :param name: The name to be shortened.
    :type name: str
    :param length: The length that the name should be shortened to.
    :type length: int
    :return: Returns the shortened name followed by three dots
    :rtype: str
    """

    # Checks if the length of the name is longer than the input length
    if len(name) >= length + 1:
        # Reduces the length of the name by the length input and adds three dots to the end
        name = f"{name[:length]}..."

    # Returns the new converted name
    return name


def yes_or_no(user_input):
    """
    Returns 1 or 0 based on if the user says yes or no to a question.

    :param user_input: The input the user gives as an answer to a question.
    :type user_input: str
    :return: Returns -1 if invalid input, 0 if input is no, 1 if input ir yes
    :rtype: int
    """

    # If the user does not input a valid response
    if (
        user_input.lower() != "yes"
        and user_input.lower() != "no"
        and user_input.lower() != "y"
        and user_input.lower() != "n"
        and user_input.lower() != "1"
        and user_input.lower() != "0"
        and user_input.lower() != "true"
        and user_input.lower() != "false"
    ):
        # Print Invalid Input and return -1
        print("Invalid Input")
        return -1

    # If the user inputs a valid reponse that means yes
    if (
        user_input.lower() == "yes"
        or user_input.lower() == "y"
        or user_input.lower() == "1"
        or user_input.lower() == "true"
    ):
        # Returns 1
        return 1
    else:
        # If the user does not return a yes response, return 0
        return 0


def ms_to_m(ms):
    """
    Converts milleseconds to well formatted minutes and seconds.

    :param ms: The amount of milleseconds to be converted.
    :type ms: int
    :return: Returns the milleseconds formatted as minutes and seconds seperated by a colon
    :rtype: str
    """

    # Convert the milleseconds to a datetime timedelta like response
    time = datetime.timedelta(milliseconds=ms)

    # Searches and groups the results using regular expressions
    search = re.search(r"\d:(\d\d):(\d\d)", str(time))

    # The first group is minutes
    # Converts it into an int to remove a possible leading zero
    minutes = int(search.group(1))

    # The second group is seconds
    seconds = search.group(2)

    # Returns the time as 1:20 for 1 minute and 20 seconds
    return f"{minutes}:{seconds}"


def artist_search():
    """
    Uses spotipy to search for an artist.
    :return: The artist id found through the search.
    :rtype: str
    """

    # Until a valid artist is found
    while True:
        # Create's a blank artist_id
        artist_id = "None"

        # Asks the user for an artists name or id
        search = input("Search for an artist (name or id): ")

        # If the search field is empty
        if search == "":
            # Print error and ask again
            print("\nSearch field empty.")
            continue

        # If the length of the input is 22 and there are no spaces in the search
        # This means that the user likely entered an artist id
        if len(search) == 22 and " " not in search:
            # Make the users input the artist id
            artist_id = search

        # If the user did not input an artist id
        else:
            # Use spotipy to search for the artists id
            data = spotify.search(search, type="artist")

            # Find the artist's items
            items = (data["artists"])["items"]

            # Search through the results to find the artist's names
            for i in range(len(items)):
                # If the artist's name is the same as the user's input
                if search.lower() == (items[i])["name"].lower():
                    # Make the artist_id the artist's id
                    artist_id = (items[i])["id"]
                    break

            # If an artist_id is never found select the first options's artist id
            if artist_id == "None":
                artist_id = items[0]["id"]

        # If the artist has no albums print error and try again
        if artists_albums(artist_id) == 0:
            print("Artist not found or artist has no albums, Try Again\n")
            continue

        break

    # Returns the artist's id
    return artist_id


def artists_albums(artist_id, popularity=False):
    """
    Gets the artists albums using the artist's id

    :param artist_id: The artist's id.
    :type artist_id: str
    :param popularity: Add popularity scores of each album if True. (This is a lengthy process)
    :type popularity: bool
    :return: Returns 0 if the artist has no albums.
    :rtype: int
    :return: Returns the data for every album the artist has as a 2D array
    :rtype: list
    """
    # Sets up the stopify library
    data = spotify.artist_albums(artist_id, "album", None, 50, 0)

    # Gets the albums of the user
    info = data["items"]

    # If the artist has no albums returns 0
    if info == []:
        return 0

    # Creates an empty list for the album data
    album_data = []

    # For every album recieved run once
    for i in range((len(info) - 1), -1, -1):
        # Append the album_data list
        album_data.append(
            [
                # The number in order of the album
                (len(info) - i),
                # The name of the album
                length_limit(info[i]["name"], 19),
                # The number of songs on the album
                info[i]["total_tracks"],
                # The release date
                info[i]["release_date"],
                # The albums id
                info[i]["id"],
            ]
        )

    # If the popularity paramater is true
    if popularity == True:
        # Run once for every album
        for i in range(len(info)):
            # Append the album popularity using the album_popularity function
            album_data[i].append(album_popularity(info[len(info) - i - 1]["id"]))

            # Prints a statement to let the user know that the program is still working
            print(f"Album {i+1} Done!")
        print("")

    # Returns the 2D array of album's data
    return album_data


def albums_table(album_data):
    """
    Creates a table for the albums

    :param album_data: A 2D array of the albums recieved from artists_albums()
    :type album_data: list
    :return: A table made from the data input
    :rtype: str
    """
    # Creates the headers used by tabulate
    headers = ["#", "Album Name", "Songs", "Rel Date", "Pop"]

    # Copies the album_data using deepcopy as to not edit the original list
    data = copy.deepcopy(album_data)

    # Removes the id from every album in the list to not show it on the table
    for i in range(len(data)):
        data[i].pop(4)

    # Returns the table
    return tabulate(data, headers, tablefmt="simple")


def album_stats(artist_id):
    """
    Gets the average song count for the artist.

    :param artist_id: The id for the artist
    :type artist_id: str
    :return: The average song count for the albums
    :rtype: int
    """

    # Gets the artist's albums
    data = artists_albums(artist_id)

    # Gets the amount of albums
    album_count = len(data)

    # Starts the total songs at zero
    album_total_songs = 0

    # Run once for every album
    for i in range(len(data)):
        # Adds the number of songs from each album to album_total_songs
        album_total_songs += data[i][2]

    # Divides the total songs from the number of albums to get the average
    average_song_count = round(album_total_songs / album_count)

    # Returns the average song count
    return average_song_count


def album_songs(album_id):
    """
    Gets a list of songs and statistics from an album

    :param album_id: The id of a spotify album
    :type album_id: str
    :return: A list of the songs from the input album and statistics related to each song
    :rtype: list
    """

    # Uses spotipy to get album tracks
    data = spotify.album_tracks(album_id, 50, 0, None)

    # Gets the items in data
    info = data["items"]

    # Creates an empty list
    songs = []

    # For every item repeat once
    for i in range((len(info))):
        # Gets the song id
        song_id = info[i]["id"]

        # Converts the song to a track
        track = spotify.track(song_id)

        songs.append(
            [
                # Gets the track number of which track it is in the album
                track["track_number"],
                # Uses length limit to shorten the song length from item
                length_limit(track["name"], 25),
                # Gets if the song is explicit or not
                track["explicit"],
                # Gets the song length then converts it to seconds and minutes
                ms_to_m(track["duration_ms"]),
                # Gets the track id
                track["id"],
                # Gets the track popularity
                track["popularity"],
            ]
        )

    # Returns the song length
    return songs


def songs_table(song_data):
    """
    Creates a table based on song data.

    :param song_data: A list of songs in an album and data about the songs
    :type song_data: list
    :return: A table representation of song data
    :rtype: str
    """
    # Creates a seperate list of songs that does not affect the original list
    songs = copy.deepcopy(song_data)

    # The headers in the table
    headers = ["#", "Song Title", "", "Len", "Pop"]

    # Repeat once for every song in the list
    for i in range(len(songs)):
        # Removes the song id's from the list
        songs[i].pop(len(songs[i]) - 2)

        # If explicit is true replace it with an E
        if songs[i][2]:
            songs[i][2] = "E"

        # If not replace it with a space
        else:
            songs[i][2] = " "

    # Return a the song stats as a table
    return tabulate(songs, headers, tablefmt="simple")


def album_popularity(album_id):
    """
    Gets the popularity stat of an album by averaging all of the popularity stats of each track in the album.

    :param album_id: The id of an album in spotify
    :type album_id: str
    :return: The average popularity of every track in an album
    :rtype: int
    """
    # Gets the song data from an album
    data = album_songs(album_id)

    # Sets total popularity to 0
    total_popularity = 0

    # For every song in an album
    for i in range(len(data)):
        # Adds the popularity of each song to the total popularity
        total_popularity += data[i][5]

    # Divides the total popularity number by the amount of songs in the album
    average_popularity = round(total_popularity / len(data))

    # Returns the average popularity
    return average_popularity


def sort_by_popularity(data):
    """
    Sorts album data and song data by popularity.

    :param data: Album or song data
    :type data: list
    :return: Returns a sorted by popularity list.
    :rtype: list
    """
    return sorted(data, key=lambda x: x[len(data[0]) - 1], reverse=True)


def artist_select():
    """
    Runs a system of processes to allow the user to see the full abilites of the functions.
    Asks the user what artist they would like to listen to
    After this it shows them the popularity, the popularity sorted then prompts them to open each individual album
    """

    # Gets the artist's id
    id = artist_search()

    # Gets artists albums
    albums = artists_albums(id, popularity=False)

    # Prints a table of the albums
    print(albums_table(albums))

    # Prints the average song count
    print(f"Average Song Count: {album_stats(id)}")

    while True:
        # Asks the user if they woud like to see the popularity stats
        # The reason this is asked is becasue getting popularity stats for every album takes a long time
        popularity = input("Would you like to show popularity stats? ")

        if yes_or_no(popularity) != -1:
            if yes_or_no(popularity) == 0:
                break

            elif yes_or_no(popularity) == 1:
                print("Loading...")

                # Gets the popularity stats and prints a table
                albums = artists_albums(id, popularity=True)
                print(albums_table(albums))

                while True:
                    # If the user gets popularity stats they will then be prompted to sort the albums by popularity
                    sort = input("Would you like to sort by popularity? ")
                    if yes_or_no(sort) == 1:
                        # If yes, print the sorted popularity stats in a table
                        print(albums_table(sort_by_popularity(albums)))
                        break

                    if yes_or_no(sort) == 0:
                        break
                break

    # Once this is complete, run album_select
    album_select(albums)


def album_select(album_data):
    """
    Allows the user to see inside of albums and how popular each song in each album is.

    :param album_data: Data including an artists albums
    :type album_data: list
    """
    while True:
        # Ask the user what album they would like to select
        album_select = input("\n[Enter to go back] Select an Album: ")

        # If the user presses enter without typing anything take them back to artist select
        if album_select == "":
            artist_select()

        try:
            # Gets the id from the selected album
            album_id = album_data[int(album_select) - 1][4]

            # Gets the songs from the album
            songs = album_songs(album_id)

            # Print the song's and data in a table
            print(songs_table(songs))
            while True:
                # Prompt the user to sort the albums by popularity
                sort = input("Would you like to sort by popularity? ")

                # If yes
                if yes_or_no(sort) == 1:
                    # Print the songs sorted by popularity
                    print(songs_table(sort_by_popularity(songs)))
                    break

                if yes_or_no(sort) == 0:
                    break

            # Adds a quick pause so the user can wait and look at the song data
            input("[press enter to go back] ")

            # Prints the album table
            print(albums_table(album_data))

        # If the user inputs a bad album number or an invalid input
        except (IndexError, ValueError):
            # Print the album again and prompt the user to input an album number
            print(albums_table(album_data))
            print("[input an album number]")


def main():
    # Uses my spotipy codes to run the program
    setup_spotipy(
        "0a240b9f9c0a42d48396b35cd459a925", "c9377c875e3146078d77ee366a76c02a"
    )

    # Starts Tkinter
    root = tk.Tk()

    # Sets the bounds of the window
    root.geometry("750x250")

    # Creates the text on screen
    myLabel = tk.Label(
        root,
        text=songs_table(album_songs("1NAmidJlEaVgA3MpcPFYGq")),
        font=("Helvetica 15 underline"),
    )
    myLabel.pack(pady=20, side=TOP, anchor="w")


    # Creates an input field in tkinter
    entry = tk.Entry(root, width=40)
    entry.focus_set()
    entry.pack()

    # Runs the window
    root.mainloop()


if __name__ == "__main__":
    main()
