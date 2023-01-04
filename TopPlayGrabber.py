from ossapi import Ossapi

#set the API key
api = Ossapi("f320af2b16dbfcb597973d754e1ca39dabeaf7ab")

class Song :
   def __init__(self, title, artist):
      self.title = title
      self.artist = artist
#method for pulling top plays from a users profile
#@param username: player userid, aka the number in your profile link
def pullTopPlays(userid):
   #initialize list for storing top plays
   songs = []
   for i in range(25) :
      #grab the top 25 plays
      #I dont see a point in grabbing more than 25
      mapID = api.get_user_best(userid, limit=25)[i].beatmap_id
      map = api.get_beatmaps(beatmap_id=mapID)[0]
      mapTitle = map.title
      mapArtist = map.artist
      print(mapID)
      print("Title:", mapTitle, ", Artist:", mapArtist)
      song = Song(mapTitle, mapArtist)
      songs.append(song)
   return songs


def main():
   pullTopPlays("9042348")
   
if __name__ == "__main__":
    main()



