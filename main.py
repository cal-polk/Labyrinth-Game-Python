class Location:
      loc_name = ""

      def setName(Self, new_name):
           Self.loc_name = new_name

      def getName(Self):
           return Self.loc_name
     
      
def clean(command_string):
      command_string = command_string.strip();
      command_string = command_string.lower();
      if (command_string == "south"):
            return "s"
      elif (command_string == "west"):
            return "w"
      elif (command_string == "east"):
            return "e"
      elif (command_string == "north"):
            return "n"
      elif (command_string.find("examine") == 0):
            command_string = command_string.replace("examine", "ex")
            return command_string
      else:
            return command_string
      
def examine(command_string):
      item = command_string[3:]
      if (item == "rug"): #need to verify the item is actually in sight. Some kind of location tracker -- object and set method?
            print("The rug is faded and dusty. It appears as though it could be moved.")
      elif (item == "slip of paper"):
            print("The slip of paper contains a list of the following items:\nBeethoven\nEmily Dickinson\nHoundstooth\n",
                  "Chicago\ne^(ix)\n7\nNarcissus\nHammurabi\nPan\nKhufu\nCatfish\nApollo 13\nBram Stoker")

def main():
      print('You are standing in the middle of a stone room on top of a rug. To the north, south, east and west', 
      'there are windows.')
      isEnd = False
      while(not isEnd):
            command = input(">")
            command = clean(command)
            if (command == "s" or command == "e" or command == 'n'):
                  print("You are standing at a window overlooking a large maze")
            elif (command == "w"):
                  print("You are standing at a window overlooking a large maze. A gateway out can be seen in the distance. On the windowsill is a slip of paper.")
            elif (command.find("ex") == 0):
                  examine(command)
            else :
                  print("That command could not be recognized")
                  isEnd = True


if __name__ =="__main__":
      main()



