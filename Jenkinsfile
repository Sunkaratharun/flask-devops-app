pipeline {
    agent any

    stages {

        stage('Pull Code') {
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

        stage('Deploy') {
    steps {
        bat 'taskkill /F /IM python.exe || exit 0'
        bat 'python app.py'
    }
}

