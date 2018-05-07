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
                sh 'python get_data.py'
            }
        }
    }
}
