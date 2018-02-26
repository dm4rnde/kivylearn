# kivylearn
Going through basic GUI concepts in kivy library. Concepts chosen randomly and presented in random order. 


### Purpose
Study and practice. Reuse.


### Specifics (environment):

- kivy 1.10.1.dev0 [python package]
- Python 3.6.2
- pygame (1.9.4.dev0) [python package]
- Cython (0.27.3) [python package]


### Setup (this is just a guide, your commands/versions might vary):

```
sudo pip3.6 install virtualenv
brew install pkg-config sdl sdl_image sdl_mixer sdl_ttf portmidi sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
brew install smpeg
cd /to/your/kivyproject/
virtualenv venv
git clone https://github.com/pygame/pygame ; cd pygame
../venv/bin/python3.6 setup.py build
#(don't mind the warnings)
../venv/bin/python3.6 setup.py install
cd .. ; rm -rf pygame
git clone https://github.com/kivy/kivy ; cd kivy
../venv/bin/pip3.6 install cython
../venv/bin/python3.6 setup.py install
cd .. ; rm -rf kivy
```
