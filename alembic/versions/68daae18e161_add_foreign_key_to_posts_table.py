"""add foreign-key to posts table

Revision ID: 68daae18e161
Revises: fbf46b84ec74
Create Date: 2023-08-04 03:36:09.589785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68daae18e161'
down_revision = 'fbf46b84ec74'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fkey', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
