## Installation

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
   
## config.json Information

**During the installation, you will be prompted to modify the `config.json` file.**

At the top of the file, you can modify the color (hex code) that will be used for the **down** and **up**
status. You can also enable debugging, and change the interval of the check.

```json
"interval" : "100",
"debug" : "2",
"colors" : {
"up": "#60bb50",
"down": "#ff2121"
}
```

| Key      | Function                                                                                                                |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| interval | **Check interval** : How often the monitors are checked                                                                 |
| debug    | **Debug output level** : Output level in the console.<br/>Check the table below for more details.                       |
| colors   | **Uptime Colors displayed in the website** : Sets the color<br/>that is used in the website for the Down and Up status. |


Debugging option in **config.json** values :

| Key | Function                                           |
|-----|----------------------------------------------------|
| 0   | **None** - Will not show any debugging information |
| 1   | **Info** - Will show minimum debugging information |
|     | **Verbose** - Will show all debugging information  |

In the config file, add the hosts you want to monitor, their name and the link that will be used in the website.

## config.json Examples

### ICMP Ping monitor

```json
 "1" : {
   "address" : "google.com",
   "webpage_link" : "https://google.com",
   "webpage_name" : "Google",
   "monitor_type" : "icmp",
   "HERC" : [""]}
```

| Key          | Function                                                                         |
|--------------|----------------------------------------------------------------------------------|
| address      | **The hostname or address** that will be pinged                                      |
| webpage_link | **A link for the website**. Can be blank.                                            |
| webpage_name | **The name of the monitor** for the website.                                         |
| monitor_type | **The type of the monitor**. In this case, **ICMP**.<br/>**This is case sensitive.** |
| ~~HERC~~         | (Expected response code)   **Not used for ICMP monitors.**                       |

### HTTP monitor :
```json
 "1" : {
   "address" : "https://google.com",
   "webpage_link" : "https://google.com",
   "webpage_name" : "Google",
   "monitor_type" : "http",
   "HERC" : ["200","301"]}
```

| Key     | Function                                                                                                                                                               |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| address | **The website that will be checked**. **Must have** protocol in front.                                                                                                     |
| webpage_link | **A link for the website**. Can be blank.                                                                                                                                  |
| webpage_name | **The name of the monitor** for the website.                                                                                                                               |
| monitor_type | **The type of the monitor**. In this case, **HTTP**.<br/>**This is case sensitive.**                                                                                       |
| HERC    | **Expected response code**. In this case, 200 and 301.<br/>Learn more about HTTP response codes : [Mdn Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) |



**After the installation is done, simply go to the IP address of the server.**