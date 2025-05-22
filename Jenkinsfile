pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "group5/calligraphygenerator:latest"
        CONTAINER_NAME = "calligrapygenerator"
        EMAIL = "brithneykong1996@Hotmail.com"
    }

    options {
        timeout(time: 20, unit: 'MINUTES')
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling source code...'

            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python requirements...'

            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Launching Flask app in background...'
        
            }
        }

        stage('Test') {
            steps {
        	echo 'Running Selenium test in app container...'
        	
    	    }
	}


        stage('Build') {
            steps {
                echo 'Building Docker image...'
               
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Docker container...'
                
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
