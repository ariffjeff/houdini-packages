## Archived project
This project won't be maintained anymore since a comprehensive GUI Houdini package manager was made instead: https://github.com/ariffjeff/houdini-package-manager

# houdini-packages
An easy, generalized configuration setup for allowing Houdini to locate and use any plugins HDAs, plugins, and scripts using [packages](https://www.sidefx.com/docs/houdini/ref/plugins.html). This is most useful for those looking to switch from the legacy `houdini.env` method.

All of the provided `.json` package files (except `redshift.json`) are configured on the idea that all of your HDAs, plugins, and scripts are placed in a single custom directory in some  arbitrary location of your choice. This makes managing everything convenient.  

Each package file uses multiple arbitrary variables for ease of readability and editing.  

# Install HDAs, plugins, and scripts
For this configuration, any HDAs (aka "otls"), plugins, and scripts should be in the relevant folder inside your custom directory:
- `/otls`
- `/plugins`
- `/scripts`

For example:
- Dump any orphan HDAs you've downloaded or created yourself that you don't feel like organizing into `/otls`
- Plugin folders like Redshift, MOPS, or any others that come downloaded as an organized folder that already has an `/otls` folder inside it should go into `/plugins`
- Scripts like [`123.py`, `456.py`](https://www.sidefx.com/docs/houdini/hom/locations.html#startup), and others should be dumped in `/scripts`
- (`/otls` and `/scripts` are located with the [`_main.json`](#newer-packages-method) config) 

# Install config files
Both the legacy `houdini.env` and newer packages (`.json`) method are included.

If you choose to go with `houdini.env`, it will be found in: `C:\Users\USER\Documents\houdiniXX.X`

For package `.json` config files, they must be placed in the Houdini packages directory.

On Windows it would be: `C:\Users\USER\Documents\houdiniXX.X\packages`

# Legacy `houdini.env` method
If you go with the legacy `houdini.env` method, uncomment the lines you need, make the necessary path changes, and then delete `/packages`. You cannot have both methods at the same time or they will conflict with each other. Houdini will get confused :(

# Newer packages method
If you choose the newer packages method, and want to use the [provided .json files](/packages), go into each file and edit the paths to be relevant to your own system.

[`_main.json`](/packages/_main.json) is there to point directly to some folders where you may be storing any loose HDAs and scripts. `HOUDINI_OTLSCAN_PATH` and `HOUDINI_SCRIPT_PATH` in `_main.json` are what do this for you. Appropriately configure the custom variable `HOUDINI_DEV` for your system to get Houdini to successfully locate your HDAs and scripts.

## Automatic package creation
You can simply run [create_plugin_package.py](/create_plugin_package.py) by clicking on it. The script will automatically create the valid package json files for you in the appropriate directory for any plugins you want. This makes it so you don't need to go through manual package config creation.

## Manual package creation
Each time you download a new plugin:  
1. Dump the new plugin folder into `/plugins` in your custom directory   
2. Ensure the actual .hda files are in a subdirectory named `/otls` (e.g. `/plugins/my_plugin/otls/my_plugin.hda`)
3. Go into `/packages` (from this repository) and duplicate one of the .json files (or consider grabbing any `packages.json` file that might have come with the plugin)  
4. Rename it to the name of the new plugin (you can name it whatever you want, it doesn't really matter)  
5. Open the file and configure it by simply replacing all instances of the name of the original plugin with the exact name of the new plugin folder  
- For example, if you've duplicated `MOPS.json` and want to configure it for a new and amazing plugin of which the folder is named `fastCheeseGrater`, replace all of the four string instances of "`MOPS`" with `fastCheeseGrater`. That's it.   
- If the name of the new plugin folder has any periods (`.`) in it (i.e. contains a version number like `fastCheeseGrater_1.0.2`) then you will need to remove or replace them with something else like underscores since Houdini won't parse them correctly. (i.e. `fastCheeseGrater_1_0_2`). Don't forget to change the .json package files to reflect this change as well.  
6. Save the .json file  
7. Start up a new instance of Houdini and see if the plugin shows up and works  

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
