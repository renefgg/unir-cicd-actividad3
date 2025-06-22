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
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running Unit Tests...'
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/unit_result.xml'
            }
        }

        stage('API Tests') {
            steps {
                echo 'Running API Tests...'
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/api_result.xml'
            }
        }

    }

    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }

        failure {
            mail to: 'rene.garcia.garcia@gmail.com',
                 subject: "Fallo en el pipeline: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "El trabajo '${env.JOB_NAME}' falló en la ejecución #${env.BUILD_NUMBER}. Revisa Jenkins para más detalles."
        }
    }
}
