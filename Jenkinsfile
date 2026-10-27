
pipeline {
    agent any

    stages {
        stage('Checkout from GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run HTML Form Tests') {
            steps {
                sh 'python3 -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }

        failure {
            echo 'FAILURE: Check the console output for errors.'
        }

        always {
            echo 'HTML form pipeline execution completed.'
        }
    }
}
