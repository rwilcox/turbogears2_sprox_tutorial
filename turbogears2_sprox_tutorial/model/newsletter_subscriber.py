from sqlalchemy import *
from sqlalchemy.orm import relation

from turbogears2_sprox_tutorial.model import DeclarativeBase, metadata, DBSession

class NewsletterSubscriber(DeclarativeBase):
    __tablename__ = "newsletter_subscriber"
    
    # column definitions
    id = Column(u'id', Integer(), primary_key=True, nullable=False)
    full_name = Column("full_name", Text)
    email_address = Column("email_address", Text)
