from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# יצירת אובייקט Flask
app = Flask(__name__)

# הגדרת ה-URI למסד הנתונים
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # השתמש בשם הקובץ שלך אם שונה
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # כדי להימנע מהתרעות מיותרות

# יצירת אובייקט db
db = SQLAlchemy(app)

# הגדרת המודל
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    agent = db.Column(db.String(100), nullable=True)  # אופציונלי, אם רוצים לשמור מי עדכן

# יצירת הטבלאות
with app.app_context():
    db.create_all()  # יצירת כל הטבלאות
    print("✅ טבלאות נוצרו בהצלחה!")
