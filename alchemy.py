from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmakerengine = create_engine('postgresql+psycopg2://pguser:password@localhost/sql_alchem')

engine.connect()Session = sessionmaker(bind=engine)

session = Session()Base = declarative_base()class Compputer(Base):    __tablename__ = 'computers'    id = Column(Integer, primary_key=True)
    hard_drive_type = Column(String)
    processor = Column(Integer)
    amount_of_ram = Column(String)
    maximum_ram = Column(String)
    hard_drive_space = Column(String)
    form_factor = Column(String)
    
    def __init__(self, hard_drive_type, processor, amount_of_ram, maximum_ram, hard_drive_space, form_factor):
        self.hard_drive_type = hard_drive_type
        self.processor = processor
        self.amount_of_ram = amount_of_ram
        self.hard_drive_space = hard_drive_space
        self.form_factor = form_factor
        
        #Lists all the compputers that have been added or saved
        def list_computers(self):
            session.list(self)

        #Add a computer to the database
        def add_computer(self):
            pass

        #Edit/Append an already exiting computer in the database
        def edit_computer(self):
            pass

        # Delete a computer in the databass
        def delete_computer(self):
            pass
        # Save all added computers
        def save_computers(self):
            session.add(self)

        session.commit()
        def __repr__(self):
        return f"Recruit: {self.email}"#Making migrations / Creating the table


# Base.metadata.create_all(engine)#Inserting
# rec = Recruits("Mk", 4, "mk@here.com", "Data")
# rec.save_recruit()#Query the database
# records = session.query(Recruits).filter(Recruits.name == 'Mk').first()# print(records)