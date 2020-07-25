from all_scrapers.Scraper_Controller import MasterScraper

import requests
from bs4 import BeautifulSoup
import unidecode
URL = f'http://nepalbrno.cz/weekly-menu/'
rep = "NEPALREPLACEME"
index_file = 'londynske.html'

# Beautifulsoup magic
def soup_magic():
    try:
        page = requests.get(URL)
        data = page.content
        soup = BeautifulSoup(data, 'html.parser')
        todays_menu = soup.find('tbody')
    except:
        print("Soup: Error, ", end=' ')
        raise Exception
    else:
        print("Soup: OK, ", end=' ')
    finally:
        return todays_menu


# Read in the file
def read_file(inputfile):
    try:
        with open(inputfile, 'r') as file:
            filedata = file.read()
    except:
        print("Read: Error, ", end=' ')
        raise Exception
    else:
        print("Read: OK, ", end=' ')
    finally:
        return filedata


# # Replace UNIONREPLACEME
def do_some_replacin(filedata, todays_menu):
    try:
        filedata = filedata.replace(rep, unidecode.unidecode(str(todays_menu)))
        filedata = filedata.replace('</tbody>', '')
        filedata = filedata.replace('<td><strong>', '<strong>')
        filedata = filedata.replace('</strong></td>', '</strong>')
        filedata = filedata.replace('<strong> Pondeli', '<hr/><tr></tr><strong> PONDELI')
        filedata = filedata.replace('<strong> UTERY', '<hr/><tr></tr><strong>  UTERY')
        filedata = filedata.replace('<strong>STREDA', '<hr/><tr></tr><strong>STREDA')
        filedata = filedata.replace('<strong>CTRVTEK', '<hr/><tr></tr><strong>CTVRTEK')
        filedata = filedata.replace('<strong>PATEK', '<hr/><tr></tr><strong>PATEK')
    except:
        print("Replace: Error, ", end=' ')
        raise Exception
    else:
        print("Replace: OK, ", end=' ')
    finally:
        return filedata


# Write the file out again
def write_file(inputfile, filedata):
    try:
        with open(inputfile, 'w') as file:
            file.write(filedata)
    except:
        print("Write: Error", end=' ')
        raise Exception
    else:
        print("Write: OK", end=' ')


try:
    print("Nepal :: ", end=" ")
    write_file(index_file, do_some_replacin(read_file(index_file), soup_magic()))
except:
    print(" ---> Nepal Error")
else:
    print(" ---> Nepal OK")
