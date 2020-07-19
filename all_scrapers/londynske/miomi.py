# import requests
# from bs4 import BeautifulSoup
# import unidecode
# import wget
# import shutil
# import os
# dl_miomi = 'pdfs_sites/miomi.txt'
# master_miomi = 'pdfs_sites/miomi_master.html'
URL = 'http://www.sushi-miomi.cz/jidelni-listek'
# rep = "MIOMIREPLACEME"
# index_file = "index.html"


# def download_miomi():
#     try:
#         wget.download(URL, dl_miomi)
#         # avoids MenuTODAY (1).pdf  problem
#         shutil.copy(dl_miomi, master_miomi)
#         os.remove(dl_miomi)
#     except:
#         print("Download: Error, ", end=' ')
#         raise Exception
#     else:
#         print("Download: OK, ", end=' ')


# def soup_magic():
#     try:
#         with open(master_miomi, mode='r', encoding='utf8') as f:
#             filedata = f.read()
#             soup = BeautifulSoup(filedata, 'html.parser')
#             all_foods = soup.find('div', attrs={'id': "food"})
#     except:
#         print("Soup: Error, ", end=' ')
#         raise Exception
#     else:
#         print("Soup: OK, ", end=' ')
#     finally:
#         return all_foods


# # Read in the file
# def read_file(inputfile):
#     try:
#         with open(inputfile, 'r') as file:
#             filedata = file.read()
#     except:
#         print("Read: Error, ", end=' ')
#         raise Exception
#     else:
#         print("Read: OK, ", end=' ')
#     finally:
#         return filedata


# def do_some_replacin(filedata, all_foods):
#     try:
#         filedata = filedata.replace(rep, unidecode.unidecode(str(all_foods)))
#         filedata = filedata.replace('Soups - salads', '')
#         filedata = filedata.replace('Temaki - fried roll sushi', '')
#         filedata = filedata.replace('Sashimi - sushi', '')
#         filedata = filedata.replace('Sushi menu', '')
#         filedata = filedata.replace('Nigiri Sushi', '')
#         filedata = filedata.replace('Maki sushi', '')
#         filedata = filedata.replace('Maki - rolls sushi', '')
#         filedata = filedata.replace('Inside - outside rolls', '')
#         filedata = filedata.replace('Nealkoholicke napoje', '')
#         filedata = filedata.replace('Teple napoje', '')
#         filedata = filedata.replace('Pivo', '')
#         filedata = filedata.replace('Japonske zakusky', '')
#         filedata = filedata.replace('Alkoholicke napoje', '')
#         filedata = filedata.replace('img class="" ', '')
#         filedata = filedata.replace('<img class="img-fluid" src="/images/menu.png"/>', '')
#         filedata = filedata.replace('                            </div>', '</div><hr/>')
#         filedata = filedata.replace(' class="product d-flex py-3 pl-1 pr-3 my-3" data-lightbox="', '')
#     except:
#         print("Replace: Error, ", end=' ')
#         raise Exception
#     else:
#         print("Replace: OK, ", end=' ')
#     finally:
#         return filedata


# # Write the file out again
# def write_file(inputfile, filedata):
#     try:
#         with open(inputfile, 'w') as file:
#             file.write(filedata)
#     except:
#         print("Write: Error", end=' ')
#         raise Exception
#     else:
#         print("Write: OK", end=' ')


# try:
#     print("Miomi :: ", end=" ")
#     download_miomi()
#     write_file(index_file, do_some_replacin(read_file(index_file), soup_magic()))
# except:
#     print(" ---> Miomi Error")
# else:
#     print(" ---> Miomi OK")
