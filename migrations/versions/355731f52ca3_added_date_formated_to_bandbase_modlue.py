"""Added date_formated to BandBase Modlue

Revision ID: 355731f52ca3
Revises: c51fda460d20
Create Date: 2024-11-06 13:39:49.620771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '355731f52ca3'
down_revision: Union[str, None] = 'c51fda460d20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('band', sa.Column('date_formed', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('band', 'date_formed')
    # ### end Alembic commands ###
