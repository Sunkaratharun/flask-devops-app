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

<<<<<<< HEAD
        stage('Deploy') {
    steps {
        bat 'taskkill /F /IM python.exe || exit 0'
        bat 'python app.py'
=======
>>>>>>> 2bb15267d212cb22019600553c214a83b0387e73
    }
}

