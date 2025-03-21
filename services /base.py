from sqlalchemy.orm import sessionmaker
from config.engine import engine

class DbConnection:
    
    def __init__(self):
        self.session = None

    #getting self.session using this decorator
    @property
    def connection(self):
        
        if self.session is None:
            Session = sessionmaker(bind=engine)
            # self.session = engine.connect()
            self.session = Session()
        return self.session

#session is basically which interacts with the db 