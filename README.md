# PyPrompt

Making a terminal based in Python 3.10.1

<a href="https://replit.com/github/joalricha869/PyPrompt"><img src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/replit.svg" alt="Deploy On Replit"></a>
<a href="https://glitch.com/edit/#!/import/github/joalricha869/PyPrompt"><img src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/glitch.svg" alt="Deploy On Glitch"></a>
<a href="https://deploy.azure.com/?repository=https://github.com/joalricha869/PyPrompt"><img src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/azure.svg" alt="Deploy On Azure"></a>
<a href="https://deploy.cloud.run/?git_repo=https://github.com/joalricha869/PyPrompt"><img src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/googlecloud.svg" alt="Deploy On Google Cloud"></a>
<a href="https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/joalricha869/PyPrompt"><img src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/amplifyconsole.svg" alt="Deploy On Amplify Console"></a>
<a target="_blank" href="https://cloud.oracle.com/resourcemanager/stacks/create?zipUrl=https://github.com/joalricha869/PyPrompt/archive/refs/heads/main.zip"><img alt="Deploy to Oracle Cloud" src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/oraclecloud.svg"></a>
<a target="_blank" href="https://railway.app/new/template?template=https://github.com/joalricha869/PyPrompt"><img alt="Deploy on Railway" src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/railway.svg"></a>
<a target="_blank" href="https://cloud.ibm.com/devops/setup/deploy?repository=https://github.com/joalricha869/PyPrompt"><img alt="Deploy to IBM Cloud" src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/ibmcloud.svg"></a>
<a target="_blank" href="https://heroku.com/deploy/?template=https://github.com/joalricha869/PyPrompt"><img alt="Deploy to Heroku" src="https://raw.githubusercontent.com/BinBashBanana/deploy-buttons/master/buttons/remade/heroku.svg"></a>


### Engine based on Termithon by Dwij

Inspired by: [This repo!](https://github.com/IdkDwij/Termithon)


## Run this in your PC

First download python from [python.org](https://python.org). Once it's installed, Run the PyPrompt file from the 'Releases' tab. 

### TO RUN IN WINDOWS TERMINAL

Name the PyPrompt file to prompt.py and put it on the root of the C drive. In Windows Terminal, make a new profile, named PyPrompt. use the following command. ```python.exe C:\prompt.py``` or ```py C:\prompt.py``` Run that new profile. PyPrompt should work.

### Why isn't there an ```.exe``` version?

Using pyinstaller it gives me an error (_apparently about the main() function. idk why it happens_)

## What is this PyPrompt Development Kit?...

It's the necessary tools needed to compile PyPrompt to a ```.pyc``` format. (_You may need to re-compile for different computers. Else it won't work..._)

I will upload it soon. Check this document regularly... I might just put it HERE: Download [PyDevKit](https://drive.google.com/file/d/1TtT72DXU6JIxWEfVa3aCU3BXcDBVyjmb/view?usp=sharing)

You may need to delete the compiled version i pre made. It might not work. Run ```compilePrompt.py``` or whatever its called and it will compile the necessary files needed.


## Features:

Many...

```
'''
  _____       _                       _           _ 
 |_   _|     | |                     | |         | |
   | |  _ __ | |_ ___  __ _ _ __ __ _| |_ ___  __| |
   | | | '_ \| __/ _ \/ _` | '__/ _` | __/ _ \/ _` |
  _| |_| | | | ||  __/ (_| | | | (_| | ||  __/ (_| |
 |_____|_| |_|\__\___|\__, |_|  \__,_|\__\___|\__,_|
                       __/ |                        
                      |___/                         

1. ip (Gives you your IP)
2. hostname (Gives you your Computer's ID)
3. mac (Retrieves the Physical MAC Address of The Device)
4. ping (lets you ping a website UPDATE: NOW ADDED!) not
5. calc (A simple calculator)
6. passgen (A very efficient password generator)
7. sysinfo (Gets relevant system info)
8. test (Tests PyPrompt Sample Command)
9. mp3search (Searches your File System for mp3 files)
10. mp4search (Searches your File System for mp4 files)
11. pysearch (Searches your File System for py files)
12. docxsearch (Searches your File System for docx files)
13. mailgen (Generates dummy E-Mail Addresses)
14. ver (Reports PyPrompt Version)
15. clear (Clears screen)
16. loadbarTest (Tests the loadbar)
17. intro (Displays initial text)
18. sqrt (Enter a number and it will calculate the square root)
19. date (Displays date)
20. cd (Navigate through folders)
21. iplocation (Find the physical location of your IP address)
22. speedtest (Speedtest.net but built into PyPrompt!)
23. encryptdecrypt (Uses the RSA Algorithm to encrypt and decrypt a message!)
24. troubleshoot (Troubleshoots extra modules neccessary for PyPrompt to run)
25. ssh (An SSH Client made in Python) DO NOT USE THIS TOOL FOR ILLEGAL PURPOSES!
26. macosdownloader (A simple macOS downloader) no longer based on gibMacOS
27. filesearch (Searches files via their extension)
28. filedownloader (Download any file via their url)
29. locateme (Obtains info about your location) This can't work under restricted proxy (ex: school wifi)
30. unblockedgames (A collection of unblocked games and sites for school) something that no one asked for but happened anyway...
31. unhelp (i'm not sure what this is. it just exists.)
32. locator (Locate basically any location in the planet)

(There's an easter egg in form of a command! Try to find it!) hint: help but not help

The PyPrompt can be used as an alternative terminal shell. It can run every shell command from WIndows and UNIX

'''
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)


## Credits

Termithon Shell/Kernel: [idkDwij](https://github.com/idkDwij)    [Termithon](https://github.com/idkDwij/Termithon)

Calculator Fix: [BigBoyTaco](https://github.com/BigBoyTaco)      [BigBoyTaco Studios](https://github.com/BigBoyTacoStudios)

Majority of Commands (slightly modified to work in PyPrompt + Bug Fixes): [hastagAB/Awesome-Python-Scripts](https://github.com/hastagAB/Awesome-Python-Scripts)  (_this helped alot_)
