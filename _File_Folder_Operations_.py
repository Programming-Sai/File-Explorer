
import os 
import shutil 
import logging
from datetime import datetime




''' Logging Module Configuration '''

logging.basicConfig( filename='/storage/emulated/0/Download/CodingPython/File_Explorer/Xtra_Files/d.log' , 
level =logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)




path = '/storage/emulated/0/Download/CodingPython/File_Explorer/Project Sandboxz'

  


class FileFolderOperations:


# This class provides various file and folder operations.


  
 
  def rename(self, old_name, new_name, path):
    
    """  
        Rename a file or folder.

        Parameters:
        old_name (str): The original name of the file/folder.
        new_name (str): The new name to assign.
        path (str): The path to the file/folder.

        Returns:
        bool: True if the operation is successful, False otherwise.
    """       
   
    
    if os.path.isfile(os.path.join(path, old_name)):
      new_name = new_name + (old_name[(old_name.find('.')) :])
    
    try:
      os.replace(
      os.path.join(path, old_name),
      os.path.join(path, new_name)
      )
      logging.info(f"{'Folder//' if os.path.isdir(os.path.join(path, new_name)) else 'File//' if os.path.isfile(os.path.join(path, new_name))  else '----?// '} ----{old_name} was renamed to {new_name} Successfully")
      
      
      
      return True 
      
    except FileNotFoundError:
      print(f'Sorry {old_name} was not found')
      logging.error(f'File Not Found Error ( {old_name} ) -- RENAME operation')

    except FileExistsError:
      print(f'Sorry {new_name} already exists')     
      logging.error(f'{new_name} already exists -- RENAME operation')  
              
    except PermissionError:
      print(f'Permission Required to rename {old_name}')
      logging.error(f'Permission Required to rename {old_name} -- RENAME operation')
            
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        logging.error(f"An unexpected error occurred -- RENAME operation: {str(e)}")     
    return False  
      

  
      
          
              
                  
                          
                  
  def cut(self, src, to, path):
   
   """
        Move a file or folder.

        Parameters:
        src (str): The source file/folder.
        to (str): The destination path.
        path (str): The current path.

        Returns:
        bool: True if the operation is successful, False otherwise.
       
    
    """
   
   
   try:
     shutil.move(src, to)
     
     
     logging.info(f"{'Folder//' if os.path.isdir(to)  else 'File//' if os.path.isfile(to)  else '----?// '} ----{src} was moved to {to} Successfully")
      
   
     return True 
     
     
   except FileNotFoundError:
     print(f'Sorry {src} was not found ----- move module')
     logging.error(f'File Not Found Error ( {src} ) -- CUT operation')

   except PermissionError:
      print(f'Permission is Required to perform move operation')
      logging.error(f'Permission is Required to perform move operation -- CUT operation')
      
      
   except FileExistsError:
      print(f'Sorry {to} already exists')     
      logging.error(f'{to} already exists -- CUT operation')  
      
   except shutil.Error:
      print(f'Sorry {src} already exists in {to} ')     
      logging.error(f'{src} already exists in {os.path.basename(path, to)}-- CUT operation')  
      
   except Exception as e:
        print(f"An unexpected error occurred during MOVE operation': {str(e)}")
        logging.error(f"An unexpected error occurred during MOVE operation 🤣 : {str(e)}")
      
   return False  
      
      
      
      
  
      
          
  @staticmethod     
  def copy_num(folder):
      
      """
        Shows the number of times a folder has been copied
        it's used to generate new names for copied folder data

        Parameters:
        folder(str): this is the name of the folder to be copied 
        
        Returns
        It returns the number of times a folder has been copied 
      """
      
      with open("Xtra_Files/COPIED.txt", 'r') as f:
        copied = []
        for line in f.readlines():
            copied.append(line.strip())           
      for fold in copied:      
        if folder in fold:
          fol = copied.index(fold)
          num_inc = int(copied[fol][(copied[fol].find(',')) +1 :]) + 1
          copied[fol] = f'{folder},{num_inc}'
          with open("COPIED.txt", 'w') as f:
                for item in copied:
                    f.write(f"{item}\n")
          return num_inc
          
       
      with open("Xtra_Files/COPIED.txt", 'a') as f:
            f.write(f'{folder},0\n')
      return 0
          
        
      
    
                  
                      
                              
      
  def copy(self, from_, to_, path):
    
    """
        Copies a file or folder.

        Parameters:
        from_ (str): The source file/folder.
        to_ (str): The destination path.
        path (str): The current path.

        Returns:
        bool: True if the operation is successful, False otherwise.
       
    
    """
    try:
      if os.path.isfile(from_):       
        shutil.copy(from_,to_)
        
        logging.info(f"{'File//'} ----{from_} was copied to {to_} Successfully")
        
    
        return True    
   
      elif os.path.isdir(from_):
          try:
            f_idx = FileFolderOperations().copy_num(os.path.basename(from_))
            to_ =  to_ + '/' + os.path.basename(from_) + f'_copy({f_idx})'        
            shutil.copytree(from_, to_)
          
              
          except shutil.Error as e:
           for src, dst, error in e.args[0]:
             if "Operation not permitted" in str(error):
               logging.info(f"{'Folder//' } ----{from_} was copied to {to_} Successfully")         
             
               return True 
             else:
               raise e   
      else:
       print(f'{from_} is not recognised')
       
    
        
        
    except (PermissionError, IsADirectoryError, FileNotFoundError, shutil.SameFileError) as e:
      logging.error(f'An error has occurred during COPY operation : {str(e)}')   
      print(f'\n\n\nAn Error has occurred 😅 :{str(e)}\n\n\n')
    return False 
            
            
            
  
            
                      
                                
                                          
                                                           
            
  def delete(self, to_del, path):  
   """
        Deletes a file or folder.

        Parameters:
        to_del(str): The file/folder to be deleted 
        path (str): The current path.

        Returns:
        bool: True if the operation is successful, False otherwise.
       
    
   """
  
  
  
   try:
     if os.path.isfile(os.path.join(path, to_del)):     
       os.remove(os.path.join(path, to_del))
       
       logging.info(f"{'File//'} ----{to_del} was deleted Successfully")
        
      
       return True 
     elif os.path.isdir(os.path.join(path, to_del)): 
       shutil.rmtree(os.path.join(path, to_del))
       
       logging.info(f"{'Folder//'} ----{to_del} was deleted Successfully")
        
   
       return True 
       
     else:
       print(f'{to_del} is not recognised')
       logging.error(f'Attempted Delete Operation on Unknown.')
       
  
  
   except (PermissionError, IsADirectoryError, FileExistsError, FileNotFoundError,OSError) as e:
      logging.error(f'An error has occurred during DELETE operation : {str(e)}')   
      print(f'\n\n\nAn Error has occurred:{str(e)}\n\n\n')
   return False 

 
 
 
 
 
 
 
  @staticmethod
  def folder_size(folder_path):
    
    """
        Calculates the size of a folder .

        Parameters:
        folder_path(str): the path of the folder

        Returns:
        int:  tuple of the folder size and number of files
       
    
    """
    
    folder_size = 0
    num_files = 0
    for roots, dirs, files in os.walk(folder_path):
      for file in files:
        file_path = os.path.join(roots, file)
        folder_size += os.path.getsize(file_path)
        num_files += 1
 
    return folder_size, num_files
 
 
 
 
 
  def get_properties(self, of, path):
   
   """
        Gets the Metadata of  a file or folder.

        Pardestination. 
        of(str): the file/folder whose metadata is needed for
        path (str): The current path.

        Returns:
        bool: True if the operation is successful, False otherwise.
       
    
   """
   
   try:
      file_folder_info = os.stat(os.path.join(path, of))
      
      if os.path.isfile(os.path.join(path, of)):
        size = file_folder_info.st_size
        num_files = 0
       
       
      elif os.path.isdir(os.path.join(path, of)):
        all_size = FileFolderOperations.folder_size(os.path.join(path, of))
        size = all_size[0]
        num_files = all_size[-1]
        
        
        
      else:
        print(f'{of} is not recognised')
        size = 0
        num_files = 0
        
      print(f'''
Name : {of} \n
Size : {size} bytes \n
Number of Files: {num_files} \n
Creation Time:\n{datetime.fromtimestamp(os.path.getctime(os.path.join(path, of)))}\n
Modification Time:\n{datetime.fromtimestamp(os.path.getmtime(os.path.join(path, of)))}\n
Last Accessed Time:\n{datetime.fromtimestamp(os.path.getatime(os.path.join(path, of)))}\n

''')
      logging.info(f"{'Folder//' if os.path.isdir(os.path.join(path, of)) else 'File//' if os.path.isfile(os.path.join(path, of))  else '----?// '} ---- Metadata for {of} was accessed Successfully")
      
   
      
      return True 

   except (PermissionError, IsADirectoryError, FileExistsError, FileNotFoundError,OSError) as e:
      logging.error(f'An error has occurred during  GET PROPERTIES operation : {str(e)}')   
      print(f'\n\n\nAn Error has occurred:{str(e)}\n\n\n')
   return False 



