DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "Welcome@123456"  
DATABASE_HOST = "40.81.230.178"
DATABASE_PORT = "3306"
DATABASE_NAME = "MY_SQL"

DATABASE_PASSWORD = DATABASE_PASSWORD.replace('@', '%40')

DATABASE_URL = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
