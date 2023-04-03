"""create post table

Revision ID: 7950c17feb61
Revises: 
Create Date: 2023-04-02 05:22:51.773194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7950c17feb61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
