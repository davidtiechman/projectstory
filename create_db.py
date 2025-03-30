from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    agent = db.Column(db.String(100), nullable=True)

with app.app_context():
    db.create_all()  # יצירת טבלאות
    print("✅ טבלאות נוצרו בהצלחה!")
