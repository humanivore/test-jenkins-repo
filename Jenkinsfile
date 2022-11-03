/* groovylint-disable DuplicateStringLiteral, NestedBlockDepth, NoDef */
/* groovylint-disable UnusedVariable, VariableName, VariableTypeRequired */
// Groovy Style Guide: http://groovy-lang.org/style-guide.html

/* groovylint-disable-next-line CompileStatic */
@Library ('PSL@LKG') _

node('aws-centos') {
    timestamps {
        wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm']) {
            def commonSCM = new ors.utils.common_scm(steps, env)
            

            stage('Checkout source') {
                sh 'printenv'
                checkout scm
                commonSCM.clean_workspace()
            }

            stage('Update configuration') {
                def env = ['dev', 'stg', 'prd']
                env.each {
                    e ->
                        def env_config = readJSON file: "./data-${e}.json"

                        sh """
                            python update_config.py -d ./source.json -o ./data-${e}.json
                        """
                }
            }
        }
    }
}