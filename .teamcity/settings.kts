import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildFeatures.dockerSupport
import jetbrains.buildServer.configs.kotlin.buildSteps.dockerCommand
import jetbrains.buildServer.configs.kotlin.projectFeatures.dockerRegistry
import jetbrains.buildServer.configs.kotlin.triggers.VcsTrigger
import jetbrains.buildServer.configs.kotlin.triggers.vcs

/*
The settings script is an entry point for defining a TeamCity
project hierarchy. The script should contain a single call to the
project() function with a Project instance or an init function as
an argument.

VcsRoots, BuildTypes, Templates, and subprojects can be
registered inside the project using the vcsRoot(), buildType(),
template(), and subProject() methods respectively.

To debug settings scripts in command-line, run the

    mvnDebug org.jetbrains.teamcity:teamcity-configs-maven-plugin:generate

command and attach your debugger to the port 8000.

To debug in IntelliJ Idea, open the 'Maven Projects' tool window (View
-> Tool Windows -> Maven Projects), find the generate task node
(Plugins -> teamcity-configs -> teamcity-configs:generate), the
'Debug' option is available in the context menu for the task.
*/

version = "2022.04"

project {

    buildType(BuildAndDeployToDockerHub)

    features {
        dockerRegistry {
            id = "PROJECT_EXT_3"
            name = "Docker Registry"
            url = "https://docker.io"
            userName = "danieljgallo"
            password = "credentialsJSON:72fb901f-036e-4db0-a53e-06e96528951e"
        }
    }
}

object BuildAndDeployToDockerHub : BuildType({
    name = "Build and Deploy to Docker Hub"

    vcs {
        root(DslContext.settingsRoot)
    }

    steps {
        dockerCommand {
            commandType = other {
                subCommand = "buildx"
                commandArgs = "build --push --platform linux/arm/v6,linux/arm/v7,linux/arm64,linux/amd64 --tag danieljgallo/givtcp:2.0.%build.number% --tag danieljgallo/givtcp:latest ."
            }
        }
    }

    triggers {
        vcs {
            enabled = false
            quietPeriodMode = VcsTrigger.QuietPeriodMode.USE_CUSTOM
            quietPeriod = 300
        }
    }

    features {
        dockerSupport {
            loginToRegistry = on {
                dockerRegistryId = "PROJECT_EXT_3"
            }
        }
    }
})
