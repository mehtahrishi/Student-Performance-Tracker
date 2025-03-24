import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_super_secret_key_123")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://student_perf_track_user:Nng88pgNlyzD8hMcounASNHBQ7Y7taau@dpg-cvgl6udds78s73f7m0jg-a.oregon-postgres.render.com/student_perf_track")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
