"""borrowed books table

Revision ID: 2c1fc15f1580
Revises: cafc546d7528
Create Date: 2024-02-04 00:47:26.736704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c1fc15f1580'
down_revision: Union[str, None] = 'cafc546d7528'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books_borrowed',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True),
        sa.Column('book_id', sa.Integer, sa.ForeignKey('books.id'), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('borrow_date', sa.DateTime, nullable=False),
        sa.Column('return_date', sa.DateTime)
    )

def downgrade() -> None:
    op.drop_table('books_borrowed')
