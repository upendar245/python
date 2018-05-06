pipeline {
  agent any
  stages {
    stage('') {
      steps {
        sh '''#!/bin/bash
cd /git
git pull rebase origin
sudo cp /git/* /var/www/html
sudo cd /var/www/html
sudo ls  > index.html
sudo chown -R apache:apache /var/www/html/*
'''
      }
    }
  }
}
