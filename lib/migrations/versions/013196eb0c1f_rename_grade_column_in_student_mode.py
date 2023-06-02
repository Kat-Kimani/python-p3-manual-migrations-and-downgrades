"""Rename grade column in Student mode

Revision ID: 013196eb0c1f
Revises: c9119ceb7028
Create Date: 2023-06-02 16:30:02.342437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "013196eb0c1f"
down_revision = "c9119ceb7028"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("scholars", "grade", new_column_name="class_grade")


def downgrade() -> None:
    op.alter_column("scholars", "class_grade", new_column_name="grade")
