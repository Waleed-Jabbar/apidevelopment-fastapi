"""Add content column to posts table

Revision ID: 9dda36610f9c
Revises: 741bab030a3d
Create Date: 2023-08-04 03:15:02.929846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dda36610f9c'
down_revision = '741bab030a3d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
