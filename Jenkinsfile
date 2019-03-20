pipeline {
  agent any
  stages {
    stage('Pull code from github') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        echo 'Building'
      }
    }
    stage('Unit tests') {
      post {
        always {
          junit(allowEmptyResults: true, testResults: 'test-reports/results.xml')

        }

      }
      steps {
        sh ''' source activate ${BUILD_TAG}
                        python -m pytest --verbose --junit-xml test-reports/results.xml
                    '''
      }
    }
    stage('Build package') {
      when {
        expression {
          currentBuild.result == null || currentBuild.result == 'SUCCESS'
        }

      }
      post {
        always {
          archiveArtifacts(allowEmptyArchive: true, artifacts: 'dist/*whl')

        }

      }
      steps {
        sh ''' source activate ${BUILD_TAG}
                        python setup.py bdist_wheel
                    '''
      }
    }
    stage('Deploy to TestPyPI') {
      steps {
        sh 'twine upload --repository-url https://test.pypi.org/legacy/ dist/*'
      }
    }
  }
  post {
    always {
      echo 'This will always run'

    }

    success {
      echo 'This will run only if successful'

    }

    failure {
      echo 'This will run only if failed'

    }

    unstable {
      echo 'This will run only if the run was marked as unstable'

    }

    changed {
      echo 'This will run only if the state of the Pipeline has changed'
      echo 'For example, if the Pipeline was previously failing but is now successful'

    }

  }
}