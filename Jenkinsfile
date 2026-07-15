pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                // Replace with your GitHub repo URL
                git branch: 'main', url: 'https://github.com/parshapalliglory-0345/two-tier-flask-app'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }
        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
    }
}