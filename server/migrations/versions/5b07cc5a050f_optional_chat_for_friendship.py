"""optional chat for friendship

Revision ID: 5b07cc5a050f
Revises:
Create Date: 2024-07-28 12:58:39.225903

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "5b07cc5a050f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Rendre la colonne chat_id nullable
    with op.batch_alter_table("friendships") as batch_op:
        batch_op.alter_column("chat_id", existing_type=sa.Integer(), nullable=True)


def downgrade():
    # Rendre la colonne chat_id non nullable
    with op.batch_alter_table("friendships") as batch_op:
        batch_op.alter_column("chat_id", existing_type=sa.Integer(), nullable=False)
