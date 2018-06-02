import os
import urllib

from bs4 import BeautifulSoup


def writeToTXT(patent_infos, file_name):
    file_name = "/media/h/06587af7-85ec-442b-872d-54fa3efc020e/2009_txt/" + str(patent_file_name) +".txt"    
    with open(file_name, "w") as txt_file:        
        for patent_info in patent_infos:            
            txt_file.write(str(patent_info))

patent_dir = "output_2009_xmls"
file_list = os.listdir(patent_dir)


for patent_file_name in file_list:
    full_path = patent_dir + "/" + patent_file_name
    if os.path.isfile(full_path):
        with open(full_path, "r") as patent_document_file:
            patent_contents = "".join(patent_document_file.readlines())
            
            soup = BeautifulSoup(patent_contents, "xml")
            #doc_id = soup.find("document-id").get_text()
            invention_title = soup.find("invention-title").get_text()

            #abstract = soup.find("abstract").get_text()
            description = soup.find("description").get_text()
            patent_infos = []
            patent_info = []
            #patent_info.append(doc_id)
            patent_info.append(invention_title)
            #patent_info.append(abstract)
            patent_info.append(description)
            
            patent_infos.append(patent_info)
            patent_info = []
            
            file_name = "output/" + str(patent_file_name)
            
    writeToTXT(patent_infos, file_name)
    
