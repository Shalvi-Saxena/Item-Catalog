Project 2: Item Catalog
=======================

This project is a simple web application that provides a list of items within several categories.
It uses third party authentication, and logged in users can add, edit, and delete their own items.
Created using [Flask] and [SQLAlchemy].

Initial [Vagrant] config cloned from https://github.com/udacity/fullstack-nanodegree-vm


Usage
-----

To use the project, download and configure the application. You will have to create a Google Developers Console project and use your own client ID.

Run the application:
```
$ python runserver.py
```

Then point your browser to ```localhost:5000```.


Installation
------------

After installing VirtualBox and Vagrant, do the following on the terminal:

1) Clone the project (if you don't have git, you may download the project from github).
```
$ git clone git@github.com:pt314/udacity-fsnd-p3-item-catalog.git
```

2) Start the virtual machine (the first time will take a while to download and setup things).
```
$ cd udacity-fsnd-p3-catalog/vagrant
$ vagrant up
```

3) Connect to the virtual machine.
```
$ vagrant ssh
$ cd /vagrant/catalog
```
(Use ```vagrant halt``` to turn it off.)

4) Create the database.
```
$ python database_setup.py
```

5) Populate the database.
```
$ python populate_database.py
```

This creates a set of predefined categories and sample items. You may want to edit this file to add different categories or skip adding sample items.

5) Configure Google sign-in.

A client ID is not provided. If you want to test the application, you will have to use your own client ID.

Follow the steps to create a [Google Developers Console project]. Then go to the credentials tab and download the client ID as a JSON file. Copy the file to the ```catalog``` folder and rename it ```client_secret_google.json```.

6) Update app configuration (optional).

You may want to update the configuration in ```runserver.py``` or ```catalog/__init__.py```. Especially, you may want to ensure debug mode is disabled in ```runserver.py``` and update the secret keys in ```catalog/__init__.py```.
