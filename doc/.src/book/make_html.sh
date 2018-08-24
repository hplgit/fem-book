#!/bin/bash
set -x

name=book
CHAPTER=chapter
BOOK=book
APPENDIX=appendix

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

pwd
preprocess -DFORMAT=html ../chapters/newcommands_keep.p.tex > newcommands_keep.tex

opt="CHAPTER=$CHAPTER BOOK=$BOOK APPENDIX=$APPENDIX --encoding=utf-8 --allow_refs_to_external_docs"

# Compile Bootstrap HTML
html=fem-book
system doconce format html $name $opt --html_style=bootswatch_readable --html_code_style=inherit --html_output=$html --without_solutions --without_answers
system doconce split_html $html.html

hash=82dee82e1274a586571086dca04d00308d3a0d86  # "book with solutions"
# Compile Bootstrap HTML with solutions
html=fem-book-sol
system doconce format html $name $opt --html_style=bootswatch_readable --html_code_style=inherit --html_output=$html #--without_solutions --without_answers
system doconce split_html $html.html
#cp password.html fem-book-sol.html
#doconce replace DESTINATION "$html" fem-book-sol.html
#doconce replace PASSWORD "d!e!cay" fem-book-sol.html

# Publish
repo=../../..
dest=${repo}/doc/pub/book
if [ ! -d $dest ]; then mkdir $dest; fi
if [ ! -d $dest/html ]; then mkdir $dest/html; fi
if [ ! -d $dest/sphinx ]; then mkdir $dest/sphinx; fi

cp *book*.html ._*book*.html $dest/html
figdirs="fig mov"
for figdir in $figdirs; do
    # slash important for copying files in links to dirs
    if [ -d $figdir/ ]; then
        cp -r $figdir/ $dest/html
    fi
done

cd $dest
git add .
