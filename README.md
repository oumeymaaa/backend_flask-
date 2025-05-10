# Drivo+
<p>
Drivo+ is an open-source app built to keep your car in top shape by monitoring its health and diagnosing potential issues. At its core, the backend powers everything—collecting, processing, and analyzing data from your car’s On-Board Diagnostics (OBD) system. It goes beyond just reading error codes by using machine learning to assess performance, catch problems early, and even predict failures before they happen.
With real-time data streaming from IoT-enabled sensors, Drivo+ keeps an eye on key aspects like engine performance, fuel efficiency, battery health, and system errors. The backend crunches this data using AI-driven analytics, offering clear, actionable insights that help you maintain your vehicle and drive more safely.

Drivo+ also builds a history of your car’s data, provides personalized recommendations, and alerts you about potential maintenance needs—so you’re always one step ahead. Designed to be scalable and secure, the backend seamlessly integrates with the cloud and APIs, making it easy to connect with different automotive systems. Whether you're a car enthusiast or just want peace of mind on the road, Drivo+ helps you take better care of your vehicle.
</p>

## Setup (Docker)
+ [Docker Engine](https://docs.docker.com/get-started/get-docker/) latest version
### Note
This system depends on another microservice that provides the drowsiness detection functionality. The service will be downloaded from the Docker registry and started automatically.

### Install Steps
#### Step 1: Clone the Repository
```bash
git clone https://github.com/mohamed52665838/drivoplus_backend.git
cd drivoplus_backend
```
#### Step 2: Create .env file
<p>
    Create the .env file at the root of the project to ensure proper system setup. <br>
    <b>Note:</b> The .env file contains sensitive project secrets and should only be shared with team members.
</p>

* Example
```bash
DATABASE_URL=CLUSTER_URI
DrivoPlus?retryWrites=true|false&w=x&appName=APP_NAME'
DATABASE_NAME='DRIVO+'
HOST_NAME=HOSTNAME|IP
PORT_NUMBER=SYSTEM_PORT_NUMBER
JWT_SECRET_KEY=JWT_SECRET_KEY
MAILER_SERVER=SMTP_SERVER
MAILER_PORT=PORT_SMTP
MAILER_USE_TLS=1
MAILER_USERNAME=MAILER_USERNAME
MAILER_PASSWORD=MAILER_PASSWORD
DROWSINESS_SERVICE_PORT=DROWSINESS_SERVICE_PORT [5643]

```


#### Step 3: Start the System
```bash
docker compose up
```
#### Step 4: That’s It
Everything is now up and running.




## Setup (Development)

### Note
This system depends on another microservice that provides the drowsiness detection functionality, so you need to start the [AI (Drowsiness Detection Service)](https://github.com/mohamed52665838/socket-drivo_plus) first.

### System Requirements
+ [Python](https://www.python.org/downloads/) version => 3.11

### Install Steps
#### Step 1: Clone the Repository
```bash
git clone https://github.com/mohamed52665838/drivoplus_backend.git
cd drivoplus_backend
```
#### Step 2: Create Virtual Environment
- Linux / Mac OS
```bash
  python -m venv .venv
  source ./.venv/bin/activate
```
- Windows

```powershell
  python -m venv .venv
  ./.venv/Scripts/activate
```

#### Step 3: Install Requirements
* flasgger==0.9.7.1
* flask==3.1.0
* python-dotenv==1.0.1
* pymongo==4.11.1
* Werkzeug~=3.1.3
* Flask-JWT-Extended~=4.7.1
* Flask-Bcrypt==1.0.1
* Flask-APScheduler==1.13.1
* Flask-Mail==0.10.0
* Flask-Pydantic==0.12.0
* Flask-PyMongo==3.0.1
* stripe==11.5.0

```bash
pip install -r requirmenets.txt
```
#### Step 4: Create .env file
<p>
    Create the .env file at the root of the project to ensure proper system setup. <br>
    <b>Note:</b> The .env file contains sensitive project secrets and should only be shared with team members.
</p>

* Example
```bash
DATABASE_URL=CLUSTER_URI
DrivoPlus?retryWrites=true|false&w=x&appName=APP_NAME'
DATABASE_NAME='DRIVO+'
HOST_NAME=HOSTNAME|IP
PORT_NUMBER=SYSTEM_PORT_NUMBER
JWT_SECRET_KEY=JWT_SECRET_KEY
MAILER_SERVER=SMTP_SERVER
MAILER_PORT=PORT_SMTP
MAILER_USE_TLS=1
MAILER_USERNAME=MAILER_USERNAME
MAILER_PASSWORD=MAILER_PASSWORD
DROWSINESS_SERVICE_PORT=DROWSINESS_SERVICE_PORT [5643]

```

#### Step 5: Start the System
```bash
python -m flask --app main run [--debug] [--port port_number] [--host ip | hostname]
```
#### Step 6: That’s It
Everything is now up and running.

## Note
To start the system for development, you need to manually configure port bindings:
* Start the drowsiness detection service on a specific port (e.g., 5643)
* Configure the main system to communicate with the service on that port

However, when using Docker, everything is assembled automatically, so this manual setup is not required.
