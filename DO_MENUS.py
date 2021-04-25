import importlib
import shutil
import os

gbl = globals()

all_areas = {
    'centrum': ['morgal', 'stopkova', 'varna', 'mezzanine', 'padowetz', 'charlies', 'mamut', 'pivniburza', 'krcma', 'tahu'],
    'londynske': ['babeta', 'mitrovski', 'pupek', 'sediveho', 'tesare', 'makalu', 'union', 'iqmoravka'],
    'zbrojovka': ['svitavska', 'kone', 'ubadinu', 'upavouka', 'musilce', 'onyx', 'osmicce']
}

os.chdir('all_scrapers')
for area in list(all_areas):
    print(f"========== {area.capitalize()} Section Start ===============")
    os.chdir(area)
    shutil.copy(f'../../site_templates/{area}.html', f'../../pages/{area.replace("_", "-")}.html')
    for restaurant in all_areas[area]:
        moduleToImport = f'.{area}.{restaurant}'
        gbl[moduleToImport] = importlib.import_module(moduleToImport, package='all_scrapers')
    os.chdir('..')
    print(f"========== {area.capitalize()} Section End ===============")
