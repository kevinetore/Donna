from bs4 import BeautifulSoup
import requests

def url_replacing_characters(text):
    text = text.replace('<td>','').replace('</td>','')
    head, sep, tail = text.partition('=')
    return tail

def get_youtube_playlist():
    data = requests.get('http://localhost:8000')
    soup = BeautifulSoup(data.text, 'html.parser')
    html_playlist = soup.tbody.tr.td
    playlist = url_replacing_characters(str(html_playlist))
    return playlist