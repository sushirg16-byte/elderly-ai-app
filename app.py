from flask import Flask, render_template, request

app = Flask(__name__)

chat_history = []

# ✅ HOME PAGE
@app.route("/")
def home():
    return render_template("index.html", chat_history=chat_history)

# ✅ PREDICTION
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

    # 🧠 DISEASE LOGIC + CAUSES + MEDICINE
    if fever and cough and fatigue:
        result = "Flu 🤒"
        cause = "Cause: Viral infection affecting respiratory system."
        medicine = "💊 Paracetamol, rest, warm fluids."
        warning = "⚠️ Visit doctor if symptoms last more than 3 days."

    elif fever and bodypain and headache:
        result = "Dengue 🦟"
        cause = "Cause: Mosquito-borne viral infection."
        medicine = "❌ Avoid self-medication."
        warning = "🚨 Serious! Visit doctor immediately."

    elif fatigue and headache:
        result = "Stress / Migraine 😓"
        cause = "Cause: Lack of sleep, stress, dehydration."
        medicine = "💊 Rest, hydration, mild pain reliever."
        warning = "⚠️ Doctor if severe or frequent."

    elif bodypain and cold:
        result = "Viral Infection 🤧"
        cause = "Cause: Seasonal virus or weak immunity."
        medicine = "💊 Paracetamol, steam inhalation."
        warning = "⚠️ Doctor if not improving."

    elif fever and fatigue:
        result = "Viral Fever 🤒"
        cause = "Cause: Body fighting infection."
        medicine = "💊 Paracetamol, fluids, rest."
        warning = "⚠️ Doctor if fever continues >2 days."

    elif cold and bodypain:
        result = "Seasonal Flu 🤧"
        cause = "Cause: Weather change, viral infection."
        medicine = "💊 Cetirizine, steam."
        warning = "⚠️ Doctor if breathing issues."

    elif cold and diarrhea:
        result = "Stomach Infection 🤢"
        cause = "Cause: Contaminated food or water."
        medicine = "💊 ORS, light food."
        warning = "⚠️ Doctor if severe dehydration."

    elif vomiting and diarrhea:
        result = "Food Poisoning 🤢"
        cause = "Cause: Eating contaminated food."
        medicine = "💊 ORS, hydration."
        warning = "⚠️ Doctor if continuous vomiting."

    elif cold and cough:
        result = "Common Cold 🤧"
        cause = "Cause: Viral infection."
        medicine = "💊 Cetirizine, steam."
        warning = ""

    elif fever:
        result = "Possible Infection 🌡️"
        cause = "Cause: Body response to infection."
        medicine = "💊 Paracetamol."
        warning = "⚠️ Doctor if high fever."

    else:
        result = "No major disease 😌"
        cause = "Cause: Mild or no illness."
        medicine = "💊 Rest and hydration."
        warning = ""

    # Combine output
    final_result = f"{result}\n{cause}\n{medicine}\n{warning}"

    chat_history.append(("Bot", final_result))

    return render_template("index.html",
                           prediction=result,
                           cause=cause,
                           medicine=medicine,
                           warning=warning,
                           chat_history=chat_history)

# ✅ EMERGENCY BUTTON
@app.route("/emergency", methods=["POST"])
def emergency():
    message = "🚑 Emergency request sent! Contacting nearest hospital..."
    message += " 📞 Call: 108"

    return render_template("index.html",
                           emergency_msg=message,
                           chat_history=chat_history)

# ✅ CHATBOT
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form.get("msg").lower()

    chat_history.append(("You", user_msg))

    if "flu" in user_msg:
        reply = "💊 Take Paracetamol, rest, fluids. ⚠️ Doctor if severe."

    elif "dengue" in user_msg:
        reply = "🚨 Serious! Go to doctor immediately."

    elif "cold" in user_msg:
        reply = "💊 Cetirizine + steam inhalation."

    elif "body pain" in user_msg:
        reply = "💊 Paracetamol, rest."

    elif "fever" in user_msg:
        reply = "💊 Paracetamol. ⚠️ Doctor if >2 days."

    elif "diarrhea" in user_msg:
        reply = "💊 ORS, hydration."

    elif "medicine" in user_msg:
        reply = "Tell symptoms (fever, cold, etc.) for suggestion."

    else:
        reply = "Sorry, I didn't understand. Please describe symptoms."

    chat_history.append(("Bot", reply))

    return render_template("index.html",
                           chat_history=chat_history)

# ✅ RUN
if __name__ == "__main__":
    app.run(debug=True)