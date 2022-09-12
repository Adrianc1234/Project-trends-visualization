# Installation

## Windows Installation

### sub

### sub

![text](url)

## MacOS Installation <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Icon-Mac.svg/2048px-Icon-Mac.svg.png" width="25" height="25">

### Creating an environtment in python 3

First we must access to our visual studio or any editor with terminal to make things easier for us. Now let's create a folder with the name `My mongo db`. We access it by means of the terminal, where we will execute: 

- `pip3 install virtualenv`

With this we will be installing the library to be able to create environments with python. As a second step we will execute the following command to generate the environment.

- `virtualenv ambiente -p python3`

### Activate the environment

In this step we will activate the environment where we can install anything necessary to be able to run any job we want without affecting the local python installations on the machine.

- `source ambiente/bin/activate`

Result:
![Result](https://snipboard.io/iBmwx0.jpg)

### Installing our library to work

PyMongo is a native Python driver for MongoDB. Use MongoClient to create a connection. MongoClient defaults to the MongoDB instance running on localhost:27017 if not specified. The PyMongo Database class represents the database construction in MongoDB.

- `pip3 install pymongo`

### Installing the module to control our server

In order to use mongo+srv protocol, you need to install pymongo-srv Launch this command to do it with python 3:

`pip3 install pymongo[srv]`
or this one for other versions:

`pip install pymongo[srv]`
And as suggested by @lukrebs, add quotes for ZSH:

If the first one got failed, try with this one:
`pip3 install 'pymongo[srv]'`

<strong>So we are ready to work!</strong>

### What if i want to finish?

just write: `deactivate` in your console.

![deactivate](https://snipboard.io/uzp2iF.jpg)

---

# Introduction section

## Accessing to MongoDB client

## Making our project

## Accessing to our project & Making our database

## connecting it to python 3

## Commands & tutorial

## Challenge


