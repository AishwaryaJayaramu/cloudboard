# cloudboard

## Notes

1. start sending data to the cloud only when the use has selected paste (otherwise you'd be sending data to the cloud all the time for no reason). Most copies are still going to be pasted locally.
2. Use https://github.com/mhammond/pywin32 for clipboard functionality on Windows. Use xclip or xsel on Linux and other X11 based Unix systems.
3. First build baseline working model with pyperclip.