from flask import Flask, render_template, request, jsonify
from skills.trip_briefing import generate_briefing_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/briefing", methods=["POST"])
def briefing():
    """接收城市名稱，回傳各個 Tool 的結果"""
    data = request.get_json()
    city = data.get("city", "").strip()
    if not city:
        return jsonify({"error": "請輸入城市名稱"}), 400

    try:
        result = generate_briefing_data(city)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
