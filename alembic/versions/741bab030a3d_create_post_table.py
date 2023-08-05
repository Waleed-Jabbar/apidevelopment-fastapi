"""Create Post Table

Revision ID: 741bab030a3d
Revises: 
Create Date: 2023-08-04 03:05:04.095430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '741bab030a3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
