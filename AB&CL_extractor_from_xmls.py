import os
import urllib
import csv
from bs4 import BeautifulSoup

def writeToTXT(description, file_name):
    
    file_name = "output/" + str(patent_file_name) +".txt"    
    with open(file_name, "w") as txt_file:        
        #for patent_info in patent_infos:
        #txt_file.write(str(IPC))
        txt_file.write(str(real_doc_id))
        txt_file.write(str(real_invention_title))
        txt_file.write(str(abstract))
        #txt_file.write(str(claim))
        
patent_dir = "input_xmls"
file_list = os.listdir(patent_dir)

for patent_file_name in file_list:
    full_path = patent_dir + "/" + patent_file_name
    if os.path.isfile(full_path):
        with open(full_path, "r") as patent_document_file:
            patent_contents = " ".join(patent_document_file.readlines())
            
            soup = BeautifulSoup(patent_contents, "xml")
            #IPC = soup.find("section").get_text()
            doc_id = soup.find("document-id").get_text()
            real_doc_id = "".join(doc_id.split())
            invention_title = soup.find("invention-title").get_text()
            real_invention_title = " ".join(invention_title.split())
            abstract = soup.find("abstract").get_text()
            description = soup.find("description").get_text()
            #real_description = " ".join(description.split())
            #claim = soup.find("claim-text").get_text()
            
           #patent_infos = []
            #patent_info = []
            #patent_info.append(doc_id)
            #patent_info.append(invention_title)
            #patent_info.append(abstract)
            #patent_info.append(description)
            #print(patent_info)
            #patent_infos.append(patent_info)
            #patent_info = []            
            file_name = "output/" + str(patent_file_name)
            
    writeToTXT(description, file_name)
    
