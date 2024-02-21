from fastapi import FastAPI


app = FastAPI()


## Creating student details
students = {}

student_data = {
    'id': 0,
    'name': '',
    'age': 0,
    'sex': '',
    'height': 0.00,
}

## Home root for our fastapi
@app.get('/')
def home():
    return {'Message': 'WELCOME TO LANDONATION TECHIE'}

## Creating getting student data in bulks
@app.get('/students')
def get_student():
    return {'Message': 'Successfully', 'data': 'Student'}

## Create a student resouce <======> New student
@app.post('/students')
def add_student(
    name: str, age: int, sex: str, height: float
):
    new_student = student_data.copy()
    new_student['id'] = str(UUID(int=len(students) + 1))
    new_student['name'] = name
    new_student['age'] = age
    new_student['sex'] = sex
    new_student['height'] = height

    students[new_student['id']] = new_student
    return {'Message': 'Student successfully create', 'data': new_student}

## Get a student date (one student)
@app.get('/students/{uuid}')
def get_one_student(uuid):
    student = students[uuid]
    return {'Message': 'successfull', 'data': student}


## Delete metthod to delete resource
@app.delete('/students/{id}')
def delete_student(id: str):
    student = students.get(id)
    if not student:
        return {'error': 'no student found'}

    del students[id]
    return {'Message': 'student successful deleted'}