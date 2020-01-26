from model import LibraryItem

def showAllView(list):
    print('In our library we have %i items. Here they are:' % len(list))
    for item in list:
      print(item.getTitle())
def startView():
    print('MVC - the simplest example')
    print('Do you want to see everyone our my database?[y/n]')

def endView():
    print('Goodbye!')