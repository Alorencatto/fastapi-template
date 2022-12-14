"""Create initial databases

Revision ID: ae7ba8d59217
Revises:
Create Date: 2022-08-27 06:12:25.901603

"""
import sqlalchemy as sa
import sqlmodel

from alembic import op

# revision identifiers, used by Alembic.
revision = "ae7ba8d59217"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("modified_at", sa.DateTime(), nullable=True),
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("full_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("hashed_password", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email", name="user_email_unique"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=False)
    op.create_index(op.f("ix_user_uuid"), "user", ["uuid"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_uuid"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
