# Curseforge Docker Server

This repository will set up a curseforge modded minecraft server utilizing the [itzg/minecraft-server
](https://hub.docker.com/r/itzg/minecraft-server) docker image

## Dependencies

1. [docker](https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe)
2. [python]() for running the backup and modswap scripts

## Running server

`docker-compose up`

## Shutting Down Server

`docker-compose down`

## Editing Modpack

1. Stop the server if running via `docker-compose down`
1. Download the desired modpack from [curseforge](https://www.curseforge.com/minecraft/modpacks)
2. Copy the downloaded server zip into the [modpacks](./modpacks) folder
3. Change the following line within the `docker-compose.yml`:
```
CF_SERVER_MOD: /modpacks/<mod_file_name>
```
4. Run the server with `docker-compose up`


## Backing Up Data / Modpacks

1. Run `./backup_server.py --backupfolder <folder_name_for_backup>`
   1. This will backup the data and modpacks by default.  Can ignore either by passing `--skipdata` or --`skipmods` respectively

## Documentation Links

1. [docker image documentation](https://github.com/itzg/docker-minecraft-server)