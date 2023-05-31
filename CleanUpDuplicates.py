import os
# create a function that is going to delete the files that have the same name inside the folder
def delete_files_with_same_name():
    # get the list of files in the folder
    files = os.listdir("generatedFiles")
    # create a dictionary to store the file names and the number of times they appear
    filesDict = {}
    # iterate over the files
    for file in files:
        
        fileName = file.split("__")[0]
        
        # if the file name is not in the dictionary, add it with the value 1
        if fileName not in filesDict:
            filesDict[fileName] = 1
        # if the file name is already in the dictionary, increment the value by 1
        else:
            # delete the file
            os.remove("generatedFiles/" + file)
            
   

# delete_files_with_same_name()
