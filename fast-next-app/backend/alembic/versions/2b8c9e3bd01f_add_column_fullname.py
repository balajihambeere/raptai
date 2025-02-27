"""add column fullname

Revision ID: 2b8c9e3bd01f
Revises: 
Create Date: 2025-02-26 15:27:01.154755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b8c9e3bd01f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('fullname', sa.String(100), nullable=False))


def downgrade() -> None:
    pass
