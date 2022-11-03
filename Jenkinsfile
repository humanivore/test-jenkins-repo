/* groovylint-disable DuplicateStringLiteral, NestedBlockDepth, NoDef */
/* groovylint-disable UnusedVariable, VariableName, VariableTypeRequired */
// Groovy Style Guide: http://groovy-lang.org/style-guide.html

/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent any
    stages {
        stage('Checkout source') {
            checkout scm
            echo "here"
        }
        stage('Update configuration') {
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
