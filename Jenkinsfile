pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'cd /Users/melissa/GitHub/automation'
                sh 'python test.py'
            }
        }
    }
}