# houdini-packages
An easy, generalized configuration setup for allowing Houdini to locate and use any plugins HDAs, plugins, and scripts.

Most of the provided `.json` files are configured on the idea that all of your HDAs, plugins, and scripts are placed in a single custom directory in some  arbitrary location of your choice. This makes managing everything convenient.

# Install HDAs, plugins, and scripts
For this configuration, any HDAs (aka "otls"), plugins, and scripts should be in the relevant folder inside your custom directory:
- `/otls`
- `/plugins`
- `/scripts`

For example:
- Dump any orphan HDAs you've downloaded or created yourself that you don't feel like organizing into `/otls`
- Plugin folders like Redshift, MOPS, or any others that come downloaded as an organized folder that already has an `/otls` folder inside it should go into `/plugins`
- Scripts like [`123.py`, `456.py`](https://www.sidefx.com/docs/houdini/hom/locations.html#startup), and others should be dumped in `/scripts`

# Install config files
Both the legacy `houdini.env` and newer `/packages` (.json) method are included.

Depending on which method you decide to use, `houdini.env` or `/packages` should be placed in the Houdini install directory.  
On Windows it would be `C:\Users\USER\Documents\houdiniXX.X`

# Legacy `houdini.env` method
If you go with the legacy `houdini.env` method, uncomment the lines you need, make the necessary path changes, and then delete `/packages`. You cannot have both methods at the same time or they will conflict with each other. Houdini will get confused :(

# Newer packages method
If you choose the newer packages method, go into each .json file and edit the paths to be relevant to your own system.

Each time you download a new plugin:  
1. Dump the new plugin folder into `/plugins` in your custom directory   
2. Go into `/packages` (from this repository) and duplicate one of the .json files (or consider grabbing any `packages.json` file that might have come with the plugin)  
3. Rename it to the name of the new plugin (you can name it whatever you want, it doesn't really matter)  
4. Open the file and configure it by simply replacing all instances of the name of the original plugin with the exact name of the new plugin folder.  
- For example, if you've duplicated `MOPS.json` and want to configure it for a new and amazing plugin of which the folder is named `fastCheeseGrater`, replace all of the four string instances of "`MOPS`" with `fastCheeseGrater`. That's it.   
- If the new plugin folder has any periods (`.`) in the name (i.e. contains a version number like `fastCheeseGrater_1.0.2`) then you will need to remove or replace them with something else like underscores since Houdini won't parse them correctly. (i.e. `fastCheeseGrater_1_0_2`). Don't forget to change the .json package files to reflect this change as well.  
5. Save the .json file.  
6. Start up a new instance of Houdini and see if the plugin shows up and works.  

# Debugging Houdini not loading HDAs/plugins/scripts
1. Save any changes to your config files  
2. Open a new instance of Houdini  
3. Go to Windows > Shell  
4. Enter `hconfig`  
5. Slowly and carefully peruse through the environment variables to see if something doesn't look correct in order to make necessary config changes.  

# Extra documentation on packages
MOPS dev blog: https://www.toadstorm.com/blog/?p=722  
SideFX: https://www.sidefx.com/docs/houdini/ref/plugins.html

# Useful video tutorials on packages
1. https://www.youtube.com/watch?v=rEaYXiY_lVg
2. https://www.youtube.com/watch?v=6vPycs4HeZM
