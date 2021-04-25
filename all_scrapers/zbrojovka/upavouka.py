import wget
import shutil
import os
dl_pavouka = '../../site_templates/pdfs_sites/PavoukaMenuTODAY.pdf'
master_pavouka = '../../site_templates/pdfs_sites/pavouka_master_menu.pdf'
URL = 'http://www.upavouka.cz/menu/Upavouka_denni_nabidka.pdf'


def download_pavouka():
    print('START --->[ Pavouka ]---->: ', end=' ')
    try:
        wget.download(URL, dl_pavouka)
        # avoids MenuTODAY (1).pdf  problem
        shutil.copy(dl_pavouka, master_pavouka)
        os.remove(dl_pavouka)
    except:
        print("Download: Error, ")
        raise Exception
    else:
        print("Download: OK, DONE ")


download_pavouka()
