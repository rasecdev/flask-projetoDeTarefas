"""empty message

Revision ID: 1c9a01b053b1
Revises: 8890d4664892
Create Date: 2020-05-01 21:23:26.825834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c9a01b053b1'
down_revision = '8890d4664892'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funcionario_projeto',
    sa.Column('projeto_id', sa.Integer(), nullable=False),
    sa.Column('funcionario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['funcionario_id'], ['funcionario.id'], ),
    sa.ForeignKeyConstraint(['projeto_id'], ['projeto.id'], ),
    sa.PrimaryKeyConstraint('projeto_id', 'funcionario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('funcionario_projeto')
    # ### end Alembic commands ###
