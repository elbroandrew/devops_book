#! /usr/bin/python3
"""
a program that discovers and runs plugins.
"""

import fire, pkgutil, importlib

# pkgutil finds all modules in `sys.path`

def find_and_run_plugins(plugin_prefix):
    plugins = {}

    # Discover plugins and Load
    print(f"Discovering plugins with prefix: {plugin_prefix}")
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module

    for name, module in plugins.items():
        print(f"Running plugin {name}")
        module.run()

if __name__ == "__main__":
    fire.Fire()

"""
./plugins_for_cli_tools.py find_and_run_plugins foo_plugin
output:
Discovering plugins with prefix: foo_plugin
Running plugin foo_plugin_a
Run plugin A
"""