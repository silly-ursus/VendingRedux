from model import LibraryItem
import view

def showAll():
  #gets list of all LibraryItem objects
  items_in_db = LibraryItem.getAll()
  #calls view
  return view.showAllView(items_in_db)

def start():
  view.startView()
  inputted = input()
  if inputted == 'y':
    return showAll()
  else:
    return view.endView()

if __name__ == "__main__":
  #running controller function
  start()