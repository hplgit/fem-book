

mkdir springer 
cp -r book.tex book.do.txt papers.bib svmonodo.cls newcommands_keep.tex t4do.sty fig latex_figs mov fem-book-4print.pdf dotxt src springer/.  
tar -cf springer.tar springer  
gzip springer.tar 

