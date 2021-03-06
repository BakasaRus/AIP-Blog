"""Increase password field size

Revision ID: 09120c7c634c
Revises: bf28c185b2a3
Create Date: 2021-03-16 22:46:14.845037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09120c7c634c'
down_revision = 'bf28c185b2a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=127),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=127),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
    # ### end Alembic commands ###
