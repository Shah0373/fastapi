"""add content column to posts table

Revision ID: e67b36316978
Revises: 7950c17feb61
Create Date: 2023-04-02 05:37:17.648145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e67b36316978'
down_revision = '7950c17feb61'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
