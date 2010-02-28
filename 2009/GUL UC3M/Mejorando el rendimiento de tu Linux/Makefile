default: tunning.pdf

tunning.pdf: tunning.tex tunning_understanding_linux.tex tunning_tunning.tex tunning_intro.tex tunning_fin.tex
	pdflatex tunning.tex
	pdflatex tunning.tex

clean:
	rm -f tunning.log tunning.out tunning.toc tunning.nav tunning.snm tunning.vrb *.aux tunning.pdf

dist: tunning.pdf
	rm -f tunning.log tunning.out tunning.toc tunning.nav tunning.snm tunning.vrb *.aux
