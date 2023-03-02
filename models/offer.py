from sqlalchemy.orm import relationship
from init_app import db


class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order = relationship('Order')
    executor = relationship('User')

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'executor_id': self.executor_id,
        }
