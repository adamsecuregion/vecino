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
                sh 'python vecino_get_data/get_data.py'
            }
        }
    }
}
