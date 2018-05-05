pipeline {
  agent any
  stages {
    stage('') {
      steps {
        sh '''#!/bin/bash
cd /git
git pull rebase origin
sudo cp /git/* /var/www/html
sudo chwon -R apache:apache /vat/www/html/*
'''
      }
    }
  }
}
