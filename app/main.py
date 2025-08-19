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
from sqlalchemy import inspect
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

class CourseMaster(Base):
    __tablename__ = 'course_master'
    __table_args__ = {"mysql_engine": "InnoDB"}
    
    id: Mapped[BigInteger] = mapped_column('id',BigInteger, primary_key=True, nullable=False, autoincrement=True)
    course_group_code: Mapped[String] = mapped_column('course_code',String(50),nullable=True)
    course_group_id: Mapped[BigInteger] = mapped_column('course_group_id',BigInteger,ForeignKey('course_group_master.id'),nullable=True)
    course_name: Mapped[String] = mapped_column('course_name',String(255),nullable=True) 
    status: Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at: Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
    created_by: Mapped[BigInteger] = mapped_column('created_by',BigInteger,nullable=True)
    updated_by: Mapped[BigInteger] = mapped_column('updated_by',BigInteger,nullable=True)
    repository_course_status: Mapped[SmallInteger] = mapped_column('repository_course_status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")

class VerticalMenuGroupMaster(Base):
    __tablename__ = 'vertical_menu_group_master'
    __table_args__ = {"mysql_engine": "InnoDB"}
    
    id: Mapped[BigInteger] = mapped_column('id',BigInteger, primary_key=True, nullable=False, autoincrement=True)
    course_id: Mapped[BigInteger] = mapped_column('course_id',BigInteger,ForeignKey('course_master.id'),nullable=True)
    group_name: Mapped[String] = mapped_column('group_name',String(255),nullable=True) 
    status: Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at: Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
    created_by: Mapped[BigInteger] = mapped_column('created_by',BigInteger,nullable=True)
    updated_by: Mapped[BigInteger] = mapped_column('updated_by',BigInteger,nullable=True)

class VerticalMenuUrlMaster(Base):
    __tablename__ = 'vertical_menu_url_master'
    __table_args__ = {"mysql_engine": "InnoDB"}
    
    id: Mapped[BigInteger] = mapped_column('id',BigInteger, primary_key=True, nullable=False, autoincrement=True)
    menu_order_by: Mapped[Integer] = mapped_column('menu_order_by',Integer,nullable=True)
    route_name: Mapped[String] = mapped_column('route_name',String(255),nullable=True)
    course_id: Mapped[BigInteger] = mapped_column('course_id',BigInteger,ForeignKey('course_master.id'),nullable=True)
    vertical_menu_group_id: Mapped[BigInteger] = mapped_column('vertica_menu_group_id',BigInteger,ForeignKey('vertical_menu_group_master.id'),nullable=True)
    status: Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at: Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
    created_by: Mapped[BigInteger] = mapped_column('created_by',BigInteger,nullable=True)
    updated_by: Mapped[BigInteger] = mapped_column('updated_by',BigInteger,nullable=True)
    chapter_heading_main: Mapped[String] = mapped_column('chapter_heading_main',String(255),nullable=True)
    url_slug: Mapped[String] = mapped_column('url_slug',String(255),nullable=True)
    menu_name: Mapped[String] = mapped_column('menu_name',String(255),nullable=True)
    is_course_home: Mapped[String] = mapped_column('is_course_home',String(1),nullable=True)
    title_tag: Mapped[String] = mapped_column('title_tag',String(255),nullable=True)
    meta_tag_keywords: Mapped[String] = mapped_column('meta_tag_keywords',String(600),nullable=True)
    hidden_ranking_contents: Mapped[String] = mapped_column('hidden_ranking_contents',String(3000),nullable=True)
    meta_tag_description: Mapped[String] = mapped_column('meta_tag_description',String(255),nullable=True)
    course_group_id: Mapped[BigInteger] = mapped_column('course_group_id',BigInteger,ForeignKey('course_group_master.id'),nullable=True)


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

    
@app.get("/course",name="coursegroup")
async def get_course(request: Request):
    try:
        dbsession = SessionLocal()
        http_status_code = status.HTTP_200_OK
        stmt = select(CourseMaster,CourseGroupMaster).join(CourseGroupMaster,CourseMaster.course_group_id == CourseGroupMaster.id).order_by(CourseMaster.id)
        result = dbsession.execute(stmt).all()
        
        datalist = list()
        for courseObj,courseGroupObj in result:
            datadict = {}
            datadict['id'] = courseObj.id
            datadict['course_name'] = courseObj.course_name
            datadict['course_group_id'] = courseObj.course_group_id
            datadict['course_group_name'] = courseGroupObj.course_group_name
            datadict['status'] = courseObj.status
            updatedatdate = ""
            if courseObj.updated_at is not None:
                updatedatdate = courseObj.updated_at.strftime("%d-%m-%Y")
            
            datadict['updated_at'] = updatedatdate
            datadict['repository_course_status'] = courseObj.repository_course_status
            datalist.append(datadict)
            
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "message":"Course message",
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
    

@app.get("/vertical_menu_group",name="verticalmenugroup")
async def get_vertical_menu_group(request: Request):
    try:
        dbsession = SessionLocal()
        http_status_code = status.HTTP_200_OK
        stmt = select(VerticalMenuGroupMaster,CourseMaster).join(CourseMaster,VerticalMenuGroupMaster.course_id == CourseMaster.id).order_by(VerticalMenuGroupMaster.id)
        result = dbsession.execute(stmt).all()
        
        datalist = list()
        for vmenuObj, courseObj in result:
            datadict = {}
            datadict['id'] = vmenuObj.id
            datadict['group_name'] = vmenuObj.group_name
            datadict['course_id'] = vmenuObj.course_id
            datadict['course_name'] = courseObj.course_name
            datadict['status'] = vmenuObj.status
            updatedatdate = ""
            if vmenuObj.updated_at is not None:
                updatedatdate = vmenuObj.updated_at.strftime("%d-%m-%Y")
            
            datadict['updated_at'] = updatedatdate
            datalist.append(datadict)
            
        response_dict = {
            "status_code": http_status_code,
            "status":True,  
            "message":"Vertical Menu Group",
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


@app.get("/vertical-menu-url",name="verticalmenuurl")
async def get_vertical_menu_url(request: Request):
    try:
        dbsession = SessionLocal()
        http_status_code = status.HTTP_200_OK
        stmt = select(VerticalMenuUrlMaster).order_by(VerticalMenuUrlMaster.id)
        result = dbsession.execute(stmt).scalars().all()
        datalist = list()
        for rowobj in result:
            datadict = {}
            datadict['id'] = rowobj.id
            datadict['menu_order_by'] = rowobj.menu_order_by
            datadict['route_name'] = rowobj.route_name
            datadict['course_id'] = rowobj.course_id
            datadict['vertical_menu_group_id'] = rowobj.vertical_menu_group_id
            datadict['status'] = rowobj.status
            updatedatdate = ""
            if rowobj.updated_at is not None:
                updatedatdate = rowobj.updated_at.strftime("%d-%m-%Y")
            
            datadict['updated_at'] = updatedatdate
            datadict['chapter_heading_main'] = rowobj.chapter_heading_main
            datadict['menu_name'] = rowobj.menu_name
            datadict['url_slug'] = rowobj.url_slug
            datadict['is_course_home'] = rowobj.is_course_home
            datadict['title_tag'] = rowobj.title_tag
            datadict['meta_tag_keywords'] = rowobj.meta_tag_keywords
            datadict['meta_tag_description'] = rowobj.meta_tag_description
            datadict['hidden_ranking_contents'] = rowobj.hidden_ranking_contents
            datadict['course_group_id'] = rowobj.course_group_id

            datalist.append(datadict)
            
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "message":"Vertical menu",
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
