#!/bin/bash

setup_git() {
  git config --global user.email "sean.davey@tieto.com"
  git config --global user.name "RH-sdavey"
}

commit_website_files() {
  git checkout master
  git add index.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  #git remote add origin RH-sdavey:$LUNCH_TOKEN@github.com:RH-sdavey/tieto_lunch.git > /dev/null 2>&1
  echo " git remote add finshed with  : $? "
  git push --quiet --set-upstream origin master
}

echo  "Starting Python Section"
python3.7 LUNCH_SCRAPER.py
echo "Ending Python script"

echo "...."

echo "Starting Git Section"
setup_git
commit_website_files
upload_files
echo "Ending Git Section"
