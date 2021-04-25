import wget
import shutil
import os
dl_tesare = '../../site_templates/pdfs_sites/TesareMenuTODAY.pdf'
master_tesare = '../../site_templates/pdfs_sites/tesare_master_menu.pdf'
URL = 'http://www.utesare.cz/Menu.pdf'


def download_tesare():
    print('START --->[ Tesare ]---->: ', end=' ')
    try:
        wget.download(URL, dl_tesare)
        # avoids MenuTODAY (1).pdf  problem
        shutil.copy(dl_tesare, master_tesare)
        os.remove(dl_tesare)
    except:
        print("Download: Error, ")
        raise Exception
    else:
        print("Download: OK, DONE ")


download_tesare()
