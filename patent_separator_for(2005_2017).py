import re
import os

def writeToFile(patent_document, file_name):    
    if not os.path.exists("output"):        
        os.makedirs("output")
        
    file_name = "output/" + str(file_name)    
    with open(file_name, "w") as patent_file:        
        for line in patent_document:            
            patent_file.write(line)
            

def getPatentNumber(patent_document):    
    for line in patent_document:
        if "file=" in line:            
            file_name_pattern = re.search(r"([^US])([0-9])+([A-Z])*([0-9])*(-)([0-9])+(.)(XML|xml)", line)
            file_name = file_name_pattern.group()
            return file_name

    return 0

patent_dir = "2011"
file_list = os.listdir(patent_dir)

for xml_source_file in file_list:
    full_path = patent_dir + "/" + xml_source_file
    if os.path.isfile(full_path):        

        counter = 0
           
        with open(full_path, "r") as xml_bulk_file:               
            contents = xml_bulk_file.readlines()                
            start_position=0                
            start_syntax = "<?xml version="              
               
            for line in contents:            
                if start_syntax in str(line) and counter > 0:                                
                    patent_document = contents[start_position:counter - 1]                
                    file_name = getPatentNumber(patent_document)                
                    writeToFile(patent_document, file_name)               
                    start_position = counter                               
                
                counter = counter + 1          
      

            patent_document = contents[start_position:counter - 1]
            file_name = getPatentNumber(patent_document)
            writeToFile(patent_document, file_name)


    
