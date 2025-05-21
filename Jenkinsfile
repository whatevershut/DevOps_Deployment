pipeline {
    agent any
    tools {
        // if you're testing a Node app
        nodejs "NodeJS_16"
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/whatevershut/DevOps_Deployment.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building app..."'
                // run any build commands e.g. npm install
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test' // or `pytest`, `junit`, etc.
            }
        }
        stage('Docker Build & Deploy') {
            steps {
                sh 'docker build -t lyimage .'
                sh 'docker run -d -p 5000:5000 lyimage'
            }
        }
    }
}
