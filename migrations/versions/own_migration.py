"""added new field

Revision ID: f5fcdb438864
Revises: 8e3111150d3a
Create Date: 2022-08-19 10:15:46.424298

"""
from sqlalchemy import text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5fcdb438865'
down_revision = 'f5fcdb438864'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = 100
                WHERE title like '%Deathly%'
            """
        )
    )

def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = NULL
                WHERE title like '%Deathly%'
            """
        )
    )
