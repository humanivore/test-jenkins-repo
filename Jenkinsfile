pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('Checkout source') {
            steps {
                checkout scm
                echo "here"
            }
        }
        stage('Update configuration') {
            steps {
                git checkout master
                sh "python update_config.py -d ./source.json -o ./data-dev.json"
                echo 'updated data-dev.json'
                git add ./data-dev.json
                git commit -m "Updated config"
                git push
            }
        }
    }
}