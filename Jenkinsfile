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
     stage('Selenium Test') {
    steps {
        sh 'docker run -d --name selenium -p 4444:4444 selenium/standalone-chrome'
        sh 'docker run --network host lyana385/my-app-test'  # Your test script
    }
}
        }
    }
}
