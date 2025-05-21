pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "group5/calligraphygenerator:latest"
        CONTAINER_NAME = "calligrapygenerator"
        EMAIL = "britneyyj923@gmail.com"
    }

    options {
        timeout(time: 20, unit: 'MINUTES')
        timestamps()
    }
    
    stages {
	
	stage('Checkout') {
            steps {
                echo 'Pulling...'
                checkout scm
            }
        }

	stage('Install Dependencies') {
            steps {
                echo 'Installing requirements...'
                sh 'pip install -r requirements.txt'
            }
        }

	stage('Test') {
            steps {
                sh 'echo "Testing..."'
                sh 'pytest test/test.py'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building..."'
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying with Docker..."'
                sh """
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p 80:5000 $DOCKER_IMAGE
                """
            }
        }
    }
    
    post {
        always {
            emailext (
                subject: "Jenkins Build ${currentBuild.currentResult}: ${env.JOB_NAME}",
                body: """Check console output at ${env.BUILD_URL}""",
                to: "britneyyj923@gmail.com"
            )
        }
    }
}
