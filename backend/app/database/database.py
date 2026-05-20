import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# 1. اقرأ اسم الملف من متغير البيئة اللي باصيناه في التيرمنال، ولو مش موجود اعتبره .env.dev كـ default
env_file_name = os.getenv("ENV_FILE", ".env.dev")

# 2. اجبر dotenv تقرأ الملف المحدد ده بالظبط
load_dotenv(dotenv_path=env_file_name)

DATABASE_URL = os.getenv("DATABASE_URL")

# تأكيد أمان: لو لسه مش قاري، ارمي Exception واضحة تفهمنا في إيه
if not DATABASE_URL:
    raise ValueError(f"المعذرة يا أحمد! لم نتمكن من العثور على DATABASE_URL داخل ملف البيئة: {env_file_name}")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()