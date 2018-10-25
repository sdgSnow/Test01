#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = 'ip'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'peng'
PASSWORD = '123456'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

#用于维护数据库的连接池
engine = create_engine(DB_URI, max_overflow=10,echo=True,echo_pool=True, pool_recycle=3600)


Base = declarative_base(engine)

# Session = sessionmaker(engine)
# session = Session()

session = sessionmaker(engine)()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(50))

    def __str__(self):
        return "<Person(name:%s,age:%s,country:%s)>" % (self.name,self.age,self.country)

# session：会话
# Base.metadata.drop_all()
# Base.metadata.create_all()

# 增
def add_data():
    p1 = Person(name='zhanghao',age=19,country='china')
    p2 = Person(name='xiaoxiong',age=20,country='china')
    session.add_all([p1,p2])
    session.commit()

# 查
def search_data():
    person = session.query(Person).first()
    print(person)


# 改
def update_data():
    person = session.query(Person).first()
    person.name = 'ketang'
    session.commit()

# 删
def delete_data():
    person = session.query(Person).first()
    session.delete(person)
    session.commit()


if __name__ == '__main__':
    add_data()
    # search_data()
    # update_data()
    # delete_data()