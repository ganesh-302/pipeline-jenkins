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
                sh '''
                    docker run --rm \
                    -v ${WORKSPACE}:/app \
                    -w /app \
                    python:3.11 \
                    bash -c "pip install -r requirements.txt && python -m unittest Test.py"
                '''
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
            echo " App deployed at http://localhost:${PORT}"
        }
        failure {
            echo " Pipeline failed. Check logs above."
        }
    }
}