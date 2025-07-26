from flask import Flask, jsonify, request

app = Flask(__name__)
students = {}

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students/<roll_number>", methods=["GET"])
def get_student(roll_number):
    student = students.get(roll_number)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    roll = data.get("roll_number")
    if roll in students:
        return jsonify({"error": "Student already exists"}), 400
    students[roll] = {"name": data["name"], "cgpa": data["cgpa"]}
    return jsonify({"message": "Student added successfully"}), 201

@app.route("/students/<roll_number>", methods=["PUT"])
def update_student(roll_number):
    if roll_number not in students:
        return jsonify({"error": "Student not found"}), 404
    new_cgpa = request.json.get("cgpa")
    students[roll_number]["cgpa"] = new_cgpa
    return jsonify({"message": "CGPA updated successfully"})

@app.route("/students/<roll_number>", methods=["DELETE"])
def delete_student(roll_number):
    if roll_number in students:
        del students[roll_number]
        return jsonify({"message": "Student deleted successfully"})
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
