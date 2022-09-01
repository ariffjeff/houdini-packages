# houdini-packages
A generalized configuration setup for allowing Houdini to locate and use any plugins HDAs, plugins, and scripts.

The provided files are configured on the idea that most, if not all, of your HDAs, plugins, and scripts are placed in a single custom directory. This makes managing everything convenient.

# Install HDAs, plugins, and scripts
For this configuration, any HDAs (aka "otls"), plugins, and scripts would be in the relevant folder inside your custom directory:
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

Each time you dump a new plugin into the `/plugins` folder in your custom directory, duplicate one of the .json files, rename it and reconfigure it accordingly.

# Extra documentation on packages
MOPS dev blog: https://www.toadstorm.com/blog/?p=722  
SideFX: https://www.sidefx.com/docs/houdini/ref/plugins.html

# Useful video tutorials on packages
1. https://www.youtube.com/watch?v=rEaYXiY_lVg
2. https://www.youtube.com/watch?v=6vPycs4HeZM
