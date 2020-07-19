import wget
import shutil
import os
dl_cookpoint='../../site_templates/pdfs_sites/CookpointMenuTODAY.pdf'
master_cookpoint='../../site_templates/pdfs_sites/cookpoint_master_menu.pdf'
URL = 'http://www.cookpoint.cz/files/1062_menu.pdf'

def download_cookpoint():
    print('START--->[ Cookpoint ]---->: ', end=' ')
    try:
        wget.download(URL, dl_cookpoint)
        # avoids MenuTODAY (1).pdf  problem
        shutil.copy(dl_cookpoint, master_cookpoint)
        os.remove(dl_cookpoint)
    except:
        print("Download: Error, ")
        raise Exception
    else:
        print("Download: OK, DONE ")


download_cookpoint()