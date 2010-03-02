default: fs.pdf

fs.pdf: fs.tex fs_intro.tex fs_ext.tex fs_fat.tex fs_ntfs.tex fs_reiserfs.tex fs_xfs.tex fs_close.tex
	pdflatex fs.tex
	pdflatex fs.tex

clean:
	rm -f fs.log fs.out fs.toc fs.nav fs.snm fs.vrb *.aux fs.pdf

dist: fs.pdf
	rm -f fs.log fs.out fs.toc fs.nav fs.snm fs.vrb *.aux
