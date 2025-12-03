def PROJECT_NAME = "UnityProjectBase"
def CUSTOM_WORKSPACE = "F:\\projects\\${PROJECT_NAME}"
def UNITY_VERSION = "6000.2.14f1"
def UNITY_INSTALLATION = "C:\\Program Files\\Unity\\Hub\\Editor\\${UNITY_VERSION}\\Editor"

pipeline{
    environment{
        PROJECT_PATH = "${CUSTOM_WORKSPACE}"
        NEXUS_PASSWORD = credentials("NEXUS_PASSWORD")
    }

    agent{
        label{
            label ""
            customWorkspace "${CUSTOM_WORKSPACE}"
        }
    }

    stages{
        stage('Build Windows'){
            when{expression {BUILD_WINDOWS == 'true'}}
            steps{
                script{
                    withEnv(["UNITY_PATH=${UNITY_INSTALLATION}"]){
                        bat ''' 
                        "%UNITY_PATH%/Unity.exe" -quit -batchmode -projectPath %PROJECT_PATH% -executeMethod Build.BuildWindows -logFile -
                        '''
                    }
                }
            }
        }

        stage('Deploy Windows'){
            when{expression {DEPLOY_WINDOWS == 'true'}}
            steps{
                script{
                    def buildDate = new Date().format("yyyy-MM-dd_HH-mm-ss")
                    def buildFolderDate = new Date().format("yyyy-MM-dd")
                    env.ARTIFACT_NAME = "${PROJECT_NAME}_${buildDate}.zip"
                    env.DATE = "${buildFolderDate}"
                    bat '''
                    curl -u nirbhaykwatra:%NEXUS_PASSWORD% --upload-file %PROJECT_PATH%\\Build\\Windows.zip http://192.168.1.245:8081/repository/UnityProjectBase/Windows_Builds/%DATE%/%ARTIFACT_NAME%
                    '''
                }
                script{
                    def nexusLink = 'http://servers.codrx.net:5000/repository/%PROJECT_NAME%/Windows_Builds/%DATE%/%ARTIFACT_NAME%'

                    def payload = """{"embeds":[{"title":"${env.ARTIFACT_NAME}","description":"Build Succeeded!","url":"${nexusLink}","color":3066993,"fields":[{"name":"Status","value":"✅ Success","inline":true}],"footer":{"text":"Jenkins CI/CD"},"timestamp":"${new Date().format("yyyy-MM-dd'T'HH:mm:ss'Z'", TimeZone.getTimeZone('UTC'))}"}]}"""

                    bat """
                    curl -H "Content-Type: application/json" -X POST -d '${payload.replaceAll("'", "'\\\\''")}' https://discord.com/api/webhooks/1445703148751814717/x1spLSEStlGUCLQYtmwwV0MbvmO-6SDfdtta8MLujE63iYf0zzrEr2cit62Wj4W6Ju8V
                    """
                }
            }
        }
    }
}