

rm -rf springer 
rm springer.tar.gz
mkdir springer 
cp -r book.tex book.do.txt make.sh papers.bib papers.pub svmonodo.cls mako_code.txt newcommands_keep.tex newcommands_keep.p.tex t4do.sty fig latex_figs mov exer fem-book-4print.pdf dotxt src springer/.  
tar -cf springer.tar springer  
gzip springer.tar 

