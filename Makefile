%.html : %.rst
	rst2html $< > $@

view : 
	see *.html

clean :
	rm -f *.html

venv :
	virtualenv -p `which python3` venv
	@echo 'now . venv/bin/activate'

freeze :
	pip freeze >requirements.txt

.PHONY :
	clean view
