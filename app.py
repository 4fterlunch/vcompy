from flask import Flask, jsonify, request, render_template

app= Flask(__name__)

@app.route('/sensors',methods=['GET', 'POST'])
def resolveSensorRequest():
    if request.method == 'POST':
        print('POST message received')
        print(request.get_json())
        return 'OK', 200
    else:
        print('returning data for GET')
        message = {"from": __name__}

@app.route('/test')
def test_page():
    return render_template('templates/index.html')