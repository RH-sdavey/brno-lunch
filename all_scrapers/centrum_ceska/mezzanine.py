import wget
import shutil
import os

dl_iq = '../../site_templates/pdfs_sites/MenuMezzanine.pdf'
master_iq = '../../site_templates/pdfs_sites/MenuMezzanine_master.pdf'
URL = 'http://www.cafe-mezzanine.cz/data/napojak2018-06.pdf'


def download_pdf_file():
    print('START --->[ Mezzanine ]---->: ', end=' ')
    try:
        wget.download(URL, dl_iq)
        # avoids MenuTODAY (1).pdf  problem
        shutil.copy(dl_iq, master_iq)
        os.remove(dl_iq)
    except:
        print("Download: Error, ")
        raise Exception
    else:
        print("Download: OK, DONE")


download_pdf_file()
