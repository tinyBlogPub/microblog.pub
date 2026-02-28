"""unpack ap_in_reply_to

Revision ID: 49774a0f5911
Revises: aa8e72de7bb6
Create Date: 2025-01-10 12:21:31.055099+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49774a0f5911'
down_revision = 'aa8e72de7bb6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('inbox', schema=None) as batch_op:
        batch_op.add_column(sa.Column('in_reply_to', sa.Integer()))
        batch_op.create_index(batch_op.f('ix_inbox_in_reply_to'), ['in_reply_to'], unique=False)

    with op.batch_alter_table('outbox', schema=None) as batch_op:
        batch_op.add_column(sa.Column('in_reply_to', sa.Integer()))
        batch_op.create_index(batch_op.f('ix_outbox_in_reply_to'), ['in_reply_to'], unique=False)

    op.execute("UPDATE inbox SET in_reply_to = json_extract(ap_object, '$.inReplyTo')")
    op.execute("UPDATE outbox SET in_reply_to = json_extract(ap_object, '$.inReplyTo')")


def downgrade() -> None:
    with op.batch_alter_table('inbox', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_inbox_in_reply_to'))
        batch_op.drop_column('in_reply_to')

    with op.batch_alter_table('outbox', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_outbox_in_reply_to'))
        batch_op.drop_column('in_reply_to')
