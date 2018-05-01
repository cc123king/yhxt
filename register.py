from start_demo import db,user
def register(username,password,role_id):
    User=user(name=username,password=password,role_id=role_id)
    db.session.add(User)
    db.session.commit()

