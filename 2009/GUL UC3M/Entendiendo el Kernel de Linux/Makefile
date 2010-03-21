default: linux.pdf

linux.pdf: linux.tex linux_process.tex linux_mm.tex linux_io.tex linux_interrup.tex linux_intro.tex linux_boot.tex linux_fin.tex
	pdflatex linux.tex
	pdflatex linux.tex

clean:
	rm -f linux.log linux.out linux.toc linux.nav linux.snm linux.vrb *.aux linux.pdf

dist: linux.pdf
	rm -f linux.log linux.out linux.toc linux.nav linux.snm linux.vrb *.aux
