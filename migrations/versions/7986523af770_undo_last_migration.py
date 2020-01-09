"""undo last migration

Revision ID: 7986523af770
Revises: e82f64dbb502
Create Date: 2019-12-22 12:28:45.680832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7986523af770'
down_revision = 'e82f64dbb502'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post') as batch_op:
        batch_op.drop_column('language')
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('language')
    # op.drop_column('post', 'language')
    # op.drop_column('user', 'language')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('language', sa.VARCHAR(length=5), nullable=True))
    op.add_column('post', sa.Column('language', sa.VARCHAR(length=5), nullable=True))
    # ### end Alembic commands ###
