
**This gonna help us in recursive use of templates which are repeatedly needed in the files

- **With the help of html file lets see how we can do this
	- **Add a folder inside the templates called base inside that `base.html` file
	- **file structure
		![[Pasted image 20250610122143.png]]
	- then in base file add the code which is repeatedly used in every html file with using a special tag 
	  `{% block content %}` __ `{% endblock content %}`
		![[Pasted image 20250610122400.png]]
		
	- then use the tags in the `index.html` file too 
		![[Pasted image 20250610122721.png]]

- this is inheritance
