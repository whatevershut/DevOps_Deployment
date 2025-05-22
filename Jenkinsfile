pipeline {
    agent any

    triggers {
        githubPush()
    }

    tools {
        ant 'Ant 1.10'  // Make sure this matches your Ant tool in Jenkins > Global Tool Config
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
    }
}
