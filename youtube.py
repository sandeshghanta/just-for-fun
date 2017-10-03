import os
import json
import ftplib
import urllib2
import requests
import argparse
from subprocess import call
from bs4 import BeautifulSoup
from time import gmtime,strftime
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
def extract(i):
    pos = len(i) - 1
    while(i[pos] != '('):
        pos = pos - 1
    url = ''
    for j in range(pos+1,len(i)-1):
        url = url + i[j]
    return url
def checkfile(day,time,hour):
    for i in os.listdir(os.getcwd()+'\\audios'):
        if (i.find(day) != -1 and i.find(time) != -1 and i.find(hour) != -1):
            print "Audio already exists in " + i
            return False
    return True
def check(videos,time,hour):
    day = strftime("%d", gmtime())
    for i in videos:
        if (i.find(day) != -1 and i.find(time) != -1 and i.find(hour) != -1):
            if (checkfile(day,time,hour)):
                endlink = extract(i)
                return endlink
    if (day[0] == '0'):
	day = day[1]
    for i in videos:
        if (i.find(day) != -1 and i.find(time) != -1 and i.find(hour) != -1):
            if (checkfile(day,time,hour)):
                endlink = extract(i)
                return endlink
    print hour + ' ' + time + " Video not yet uploaded"
    return False
DEVELOPER_KEY = "AIzaSyCdL0bgv_3WungLZn1PQHsN13Kyu4mrp3g"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
def youtube_search(options,time,hour):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()
  videos = []
  channels = []
  playlists = []
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))
#  print "Videos:\n", "\n".join(videos), "\n"
#  print "Channels:\n", "\n".join(channels), "\n"
#  print "Playlists:\n", "\n".join(playlists), "\n"
  endlink = check(videos,time,hour)
  print endlink
  if (endlink != False):
      command = """youtube-dl -o "audios/%(title)s.%(ext)s" -x --audio-format mp3 https://www.youtube.com/watch?v="""+endlink
      os.system(command)
      print hour + ' ' + time + " Audio Downloaded"
day = strftime("%d", gmtime())
month = "October"
argparser = argparse.ArgumentParser()
argparser.add_argument("--q", help="Search term", default="7 AM ETV Telugu News | "+ day + " " + month + " 2017")
argparser.add_argument("--max-results", help="Max results", default=25)
args = argparser.parse_args()
youtube_search(args,"AM","7")
argparser = argparse.ArgumentParser()
argparser.add_argument("--q", help="Search term", default="9 PM ETV Telugu News | "+ day + " " + month + " 2017")
argparser.add_argument("--max-results", help="Max results", default=25)
args = argparser.parse_args()
youtube_search(args,"PM","9")
    

