from app import db, models
post = models.Post.query.all()
for p in post:
    print("before"+str(p))
    db.session.delete(p)
    print("after"+str(p))
users = models.User.query.all()
for u in users:
    print("before"+str(u))
    db.session.delete(u)
    print("after" + str(u))

