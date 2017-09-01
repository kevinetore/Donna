from apiclient.discovery import build
from apiclient.errors import HttpError
import insert_playlist
import fingerprinting.fingerprint as donna
import nlp.added as textToSpeech
import retrieve_playlist

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyAJRQQxKwic0ofezl-YRwxfOzHW8zg4FwY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  donna_magic = donna.recognizeSong()
  print(donna_magic)
  song = donna_magic['song_name']

  videos = ""
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=song,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos = ("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))

  youtube_search.song = videos.split()[-1].replace("(","").replace(")","")
  print("found the song on Youtube " + youtube_search.song)
  
  insert_playlist.playlist_items_insert(
      {'snippet.playlistId': str(retrieve_playlist.get_youtube_playlist()),
       #'PLmlXzyxigzqmWTk6-_9x2XTydGpOlGmHN',
       'snippet.resourceId.kind': 'youtube#video',
       'snippet.resourceId.videoId': youtube_search.song,
       'snippet.position': ''},
      part='snippet',
      onBehalfOfContentOwner='')
  
  textToSpeech.addedSong(song)