# ableton-custom-midi-remote-control

This repo is based on [Generic-Python-Remote-Script](https://github.com/luisangelsm/Generic-Python-Remote-Script)

Install it by copying all the python files in a folder called MocoLUFA and then place the folder in `\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\` or `/Contents/App-Resources/MIDI Remote Scripts/` depending if you are in Windows or mac.

It supports Ableton Live 11 and can toggle the session record button. Edit `MIDI_Map.py` to customize it.

I use it to control Ableton from a pedal board I built using arduino.

## Debug tips

Since this kind of scripts aren't really supported by Ableton modifying them is always kind of tricky and it requires some trial and error. If for some reasong the script isn't working, check Ableton's Log.txt file:

    Windows - \Users\[username]\AppData\Roaming\Ableton\Live x.x.x\Preferences\Log.txt
    Mac - /Users/[username]/Library/Preferences/Ableton/Live x.x.x/Log.txt
    
I usualy run `tail` to constantly seeing what is going on `tail -f Log.txt`.

## TODO

- Add mappings to control the current track (volume, arm, etc)
