pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-pipeline-app"
        CONTAINER_NAME = "my-app"
        PORT = "7002"
    }

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'sudo docker build --target test -t ${IMAGE_NAME}:test .'
            }
        }

        stage('Build Image') {
            steps {
                sh 'sudo docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh '''
                    sudo docker stop ${CONTAINER_NAME} || true
                    sudo docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    sudo docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p ${PORT}:${PORT} \
                    ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        success {
            echo " App deployed at http://localhost:${PORT}"
        }
        failure {
            echo " Pipeline failed. Check logs above."
        }
    }
}