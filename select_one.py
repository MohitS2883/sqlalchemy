from main import session
from models import User

user = session.query(User).filter_by(username = 'eshwar').all()

print(user)