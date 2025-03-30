from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# הגדרת הנתיב לקובץ ה-DB בתיקיית instance
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# הגדרת מסד הנתונים (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# יצירת מודל של מסד הנתונים
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    agent = db.Column(db.String(100))

# יצירת הטבלאות אם לא קיימות
with app.app_context():
    db.create_all()

# דף הבית (מציג טופס להזנת פריט חדש)
@app.route('/')
def index():
    return render_template('index.html')

# דף להוספת פריט חדש
@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item']
    quantity = request.form['quantity']
    agent = request.form['agent']

    # יצירת פריט חדש
    new_item = Inventory(item=item_name, quantity=int(quantity), agent=agent)

    # הוספת הפריט למסד הנתונים
    db.session.add(new_item)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

