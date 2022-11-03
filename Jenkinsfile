pipeline {
    { docker { image 'python:3.10.7-alpine' } }
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
                echo 'updated data-dev.json'
            }
        }
    }
}
