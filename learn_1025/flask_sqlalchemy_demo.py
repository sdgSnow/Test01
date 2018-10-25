from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOSTNAME = 'ip'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'peng'
PASSWORD = '123456'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user_model'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        # return "<User(username: %s)>" % self.username
        return "{id=%s,username=%s}" % (self.id,self.username)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey("user_model.id"))

    author = db.relationship("User",backref="artiles")

db.drop_all()
db.create_all()

@app.route('/')
def hello_world():
    user = User(username='peng')
    article = Article(title='title one')
    # cascade save-update
    article.author = user
    #
    db.session.add(article)
    db.session.commit()
    return 'Hello World!'

@app.route('/info')
def hello_world2():
    info = User.query.filter_by(username='peng').all()
    #     for u in info:
    #         print(u.__dict__)
    #     # print(info)
    return 'info'


if __name__ == '__main__':
    app.run()
