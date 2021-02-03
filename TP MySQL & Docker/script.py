from sqlachemy import create_engine
from sqlachemy import MetaData,Table,Column,Integer,String
from sqlachemy.orm import mapper

#Specify database configurations
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'newuser',
    'password': 'newpassword',
    'database': 'classicmodels',
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}

#connect to database
engine = create_engine(connection_str)
connection = engine.connect()
print(' --- MySQL Docker Container Python connection ok --- \n')







DB_URL = 'mysql+mysqldb://root:root@localhost:3306/employee'
ENGINE = create_engine(DB_URL)

metadata = MetaData()

user = Table ('user', metadata,
                Column('id', Integer, primaryKey = True)
                Column('name', String(50))
                Column('password', String(50))
                ) 

class User():
    def __init__(self, name, password)
    self.name = name 
    self.password = password 

mapper(User, user)  
metadata.create_all(ENGINE)      