import json

class LibraryItem(object):
  #Create
  def __init__(self, title = None, genre = None, media = None):
    self.title = title
    self.genre = genre
    self.media = media
  #returns a LibraryItem in the format of title, genre, media
  def getTitle(self):
    return("%s is a %s %s" % (self.title, self.genre, self.media))

  @classmethod
  #returns all items inside db.txt as a list of Library contents
  def getAll(self):
    database = open('db.txt', 'r')
    result = []
    json_list = json.loads(database.read())
    for item in json_list:
      lib = LibraryItem(item['title'], item['genre'], item['media'])
      result.append(lib)
    return result