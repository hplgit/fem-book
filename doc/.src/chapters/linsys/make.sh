#!/bin/sh
# Just a preliminary make script while transforming latex to doconce
name=cg
preprocess -DFORMAT=pdflatex ../newcommands_keep.p.tex > newcommands.tex
doconce format pdflatex $name --latex_code_style=blue1 --allow_refs_to_external_docs
if [ $? -ne 0 ]; then
    exit
fi
pdflatex $name
pdflatex $name
