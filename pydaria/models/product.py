from ext.database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)


    def __init__(self, id, name, price, description):
        self.id = id 
        self.name = name 
        self.price = price
        self.description = description


    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price' : self.price,
            'description' : self.description
        }
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

