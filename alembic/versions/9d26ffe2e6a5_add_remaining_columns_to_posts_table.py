"""add remaining columns to posts table

Revision ID: 9d26ffe2e6a5
Revises: 68daae18e161
Create Date: 2023-08-04 03:45:59.639627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d26ffe2e6a5'
down_revision = '68daae18e161'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
    sa.Column("published", sa.Boolean(), server_default='True', nullable=False))
    op.add_column('posts',
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
