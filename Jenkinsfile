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

<<<<<<< HEAD
        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name flask-container flask-devops-app'
            }
        }
    }
}
=======
       stage('Deploy') {
    steps {
        bat 'taskkill /F /IM python.exe || exit 0'
        bat 'start "" "C:\\Users\\SWAPNA MANI\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" app.py'
    }
}


    }
}


>>>>>>> 8332bc94accd1c6dbc384131a63f647b9c8ec42f
