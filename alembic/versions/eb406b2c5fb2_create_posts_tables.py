"""create posts tables

Revision ID: eb406b2c5fb2
Revises: 
Create Date: 2022-05-18 20:51:36.474207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb406b2c5fb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False),
    )
    pass


def downgrade():
    pass
