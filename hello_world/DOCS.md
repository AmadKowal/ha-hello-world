# Hello world

## Install

1. On Home Assistant OS, open Settings > Apps > Install app.
2. Open the top-right menu and select Repositories.
3. Add `https://github.com/AmadKowal/ha-hello-world`.
4. Select Hello world, then Install. The Supervisor clones this repository and builds the image on the device.
5. Start the app and select Open Web UI. Turn on Show in sidebar to keep the page in the sidebar.

## What it does

On start, the log contains `Hello world!`. The page greets the signed-in user when Home Assistant sends a display name, and otherwise says hello to the world.

The page is only reachable through Home Assistant ingress. The server refuses every connection except the Supervisor at `172.30.32.2`.
