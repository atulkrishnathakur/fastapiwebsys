from fastapi import FastAPI
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


engine = create_engine("mysql+pymysql://root:123456789@mysqlcontainer:3306/websysdb?charset=utf8mb4")

metadata = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 3"}
    


@app.post("/sqlalchemy-core-select", name="select1")
def select1():
    datalist = list()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM employee_master")).mappings()
        for row in result:
            datalist.append(dict(row))
    return {"employee":datalist}


@app.post("/sqlalchemy-core-insert", name="insert1")
def insert1():
    datalist = list()
    query = """INSERT INTO employee_master (emp_hame, email, mobile, status,password,Login_Route)
        VALUES (:emp_hame,:email, :mobile, :status, :password, :Login_Route)"""
    querydict = {"emp_hame": "Atul Test", "email": "test@yopmail.com", "mobile": "123456789","status":"A","password":"$2y$10$T.6Dx9YvqhSQzEioDCDoC.MG5TY/TYmA3gHksXO2xZIvAxBGjPV7q","Login_Route":"web"}
    with engine.connect() as conn:
        conn.execute(text(query),querydict)
        conn.commit()
    return {"employee":datalist}


@app.post("/sqlalchemy-core-update", name="update1")
def update1():
    datalist = list()
    query = """UPDATE employee_master set mobile= :mobile where id=:id"""
    querydict = {"mobile": "1234560000","id":2}
    with engine.connect() as conn:
        conn.execute(text(query),querydict)
        conn.commit()
    return {"employee":datalist}


@app.post("/sqlalchemy-core-delete", name="delete1")
def delete1():
    datalist = list()
    query = """DELETE FROM employee_master where id=:id"""
    querydict = {"id":2}
    with engine.connect() as conn:
        conn.execute(text(query),querydict)
        conn.commit()
    return {"employee":datalist}