from sqlalchemy import create_engine, Column, String,NUMERIC,VARCHAR,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://user:pass@localhost:5432/pc')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#Class declaration
class Computers(Base):
    __tablename__ = 'computers'
    id = Column(Integer, primary_key= True)

    hard_drive = Column(VARCHAR)
    processor = Column(VARCHAR)
    amount_of_ram = Column(VARCHAR)
    maximum_ram = Column(VARCHAR)
    hard_drive_space = Column(VARCHAR)
    form_factor = Column(VARCHAR)

    def __init__(self, hard_drive, processor, amount_of_ram, maximum_ram, hard_drive_capacity, form_factor):
        
        self.hard_drive = hard_drive
        self.processor = processor
        self.amount_of_ram = amount_of_ram
        self.maximum_ram = maximum_ram
        self.hard_drive_capacity = hard_drive_capacity
        self.form_factor = form_factor
        
        session.commit()
        
    # Function inserts all instances of computer and commits the changes
    def save_computer(self):
        session.add(self)
        session.commit()

#Insert into functions
Computer_1 = Computer("WD","Intel Core i3","2GB","2.4GB","512GB","Micro-ATX")
Computer_2 = Computer("Western Digital","Intel Core i7","8GB","16GB","2TB","Mini-ITX")
Computer_3 = Computer("Toshiba Canvio Advance","Intel Core i7 6th Gen","4GB","8GB","4TB","Mini-ITX")
Computer_4 = Computer("WD","Intel Core i3","8GB","16GB","4TB","Micro-ATX")
Computer_5 = Computer("Seagate","Intel Core i5 6th Gen","2.4GB","4GB","1TB","Standard-ATX")
session.add(Computer1)
session.add(Computer2)
session.add(Computer3)
#Commits all the changes to the database
session.commit()