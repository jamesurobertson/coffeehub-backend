"""initial migration

Revision ID: c80ff94d3f6b
Revises: 
Create Date: 2020-07-18 14:32:22.718550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c80ff94d3f6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('origins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('fullName', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('hashedPassword', sa.String(length=128), nullable=False),
    sa.Column('profileImageUrl', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=2000), nullable=True),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('follows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('userFollowedId', sa.Integer(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roasts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('supplier', sa.String(length=100), nullable=True),
    sa.Column('originId', sa.Integer(), nullable=True),
    sa.Column('bean', sa.String(length=50), nullable=True),
    sa.Column('ambientTemp', sa.Float(), nullable=True),
    sa.Column('load', sa.Float(), nullable=True),
    sa.Column('yieldNum', sa.Float(), nullable=True),
    sa.Column('firstCrack', sa.String(), nullable=True),
    sa.Column('secondCrack', sa.String(), nullable=True),
    sa.Column('totalTime', sa.String(length=10), nullable=True),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['originId'], ['origins.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('roastId', sa.Integer(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['roastId'], ['roasts.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('roastId', sa.Integer(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['roastId'], ['roasts.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('milestones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roastId', sa.Integer(), nullable=False),
    sa.Column('roastTemp', sa.String(length=20), nullable=True),
    sa.Column('timestamp', sa.String(length=20), nullable=True),
    sa.Column('fanspeed', sa.Integer(), nullable=False),
    sa.Column('heatLevel', sa.Integer(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['roastId'], ['roasts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roastId', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(length=255), nullable=False),
    sa.Column('timestamp', sa.String(length=20), nullable=True),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['roastId'], ['roasts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('timestamps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roastId', sa.Integer(), nullable=False),
    sa.Column('roastTemp', sa.Float(), nullable=False),
    sa.Column('timestamp', sa.Float(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['roastId'], ['roasts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timestamps')
    op.drop_table('notes')
    op.drop_table('milestones')
    op.drop_table('cups')
    op.drop_table('comments')
    op.drop_table('roasts')
    op.drop_table('follows')
    op.drop_table('users')
    op.drop_table('origins')
    # ### end Alembic commands ###