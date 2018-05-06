pipeline {
  agent any
  stages {
    stage('') {
      steps {
        sh '''#!/bin/bash
cd /git
git pull  
sudo cp /git/* /var/www/html
sudo cd /var/www/html
sudo ls  > index.html
sudo chown -R apache:apache /var/www/html/*
'''
      }
    }
  }
}
