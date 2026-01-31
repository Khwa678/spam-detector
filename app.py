from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('spam_classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    message = data.get('message', '').strip()

    if not message:
        return jsonify({'result': '⚠️ Please enter a message'}), 400

    prediction = model.predict([message])[0]
    result = "🚨 Spam Message" if prediction == 1 else "✅ Not Spam (Ham)"
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
