"""For Database Entries"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog import db
from catalog.models import User, Category, Item


def add_items(category, item_names):
	for name in item_names:
		item = Item(name = name, category_id = category.id)
		db.add(item)
	db.commit()

def add_item(category, item):
    item.category_id = category.id
    db.add(item)
    db.commit()


user = User(name = "Peter Pan",
    email = "peter@neverlandmail.org",
    picture = "https://placehold.it/300x300.png?text=Peter+Pan")

db.add(user)
db.commit()


category1 = Category(name = "Books")
db.add(category1)

category2 = Category(name = "Electronics")
db.add(category2)

category3 = Category(name = "Food")
db.add(category3)

category4 = Category(name = "Miscellaneous")
db.add(category4)

db.commit()


add_item(category1, Item(user = user, name = "Data Structures Algorithms Design", description = "Great book!"))
add_item(category1, Item(user = user, name = "Harry Potter", description = "Did you see the movie?"))
add_item(category1, Item(user = user, name = "Romeo and Juliet", description = "Classic love story."))

add_item(category2, Item(user = user, name = "Android phone", description = "Awsome phone."))
add_item(category2, Item(user = user, name = "Laptop", description = "Who needs a computer?"))
add_item(category2, Item(user = user, name = "DVD player", description = "Sorry, no blu-ray here, but still cool :)"))

add_item(category3, Item(user = user, name = "Strawberry", description = "This is my fav fruit."))
add_item(category3, Item(user = user, name = "Custard Apple", description = "This is an apple."))
add_item(category3, Item(user = user, name = "Orange", description = "This is an orange orange."))

add_item(category4, Item(user = user, name = "Add Gel Cat", description = "A pen."))
add_item(category4, Item(user = user, name = "Apsara Pencil", description = "This can be pretty handy if you need to erase things you write."))
add_item(category4, Item(user = user, name = "Notepad", description = "Combined with a pen or pencil, can be used to write anything you want."))
add_item(category4, Item(user = user, name = "Playing cards", description = "Standard 52 card deck. What games do you like to play?"))
