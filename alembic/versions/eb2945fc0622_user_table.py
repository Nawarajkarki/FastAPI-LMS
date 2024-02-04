"""user table

Revision ID: eb2945fc0622
Revises: 
Create Date: 2024-02-04 00:27:08.134184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb2945fc0622'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True),
        sa.Column('name', sa.VARCHAR(50), nullable=False),
        sa.Column('email', sa.VARCHAR(50), nullable=False),
        sa.Column('membership_date', sa.DateTime, default=sa.func.now())
    )



def downgrade() -> None:
    op.drop_table('users')
