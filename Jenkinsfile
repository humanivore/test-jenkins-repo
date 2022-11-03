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
                def env = ['dev', 'stg', 'prd']
                env.each {
                    e ->
                        def env_config = readJSON file: "./data-${e}.json"
                        sh "python update_config.py -d ./source.json -o ./data-${e}.json"
                        sh "echo 'updated data-${e}.json'"
                }
            }
        }
    }
}
