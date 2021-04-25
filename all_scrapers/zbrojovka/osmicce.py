import wget
import shutil
import os
dl_osm = '../../site_templates/pdfs_sites/OsmicceMenuTODAY.pdf'
master_osm = '../../site_templates/pdfs_sites/Osmicce_master_menu.pdf'
URL = 'http://www.naosmicce.cz/Menu.pdf'


def download_osm():
    print('START --->[ Osmicce ]---->: ', end=' ')
    try:
        wget.download(URL, dl_osm)
        # avoids MenuTODAY (1).pdf  problem
        shutil.copy(dl_osm, master_osm)
        os.remove(dl_osm)
    except:
        print("Download: Error, ")
        raise Exception
    else:
        print("Download: OK, DONE ")


download_osm()
