%.html : %.rst
	rst2html $< > $@

view : 
	see *.html

clean :
	rm -f *.html

.PHONY :
	clean view
