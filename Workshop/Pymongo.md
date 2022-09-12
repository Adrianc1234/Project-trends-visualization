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

<strong>So we are ready to work!</strong>

---

# Introduction section

## Accessing to MongoDB client

## Making our project

## Accessing to our project & Making our database

## connecting it to python 3

## Commands & tutorial

## Challenge


