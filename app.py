from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_chars = []
        total_sum = 0
        concat_str = ""

        for item in data:
            if str(item).isdigit() or (item.startswith('-') and item[1:].isdigit()):
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(item))
                else:
                    odd_numbers.append(str(item))
            elif str(item).isalpha():
                alphabets.append(str(item).upper())
                concat_str += str(item)
            else:
                special_chars.append(str(item))

        # alternating caps reverse
        alt_concat = ""
        reversed_concat = concat_str[::-1]
        upper = True
        for c in reversed_concat:
            alt_concat += c.upper() if upper else c.lower()
            upper = not upper

        response = {
            "is_success": True,
            "user_id": "khushi_srivas_18052005",
            "email": "khushishrivas1805@gmail.com",
            "roll_number": "22BCE2424",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": alt_concat
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
