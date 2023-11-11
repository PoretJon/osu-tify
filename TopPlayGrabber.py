from os import getenv
import os
from ossapi import OssapiV1
from Song import Song


#set the API key
api = OssapiV1(getenv("OSU_CLIENT"))
#method for pulling top plays from a users profile
#@param username: player userid, aka the number in your profile link
def pullTopPlays(userid):
   #initialize list for storing top plays
   songs = []
   #grab the top plays
   maps = api.get_user_best(userid, limit = 100)
   for i in range(100) :
      #set the beatmap id so we can search for it
      # mapID = api.get_user_best(userid, limit=100)[i].beatmap_id
      mapID = maps[i].beatmap_id
      map = api.get_beatmaps(beatmap_id=mapID)[0] #since get_beatmaps() returns a list i have to do this bullshit that looks bad
      mapTitle = map.title
      mapArtist = map.artist
      print(mapID)
      print("Title:", mapTitle, ", Artist:", mapArtist)
      song = Song(mapTitle, mapArtist) #creates a "Song" object with the title and artist
      songs.append(song) #adds the song to the list of songs
      # print (songs)
   return songs



