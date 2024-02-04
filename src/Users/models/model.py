import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref


from src.entrypoint.database import Base




class User(Base):
    __tablename__ = "users"
    
    id = sa.Column( sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    name = sa.Column( sa.VARCHAR(50), nullable=False)
    email = sa.Column( sa.VARCHAR(50), nullable=False)
    membership_date = sa.Column( sa.DateTime, default=sa.func.now())
    
    # # Relationships
    # borrowings = relationship("BorrowedBooks", back_populates="user")
    
    