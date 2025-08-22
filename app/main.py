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


# general function
def none_to_empty(value):
    if value is None:
        return ""
    return value


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


class CourseChapterDataDtl(Base):
    __tablename__ = 'course_chapter_data_dtl'
    __table_args__ = {"mysql_engine": "InnoDB"}
    
    id: Mapped[BigInteger] = mapped_column('id',BigInteger, primary_key=True, nullable=False, autoincrement=True)
    course_id: Mapped[BigInteger] = mapped_column('course_id',BigInteger,ForeignKey('course_master.id'),nullable=True)
    vertical_menu_id: Mapped[BigInteger] = mapped_column('vertical_menu_id',BigInteger,ForeignKey('vertical_menu_url_master.id'),nullable=True)
    chapter_block_heading: Mapped[String] = mapped_column('chapter_block_heading',String(255),nullable=True)
    paragraph1: Mapped[String] = mapped_column('paragraph1',String(1200),nullable=True)
    paragraph2: Mapped[String] = mapped_column('paragraph2',String(1200),nullable=True)
    paragraph3: Mapped[String] = mapped_column('paragraph3',String(1200),nullable=True)
    paragraph4: Mapped[String] = mapped_column('paragraph4',String(1200),nullable=True)
    paragraph5: Mapped[String] = mapped_column('paragraph5',String(1200),nullable=True)
    syntax: Mapped[String] = mapped_column('syntax',String(1200),nullable=True)
    syntax_example: Mapped[String] = mapped_column('syntax_example',String(1200),nullable=True)
    program_code: Mapped[Text] = mapped_column('program_code',Text,nullable=True)
    program_output: Mapped[Text] = mapped_column('program_output',Text,nullable=True)
    program_algorithm: Mapped[Text] = mapped_column('program_algorithm',Text,nullable=True)
    note1: Mapped[String] = mapped_column('note1',String(255),nullable=True)
    note2: Mapped[String] = mapped_column('note2',String(255),nullable=True)
    note3: Mapped[String] = mapped_column('note3',String(255),nullable=True)
    note4: Mapped[String] = mapped_column('note4',String(255),nullable=True)
    note5: Mapped[String] = mapped_column('note5',String(255),nullable=True)
    img1: Mapped[String] = mapped_column('img1',String(255),nullable=True)
    img2: Mapped[String] = mapped_column('img2',String(255),nullable=True)
    img3: Mapped[String] = mapped_column('img3',String(255),nullable=True)
    img4: Mapped[String] = mapped_column('img4',String(255),nullable=True)
    img5: Mapped[String] = mapped_column('img5',String(255),nullable=True)
    status: Mapped[String] = mapped_column('status',String(1),nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at: Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
    created_by: Mapped[BigInteger] = mapped_column('created_by',BigInteger,nullable=True)
    updated_by: Mapped[BigInteger] = mapped_column('updated_by',BigInteger,nullable=True)
    is_try_yourself: Mapped[String] = mapped_column('is_try_yourself',String(1),nullable=True)
    

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
        # outerjoin() used for left join
        stmt = (
            select(VerticalMenuUrlMaster,VerticalMenuGroupMaster,CourseMaster,CourseGroupMaster)
            .outerjoin(VerticalMenuGroupMaster,VerticalMenuUrlMaster.vertical_menu_group_id==VerticalMenuGroupMaster.id)
            .outerjoin(CourseMaster,VerticalMenuUrlMaster.course_id==CourseMaster.id)
            .outerjoin(CourseGroupMaster,VerticalMenuUrlMaster.course_group_id==CourseGroupMaster.id)
            .order_by(VerticalMenuUrlMaster.id)
            )
        result = dbsession.execute(stmt).all()
        datalist = list()
        for vmenu,vmenugroup,course,coursegroup in result:
            datadict = {}
            datadict['id'] = vmenu.id
            datadict['menu_order_by'] = vmenu.menu_order_by
            datadict['route_name'] = none_to_empty(vmenu.route_name)
            datadict['course_id'] = vmenu.course_id
            datadict['course_name'] = course.course_name
            datadict['vertical_menu_group_id'] = vmenu.vertical_menu_group_id
            datadict['vertical_menu_group_name'] = vmenugroup.group_name
            datadict['status'] = vmenu.status
            updatedatdate = ""
            if vmenu.updated_at is not None:
                updatedatdate = vmenu.updated_at.strftime("%d-%m-%Y")
            
            datadict['updated_at'] = none_to_empty(updatedatdate)
            datadict['chapter_heading_main'] = vmenu.chapter_heading_main
            datadict['menu_name'] = vmenu.menu_name
            datadict['url_slug'] = vmenu.url_slug
            datadict['is_course_home'] = vmenu.is_course_home
            datadict['title_tag'] = vmenu.title_tag
            datadict['meta_tag_keywords'] = vmenu.meta_tag_keywords
            datadict['meta_tag_description'] = vmenu.meta_tag_description
            datadict['hidden_ranking_contents'] = vmenu.hidden_ranking_contents
            datadict['course_group_id'] = vmenu.course_group_id
            datadict['course_group_name'] = coursegroup.course_group_name

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

@app.get("/all-chapters",name="allchapters")
async def get_all_chapter_data(request: Request):
    try:
        dbsession = SessionLocal()
        http_status_code = status.HTTP_200_OK
        # outerjoin() used for left join
        baseUrl = request.base_url._url
        stmt = (
            select(CourseChapterDataDtl,CourseMaster,VerticalMenuUrlMaster)
            .outerjoin(CourseMaster,CourseChapterDataDtl.course_id==CourseMaster.id)
            .outerjoin(VerticalMenuUrlMaster,CourseChapterDataDtl.vertical_menu_id==VerticalMenuUrlMaster.id)
            .order_by(CourseChapterDataDtl.id)
            )
        result = dbsession.execute(stmt).all()
        datalist = list()
        for courseChapDtl,course,vmenu in result:
            datadict = {}
            datadict['id'] = courseChapDtl.id
            datadict['course_id'] = courseChapDtl.course_id
            datadict['course_name'] = course.course_name
            datadict['vertical_menu_id'] = courseChapDtl.vertical_menu_id
            datadict['menu_name'] = vmenu.menu_name
            datadict['chapter_block_heading'] = courseChapDtl.chapter_block_heading
            datadict['paragraph1'] = courseChapDtl.paragraph1
            datadict['paragraph2'] = courseChapDtl.paragraph2
            datadict['paragraph3'] = courseChapDtl.paragraph3
            datadict['paragraph4'] = courseChapDtl.paragraph4
            datadict['paragraph5'] = courseChapDtl.paragraph5
            datadict['syntax'] = courseChapDtl.syntax
            datadict['syntax_example'] = courseChapDtl.syntax_example
            
            datadict['program_code'] = courseChapDtl.program_code
            datadict['program_output'] = courseChapDtl.program_output
            datadict['program_algorithm'] = courseChapDtl.program_algorithm
            datadict['note1'] = courseChapDtl.note1
            datadict['note2'] = courseChapDtl.note2
            datadict['note3'] = courseChapDtl.note3
            datadict['note4'] = courseChapDtl.note4
            datadict['note5'] = courseChapDtl.note5
            img1_url = ""
            if courseChapDtl.img1 is not None:
                img1_url = f"{baseUrl}static/uploads/{courseChapDtl.img1}"
            datadict['img1'] = img1_url
            datadict['img2'] = courseChapDtl.img2
            datadict['img3'] = courseChapDtl.img3
            datadict['img4'] = courseChapDtl.img4
            datadict['img5'] = courseChapDtl.img5
            datadict['status'] = courseChapDtl.status
            updatedatdate = ""
            if courseChapDtl.updated_at is not None:
                updatedatdate = courseChapDtl.updated_at.strftime("%d-%m-%Y")
            
            datadict['updated_at'] = none_to_empty(updatedatdate)
            datadict['is_try_yourself'] = courseChapDtl.is_try_yourself
            datalist.append(datadict)
            
        response_dict = {
            "status_code": http_status_code,
            "status":True,
            "message":"all chapter data menu",
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

