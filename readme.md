### Installation

1) Download the installation script
    ```shell
    wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/install.sh
    ```

2) Make the installation script executable
    ```shell
    sudo chmod +x ./install.sh
    ```
3) Run the script
    ```shell
    sudo ./install.sh
    ```
   
During the installation, you will be prompted to modify the `config.json` file.

At the top of the file, you can modify the color (hex code) that will be used for the **down** and **up**
status. You can also enable debugging, and change the interval of the check.

Debugging option in **config.json** values :

| Value | Function                                           |
|-------|----------------------------------------------------|
| 0     | **None** - Will not show any debugging information |
| 1     | **Info** - Will show minimum debugging information |
|       | **Verbose** - Will show all debugging information  |

In the config file, add the hosts you want to monitor, their name and the link that will be used in the website.

**After the installation is done, simply go to the IP address of the server.**