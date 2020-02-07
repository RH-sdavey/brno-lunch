#!/bin/sh

setup_git() {
  git config --global user.email "sean.davey@tieto.com"
  git config --global user.name "Sean Davey"
}

commit_website_files() {
  git checkout master
  git add index.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add master https://${LUNCH_TOKEN}@github.com/tieto_lunch.git > /dev/null 2>&1
  git push --quiet --set-upstream origin master
}

echo "Starting Git Section"
setup_git
commit_website_files
upload_files
echo "Ending Git Section"
