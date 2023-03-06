"""add farmer target address wallet farmed

Revision ID: 90ef99cf2702
Revises: 9c3e39b16d38
Create Date: 2023-03-06 21:34:11.262233

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '90ef99cf2702'
down_revision = '9c3e39b16d38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('farmer_target_wallet_balance_events', sa.Column('farmed', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('farmer_target_wallet_balance_events', 'farmed')
    # ### end Alembic commands ###
