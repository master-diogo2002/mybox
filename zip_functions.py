from zipfile import ZipFile
import os


class zip_files:
    def __init__(self):
        pass


    def get_all_file_paths(self,directory):
    
        # initializing empty file paths list
        file_paths = []
    
        # crawling through directory and subdirectories
        for root, directories, files in os.walk(directory):
            for filename in files:
                # join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
    
        # returning all file paths
        return file_paths        
    
    def writezip(self,pasta):
        # path to folder which needs to be zipped
        directory = f'./ficheiros/{pasta}'
    
        # calling function to get all file paths in the directory
        file_paths = main_=os.listdir(directory)
        # print(file_paths)
        # printing the list of all files to be zipped
        print('Os seguintes ficheiros vao ser zipados:')
        for file_name in file_paths:
            print(file_name)
    
        # writing files to a zipfile
        with ZipFile(f'temp/{pasta}.zip','w') as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(directory+f'/{file}')
    
        print('Todos os ficheiros zipados')        
    


    def list_files_zip(self):
        with ZipFile('./ficheiros/test/my_python_files.zip', 'r') as zipObj:
            listOfFileNames = zipObj.namelist()
            print(listOfFileNames)
            if 'zip_teste/ola.txt' in listOfFileNames:
                zipObj.extract('zip_teste/ola.txt', 'temp')
        


