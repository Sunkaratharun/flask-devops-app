pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\SWAPNA MANI\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\SWAPNA MANI\\AppData\\Local\\Programs\\Python\\Python314\\Scripts\\pytest.exe"'
            }
        }

    }
}
