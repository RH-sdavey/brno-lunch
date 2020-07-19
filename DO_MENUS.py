import importlib
import shutil
import os

gbl = globals()

all_areas = {
    'tech_park': ['purkynka', 'jkanas', 'rkanas', 'portoriko', 'asport', 'liquidbread', 'tri_opic', 'cookpoint', 'taste_of_india'],
    'centrum_ceska': ['morgal', 'stopkova', 'opice', 'varna', 'mezzanine'],
    'londynske': ['babeta', 'gingilla', 'mitrovski', 'pupek', 'sediveho', 'tesare', 'iqmoravka', 'makalu', 'union']
}

print(os.getcwd())
os.chdir('all_scrapers')
for area in list(all_areas):
    print(f"========== {area.capitalize()} Section Start ===============")
    os.chdir(area)
    shutil.copy(f'../../site_templates/{area}.html', f'../{area.replace("_", "-")}.html')
    for restaurant in all_areas[area]:
        moduleToImport = f'.{area}.{restaurant}'
        gbl[moduleToImport] = importlib.import_module(moduleToImport, package='all_scrapers')
    os.chdir('..')
    print(f"========== {area.capitalize()} Section End ===============")
