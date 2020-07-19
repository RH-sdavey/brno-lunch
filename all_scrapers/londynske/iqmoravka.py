import wget
import shutil
import os
import datetime

dl_iq = '../../site_templates/pdfs_sites/MenuIQ.pdf'
master_iq = '../../site_templates/pdfs_sites/menuIQ_master.pdf'
URL = 'http://www.iqrestaurant.cz/moravka/'


def download_pdf_file():
    print('START --->[ IQ MORAVKA ]---->: ', end=' ')
    try:
        wget.download(URL + get_todays_pdf(), dl_iq)
        # avoids MenuTODAY (1).pdf  problem
        shutil.copy(dl_iq, master_iq)
        os.remove(dl_iq)
    except:
        print("Download: Error, ")
        raise Exception
    else:
        print("Download: OK, DONE")


def get_todays_pdf():
    today_as_a_number = datetime.datetime.today().weekday()
    if today_as_a_number == 0:  # Mon = 0
        pdf_file = '01 PONDĚLÍ.pdf'
    elif today_as_a_number == 1:  # Tues = 1
        pdf_file = '02 ÚTERÝ.pdf'
    elif today_as_a_number == 2:  # Wed = 2
        pdf_file = '03 STŘEDA.pdf'
    elif today_as_a_number == 3:  # Thurs = 3
        pdf_file = '04 ČTVRTEK.pdf'
    elif today_as_a_number == 4:  # Fri = 4
        pdf_file = '05 PÁTEK.pdf'
    elif today_as_a_number == 5:  # Sat = 4
        pdf_file = '05 PÁTEK.pdf'
    elif today_as_a_number == 6:  # Sun = 4
        pdf_file = '01 PONDĚLÍ.pdf'
    return pdf_file


download_pdf_file()
