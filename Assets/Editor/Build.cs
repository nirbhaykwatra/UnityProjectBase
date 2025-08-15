using UnityEditor;

public class Build
{
    static void BuildWindows()
    {
        string[] scenes = {"Assets/Demo/Scenes/Menu.unity"};
        
        BuildPipeline.BuildPlayer(scenes, "Build/UnityProjectBase.exe", BuildTarget.StandaloneWindows64, BuildOptions.None);
    }
}
