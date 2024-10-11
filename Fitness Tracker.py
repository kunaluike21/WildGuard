from flask import Flask, request, jsonify

app = Flask(__name__)

workouts = []

@app.route('/workouts', methods=['GET', 'POST'])
def manage_workouts():
    if request.method == 'POST':
        workout = request.json
        workouts.append(workout)
        return jsonify(workout), 201
    else:
        return jsonify(workouts)

if __name__ == '__main__':
    app.run(debug=True)
