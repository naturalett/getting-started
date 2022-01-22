job('NodeJS Docker example') {
    scm {
        git('git://github.com/yanivomc/docker-cicd.git','master') {  node -> // is hudson.plugins.git.GitSCM
            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@devophift.work')
        }
    }
    triggers {
        scm('H/5 * * * *')
    }
   
    
    steps {
        dockerBuildAndPublish {
            repositoryName('naturalett/playground')
            tag('${GIT_REVISION,length=9}')
            registryCredentials('lidor-dockerhub')
            buildContext('./basics/')
            forcePull(false)
            forceTag(false)
            createFingerprints(false)
            skipDecorate()
        }
    }
    steps {
        buildDescription(description=$GIT_COMMIT)
    }
}

