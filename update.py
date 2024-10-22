from main import session
from models import User,Comment

comment = session.query(Comment).filter_by(id=29).first()
print(comment)
comment.text = "Updated comment"

user = session.query(User).filter_by(username='mohit').first()
user.username = 'yatin'
session.commit()