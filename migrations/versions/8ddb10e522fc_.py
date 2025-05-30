"""Create expense table

Revision ID: 8ddb10e522fc
Revises: 
Create Date: 2024-04-24 03:12:08.539843

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8ddb10e522fc"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "expense",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=50), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_expense")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("expense")
    # ### end Alembic commands ###
