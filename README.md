# Bigdata
Project：Handwriting recognition based on the Mnist

Students： Xi Wang

Teacher： Fan Zhang

Time period： 12th July,2019-18th August,2019

1.Research background：
  (1).Mnist:The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.
 (2):Docker:In the Forrester New Wave ™: Enterprise Container Platform Software Suites, Q4 2018 report, Docker was cited as a leader in enterprise container platform category with Docker and our Docker Enterprise Container platform receiving a “differentiated” rating in eight criteria including runtime and orchestration, security, image management, user experience, vision and more.

2.Knowledge points：
(1).Flask：
1-using the “pip install flask”to install the flask
2-using the code paragraph like the “
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
return 'Hello, World!'  ”to create a flask program
3-using the code like the  “ Running on http://127.0.0.1:5000/”to run a flask.
4-Using the code like the “curl -F/--form <name>=@<filepath> <url>” to upload a file,the uploading file paragraph is like the “
from flask import Flask, request  
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image01']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        image_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename)
        upload_file.save(image_path)
        return imagepredict(image_path)+'. success\n'
    else:
        return 'failed!\n'   ”



(2)Cassandra:
1-It can be inferred from the website:
https://www.w3cschool.cn/cassandra/cassandra_data_model.html
(3)Docker:
2-Building a container:It can be referred from the website :
https://docs.docker.com/get-started/
3-Connecting containers:using the code like：
”docker run --link <container_name>:<alias> <img_name>”
(4)Mnist:
It can be referred from the website:
 https://blog.csdn.net/u011389706/article/details/81455750


3.Process：
Firstly,we need to use “pip install ***“  to download the package we need like the pillow,flask,tensorflow and cassandra-driver and so on.Then,we should try to run the mnist traing code to download the traing collection from the official website.As we have successfully run the program,we could try to build the Image of the Mnist and flask.After that,we need to pull a Cassandra Image and create a network.After that,try to build a Cassandra container and then use the connecting code to link the Cassandra container with the Mnist and flask container.As these have been down,we could try to upload a picture and then check the answer in the containers.


4.Problems and solutions：
1-Because my docker was installed under the virtualbox,so I was unable to use the flask with the url which the program showed like the “0.0.0.0:Port Number”.In that case,I have been in trouble for a long time.However,I found that I need to enter to set the virtualbox’s Port translation.The host IP could be set as the IP of the “VirtualBox Host-Only Network”,and the IP of the subnet should be set as the IP of the what is shown at the Docker program’s beginning line.And the host and the subnet Port should be set as the port which I exposed.After that,I successfully realized the website’s interaction with flask,while the url should be the “subnet IP:Port Number”.
2-As I built the container of the flask and mnist first,I could not realize the connection of it with the cassandra container.In order to solve this,I have to build the cassandra container first,and then use the code like the
“docker run -p <port>:<port> --network <network>--link <container_name>:<alias> <img_name>” to realize the connection and build the container of the flask and the mnist because they are under the same network now,which would allow their connection.
3-Because I am in China,so I need to use the VPN to download the package,which is so slow and not readily.Because of this,I changed the downloading source with the code “RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.tx”.And it became efficient soon.


5.My impressions：
3-From this project,I have just tried to contact with the Big data and the technique of Docker.I have felt the advantages of containers rather than the virtual system because I could start several containers at the same time,while the virtual system have much higher requirements of the CPU.I also started to learn to find my problems and find the solution on my own,by searching the Internet and do some bold attempts.
