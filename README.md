# basicRAT

# Para hacer

## Funcionalidades
- [ ] keylogger
- [ ] webcam
- [ ] minar
- [ ] broadcaster de funcionalidades

- [ ] Pasar a exe
- [ ] Ocultarlo
- [ ] Escanear puertos
- [ ] Replicación

## More Todo
* Interactive shell
* Client binary generation tool (cross-platform)
  * Pyinstaller
  * Switch options for remote IP, port, etc
* Persistence (cross-platform)
  * Windows: Registry keys, WMIC, Startup Dir
  * Linux: cron jobs, services, modprobe
  * macOS: LaunchAgent, LaunchDaemons
* Privilege Escalation (getsystem-esque, dirty cow)
* Common C2 Protocols (HTTP, DNS)
* Clean log files
    * Linux: bash history, var logs, audit logs, etc
    * Windows: Event logs, prefetch, etc
* Screenshot
* Keylogger
* Expand toolkit (unrar, sysinfo)
* Scanning utilities (probe scan / ping sweep, scanning subnet)
* Password dumping (mimikatz / gsecdump)
* Tunneling / Pivoting (ssh)
* Anti-virus detection and evasion
* VM and Sandbox detection
* Exfil browser history
* Search file system for sensitive information using regex
    * addresses, credit cards numbers, socials, PII, etc
* Detect web cameras and take snapshots
* Steal wifi passwords

## Features
* Cross-platform (Windows, Linux, and macOS)
* AES-256 encrypted C2 with D-H exchange
* Accepts connection from multiple clients
* Command execution
* Standard utilities (cat, ls, pwd, unzip, wget)
* System survey
* Self-destruct
* Primitive port scanning
* Client reconnect

## Build a stand-alone executable
Keep in mind that before building you will likely want to modify both the `HOST` and `PORT` variables located at the top of `basicRAT_client.py` to fit your needs.

On Linux you will need Python 2.x, [PyInstaller](http://www.pyinstaller.org/), and pycrypto. Then run something like `pyinstaller2 --onefile basicRAT_client.py` and it should generate a `dist/` folder that contains a stand-alone ELF executable.

On Windows you will need Python 2.x, PyInstaller, pycrypto, pywin32, and pefile. Then run something like `C:\path\to\PyInstaller-3.2\PyInstaller-3.2\pyinstaller.py --onefile basicRAT_client.py` and it should generate a `dist/` folder that contains a stand-alone PE (portable executable).

## Authors
* Austin Jackson [@vesche](https://github.com/vesche)
* Skyler Curtis [@deadPix3l](https://github.com/deadPix3l)

## Thanks
* [@bozhu](https://github.com/bozhu), AES-GCM Python implementation.
* [@reznok](https://github.com/reznok), multiple client connection prototype.

## Other open-source Python RATs for Reference
* [nathanlopez/Stitch](https://github.com/nathanlopez/Stitch)
* [n1nj4sec/pupy](https://github.com/n1nj4sec/pupy)
* [sweetsoftware/Ares](https://github.com/sweetsoftware/Ares)
* [ahhh/Reverse_DNS_Shell](https://github.com/ahhh/Reverse_DNS_Shell)
