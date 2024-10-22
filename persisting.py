from models import User,Comment
from main import session

user1 = User(
    username = 'mohit',
    email = 'svenkatmohit2883@gmail.com',
    comments = [
        Comment(text = "Hello World"),
        Comment(text="Please Subscribe")
    ]
)

eshwar = User(
    username = 'eshwar',
    email = 'eshwar@gmail.com',
    comments = [
        Comment(text = "AIIMS Mangalagiri"),
        Comment(text="Please Subscribe")
    ]
)

Walter = User(
    username = 'Heisenber',
    email = 'wwhite@gmail.com',
    comments = [
        Comment(text = "AIIMS Mangalagiri"),
        Comment(text="Please Subscribe")
    ]
)


session.add_all([user1,eshwar,Walter])
session.commit()