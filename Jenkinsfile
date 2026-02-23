pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "tharunsunkara"
        IMAGE_NAME = "tharunsunkara/flask-devops-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def versionTag = "${env.BUILD_NUMBER}"
                    
                    bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
                    bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', 
                usernameVariable: 'DOCKER_USER', 
                passwordVariable: 'DOCKER_PASS')]) {

                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                }
            }
        }

        stage('Push Image') {
            steps {
                bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
                bat "docker push %IMAGE_NAME%:latest"
            }
        }
    }
}
