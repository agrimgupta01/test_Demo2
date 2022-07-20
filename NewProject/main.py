from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'JavaScript'}, {'name': 'Python'}, {'name': 'Ruby'}]


@app.route("/")
def hello_world():
    return "Hello World !"


@app.route("/lang", methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
    langauge2 = {'name2': request.json['name2'], 'name': request.json['name']}
    return jsonify(langauge2)
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})

@app.route('/predict', methods=['post'])
    def predict():
        
        
@app.route("/armstrong/<int:n>")
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n > 0):
        digit = n % 10
        sum += digit ** order
        n = n//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Is Armstrong ?": True,
            "Number": copy_n,
            "Other Numbers": [1, 370, 407],
            "Server link": f"127.0.0.1:5000/armstrong/{copy_n}"
        }

    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Is Armstrong ?": False,
            "Number": copy_n,
            "Other Numbers": [5, 129, 236],
            "Server link": f"127.0.0.1:5000/armstrong/{copy_n}"
        }

    return result


if __name__ == "__main__":
    app.run(debug=True)
