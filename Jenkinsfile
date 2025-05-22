pipeline {
    agent any

    triggers {
        githubPush()
    }

    tools {
        ant 'Ant 1.10'  // Ensure this matches your Jenkins tool config
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/whatevershut/DevOps_Deployment.git'
            }
        }

        stage('Build with Ant') {
            steps {
                ant {
                    buildFile 'build.xml'
                    targets 'clean compile'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("lyimage:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo "Running Selenium tests..."
                // TODO: Replace below with actual test command when ready
                sh 'echo "Run your Selenium tests here, e.g. mvn test or ./run-selenium.sh"'
            }
        }
    }

    post {
        success {
            emailext to: 'whateverworld.shut@gmail.com',
                     subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     body: "Good news!\n\nBuild succeeded: ${env.BUILD_URL}"
        }
        failure {
            emailext to: 'whateverworld.shut@gmail.com',
                     subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     body: "Build failed.\n\nCheck console: ${env.BUILD_URL}"
        }
    }
}
