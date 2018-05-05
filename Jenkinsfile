pipeline {
  agent any
  stages {
    stage('') {
      steps {
        sh '''#!/bin/bash
cd /git
git pull rebase origin
cp /git/* /var/www/html
'''
      }
    }
  }
}