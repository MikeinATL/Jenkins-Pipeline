pipeline {
    agent any

    stages {
        stage ('Create Some General output'){
            steps {
                echo pwd()
                sh '"'python -u test.py'

                // Make the output directory.
                sh '"'mkdir -p /Users/melissa/output'

                // Write an useful file, which is needed to be archived.
                writeFile file: '"'output/usefulfile.txt", text: "This file is useful, and we will need to archive it.''

                // Write a useless file, which is not needed to be archived.
                writeFile file: 'output/uselessfile.md", text: "This file is useless, no need to archive it.''
            }
        }
       
    }

}