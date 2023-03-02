from sqlalchemy.orm import relationship
from init_app import db


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text(200))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.Text(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    customer = relationship('User', foreign_keys=[customer_id])
    executor = relationship('User', foreign_keys=[executor_id])

    def to_dict(self, customer=None, executor=None):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.strftime('%m/%d/%Y'),
            'end_date': self.end_date.strftime('%m/%d/%Y'),
            'address': self.address,
            'price': self.price,
            'customer_id': self.customer_id,
            'executor_id': self.executor_id,
            'customer': customer,
            'executor': executor,
        }