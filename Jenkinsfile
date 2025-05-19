pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                // Add your build commands here
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."'
                // Add your test commands here
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying with Docker..."'
                // Add your Docker commands here
            }
        }
    }
    
    post {
        always {
            emailext (
                subject: "Jenkins Build ${currentBuild.currentResult}: ${env.JOB_NAME}",
                body: """Check console output at ${env.BUILD_URL}""",
                to: "your-email@example.com"
            )
        }
    }
}
