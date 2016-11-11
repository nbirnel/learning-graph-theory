%.html : %.rst
	rst2html $< > $@

view : 
	see *.html
