from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from discerner import imagepredict
import time
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

import logging
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

KEYSPACE = "mykeyspace"

# For a given file, return whether it's an allowed type or not


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image01']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        image_path = os.path.join(
            app.root_path, app.config['UPLOAD_FOLDER'], filename)
        upload_file.save(image_path)
        # return imagepredict(image_path)+'. success\n'
        prediction = imagepredict(image_path)
        millis = int(round(time.time() * 1000))
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(millis/1000))
        if insert_into_table(image_path, prediction, timestamp):
            return 'insert (' + image_path + ', ' + prediction + ', ' + timestamp + ') into table success!\n'
        else:
            return 'failed!\n'
    else:
        return 'failed!\n'

def insert_into_table(img_name, prediction, timestamp):
    cluster=Cluster(contact_points=['my-csda'], port=9042)
    session=cluster.connect()
    try:
        log.info("setting keyspace...")
        session.set_keyspace(KEYSPACE)
        log.info("inserting info...")
        # command = "INSERT INTO mytable (mykey, col1, col2) VALUES ('" + img_name + "', '" + prediction + "', '" + timestamp + "');"
        command = "INSERT INTO mytable (mykey, col1, col2) VALUES ('{name}', '{prediction}', '{time}');".format(name = img_name, prediction = prediction, time = timestamp)
        session.execute(command)
        cluster.shutdown()
        return True
    except Exception as e:
        log.error("Unable to insert info")
        log.error(e)
        cluster.shutdown()
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0')