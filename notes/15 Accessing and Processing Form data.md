
**As the data comes into the form we can check and manipulate it as we want 
- there are many modules which do the checking and many other things in the django by its own making it easy to work with the data


`views.py`

![[Pasted image 20250623170357.png]]


![[Pasted image 20250623170341.png]]


 
 **now define the logout of the user after log in 
- we have to create a new view class in `views.py`(all it do is if a request come for logout then this class gonna handle what to do )
	![[Pasted image 20250623171053.png]]
- now urls path setup in `urls.py`
	![[Pasted image 20250623171205.png]]
- Now a bit of up-gradation in navbar so login use can see logout and logout user and see login (with a bit of python)
	![[Pasted image 20250623171357.png]]
	