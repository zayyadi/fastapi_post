"""add foreign key to post

Revision ID: c42400dc6595
Revises: 217dae25ce45
Create Date: 2022-05-19 11:52:41.033335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c42400dc6595'
down_revision = '217dae25ce45'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        'post_users_fk', source_table="posts", referent_table="users",
        local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE"
    )
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
