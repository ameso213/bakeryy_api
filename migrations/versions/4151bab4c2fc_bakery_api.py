"""bakery_api

Revision ID: 4151bab4c2fc
Revises: 
Create Date: 2024-06-20 11:56:17.450793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4151bab4c2fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('contact', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('join_date', sa.DateTime(), nullable=False),
    sa.Column('loyalty_points', sa.Integer(), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('unit', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('restock_date', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('payment_method', sa.String(length=50), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('transaction_id', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('transaction_id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('stock_quantity', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_type', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('contact', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_type')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('address_line1', sa.String(length=255), nullable=False),
    sa.Column('address_line2', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=100), nullable=False),
    sa.Column('zip_code', sa.String(length=20), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('order_items')
    op.drop_table('addresses')
    op.drop_table('users')
    op.drop_table('products')
    op.drop_table('payments')
    op.drop_table('orders')
    op.drop_table('inventory')
    op.drop_table('ingredients')
    op.drop_table('customers')
    op.drop_table('category')
    # ### end Alembic commands ###