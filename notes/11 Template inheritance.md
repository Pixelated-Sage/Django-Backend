**This gonna help us in recursive use of templates which are repeatedly needed in the files

- **With the help of html file lets see how we can do this
    - **Add a folder inside the templates called base inside that `base.html` file
    - **file structure
        ![Pasted image 20250610122143](img/Pasted%20image%2020250610122143.png)
    - then in base file add the code which is repeatedly used in every html file with using a special tag 
      `{% block content %}` __ `{% endblock content %}`
        ![Pasted image 20250610122400](img/Pasted%20image%2020250610122400.png)
        
    - then use the tags in the `index.html` file too 
        ![Pasted image 20250610122721](img/Pasted%20image%2020250610122721.png)
- we make a semantics folder inside the templates/restaurant
    ![Pasted image 20250611110956](img/Pasted%20image%2020250611110956.png)
    
- Then put the header holder inside that semantics and make a component of it 
- then we have to show it in the base file so we add the code into the `base.html`

    ![Pasted image 20250611111133](img/Pasted%20image%2020250611111133.png)
- same we gonna do for the footer