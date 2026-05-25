from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    cost = Column(Float)
    supplier = Column(String)
    discount = Column(Float, default=1.0)
    image_url = Column(String)
    shelf_id = Column(Integer)          # 关联货架ID
    pos_x = Column(Float, nullable=False)  # 物理坐标X(米)
    pos_y = Column(Float, nullable=False)  # 物理坐标Y(米)

class Obstacle(Base):
    __tablename__ = "obstacles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)               # 'rect', 'polygon'
    # 如果是矩形：x1,y1为左下角，x2,y2为右上角
    x1 = Column(Float)
    y1 = Column(Float)
    x2 = Column(Float)
    y2 = Column(Float)
    polygon_coords = Column(Text)       # JSON字符串，用于多边形

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ingredients = Column(Text)          # JSON数组，如 '["五花肉","酱油"]'