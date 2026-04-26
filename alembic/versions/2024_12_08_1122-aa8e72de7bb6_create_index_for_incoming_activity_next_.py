"""create index for incoming activity next try

Revision ID: aa8e72de7bb6
Revises: a209f0333f5a
Create Date: 2024-12-09 11:22:57.917748+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa8e72de7bb6'
down_revision = 'a209f0333f5a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('incoming_activity', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_incoming_activity_next_try'), ['next_try'], unique=False)
        batch_op.create_index(batch_op.f('ix_incoming_activity_status'), ['is_processed', 'is_errored'], unique=False)


def downgrade() -> None:
    with op.batch_alter_table('incoming_activity', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_incoming_activity_next_try'))
        batch_op.drop_index(batch_op.f('ix_incoming_status'))
