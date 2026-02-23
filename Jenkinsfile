pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "tharunsunkara/flask-devops-app"
        BUILD_TAG = "${env.BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE%:%BUILD_TAG% ."
                bat "docker tag %DOCKER_IMAGE%:%BUILD_TAG% %DOCKER_IMAGE%:latest"
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                }
            }
        }

        stage('Push Image') {
            steps {
                bat "docker push %DOCKER_IMAGE%:%BUILD_TAG%"
                bat "docker push %DOCKER_IMAGE%:latest"
            }
        }

        stage('Deploy Container') {
            steps {
                bat "docker stop flask-container || echo No container"
                bat "docker rm flask-container || echo No container"
                bat "docker run -d -p 5000:5000 --name flask-container %DOCKER_IMAGE%:%BUILD_TAG%"
            }
        }
    }
}
