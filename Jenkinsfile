pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/renefgg/unir-cicd-actividad3.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'make build'
                sh 'exit 1'
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running Unit Tests...'
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/unit_result.*ml'
            }
        }

        stage('API Tests') {
            steps {
                echo 'Running API Tests...'
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/api_result.*ml'
            }
        }

    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo 'mail to: rene.garcia.garcia@gmail.com'
            echo "subject: Fallo en el job: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
            echo "body: El pipeline ha fallado. Revisa Jenkins: ${env.BUILD_URL}"
        }
    }
}
