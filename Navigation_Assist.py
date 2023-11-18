import os 
import shutil 
import logging
from datetime import datetime
import _File_Folder_Operations_ as FFO

''' Logging Module Configuration '''

logging.basicConfig(filename='/storage/emulated/0/Download/CodingPython/File_Explorer/e.log', 
                    level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s")



class Nav_Assist():
    """
      This class provides navigation and search assistance for folders.
    """
   
    def folder_content(self, path, current):
        
        """
        Get the list of files and folders in a directory.

        Parameters:
        path (str): The path to the directory.
        current (str): The current directory name.

        Returns:
        list: A list of tuples containing (name, path) of files and folders.
        """
        
        content_list = []
        try:
        
            content_list_folder = []
            content_list_file = []
            
            with os.scandir(path) as entries:
                for entry in entries:
                    if os.path.isdir(entry):
                        content = (entry.name, entry.path)
                        content_list_folder.append(content)

                    elif os.path.isfile(entry):
                        content = (entry.name, entry.path)
                        content_list_file.append(content)

                content_list = content_list_folder + content_list_file

            logging.info(f'{current} has been viewed---- FOLDER_CONTENT  OPERATION--') 
            return (content_list)
            
            
        except FileNotFoundError:
            print(f'{current} is not found')
            logging.error(f'{current} is not found --- FOLDER_CONTENT OPERATION--')
        except NotADirectoryError:
            print(f'{current} is not a directory')
            logging.error(f'{current} is not a directory --- FOLDER_CONTENT OPERATION--')
        except PermissionError:
            print(f'Permission is Required to create folder_content {current}')
            logging.error(f'Permission is required to create folder_content {current}')
        except (OSError, UnicodeEncodeError, TypeError, MemoryError) as e:
            print(f'Error: {str(e)}')
            logging.error(f'Error: {str(e)}')
        return (content_list)
        
        
        
        
        

    def folder_search(self, search_value, path):  
    
        """
        Search for files and folders in a directory.

        Parameters:
        search_value (str): The value to search for.
        path (str): The path to the directory.

        Returns:
        list: A list of tuples containing (root, name) of matching files and folders.
        """
       
        search_result = []
        try:
            dirs_ = []
            files_ = []
             
            for root, dirs, files in os.walk(path):
                files_ += [(root,file) for file in files]
                dirs_ += [(root, dir) for dir in dirs]
         
            d_result = [result for result in dirs_ if search_value in result[-1]] #might possibly change '==' to "in"
            f_result = [result for result in files_ if search_value in result[-1]] # to include more possible search results 
         
            search_result = d_result + f_result
            logging.info(f"The folder_search operation has been used to search for {search_value} and was {'found' if bool(search_result) else 'not found'} ") 
             
        except Exception as e:
            print(f'Error: {str(e)}')
            logging.error(f'Error: {str(e)}')
         
        return (search_result)






    def create_folder(self, name, path):
        
        """
        Creates New folders 

        Parameters:
        name (str): The name to be given to the new folder
        path (str): The path to the directory.

        Returns:
        bool: True if the operation is successful, False otherwise.
        """
        
        try:
            os.mkdir(os.path.join(path, name))
            
            logging.info(f"{name} was created Successfully-------CREATE_FOLDER")
              
            
              
            return True 
              
        except FileNotFoundError:
            logging.error(f'{os.path.basename(path)} Does not Exist-----CREATE_FOLDER ')
            print(f'{os.path.basename(path)} does not exist ')
        except PermissionError:
            logging.error(f'Permission is required to create {name}-----CREATE_FOLDER ')
            print(f'Permission is required to create {name} ')
        except FileExistsError:
            logging.error(f'{name} already exists in {os.path.basename(path)}-----CREATE_FOLDER ')
            print(f'{name} already exists in {os.path.basename(path)} ')
        except OSError as e:
            print(f"An unexpected error occurred: {e}")
            logging.error(f"An unexpected error occurred: {e}-----CREATE_FOLDER")
        return False

    
           
           
           

