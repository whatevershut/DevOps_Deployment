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
                echo 'Pulling source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python requirements...'
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Launching Flask app in background...'
                sh 'nohup python3 app.py > flask.log 2>&1 & sleep 5'
            }
        }

        stage('Test with Docker Selenium') {
            steps {
                echo 'Running Selenium test inside Docker...'
                sh '''
                    docker run --rm \
                        --network host \
                        -v $PWD:/app \
                        -w /app \
                        selenium/standalone-chrome:latest \
                        python3 test/test.py
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Docker container...'
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p 80:5000 $DOCKER_IMAGE
                '''
            }
        }
    }

    post {
        always {
            emailext (
                subject: "Jenkins Build ${currentBuild.currentResult}: ${env.JOB_NAME}",
                body: "Check console output at: ${env.BUILD_URL}",
                to: "${env.EMAIL}"
            )
        }
    }
}
