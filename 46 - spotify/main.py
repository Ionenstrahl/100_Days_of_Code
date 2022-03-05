import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


date = "2004-09-12"
german = True

# - - - Scraping for top 100 Songs - - -

if german:
    url_01_01_00 = "https://www.offiziellecharts.de/charts/single/for-date-946681200000"
    print(int(date[-2:]) )
    url_date = 946681200000 + \
               (int(date[-2:])-1) * 6400000 + \
               (int(date[5:7])-1) * 6400000 * 30 + \
               int(date[-2:])     * 6400000 * 365

    url = "https://www.offiziellecharts.de/charts/single/for-date-" + str(url_date)
    response = requests.get(url)
    print(response)
else:
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")

# für mich hat angelas lösung nicht funktioniert
# für Billboard
if german:
    titles = [title.getText() for title in soup.find_all(name="span", class_="info-title")]
else:
    titles = [title.getText()[1:-1] for title in soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]


# - - - Authenticating in Spotify - - -
CLIENT_ID = os.environ["ID"]
CLIENT_SECRET = os.environ["SECRET"]
# habe einfach versuche mein spotifyprofil in whatsapp zu teilen. da siehht man diese zahl
# wie kommt man auf sp.current_user()["id"]
spotify_uid = os.environ["UID"]

# habe die andere anmleldungsmethods versucht.
# anmelden ging, aber playlist erstellen nicht mehr
# habe das dann einfach kopiert
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="../../private/token.txt"
    )
)


# - - - Searching for top 100 - - -
title_uris = []
for title in titles:
    try:
        # search keyword habe ich auch nicht gefunden
        uri = sp.search(f"track: {title} year: {date[:4]}", limit=1, type='track')["tracks"]["items"][0]["uri"]
        title_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")


# - - - Creating Playlist - - -
# spotify_uid = sp.current_user()["id"]
# habs genauso versucht, aber ging nicht wil ich public = true hatte
# nirgendwo steht, dass die funktion die Playlist_id returned
playlist = sp.user_playlist_create(user=spotify_uid, name=f"Top 100 from {date}", public=False, collaborative=False, description='Created with Spotipy')
sp.playlist_add_items(playlist_id=playlist["id"], items=title_uris)
