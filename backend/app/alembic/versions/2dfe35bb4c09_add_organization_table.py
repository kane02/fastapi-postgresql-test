"""Add organization table

Revision ID: 2dfe35bb4c09
Revises: d4867f3a4c0a
Create Date: 2023-09-08 12:16:06.524381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dfe35bb4c09'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organization_id'), 'organization', ['id'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_organization_id'), table_name='organization')
    op.drop_table('organization')
    # ### end Alembic commands ###
