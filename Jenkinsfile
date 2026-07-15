pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Starting Docker build..."
                    docker build -t flask-app:latest .
                '''
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh '''
                    echo "Starting Docker Compose deployment..."
                    docker compose down || true
                    docker compose up -d --build
                '''
            }
        }
    }
}
