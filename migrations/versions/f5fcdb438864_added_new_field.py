"""added new field

Revision ID: f5fcdb438864
Revises: 8e3111150d3a
Create Date: 2022-08-19 10:15:46.424298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5fcdb438864'
down_revision = '8e3111150d3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('test', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'test')
    # ### end Alembic commands ###
