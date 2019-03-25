

mkdir springer 
cp -r book.tex papers.bib svmonodo.cls t4do.sty fig latex_figs mov fem-book-4print.pdf springer/.  
tar cf springer.tar 
gzip springer.tar.gz 

