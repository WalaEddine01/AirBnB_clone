# 0x00. AirBnB clone - The console

## Description of the project:
#### This is the first full web application project for every software engineering trainee at Alx Africa.It is a hands-on practice showing the implementation of all the fundamental concepts covered in the Alx high-level programming track.
###
## Description of the command interpreter:
#### This console is a command interpreter to manipulate data without a visual interface, like in a shell (perfect for development and debugging).
###
## how to start it
- Installation and execution 🔧
Clone the repository
```bash
$ git clone https://github.com/JoseR98/AirBnB_clone.git
```
Move in to the directory
```bash
$ cd AirBnB_clone
```
Execute the console file
```bash
/AirBnB_clone$ ./console.py
```
## how to use it
# console commands:
 - create : Creates a new instance of the class passed by argument.
 - show : Prints the string representation of an instance.
 - destroy : Deletes an instance that was already created.
 - all : Prints string representation of all instances or of all instances of a specified class.
 - update : Updates an instance attribute if exists otherwise create it.
 - help : Show all commands or display information about a specific command.
 - quit : Exit the console.
 - EOF : Exit the console.
# Commands usage:
 - create : create <class_name>
 - show : show <class_name> <object_id> ; <class_name>.show(<object_id>)()
 - destroy : destroy <class_name> <object_id ; <class_name>.destroy(<object_id>)()
 - all : all <class_name> ; <class_name>.all()
 - update : update <class_name> <object_id> "" ; .update(<object_id>, , ) ; .update(<object_id>, )
 - help : help ; help <command_name>
 - quit : quit
 - EOF : EOF ; (ctrl + d)

###
## Concepts:
#### * Python package
#### * cmd module
#### * Unit testing
#### * serialize and deserialize a Class
#### * JSON file
#### * datetime modual
#### * What is an UUID
#### * \*args and \*\*kwargs


## Examples


Example 1: Using create, count and all commands
```bash
$ ./console.py
(hbnb) all
[]
(hbnb) create Place
482f60f3-ff1e-43c7-bb11-f8407b04dd69
(hbnb) create BaseModel
88f01e9a-98c0-43af-8c10-c35cadee1d5e
(hbnb) BaseModel.count()
1
(hbnb) all
["[Place] (482f60f3-ff1e-43c7-bb11-f8407b04dd69) {'id': '482f60f3-ff1e-43c7-bb11-f8407b04dd69', 'created_at': datetime.datetime(2023, 11, 14, 19, 59, 24, 576486), 'updated_at': datetime.datetime(2023, 11, 14, 19, 59, 24, 576530)}", "[BaseModel] (88f01e9a-98c0-43af-8c10-c35cadee1d5e) {'id': '88f01e9a-98c0-43af-8c10-c35cadee1d5e', 'created_at': datetime.datetime(2023, 11, 14, 20, 00, 30, 773211), 'updated_at': datetime.datetime(2023, 11, 14, 20, 00, 30, 773236)}"]
(hbnb)
```
Example 2: Using basic update with an Id and show command
```bash
(hbnb) update BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f first_name "Betty"
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2023, 11, 14, 20, 00, 30, 773211), 'updated_at': datetime.datetime(2023, 11, 14, 20, 00, 30, 773236), 'first_name': 'Betty'}
(hbnb) Place.update("492f60f3-ff1e-43c7-bb11-f8407b04dd59", "first_name", "John")
(hbnb) show Place 492f60f3-ff1e-43c7-bb11-f8407b04dd59
[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2023, 11, 14, 20, 00, 24, 576486), 'updated_at': datetime.datetime(2023, 11, 14, 20, 00, 24, 576530), 'first_name': 'John'}
```
Example 3: Using update with a dictionary
```bash
(hbnb) BaseModel.update("99f01e9a-99c0-42af-8c10-c35cadee1d8f", {'first_name': "Petter", "age": 45})
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2023, 11, 14, 20, 00, 30, 773211), 'updated_at': datetime.datetime(2023, 11, 14, 20, 00, 30, 773236), 'first_name': 'Petter', 'age': '45'}
```
Example 4: Using destroy and count command
```bash
(hbnb) BaseModel.destroy("99f01e9a-99c0-42af-8c10-c35cadee1d8f")
(hbnb) all
["[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2023, 11, 14, 20, 00, 24, 576486), 'updated_at': datetime.datetime(2023, 11, 14, 20, 00, 24, 576530), 'first_name': 'John'}"]
(hbnb) BaseModel.count()
0
(hbnb) quit
$
```
Example 5: Non - Interactive Mode
```bash
$ echo "create User" | ./console.py
(hbnb) 55b76419-6009-4b36-b88a-7c2930283f4a
$ echo "show User 55b76419-6009-4b36-b88a-7c2930283f4a" | ./console.py
(hbnb) [User] (55b76419-6009-4b36-b88a-7c2930283f4a) {'id': '55b76419-6009-4b36-b88a-7c2930283f4a', 'created_at': datetime.datetime(2023, 11, 14, 20, 37, 15, 575191), 'updated_at': datetime.datetime(2023, 11, 14, 20, 37, 15, 575237)}
```

## Collaborators

| [Nadjib M](https://github.com/Nadjib-coder) | [Wala Eddine B](https://github.com/WalaEddine01)|
| :-------- | :------------------------- |
| ![nadjib](https://media.licdn.com/dms/image/D4D03AQHbpHMnAT3M4Q/profile-displayphoto-shrink_100_100/0/1683302678870?e=1704931200&v=beta&t=W4jhaI52ZHou5RNqp7FT7GPOxlu5tx2-l-ze8Xjn3mQ) | ![wala](https://media.licdn.com/dms/image/D4E03AQFfHDWs3YS-lQ/profile-displayphoto-shrink_100_100/0/1688823968266?e=1704931200&v=beta&t=9tMejXQG7F094hnPNiiT-2s4eA8IOFjgsj0W47yi2AE) |

## Coded with


![py](https://cdn-icons-png.flaticon.com/128/3098/3098090.png)
