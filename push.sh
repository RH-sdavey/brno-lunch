#!/bin/bash

setup_git() {
  echo "Setting git configs"
  git config --global user.email "sean.davey@tieto.com"
  git config --global user.name "RH-sdavey"
  echo "End git config"
}

do_the_scraping() {
  echo  "Starting Python Section"
  python3.7 DO_MENUS.py
  echo "Ending Python script"
}

do_some_sleeping() {
  echo "Sleeping for 5 x 9 minutes"
  for i in $(seq 1 5); do
    printf "This is the $i x 9m loop"
    sleep 9m
    echo "Starting again..."
  done
}

commit_website_files() {
  echo "Starting Git Section"
  git checkout gh-pages
  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
  echo "Ending Git Section"
}

setup_git
do_the_scraping
do_some_sleeping
commit_website_files
