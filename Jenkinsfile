pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-devops-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop flask-container || exit 0'
                bat 'docker rm flask-container || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name flask-container flask-devops-app'
            }
        }
    }
}