import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '5U/Q_jcO(YPxSNkj')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://kaydee:#Kayode1@localhost/government_crime_report_system')
