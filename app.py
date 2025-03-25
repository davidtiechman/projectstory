from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# נתיב להצגת העמוד הראשי
@app.route("/")
def index():
    return render_template("index.html")

# נתיב לקבלת המלאי הנוכחי
@app.route("/inventory")
def get_inventory():
    with open("inventory.json", "r") as file:
        inventory = json.load(file)
    return jsonify(inventory)

# נתיב לעדכון המלאי
@app.route("/update", methods=["POST"])
def update_inventory():
    item = request.form["item"]
    quantity = int(request.form["quantity"])
    agent = request.form["agent"]

    # קריאת הנתונים מהקובץ
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    # עדכון המלאי
    if item in inventory:
        inventory[item] -= quantity  # מחסירים מהמלאי את הכמות שנמכרה

    # שמירת השינויים בקובץ
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    # אפשר להוסיף את שם הסוכן לנתונים (למשל בהודעות או לוגים)
    print(f"סוכן {agent} עדכן את המלאי: {item} - {quantity} פריטים נמכרו.")

    return "Inventory updated successfully!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

