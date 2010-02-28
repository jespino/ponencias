default: fs.pdf

fs.pdf: fs.tex fs_intro.tex fs_ext.tex
	pdflatex fs.tex
	pdflatex fs.tex

clean:
	rm -f fs.log fs.out fs.toc fs.nav fs.snm fs.vrb *.aux fs.pdf

dist: fs.pdf
	rm -f fs.log fs.out fs.toc fs.nav fs.snm fs.vrb *.aux
