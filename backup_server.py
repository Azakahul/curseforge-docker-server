from distutils.dir_util import copy_tree
import os
import click
import pathlib

@click.command()
@click.option('--backupfolder', prompt='backup folder name', help='backup folder name')
@click.option('--skipdata', is_flag=True)
@click.option('--skipmods', is_flag=True)

def backupactiveserver(backupfolder, skipdata, skipmods):
    if not skipdata:
        backup(backupfolder, "data")
    
    if not skipmods:
        backup(backupfolder, "modpacks")

    print("backup complete!")

def backup(backupFolder, activeDirectory):
    currentDirectory = os.getcwd()
    backupPath = os.path.join(currentDirectory, backupFolder, activeDirectory) 
    pathlib.Path(backupPath).mkdir(parents=True, exist_ok=True)

    activePath = os.path.join(currentDirectory, activeDirectory)

    copy_tree(activePath, backupPath)
    print("Active {0} copied to: {1}".format(activeDirectory, backupPath))

if __name__ == '__main__':
    backupactiveserver()