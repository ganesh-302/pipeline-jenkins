pipeline {
    agent any

    environment {
        IMAGE_NAME = "pipeline-app"
        CONTAINER_NAME = "pipeline-container"
        PORT = "7002"
    }

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p ${PORT}:${PORT} \
                    ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        success {
            echo "App deployed at http://localhost:${PORT}"
        }
        failure {
            echo "Pipeline failed. Check logs above."
        }
    }
}