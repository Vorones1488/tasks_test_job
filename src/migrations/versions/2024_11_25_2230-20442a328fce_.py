"""empty message

Revision ID: 20442a328fce
Revises: 
Create Date: 2024-11-25 22:30:07.299377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20442a328fce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_name', sa.String(length=50), nullable=False),
    sa.Column('task_description', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_task', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('new_task', 'in_progress', 'completed_successfully', 'error', name='statusenum'), nullable=False),
    sa.ForeignKeyConstraint(['id_task'], ['task.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'id_task')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task_status')
    op.drop_table('task')
    # ### end Alembic commands ###
