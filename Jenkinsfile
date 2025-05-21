pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/whatevershut/DevOps_Deployment.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t my-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run my-app npm test'  # Example test command
            }
        }
    }
}
