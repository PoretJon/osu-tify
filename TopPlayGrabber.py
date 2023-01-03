from ossapi import Ossapi

#set the API key
api = Ossapi("f320af2b16dbfcb597973d754e1ca39dabeaf7ab")

#method for pulling top plays from a users profile
#@param username: player userid, aka the number in your profile link
def pullTopPlays(userid):
   #initialize list for storing top plays
   scores = []
   for i in range(25) :
      #grab the top 25 plays
      #I dont see the point in grabbing the top 100 plays
      #given that most songs in osu are on spotify the top 25
      #should be enough to get a solid playlist made
      mapID = api.get_user_best(userid)[i].beatmap_id
      mapName = api.beatmap(mapID).title
      mapArtist = api.beatmap(mapID).artist
      print("Title: ", mapName, ", Artist: ", mapArtist)


def main():
   pullTopPlays("9042348")
   



