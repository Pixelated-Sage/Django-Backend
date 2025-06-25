- this is used to get static and media data from the apps and use it for applications
- we have to set up the links in the `settings.py`
    ![Pasted image 20250611112453](img/Pasted%20image%2020250611112453.png)
- In my site `usls.py` file we have to setup manually for the media data

    ![Pasted image 20250611112800](img/Pasted%20image%2020250611112800.png)


## **Now Adding and Accessing the media file

 - we gonna use our static things like css , js and img in the html pages via using static commands 
   
**folder structure

![Pasted image 20250611114908](img/Pasted%20image%2020250611114908.png)

- then we gonna import this css file in the base file 
  
  ![Pasted image 20250611114958](img/Pasted%20image%2020250611114958.png)

same for the index.html

![Pasted image 20250611115432](img/Pasted%20image%2020250611115432.png)

**now we gonna work on media (img)
- we have to make media folder 
- **folder structure
    ![Pasted image 20250611120326](img/Pasted%20image%2020250611120326.png)

- then in the database make the changes and make a new image column 
- `models.py`
    ![Pasted image 20250611120558](img/Pasted%20image%2020250611120558.png)

- **now we gonna install pillow library for better image handling or manipulation

- after adding a image in the media file we gonna call those inside the index and also in the admin panel we can see those after doing these changes in `admin.py`
    ![Pasted image 20250611121334](img/Pasted%20image%2020250611121334.png)

-  then we can see the images in the admin panel
    ![Pasted image 20250611121424](img/Pasted%20image%2020250611121424.png)

- then we can also call these images in index page via indexing db.
 	![Pasted image 20250611121509](img/Pasted%20image%2020250611121509.png)