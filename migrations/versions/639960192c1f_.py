"""empty message

Revision ID: 639960192c1f
Revises: 1c9a01b053b1
Create Date: 2020-05-03 17:49:56.138014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '639960192c1f'
down_revision = '1c9a01b053b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###