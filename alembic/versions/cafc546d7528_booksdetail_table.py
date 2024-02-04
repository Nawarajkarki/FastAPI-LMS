"""booksdetail table

Revision ID: cafc546d7528
Revises: 9b1d7cf45a6e
Create Date: 2024-02-04 00:44:00.351687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cafc546d7528'
down_revision: Union[str, None] = '9b1d7cf45a6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books_detail',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True),
        sa.Column('book_id', sa.Integer, sa.ForeignKey('books.id'),unique=True, nullable=False),
        sa.Column('num_of_pages', sa.INTEGER, nullable=False),
        sa.Column('publisher', sa.VARCHAR(50), nullable=False),
        sa.Column('language', sa.VARCHAR(10))
    )

def downgrade() -> None:
    op.drop_table('books_detail')
