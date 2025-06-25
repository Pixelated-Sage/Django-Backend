**In py files we can do to many things in django as we are working with the form we can do  
- required field
- password visibility
- add a button which allow to show password when clicked
- and many more

`form.py`

![Pasted image 20250623172445](img/Pasted%20image%2020250623172445.png)

 - Now to make a check box which allows us to show password and hide it - first we have to make a field for it in `form.py`
    ![Pasted image 20250623173548](img/Pasted%20image%2020250623173548.png)

- then using the javascript in the Login.html in `<script>` tag we can use the login to see the text
    ![Pasted image 20250623173745](img/Pasted%20image%2020250623173745.png)


**Result
![Pasted image 20250623173811](img/Pasted%20image%2020250623173811.png)


![Pasted image 20250623173821](img/Pasted%20image%2020250623173821.png)


### Customization in Views.py

- django is pretty flexible so lets do some customization 

if we enter wrong password or username so in this condition the page should show some error lets make it 

![Pasted image 20250623174453](img/Pasted%20image%2020250623174453.png)

in this way we can add some logic into the views.py file with ease

**Result

![Pasted image 20250623174528](img/Pasted%20image%2020250623174528.png)