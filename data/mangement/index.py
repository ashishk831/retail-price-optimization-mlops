import os
from dotenv import load_dotenv
from sqlalchemy import Column,Date,DateTime,Integer,Numeric,Sequence,create_engine,String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool

load_dotenv()

engine = create_engine(
    os.getenv("DB_URL"),
    echo=True,
    pool_size=5,
    max_overflow=-1,
    pool_recycle=3600,
    pool_pre_ping=True,
    connect_args={
        "connect_timeout":60,
        "keepalives":1,
        "keepalives_idle":30,
        "keepalives_interval":10,
        "keepalives_count":5,
    },
)

Session = sessionmaker(bind=engine)
connection = engine.connect()
connection.close()

Base = declarative_base()

class RetailPrices(Base):
    __tablename__ = 'retail_prices'
    id = Column(Integer,Sequence("retail_prices_id_seq"),primary_key=True)
    product_id = Column(String)
    product_category_name = Column(String)
    month_year = Column(DateTime)
    qty = Column(Integer)
    total_price = Column(Numeric(precision=23,scale=15))
    freight_price = Column(Numeric(precision=23,scale=15))
    unit_price = Column(Numeric(precision=23,scale=15))
    product_name_lenght = Column(Integer)
    product_description_lenght = Column(Integer)
    product_photos_qty = Column(Integer)
    product_weight_g = Column(Integer)
    product_score = Column(Numeric(precision=5,scale=3))
    customers = Column(Integer)
    weekday = Column(Integer)
    weekend = Column(Integer)
    holiday = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    s = Column(Numeric(precision=23,scale=15))
    volume = Column(Integer)
    comp_1 = Column(Numeric(precision=23,scale=15))
    ps1 = Column(Numeric(precision=5,scale=3))
    fp1 = Column(Numeric(precision=23,scale=15))
    comp_2 = Column(Numeric(precision=23,scale=15))
    ps2 = Column(Numeric(precision=5,scale=3))
    fp2 = Column(Numeric(precision=23,scale=15))
    comp_3 = Column(Numeric(precision=23,scale=15))
    ps3 = Column(Numeric(precision=5,scale=3))
    fp3 = Column(Numeric(precision=23,scale=15))
    lag_price = Column(Numeric(precision=23,scale=15))
