"""books table

Revision ID: 9b1d7cf45a6e
Revises: eb2945fc0622
Create Date: 2024-02-04 00:34:00.184552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b1d7cf45a6e'
down_revision: Union[str, None] = 'eb2945fc0622'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True),
        sa.Column('title', sa.VARCHAR(255), nullable=False),
        sa.Column('isbn', sa.BIGINT, nullable=False, unique=True),
        sa.Column('published_date', sa.DateTime, server_default=sa.func.now()),
        sa.Column('genre', sa.VARCHAR(55))
    )

def downgrade() -> None:
    op.drop_table('books')
