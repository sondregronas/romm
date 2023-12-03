"""empty message

Revision ID: 0012_asset_files
Revises: 0011_drop_has_cover
Create Date: 2023-11-29 14:38:33.068098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0012_asset_files"
down_revision = "0011_drop_has_cover"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "bios",
        sa.Column("platform_slug", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("file_name", sa.String(length=450), nullable=False),
        sa.Column("file_name_no_tags", sa.String(length=450), nullable=False),
        sa.Column("file_extension", sa.String(length=10), nullable=False),
        sa.Column("file_path", sa.String(length=1000), nullable=False),
        sa.Column("file_size_bytes", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["platform_slug"], ["platforms.slug"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "emulators",
        sa.Column("platform_slug", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("file_name", sa.String(length=450), nullable=False),
        sa.Column("file_name_no_tags", sa.String(length=450), nullable=False),
        sa.Column("file_extension", sa.String(length=10), nullable=False),
        sa.Column("file_path", sa.String(length=1000), nullable=False),
        sa.Column("file_size_bytes", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["platform_slug"], ["platforms.slug"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "saves",
        sa.Column("emulator", sa.String(length=50), nullable=False),
        sa.Column("rom_id", sa.Integer(), nullable=False),
        sa.Column("platform_slug", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("file_name", sa.String(length=450), nullable=False),
        sa.Column("file_name_no_tags", sa.String(length=450), nullable=False),
        sa.Column("file_extension", sa.String(length=10), nullable=False),
        sa.Column("file_path", sa.String(length=1000), nullable=False),
        sa.Column("file_size_bytes", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["platform_slug"], ["platforms.slug"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["rom_id"], ["roms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "screenshots",
        sa.Column("rom_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("file_name", sa.String(length=450), nullable=False),
        sa.Column("file_name_no_tags", sa.String(length=450), nullable=False),
        sa.Column("file_extension", sa.String(length=10), nullable=False),
        sa.Column("file_path", sa.String(length=1000), nullable=False),
        sa.Column("file_size_bytes", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["rom_id"], ["roms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "states",
        sa.Column("emulator", sa.String(length=50), nullable=False),
        sa.Column("rom_id", sa.Integer(), nullable=False),
        sa.Column("platform_slug", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("file_name", sa.String(length=450), nullable=False),
        sa.Column("file_name_no_tags", sa.String(length=450), nullable=False),
        sa.Column("file_extension", sa.String(length=10), nullable=False),
        sa.Column("file_path", sa.String(length=1000), nullable=False),
        sa.Column("file_size_bytes", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["platform_slug"], ["platforms.slug"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["rom_id"], ["roms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("states")
    op.drop_table("screenshots")
    op.drop_table("saves")
    op.drop_table("emulators")
    op.drop_table("bios")
    # ### end Alembic commands ###