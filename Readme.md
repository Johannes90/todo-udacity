# Udacity Flask Project

This project was created for the Full Stack Developer Nanodegree from Udacity. The goal of the project was to create a flask application that exposes json endpoints and views for 2 related models. I chose to create a todo application that maps projects and tasks together. The project utilizes the following technologies:
- Flask RESTful - for creating API endpoints and handling storage of data
- Vue.js - used as a single page application to display views
- Docker and Docker Compose - for creating a unified environment for the project

## Installation

### Prerequisites
- You need to have docker and docker-compose installed (docker-compose version > 2)
- You need to have the latest npm version installed

1. Clone the repo locally
2. Navigate to 'cd server'
3. Rename the config.example.py file to config.py and enter your credentials. For the app to function you only need to add a valid google client id.
4. Run 'docker-compose up' - this will donwload the postgres and python images and create the server environment. The first time this task may take several minutes, but launches fast the second time.
5. Your server should now be running and logging the debug messages from flask.
6. Navigate to the client directory 'cd ../client'
7. Rename the prod.env.example.js to prod.env.js and enter your Google Client ID.
7. Run 'npm install' to install all dependencies for the client
8. Run 'npm run dev' - this should open a new browser tab that navigates you to the home screen

## Usage

- Before you are able to create new projects or todos you will need to sign up on the homepage.
- After this you will be redirected to the Inbox view. Here you can create projects and tasks. You can also show views for specific projects or users. Create a project first, to add todos to it.
- Todos and projects can be viewed by anyone, but you can only edit and delete todos and projects that you created yourself

## JSON Endpoints
The json endpoints are protected by a JSON Web token. You first have to call /google-sign or /register to register a user with OAUTH Google or with a username and password. You then need to call /auth with a valid token for OAUTh or password for the user model to access resources. You will receive a JSON Web token in return that you can use to access all other endpoints.

* /register - POST
* /sign-in - POST
* /auth - POST
* /todos - POST and GET
* /todo/<int:id> - GET, DELETE and PUT
* /projects - POST and GET
* /project/<int:id> - GET, DELETE and PUT

See the relevant resources and app.py for which values to send to the endpoints.