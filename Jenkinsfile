def PROJECT_NAME = "UnityProjectBase"
def CUSTOM_WORKSPACE = "F:\\projects\\${PROJECT_NAME}"
def UNITY_VERSION = "6000.2.14f1"
def UNITY_INSTALLATION = "C:\\Program Files\\Unity\\Hub\\Editor\\${UNITY_VERSION}\\Editor"
def DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1445797075832013043/b8JLDoWq8EByEZUsauY-BRvJiUHl1KNbl35I_Od7pwBsSemOv1UdN5M6IW4lYXxA7aEY"

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
                discordSend(customAvatarUrl: "https://alt-battles.fandom.com/wiki/SCP-6488", customUsername: "SCP-6488", description: "", footer: "Jenkins", link: "http://servers.codrx.net:5000/repository/${env.PROJECT_NAME}/Windows_Builds/${env.DATE}/${env.ARTIFACT_NAME}", result: currentBuild.currentResult, title: "${env.ARTIFACT_NAME}", showChangeset: true, successful: currentBuild.resultIsBetterOrEqualTo('SUCCESS'), webhookURL: "${DISCORD_WEBHOOK}")
            }
        }
    }
}