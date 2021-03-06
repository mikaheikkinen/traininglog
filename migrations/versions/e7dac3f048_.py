"""empty message

Revision ID: e7dac3f048
Revises: None
Create Date: 2015-09-22 16:03:30.578268

"""

# revision identifiers, used by Alembic.
revision = 'e7dac3f048'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('result_all', postgresql.JSON(), nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###
