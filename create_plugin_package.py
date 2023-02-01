# This script creates a Houdini package .json config file in the appropriate Houdini packages directory for the plugin of your choice.
# Place this script in the same directory that contains your custom folder of Houdini plugins. Then run this script whenever you want to create a new package config.

import json
import os
from pathlib import Path


def main():

  # determine where to create/find the json config containing paths that helps this script
  PATHS_CONFIG_NAME = os.path.basename(__file__).split('.')[0] + ".json"
  SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
  HELPER_CONFIG_FILEPATH = Path(SCRIPT_PATH, PATHS_CONFIG_NAME)
  if(not validate_path(HELPER_CONFIG_FILEPATH)):
    create_helper_config(HELPER_CONFIG_FILEPATH)
  
  # get helper config json data
  helper_config = read_json(HELPER_CONFIG_FILEPATH)

  # set custom plugin path in helper config
  if(not validate_path(helper_config["custom_plugin_path"])):
    helper_config['custom_plugin_path'] = str(input_validate_path("Enter the path to your custom folder that contains your Houdini plugins: "))
    write_json(HELPER_CONFIG_FILEPATH, helper_config)

  # set Windows Documents directory path (typically in Windows Documents directory) in helper config
  if(not validate_path(helper_config['windows_documents_path'])):
    helper_config['windows_documents_path'] = str(input_validate_path("Enter your Windows Documents path (this is for finding your Houdini package config location): "))
    write_json(HELPER_CONFIG_FILEPATH, helper_config)

  # set latest Houdini version in the format of the Houdini install config folder names in the Windows Documents directory
  hv_latest = latest_installed_houdini_version("C:/Program Files/Side Effects Software").split(".")
  hv_latest = "houdini" + hv_latest[0] + "." + hv_latest[1] # format to packages directory names
  hv_saved = helper_config['target_houdini_version']
  # can't just do simple check for valid package path of an already config-saved target version since it might be out of date if a newer version of houdini is installed
  if(hv_saved == "" or hv_latest != hv_saved): # ensure always using latest installed houdini packages directory
    helper_config['target_houdini_version'] = hv_latest
    write_json(HELPER_CONFIG_FILEPATH, helper_config)
  
  # get which plugin user wants to create Houdini package json config for
  message = "Enter the name of the folder of the Houdini plugin to create a json package config for: "
  target_plugin = input_validate_path(message, prefix=helper_config["custom_plugin_path"], no_cwd=True)

  # create new json package config from template
  target_package_filepath = os.path.join(helper_config['windows_documents_path'], helper_config['target_houdini_version'], "packages", target_plugin.name + ".json")
  package_json = create_houdini_package(helper_config["custom_plugin_path"], target_plugin.name)
  write_json(target_package_filepath, package_json)
  print("Created Houdini package config for: {} at {}".format(target_plugin.name, target_package_filepath))
  input("Press Enter to quit...")


def create_houdini_package(custom_plugins_path: str, plugin_name: str):
  '''
  Create a Houdini package json template that ensures that Houdini can read any given plugin.
  This template only works with the houdini-packages setup
  '''
  hou_package = {
    "env": [
      {"CUSTOM_PLUGIN_PATH": custom_plugins_path},
      {plugin_name: "$CUSTOM_PLUGIN_PATH/{}".format(plugin_name)},
      {"HOUDINI_PATH": "${};".format(plugin_name)},
      {"HOUDINI_TOOLBAR_PATH": "${}/toolbar;".format(plugin_name)},
    ]
  }
  return hou_package


def create_helper_config(path="."):
  '''
  Create the config template that supports this script.
  '''
  config = {
    "custom_plugin_path": "",
    "windows_documents_path": "",
    "target_houdini_version": ""
  }
  write_json(path, config)
  print("Created helper config: {}".format(path))


def read_json(filepath: str) -> json:
  '''
  Read all data from a json file.
  '''
  validate_path(filepath, do_exceptions=True)
  with open(filepath, 'r') as f:
    j = json.load(f)
  return j


def write_json(filepath: str, data) -> None:
  '''
  Write data to a json file.
  '''
  with open(filepath, 'w') as f:
    json.dump(data, f, indent=4)


def latest_installed_houdini_version(houdini_install_path: str) -> str:
  ''' Determine latest installed houdini version. '''
  houdini_dir = Path(houdini_install_path)

  if(not houdini_dir.exists):
      print("Houdini install directory not found at {}".format(houdini_dir))
      return

  ls = os.listdir(houdini_dir.__str__())
  houdini_versions = []
  for elem in ls:
      elem_split = elem.split()
      if(len(elem_split) == 2 and elem_split[0] == "Houdini"):
          contains_num = any(chr.isdigit() for chr in elem_split[1])
          if(contains_num):
            houdini_versions.append(elem_split[1])

  houdini_versions.sort(key = lambda x: [int(y) for y in x.split('.')]) # sort semantic versions
  return houdini_versions[-1]


def input_validate_path(message_and_user_input: str, prefix="", postfix="", no_cwd=False) -> Path:
  '''
  Take user input and validates if it's a valid path.
  prefix and postfix surround message_and_user_input. This is useful for modifying the user input on the fly.
  Keep asking for input if it's an invalid path.
  Return a Path object of a valid string.
  '''
  input_path = input(message_and_user_input)
  try:
      custom_plugin_path = Path(os.path.join(prefix, input_path, postfix))
  except:
      print("Invalid path!")
      return input_validate_path(message_and_user_input, prefix, postfix, no_cwd)

  if(no_cwd and (str(input_path) == '.' or str(input_path) == "")):
    print("Invalid relative path to current directory!")
    return input_validate_path(message_and_user_input, prefix, postfix, no_cwd)
  
  if(not custom_plugin_path.exists()):
    print("Invalid path: {}".format(custom_plugin_path))
    return input_validate_path(message_and_user_input, prefix, postfix, no_cwd)
  return custom_plugin_path


def validate_path(filepath: str, do_exceptions=False) -> bool:
  '''
  Validates a file path.
  Returns a boolean.
  Raises exception instead of a boolean if do_exceptions==True
  '''

  if(type(filepath) != Path):
    try:
      filepath = Path(filepath)
    except:
      if(do_exceptions):
        raise Exception("Can't convert to Path object: {}".format(filepath))
      print("Can't convert to Path object: {}".format(filepath))
      return False

  # don't validate relative paths of current dir
  if(str(filepath) == '.'): # Path filepath "" auto converts to "." on str()  
    if(do_exceptions):
      raise Exception("Cannot validate empty relative path: \".\"")
    return False
  
  if(not filepath.exists()):
    if(do_exceptions):
      raise Exception("Not found: {}".format(filepath))
    print("Not found: {}".format(filepath))
    return False
  
  return True


if(__name__ == "__main__"):
   main()
