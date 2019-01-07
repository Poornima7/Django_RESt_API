# Django_REST_API





Django is a Python based full stack web development framework means it is used to develop full fledged websites in Python. it encourages rapid development and advocates pragmatic and clean code..

### Prequisites
Make sure, you have following things installed
 -Python
 -Django

### Dependencies 
###### Python Installation [python](https://www.python.org/downloads/) 
###### Django Installation
   ######  windows [Django](https://docs.djangoproject.com/en/2.1/howto/windows/)
   ###### Linux/(MAC OS) [Django](https://www.howtoforge.com/tutorial/how-to-install-django-on-ubuntu/)


####
###### Here we build a small application that will keep track of all my friends with their respective details.

  - API to list all friends. 
  - API to get detail of a particular friend. 
  - API to add a friend in the list.
  - API to delete a friend from the list. 







### Running

 - Clone repo 
  ```sh
git clone https://github.com/Poornima7/Django_RESt_API.git
  ```
  
```sh
cd Django_RESt_API
```

- Run the application using following command
```sh 
python manage.py runserver
```
- Verify the deployment by navigating to your server address in your preferred browser.
```sh 
http://127.0.0.1:8000/
```


###### Add friend to the list
   - POST METHOD
```sh   
http://127.0.0.1:8000/friends/
```
```sh
{
"friend_name" : "Rohini Gowda",
"mobile_no": 7892199917
}
```

###### Get friend
   -  METHOD GET
``` sh
   http://127.0.0.1:8000/friends/  
```
###### Edit the name of the friend
   - METHOD PUT
``` sh
   - http://127.0.0.1:8000/friends/1 
```
``` sh
{
    "friend_name" : Rashmi Rao
}
```
###### Fetch the detail of particular friend
   - METHOD GET
``` sh
   - http://127.0.0.1:8000/friends/1 
```

###### Delete a friend from the friends list
   - METHOD DELETE
``` sh
   - http://127.0.0.1:8000/friends/1 
```

   
   



## 🎩 Authors
- Poornima Subramani Naidu - [GitHub](https://github.com/Poornima7/) &bull; [stackoverflow](https://stackoverflow.com/users/9353529/poornima-subramani-naidu) &bull; [LinkedIn](https://www.linkedin.com/in/poornima-subramani-naidu-3079a2b1/)



## 📜 License
Copyright (c) 2019-20 Poornima Subramani https://github.com/Poornima7/



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
