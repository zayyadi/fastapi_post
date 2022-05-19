"""create content column tables

Revision ID: d43d391c3774
Revises: eb406b2c5fb2
Create Date: 2022-05-18 21:01:43.157795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd43d391c3774'
down_revision = 'eb406b2c5fb2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
