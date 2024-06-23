import os 
import shutil 
import logging
from datetime import datetime
import _File_Folder_Operations_ as FFO
import Navigation_Assist as folder




class CLI:
    """
    This class represents the Command-Line Interface for the file and folder management system.
    """

    # Class Attributes Initialisation 
    
    ff = FFO.FileFolderOperations()
    directory = folder.Nav_Assist()
    path = FFO.path 
    commands = ['.RENAME_', '.CUT_', '.COPY_', '.DELETE_', '.INFO_', '.OPEN_', '.PASTE_']
     
              
    def cmd_input(self):  
    
        """
          Get user input for command and parameter.
  
          Returns:
          tuple: A tuple containing the command and parameter.
        """
          
        cmd = ''
        while True:
            
            cmd = input('>>>  ').upper()
             
            if '_' in cmd and cmd[:(cmd.find('_'))+1] in self.commands and cmd[(cmd.find('_'))+1:] in [str(a) for a in range(10)] :
                return (cmd[:(cmd.find('_'))+1],  int(cmd[(cmd.find('_'))+1:]))
                break 
           
            elif cmd in ['.EXIT', '.BACK', '.HELP', '.DISPLAY', '.SEARCH', '.NEW']:
                return (cmd, 1)
                break
          
    
    
    
    
    
    def cmd_parameter_input(self):
        
        """
        Get user input for command parameter.

        Returns:
        str: The command parameter.
        """
        
        cmd_parameter = "/"       
        while '/' in cmd_parameter or '.' in cmd_parameter:
          cmd_parameter = input('>> ')
        return (cmd_parameter)
          



    def nav_input(self):   
    
        """
        Get user input for navigation.

        Returns:
        str: The tuple of the navigation command, and the navigation parameter.
        """
                   
        nav_input = ''        
        while True:         
          nav_input = input('> ').upper()
          if '_' in nav_input and nav_input[:(nav_input.find('_'))+1] in self.commands[5:] and nav_input[(nav_input.find('_'))+1:] in [str(a) for a in range(10)] :
                return (nav_input[:(nav_input.find('_'))+1],  int(nav_input[(nav_input.find('_'))+1:]))
                break 
           
          elif nav_input == '.BACK':
                return (nav_input, 1)
                break
        
          



    
    def help(self):
        
        """
        Serves as a user manual for the program .
        
        """
        
        with open('help.txt', 'r') as help:
          print(help.read())
        


    def display(self):
         
         """
          Displays the contents of the current folder.
        
         """
         
        #  print(' '*2000)
         os.system('cls' if os.name == 'nt' else 'clear')
         print(os.path.basename(self.path))
         content = self.directory.folder_content(self.path, '')
         
         for line, item in enumerate((content), start = 1):
           print(f'{str(line) +")" :3} ~~ {item[0]}')



    
      
      
    def back(self):       
    
        """
          Assists in navigation by changing directory 
          to previous directory 
          
          Returns:
          str: The current directory.
        """
    
        current_directory = ''
        if os.path.basename(self.path) == 'Project Sandboxz':
            current_directory = self.path
            return current_directory
        else:
            current_directory = os.path.dirname(self.path)
            return current_directory
            
        
    
    
    
    def forward(self, to):
        
        """
        Assists in navigation by changing directory 
        to next directory/file
        
        Parameter
        to(str): the next file/folder to move to 

        Returns:
        str: The current directory.
        """
        
        current_directory = os.path.join(self.path, to)  
        return current_directory  
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    @staticmethod
    def clear():
        
        """
          Clears the screen, then shows the current directory content 
        """
        
        x = CLI()
        os.system('cls' if os.name == 'nt' else 'clear')
        x.display()
        





    def open(self, old, next_action = 'x'):
      
      """
        Opens a folder or file

        Parameter
        old(str): the file/folder to opened
        next_action(str): activates the next action to be taken

      """
      
      folders = self.directory.folder_content(os.path.join(self.path, old), os.path.basename(os.path.join(self.path, old)))      
      folder_list =  [folder[0] for folder in folders]     
      if os.path.isdir(os.path.join(self.path, old)):              
              if len(folder_list) == 0:
                  print("Folder Empty")                                         
              else:
                  print(folder_list)  
                  self.change_directory(self.forward(old))
                  CLI.clear()                          
      else:
            if os.path.splitext(old)[1] in [".mp3", ".wav", ".flac", ".ogg", ".aac", ".m4a", ".wma", ".aiff", ".mid", ".midi"]:
               print(f"\n{old}, audio file cannot be played on this program\n")   
                
            elif os.path.splitext(old)[1] in [ ".txt", ".csv", ".log", ".xml", ".json", ".html", ".htm", ".md", ".rtf", ".doc"]:
               try:
                 with open(old, 'r') as text:
                    print(text.read())

               except Exception:
                 print(f"{old}, text file could not be read")
                 
            elif os.path.splitext(old)[1] in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".ico", ".svg", ".psd"]:
                print(f"\n{old}, image file cannot be displayed on this program\n")   
                
            elif os.path.splitext(old)[1] in [ ".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm", ".m4v", ".3gp", ".mpeg"]:
                print(f"\n{old}, video file cannot be played on this program\n")   

            else:
                print(f'\n{old} file cannot be read in this program\n')
                    
      self.take_action()  if next_action == 'x' else ''





    def paste(self, at):    
      """
        Just returns the destination of any paste operation 

        Returns:
        str: destination .
      """
      return at
      


    def past(self, parameter = 'x'):
        
        """
        Modifies command and navigation command inputs for 
        easy usage by other methods
        
        Parameter
        parameter(str): activates which command to use

        Returns:
        str: Tuple of the command, current and destination point.
        
        """
        
        folders = self.directory.folder_content(self.path, '')
        folder_list =  [folder[0] for folder in folders]
        folder_path_list = [folder[-1] for folder in folders]       
        file_folder = 0
        while file_folder <= 0 or file_folder >= len(folder_list)+1:
            cmd, file_folder =  self.cmd_input() if parameter == 'x' else self.nav_input()         
    
        old = folder_list[(file_folder)-1]
        at = folder_path_list[(file_folder)-1]
        
        return (cmd, old, at)
        
        
        
        



    def nav(self, mold, action):
          
          """
          Navigates the Copy or Cut commands
          
          Parameter
          action(str): activates which command to use
          mold(str): holds the previous directory 
  
          
          """
          
          cmd2, old, at = self.past(parameter = 's')
          
          
          if cmd2 == self.commands[5]:
            self.open(old, next_action = 's')
            self.nav(mold, action)
            
          elif cmd2 == self.commands[6]:    
          
            self.ff.copy(mold, self.paste(at), self.path) if action == 'copy' else self.ff.cut(mold, self.paste(at), self.path)
            print(f'{os.path.basename(mold)} was {"copied" if action == "copy" else "cut"} to {old} successfully\n')
            self.take_action()
            
            
          
          elif cmd2 == ".BACK":
                self.change_directory(self.back())
                CLI.clear()
                self.nav(mold, action)
            






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def take_action(self) : 
    
      
        """
        Performs all commands
        It also serves as the 
        main method of the entire
        class.

        """
        cmd, old, at = self.past()
        
        if cmd == self.commands[0]:
            new_name = self.cmd_parameter_input()
            self.ff.rename(old, new_name, self.path)
            CLI.clear()    
            self.take_action()    
                         
              
        elif cmd == self.commands[1]:   
          mold = at
          self.nav(mold, 'cut')
            
            
            
                  
        elif cmd == self.commands[2]:
          mold = at
          self.nav(mold, 'copy')
          
                    

        elif cmd == self.commands[3]:
          verification = input(f"Are You Sure You Want To Delete -- {old} -- ?.... (Y/N)   ").upper()
          if verification == 'Y':
              self.ff.delete(old, self.path)
              print(f"{old} was deleted successfully")      
              folders = self.directory.folder_content(os.path.join(self.path, old), os.path.basename(os.path.join(self.path, old)))      
              folder_list =  [folder[0] for folder in folders]                          
              if len(folder_list) == 0:
                    print("Folder Empty")
                    self.change_directory(self.back())              
              CLI.clear()     
              self.take_action()
                
               
                   
        elif cmd == self.commands[4]:
           self.ff.get_properties(old, self.path)
           self.take_action()
        
        elif cmd == self.commands[5]:
          self.open(old)                   
          self.take_action()
        
             
        
        elif cmd == '.NEW':
          new = self.cmd_parameter_input()
          self.directory.create_folder(new, self.path)
          CLI.clear()
          self.take_action()
        
        
        elif cmd == '.BACK':
          self.change_directory(self.back())
          CLI.clear()
          self.take_action()
          
         
        elif cmd == '.DISPLAY':
            self.display()
            self.take_action()
        
              
        elif cmd == '.SEARCH':
           target = self.cmd_parameter_input()
           search_results = self.directory.folder_search(target, self.path)
          
           if len(search_results) > 0:
             
             for line, result in enumerate(search_results, start =1):
               print(f"{line:5}).  {result[-1]}\n {result[0][(result[0].find('z') +1):]} \n")
              
           else:
             print(f'{target} was not found')
           self.take_action()
           
            
         
        elif cmd == '.EXIT':
          raise SystemExit


        elif  cmd == '.HELP':
          self.help()
          self.take_action()


    
    

    @classmethod
    def change_directory(cls, current_directory):
             
        """
        Changea the current directory based on it's parameter 
        
        Parameter
        current_directory(str): this is obtained from the back or forward methods
        
        """
        cls.path = current_directory 


          

  
    
if __name__ == '__main__':
      
    s = CLI()   
    s.take_action()
    



