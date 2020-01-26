from model import LibraryItem

def showAllView(list):
    print('In our library we have %i items. Here they are:' % len(list))
    for item in list:
      print(item.getTitle())
def startView():
    print('Welcome to The Finite Library')
    print('Would you like to see our entire database?[y/n]')

def endView():
    print('Thanks for visiting, goodbye!')