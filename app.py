from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)

chat_history = []

@app.route("/predict", methods=["POST"])
def prediction():

    fever = 1 if request.form.get("fever")=="on" else 0
    cough = 1 if request.form.get("cough")=="on" else 0
    fatigue = 1 if request.form.get("fatigue")=="on" else 0
    headache = 1 if request.form.get("headache")=="on" else 0
    cold = 1 if request.form.get("cold")=="on" else 0
    bodypain = 1 if request.form.get("bodypain")=="on" else 0
    vomiting = 1 if request.form.get("vomiting")=="on" else 0
    diarrhea = 1 if request.form.get("diarrhea")=="on" else 0

    # 🧠 Disease Logic
    if fever and cough and fatigue:
        result = "Flu 😷"

    elif fever and bodypain and headache:
        result = "Dengue 🦟"
        result += " ⚠️ Please consult a doctor immediately!"

    elif cold and cough:
        result = "Common Cold 🤧"

    elif vomiting and diarrhea:
        result = "Food Poisoning 🤢"

    elif fatigue and headache:
        result = "Stress 😓"

    else:
        result = "No major disease detected 🙂"

    return render_template("index.html", prediction=result, chat_history=chat_history)

@app.route("/emergency", methods=["POST"])
def emergency():
    message = "🚑 Emergency request sent! Contacting nearest hospital..."
    message += " 📞 Call: 108"

    return render_template("index.html",
                           emergency_msg=message,
                           chat_history=chat_history)
    
if __name__ == "__main__":
    app.run(debug=True)