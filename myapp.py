from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        numbers = [x for x in data if x.isdigit()]  
        alphabets = [x for x in data if x.isalpha()]  
        lowercase_alphabets = [x for x in alphabets if x.islower()]  
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else ""

        response = {
            "is_success": True,
            "user_id": "rahul_l_0508",  
            "email": "rahul.l2021@vitstudent.ac.in",
            "roll_number": "21BIT0343",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == "__main__":
    app.run(debug=True)
