"""Add is_admin field

Revision ID: 3753a06e3dd6
Revises: 
Create Date: 2021-03-02 20:02:14.951765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3753a06e3dd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_admin')
    # ### end Alembic commands ###
