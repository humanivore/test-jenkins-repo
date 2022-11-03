pipeline {
    agent any
    stages {
        stage('Checkout source') {
            steps {
                checkout scm
                echo "here"
            }
        }
        stage('Update configuration') {
            steps {
                sh "python update_config.py -d ./source.json -o ./data-dev.json"
                sh "echo 'updated data-dev.json'"
            }
        }
    }
}
