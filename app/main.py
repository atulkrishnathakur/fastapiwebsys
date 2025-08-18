from fastapi import FastAPI,Request,Depends,status,HTTPException,Path
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import text
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint,ForeignKey,Identity)
from sqlalchemy import (select,insert,update,delete,join,and_, or_ )
from typing import Annotated
from fastapi.responses import JSONResponse, ORJSONResponse
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from datetime import datetime

app = FastAPI()

engine = create_engine("mysql+pymysql://root:123456789@mysqlcontainer:3306/websysdb?charset=utf8mb4")
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DeclarativeBase used in sqlalchemy 2.0 

class Base(DeclarativeBase):
    pass

# https://docs.sqlalchemy.org/en/20/dialects/mysql.html#mysql-data-types 
# https://docs.sqlalchemy.org/en/20/orm/
# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-table-configuration
# https://docs.sqlalchemy.org/en/20/core/type_basics.html
# https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.execute 
# https://www.w3schools.com/python/python_datetime.asp 

class CourseGroupMaster(Base):
    __tablename__ = 'course_group_master'
    __table_args__ = {"mysql_engine": "InnoDB"}
    
    id: Mapped[BigInteger] = mapped_column('id',BigInteger, primary_key=True, nullable=False, autoincrement=True)
    course_group_code: Mapped[String] = mapped_column('course_group_code',String(50),nullable=True)
    course_group_name: Mapped[String] = mapped_column('course_group_name',String(255),nullable=True)
    status: Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at: Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
    created_by: Mapped[BigInteger] = mapped_column('created_by',BigInteger,nullable=True)
    updated_by: Mapped[BigInteger] = mapped_column('updated_by',BigInteger,nullable=True)


app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_item(request: Request):
    dbsession = SessionLocal()
    return templates.TemplateResponse(request=request, name="dashboard.html")

@app.get("/course_group",name="coursegroup")
async def get_course_group(request: Request):
    try:
        dbsession = SessionLocal()
        http_status_code = status.HTTP_200_OK
        stmt = select(CourseGroupMaster).order_by(CourseGroupMaster.id)
        result = dbsession.execute(stmt).scalars().all()
        datalist = list()
        for rowobj in result:
            datadict = {}
            datadict['id'] = rowobj.id
            datadict['course_group_name'] = rowobj.course_group_name
            datadict['status'] = rowobj.status
            updatedatdate = ""
            if rowobj.updated_at is not None:
                updatedatdate = rowobj.updated_at.strftime("%d-%m-%Y")
            
            datadict['updated_at'] = updatedatdate
            datalist.append(datadict)
            
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "message":"Course group message",
            "data":datalist
        }
        return response_dict
    except Exception as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":str(e)
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        return response