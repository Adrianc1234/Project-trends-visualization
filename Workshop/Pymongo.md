## Windows PowerShell Installation <img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Windows_logo_-_2012.png" width="25" height="25">

1. **Install virtualenv**

~~~
pip install virtualenv 
~~~

2. **Create virtualenv**

Go to the directory you want to create the environment and type,
~~~
python –m venv NameOfEnvironment 
~~~

3. **Activate virtualenv**

In the same directory use,
~~~
NameOfEnvironment\Scripts\activate
~~~

4. **Installing our library to work**

PyMongo is a native Python driver for MongoDB. Use MongoClient to create a connection. MongoClient defaults to the MongoDB instance running on localhost:27017 if not specified. The PyMongo Database class represents the database construction in MongoDB.

~~~
pip3 install pymongo
~~~ 

<strong>So we are ready to work!</strong>

**To deactivate**

~~~
deactivate
~~~

### Troubleshooting

The activation of the environment can cause issues

![Error](https://www.cdmon.com/images/easyblog_articles/1695/b2ap3_large_scrip.png)

If you get the error above, open windows PowerShell as admin

![Error1](https://www.cdmon.com/images/easyblog_articles/1695/b2ap3_medium_script-1.png)

Run the following to show the execution policy, the output should look like the image

~~~
Get-ExecutionPolicy -List
~~~

![Error2](https://www.cdmon.com/images/easyblog_articles/1695/script-2.png)

To fix it, run 
~~~
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
~~~

![Error3](https://www.cdmon.com/images/easyblog_articles/1695/script-3.png)

Now if you show the execution policy again it will look like this
![Error4](https://www.cdmon.com/images/easyblog_articles/1695/script-4.png)

You can go back to the command to activate the environment and it will work!

For more info on the error click [here](https://www.cdmon.com/es/blog/la-ejecucion-de-scripts-esta-deshabilitada-en-este-sistema-te-contamos-como-actuar).


## MacOS Installation <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Icon-Mac.svg/2048px-Icon-Mac.svg.png" width="25" height="25">

### Creating an environtment in python 3

First we must access to our visual studio or any editor with terminal to make things easier for us. Now let's create a folder with the name `My mongo db`. We access it by means of the terminal, where we will execute: 

~~~
pip3 install virtualenv
~~~

With this we will be installing the library to be able to create environments with python. As a second step we will execute the following command to generate the environment.

~~~
virtualenv ambiente -p python3
~~~

### Activate the environment

In this step we will activate the environment where we can install anything necessary to be able to run any job we want without affecting the local python installations on the machine.

~~~
source ambiente/bin/activate
~~~

Result:
![Result](https://snipboard.io/iBmwx0.jpg)

### Installing our library to work

PyMongo is a native Python driver for MongoDB. Use MongoClient to create a connection. MongoClient defaults to the MongoDB instance running on localhost:27017 if not specified. The PyMongo Database class represents the database construction in MongoDB.

~~~
pip3 install pymongo
~~~

Also we must install: 

In order to use mongo+srv protocol, you need to install pymongo-srv Launch this command to do it with python 3:

~~~
pip3 install pymongo[srv]
~~~
or this one for other versions:
~~~
pip install pymongo[srv]
~~~
And as suggested by @lukrebs , add quotes for ZSH:
~~~
pip3 install 'pymongo[srv]'
~~~
<strong>So we are ready to work!</strong>

---

# Introduction section

## Accessing to MongoDB client
### What is Mongodb?

MongoDB is a document database that offers great scalability and flexibility, and an advanced query and indexing model. Is MongoDB good for anything and everything? Before defining why you should use MondoDB in your project, it is worth reviewing the pros and cons. MongoDB is a very interesting resource for developers but it is not perfect. For example:

<i>Advantages</i>

- Document validation
- Integrated storage engines
- Shorter recovery time in case of failures

<i>Disadvantages</i>

- Not a suitable solution for applications with complex transactions
- No replacement for legacy solutions
- Still a young technology

### How does it work?

MongoDB stores data in flexible documents similar to JSON, so fields may vary between documents and the data structure may change over time.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200120181841/Untitled-Diagram-1-13.jpg" width="500" height="700">

# Workshop 
---

## Making our project in mongo db

### step 1 - Creating our account 
we need to access or you already have an account for MongoBD site, would be better, but in case that not, just access to it using your gmail account in this page:

[Click Here!](https://account.mongodb.com/account/login)

You should see something like this page view:

![Image](https://snipboard.io/V7k6SE.jpg)

### step 2 - Creating a new project 

In this step, we just need to create a new project to design our database, so in fact, it would be so easy. Please put your project name and click in the button `Next`. 

![Image2](https://snipboard.io/6cNb3u.jpg)

### step 3 - Choosing our main manager for the project

In this step, we just need to change the main manager for this project. Then, a button will appear below to do a click on it and create this project. Be patient because it could take some minutes.

![Img3](https://snipboard.io/LbF7It.jpg)

## Accessing to our project & Making our database

## Connecting it to python 3

## Commands & tutorial

## Challenge


