from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 数据库文件路径（会自动在 backend/data 下生成 supermarket.db）
DATABASE_URL = "sqlite:///./data/supermarket.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()