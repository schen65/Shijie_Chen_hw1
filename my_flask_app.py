from flask import Flask

app = Flask('project_folder_1')

data = {'a':[1,2,3],'b':[1,2,3]}



@app.route('/')
def serve_data():
    return data