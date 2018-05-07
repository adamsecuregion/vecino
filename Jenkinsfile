pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'building...'
                checkout scm
            }
        }
    stage('run'){
            steps {
                sh 'python --version'
                sh 'python python_test.py'
            }
        }
    }
}
