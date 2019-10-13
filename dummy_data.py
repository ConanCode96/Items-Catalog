from DB_setup import Item, User, Category
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# creating an engine to the SQL database
engine = create_engine('sqlite:///ItemCatalogDB.db',
                       connect_args={'check_same_thread': False})

# Bind the db engine to a session to interact with the database.
Session = sessionmaker(bind=engine)

# Create a DataBase Session object.
session = Session()

# Fake user data
fake_user = User(
    name='Hossam',
    email='conancode96@gmail.com',
    picture='''http://icons.iconarchive.com
               /icons/aha-soft/free-large-boss/512/Caucasian-Boss-icon.png'''
)
# Adding then committing
session.add(fake_user)
session.commit()

# Fake category data
fake_category = Category(
    name='MEWOs',
    user=fake_user
)
# Adding then committing
session.add(fake_category)
session.commit()

# Fake Item data
item1 = Item(
    name='Cat',
    description='meow! meow! can you recognize me now?!',
    category=fake_category,
    user=fake_user
)
# Adding then committing
session.add(item1)
session.commit()


# Voila!!! ^_^
print('Finished populating the database!')
