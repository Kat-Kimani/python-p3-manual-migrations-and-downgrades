"""Renaming students to scholars

Revision ID: c9119ceb7028
Revises: 791279dd0760
Create Date: 2023-06-02 14:01:39.876095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c9119ceb7028"
down_revision = "791279dd0760"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students", "scholars")


def downgrade() -> None:
    op.rename_table("scholars", "students")
