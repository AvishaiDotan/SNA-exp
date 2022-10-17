#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 14, 2022, at 09:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

cardWidthMM = 85.6
cardAspectRatio = 817 / 1284
cardWidthPXMax = 900

def split(word):
    return list(word)
    


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'SNA'  # from the Builder filename that created this script
expInfo = {'Group': '', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Exp_Folder\\SNA numbers and Arrows\\SNA.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Init"
InitClock = core.Clock()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
inst_ImageCount = 1
inst_Image = visual.ImageStim(
    win=win,
    name='inst_Image', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key = keyboard.Keyboard()

# Initialize components for Routine "Animation01"
Animation01Clock = core.Clock()
Animation01_Video = visual.MovieStim3(
    win=win, name='Animation01_Video',units='height', 
    noAudio = False,
    filename='EXP_DATA/Instructions/Credit_Animation.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=True,
    size=(0.9, 0.5),
    depth=0.0,
    )
Animation01_Key = keyboard.Keyboard()
Animation01_text = visual.TextStim(win=win, name='Animation01_text',
    text='לחץ על כל מקש להמשך',
    font='Open Sans',
    units='height', pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
inst_ImageCount = 1
inst_Image = visual.ImageStim(
    win=win,
    name='inst_Image', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key = keyboard.Keyboard()

# Initialize components for Routine "estimate_screen_size"
estimate_screen_sizeClock = core.Clock()
card = visual.ImageStim(
    win=win,
    name='card', units='pix', 
    image='EXP_DATA/Card/card.png', mask=None,
    ori=0.0, pos=(0, 0), size=(450, (450 * (817 / 1284))),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(0, 1), granularity=(0.001),
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='yellow', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Results"
ResultsClock = core.Clock()
import math
Res_text = visual.TextStim(win=win, name='Res_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()
Results_Text_Cont = visual.TextStim(win=win, name='Results_Text_Cont',
    text='לחץ על כל מקש להמשך',
    font='Open Sans',
    units='height', pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Hcm = 0

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
inst_ImageCount = 1
inst_Image = visual.ImageStim(
    win=win,
    name='inst_Image', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key = keyboard.Keyboard()

# Initialize components for Routine "Init_Counter"
Init_CounterClock = core.Clock()

# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Blank_3"
Blank_3Clock = core.Clock()
Blank_ = visual.TextStim(win=win, name='Blank_',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Blank_3"
Blank_3Clock = core.Clock()
Blank_ = visual.TextStim(win=win, name='Blank_',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Blank_3"
Blank_3Clock = core.Clock()
Blank_ = visual.TextStim(win=win, name='Blank_',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Blank_3"
Blank_3Clock = core.Clock()
Blank_ = visual.TextStim(win=win, name='Blank_',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Condition"
ConditionClock = core.Clock()
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
C_Response = keyboard.Keyboard()
Arrow_Image = "EXP_DATA\Arrows\Cutout.png"


# Initialize components for Routine "Block_iNTS"
Block_iNTSClock = core.Clock()
Block_n = 1
Inst_n = 1
inst_Image_2 = visual.ImageStim(
    win=win,
    name='inst_Image_2', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
inst_ImageCount = 1
inst_Image = visual.ImageStim(
    win=win,
    name='inst_Image', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key = keyboard.Keyboard()

# Initialize components for Routine "_Count_Side"
_Count_SideClock = core.Clock()
Cir1_3 = visual.ShapeStim(
    win=win, name='Cir1_3',units='height', 
    size=[0.3], vertices='circle',
    ori=0.0, pos=(-0.675, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
Cir2_3 = visual.ShapeStim(
    win=win, name='Cir2_3',units='height', 
    size=[0.3], vertices='circle',
    ori=0.0, pos=(-0.225, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
Cir3_3 = visual.ShapeStim(
    win=win, name='Cir3_3',units='height', 
    size=[0.3], vertices='circle',
    ori=0.0, pos=(0.225, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
Cir4_3 = visual.ShapeStim(
    win=win, name='Cir4_3',units='height', 
    size=[0.3], vertices='circle',
    ori=0.0, pos=(0.675, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
key_resp_8 = keyboard.Keyboard()
mouse_click_locations = []
Fini_text = visual.TextStim(win=win, name='Fini_text',
    text='',
    font='Open Sans',
    units='height', pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
inst_ImageCount = 1
inst_Image = visual.ImageStim(
    win=win,
    name='inst_Image', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.88, 0.66),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Inst_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Init"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
InitComponents = []
for thisComponent in InitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Init"-------
while continueRoutine:
    # get current time
    t = InitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Init"-------
for thisComponent in InitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Inst_Loop01 = data.TrialHandler(nReps=6.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Inst_Loop01')
thisExp.addLoop(Inst_Loop01)  # add the loop to the experiment
thisInst_Loop01 = Inst_Loop01.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInst_Loop01.rgb)
if thisInst_Loop01 != None:
    for paramName in thisInst_Loop01:
        exec('{} = thisInst_Loop01[paramName]'.format(paramName))

for thisInst_Loop01 in Inst_Loop01:
    currentLoop = Inst_Loop01
    # abbreviate parameter names if possible (e.g. rgb = thisInst_Loop01.rgb)
    if thisInst_Loop01 != None:
        for paramName in thisInst_Loop01:
            exec('{} = thisInst_Loop01[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    inst_ImagePath = "EXP_DATA/Instructions/Inst_Image/" + str(inst_ImageCount) + ".JPG"
    
    inst_Image.setImage(inst_ImagePath)
    Inst_key.keys = []
    Inst_key.rt = []
    _Inst_key_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [inst_Image, Inst_key]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_Image* updates
        if inst_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst_Image.frameNStart = frameN  # exact frame index
            inst_Image.tStart = t  # local t and not account for scr refresh
            inst_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst_Image, 'tStartRefresh')  # time at next scr refresh
            inst_Image.setAutoDraw(True)
        
        # *Inst_key* updates
        if Inst_key.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            Inst_key.frameNStart = frameN  # exact frame index
            Inst_key.tStart = t  # local t and not account for scr refresh
            Inst_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Inst_key, 'tStartRefresh')  # time at next scr refresh
            Inst_key.status = STARTED
            # keyboard checking is just starting
            Inst_key.clock.reset()  # now t=0
            Inst_key.clearEvents(eventType='keyboard')
        if Inst_key.status == STARTED:
            theseKeys = Inst_key.getKeys(keyList=None, waitRelease=False)
            _Inst_key_allKeys.extend(theseKeys)
            if len(_Inst_key_allKeys):
                Inst_key.keys = _Inst_key_allKeys[-1].name  # just the last key pressed
                Inst_key.rt = _Inst_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    inst_ImageCount = inst_ImageCount+1
    
    
    
    # check responses
    if Inst_key.keys in ['', [], None]:  # No response was made
        Inst_key.keys = None
    Inst_Loop01.addData('Inst_key.keys',Inst_key.keys)
    if Inst_key.keys != None:  # we had a response
        Inst_Loop01.addData('Inst_key.rt', Inst_key.rt)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'Inst_Loop01'


# ------Prepare to start Routine "Animation01"-------
continueRoutine = True
# update component parameters for each repeat
Animation01_Key.keys = []
Animation01_Key.rt = []
_Animation01_Key_allKeys = []
# keep track of which components have finished
Animation01Components = [Animation01_Video, Animation01_Key, Animation01_text]
for thisComponent in Animation01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Animation01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Animation01"-------
while continueRoutine:
    # get current time
    t = Animation01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Animation01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Animation01_Video* updates
    if Animation01_Video.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Animation01_Video.frameNStart = frameN  # exact frame index
        Animation01_Video.tStart = t  # local t and not account for scr refresh
        Animation01_Video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Animation01_Video, 'tStartRefresh')  # time at next scr refresh
        Animation01_Video.setAutoDraw(True)
    if Animation01_Video.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *Animation01_Key* updates
    if Animation01_Key.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Animation01_Key.frameNStart = frameN  # exact frame index
        Animation01_Key.tStart = t  # local t and not account for scr refresh
        Animation01_Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Animation01_Key, 'tStartRefresh')  # time at next scr refresh
        Animation01_Key.status = STARTED
        # keyboard checking is just starting
        Animation01_Key.clock.reset()  # now t=0
        Animation01_Key.clearEvents(eventType='keyboard')
    if Animation01_Key.status == STARTED:
        theseKeys = Animation01_Key.getKeys(keyList=None, waitRelease=False)
        _Animation01_Key_allKeys.extend(theseKeys)
        if len(_Animation01_Key_allKeys):
            Animation01_Key.keys = _Animation01_Key_allKeys[-1].name  # just the last key pressed
            Animation01_Key.rt = _Animation01_Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Animation01_text* updates
    if Animation01_text.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
        # keep track of start time/frame for later
        Animation01_text.frameNStart = frameN  # exact frame index
        Animation01_text.tStart = t  # local t and not account for scr refresh
        Animation01_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Animation01_text, 'tStartRefresh')  # time at next scr refresh
        Animation01_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Animation01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Animation01"-------
for thisComponent in Animation01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Animation01_Video.stop()
# check responses
if Animation01_Key.keys in ['', [], None]:  # No response was made
    Animation01_Key.keys = None
thisExp.addData('Animation01_Key.keys',Animation01_Key.keys)
if Animation01_Key.keys != None:  # we had a response
    thisExp.addData('Animation01_Key.rt', Animation01_Key.rt)
thisExp.nextEntry()
# the Routine "Animation01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
inst_ImagePath = "EXP_DATA/Instructions/Inst_Image/" + str(inst_ImageCount) + ".JPG"

inst_Image.setImage(inst_ImagePath)
Inst_key.keys = []
Inst_key.rt = []
_Inst_key_allKeys = []
# keep track of which components have finished
InstructionsComponents = [inst_Image, Inst_key]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image* updates
    if inst_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image.frameNStart = frameN  # exact frame index
        inst_Image.tStart = t  # local t and not account for scr refresh
        inst_Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image, 'tStartRefresh')  # time at next scr refresh
        inst_Image.setAutoDraw(True)
    
    # *Inst_key* updates
    if Inst_key.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key.frameNStart = frameN  # exact frame index
        Inst_key.tStart = t  # local t and not account for scr refresh
        Inst_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key, 'tStartRefresh')  # time at next scr refresh
        Inst_key.status = STARTED
        # keyboard checking is just starting
        Inst_key.clock.reset()  # now t=0
        Inst_key.clearEvents(eventType='keyboard')
    if Inst_key.status == STARTED:
        theseKeys = Inst_key.getKeys(keyList=None, waitRelease=False)
        _Inst_key_allKeys.extend(theseKeys)
        if len(_Inst_key_allKeys):
            Inst_key.keys = _Inst_key_allKeys[-1].name  # just the last key pressed
            Inst_key.rt = _Inst_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
inst_ImageCount = inst_ImageCount+1



# check responses
if Inst_key.keys in ['', [], None]:  # No response was made
    Inst_key.keys = None
thisExp.addData('Inst_key.keys',Inst_key.keys)
if Inst_key.keys != None:  # we had a response
    thisExp.addData('Inst_key.rt', Inst_key.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "estimate_screen_size"-------
continueRoutine = True
# update component parameters for each repeat
slider.reset()
slider.markerPos = 0.5
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
estimate_screen_sizeComponents = [card, slider, key_resp_2]
for thisComponent in estimate_screen_sizeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
estimate_screen_sizeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "estimate_screen_size"-------
while continueRoutine:
    # get current time
    t = estimate_screen_sizeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=estimate_screen_sizeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *card* updates
    if card.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        card.frameNStart = frameN  # exact frame index
        card.tStart = t  # local t and not account for scr refresh
        card.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(card, 'tStartRefresh')  # time at next scr refresh
        card.setAutoDraw(True)
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    if slider.markerPos:
      newW = cardWidthPXMax * slider.markerPos
      newH = newW * cardAspectRatio
      newSize = [newW, newH]
      card.setSize(newSize)
      cardWidthPX = newW
      px2mm = cardWidthPX / cardWidthMM
    
    
    
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in estimate_screen_sizeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "estimate_screen_size"-------
for thisComponent in estimate_screen_sizeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "estimate_screen_size" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Results"-------
continueRoutine = True
# update component parameters for each repeat
(w, h) = win.size
Wcm = (w/px2mm)/10
Hcm = (h/px2mm)/10
dist_text = "Your screen Height is " + str(round(Hcm ,2)) + " Cm" + "\n" + "Your screen Width is " + str(round(Wcm ,2)) + " Cm" + "\n" + "Your screen Resolution is " + str(win.size) + " Pixels"
#dist_text = (((((((((("Your screen Height is " + rounder(Hcm).toString()) + " Cm") + "\n") + "Your screen Width is ") + rounder(Wcm).toString()) + " Cm") + "\n") + "Your screen Resolution is ") + psychoJS.window.size.toString()) + " Pixels");
#dist_text = (((((((((("Your screen Height is " + Math.round(Hcm).toString()) + " Cm") + "\n") + "Your screen Width is ") + Math.round(Wcm).toString()) + " Cm") + "\n") + "Your screen Resolution is ") + psychoJS.window.size.toString()) + " Pixels");
#var Hcm;
Res_text.setText(dist_text)
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
ResultsComponents = [Res_text, key_resp_4, Results_Text_Cont]
for thisComponent in ResultsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ResultsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Results"-------
while continueRoutine:
    # get current time
    t = ResultsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ResultsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Res_text* updates
    if Res_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Res_text.frameNStart = frameN  # exact frame index
        Res_text.tStart = t  # local t and not account for scr refresh
        Res_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Res_text, 'tStartRefresh')  # time at next scr refresh
        Res_text.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=None, waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Results_Text_Cont* updates
    if Results_Text_Cont.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Results_Text_Cont.frameNStart = frameN  # exact frame index
        Results_Text_Cont.tStart = t  # local t and not account for scr refresh
        Results_Text_Cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Results_Text_Cont, 'tStartRefresh')  # time at next scr refresh
        Results_Text_Cont.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ResultsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Results"-------
for thisComponent in ResultsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
screen_Prop = Hcm/29.5
thisExp.addData('screen_Prop', screen_Prop)
thisExp.addData('Res_text.started', Res_text.tStartRefresh)
thisExp.addData('Res_text.stopped', Res_text.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
screen_Prop = Hcm/29.5
thisExp.addData('screen_Prop', screen_Prop)
# the Routine "Results" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    inst_ImagePath = "EXP_DATA/Instructions/Inst_Image/" + str(inst_ImageCount) + ".JPG"
    
    inst_Image.setImage(inst_ImagePath)
    Inst_key.keys = []
    Inst_key.rt = []
    _Inst_key_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [inst_Image, Inst_key]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_Image* updates
        if inst_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst_Image.frameNStart = frameN  # exact frame index
            inst_Image.tStart = t  # local t and not account for scr refresh
            inst_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst_Image, 'tStartRefresh')  # time at next scr refresh
            inst_Image.setAutoDraw(True)
        
        # *Inst_key* updates
        if Inst_key.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            Inst_key.frameNStart = frameN  # exact frame index
            Inst_key.tStart = t  # local t and not account for scr refresh
            Inst_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Inst_key, 'tStartRefresh')  # time at next scr refresh
            Inst_key.status = STARTED
            # keyboard checking is just starting
            Inst_key.clock.reset()  # now t=0
            Inst_key.clearEvents(eventType='keyboard')
        if Inst_key.status == STARTED:
            theseKeys = Inst_key.getKeys(keyList=None, waitRelease=False)
            _Inst_key_allKeys.extend(theseKeys)
            if len(_Inst_key_allKeys):
                Inst_key.keys = _Inst_key_allKeys[-1].name  # just the last key pressed
                Inst_key.rt = _Inst_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    inst_ImageCount = inst_ImageCount+1
    
    
    
    # check responses
    if Inst_key.keys in ['', [], None]:  # No response was made
        Inst_key.keys = None
    trials.addData('Inst_key.keys',Inst_key.keys)
    if Inst_key.keys != None:  # we had a response
        trials.addData('Inst_key.rt', Inst_key.rt)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials'


# ------Prepare to start Routine "Init_Counter"-------
continueRoutine = True
# update component parameters for each repeat
G_Condition = (expInfo['Group'])
e_LIST = split(G_Condition)
C1 = e_LIST[0]
C2 = e_LIST[1]
C3 = e_LIST[2]
C4 = e_LIST[3]

con1 = 'EXP_DATA\Conditions\SNA\Con' + C1 + '.xlsx'
con2 = 'EXP_DATA\Conditions\SNA\Con' + C2 + '.xlsx'
con3 = 'EXP_DATA\Conditions\SNA\Con' + C3 + '.xlsx'
con4 = 'EXP_DATA\Conditions\SNA\Con' + C4 + '.xlsx'

print('e_LIST:', e_LIST)

# keep track of which components have finished
Init_CounterComponents = []
for thisComponent in Init_CounterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Init_CounterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Init_Counter"-------
while continueRoutine:
    # get current time
    t = Init_CounterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Init_CounterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Init_CounterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Init_Counter"-------
for thisComponent in Init_CounterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Init_Counter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Block_iNTS"-------
continueRoutine = True
# update component parameters for each repeat
if Inst_n == 4:
   Block_n = Block_n+1
   Inst_n = 1

if Block_n == 1:
   CON = C1
if Block_n == 2:
   CON = C2
if Block_n == 3:
   CON = C3
if Block_n == 4:
   CON = C4

Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'

print('Phase_ImagePath', Phase_ImagePath)
inst_Image_2.setImage(Phase_ImagePath)
Inst_key_2.keys = []
Inst_key_2.rt = []
_Inst_key_2_allKeys = []
# keep track of which components have finished
Block_iNTSComponents = [inst_Image_2, Inst_key_2]
for thisComponent in Block_iNTSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block_iNTS"-------
while continueRoutine:
    # get current time
    t = Block_iNTSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image_2* updates
    if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image_2.frameNStart = frameN  # exact frame index
        inst_Image_2.tStart = t  # local t and not account for scr refresh
        inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
        inst_Image_2.setAutoDraw(True)
    
    # *Inst_key_2* updates
    if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key_2.frameNStart = frameN  # exact frame index
        Inst_key_2.tStart = t  # local t and not account for scr refresh
        Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
        Inst_key_2.status = STARTED
        # keyboard checking is just starting
        Inst_key_2.clock.reset()  # now t=0
        Inst_key_2.clearEvents(eventType='keyboard')
    if Inst_key_2.status == STARTED:
        theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
        _Inst_key_2_allKeys.extend(theseKeys)
        if len(_Inst_key_2_allKeys):
            Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
            Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_iNTS"-------
for thisComponent in Block_iNTSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Inst_n = Inst_n+1






# check responses
if Inst_key_2.keys in ['', [], None]:  # No response was made
    Inst_key_2.keys = None
thisExp.addData('Inst_key_2.keys',Inst_key_2.keys)
if Inst_key_2.keys != None:  # we had a response
    thisExp.addData('Inst_key_2.rt', Inst_key_2.rt)
thisExp.nextEntry()
# the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice_First_Con = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con1),
    seed=None, name='Practice_First_Con')
thisExp.addLoop(Practice_First_Con)  # add the loop to the experiment
thisPractice_First_Con = Practice_First_Con.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_First_Con.rgb)
if thisPractice_First_Con != None:
    for paramName in thisPractice_First_Con:
        exec('{} = thisPractice_First_Con[paramName]'.format(paramName))

for thisPractice_First_Con in Practice_First_Con:
    currentLoop = Practice_First_Con
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_First_Con.rgb)
    if thisPractice_First_Con != None:
        for paramName in thisPractice_First_Con:
            exec('{} = thisPractice_First_Con[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_First_Con.addData('Fixation_.started', Fixation_.tStartRefresh)
    Practice_First_Con.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    Practice_First_Con.addData('image.started', image.tStartRefresh)
    Practice_First_Con.addData('image.stopped', image.tStopRefresh)
    Practice_First_Con.addData('text_.started', text_.tStartRefresh)
    Practice_First_Con.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Practice_First_Con (TrialHandler)
    Practice_First_Con.addData('C_Response.keys',C_Response.keys)
    Practice_First_Con.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        Practice_First_Con.addData('C_Response.rt', C_Response.rt)
    Practice_First_Con.addData('C_Response.started', C_Response.tStartRefresh)
    Practice_First_Con.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    
    # ------Prepare to start Routine "Blank_3"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text_4.setColor(Feedback_Color, colorSpace='rgb')
    text_4.setText(Feedback)
    # keep track of which components have finished
    Blank_3Components = [Blank_, text_4, text_5]
    for thisComponent in Blank_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Blank_* updates
        if Blank_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank_.frameNStart = frameN  # exact frame index
            Blank_.tStart = t  # local t and not account for scr refresh
            Blank_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank_, 'tStartRefresh')  # time at next scr refresh
            Blank_.setAutoDraw(True)
        if Blank_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank_.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank_.tStop = t  # not accounting for scr refresh
                Blank_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank_, 'tStopRefresh')  # time at next scr refresh
                Blank_.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank_3"-------
    for thisComponent in Blank_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_First_Con.addData('Blank_.started', Blank_.tStartRefresh)
    Practice_First_Con.addData('Blank_.stopped', Blank_.tStopRefresh)
    Practice_First_Con.addData('text_4.started', text_4.tStartRefresh)
    Practice_First_Con.addData('text_4.stopped', text_4.tStopRefresh)
    Practice_First_Con.addData('text_5.started', text_5.tStartRefresh)
    Practice_First_Con.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Practice_First_Con'


# ------Prepare to start Routine "Block_iNTS"-------
continueRoutine = True
# update component parameters for each repeat
if Inst_n == 4:
   Block_n = Block_n+1
   Inst_n = 1

if Block_n == 1:
   CON = C1
if Block_n == 2:
   CON = C2
if Block_n == 3:
   CON = C3
if Block_n == 4:
   CON = C4

Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'

print('Phase_ImagePath', Phase_ImagePath)
inst_Image_2.setImage(Phase_ImagePath)
Inst_key_2.keys = []
Inst_key_2.rt = []
_Inst_key_2_allKeys = []
# keep track of which components have finished
Block_iNTSComponents = [inst_Image_2, Inst_key_2]
for thisComponent in Block_iNTSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block_iNTS"-------
while continueRoutine:
    # get current time
    t = Block_iNTSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image_2* updates
    if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image_2.frameNStart = frameN  # exact frame index
        inst_Image_2.tStart = t  # local t and not account for scr refresh
        inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
        inst_Image_2.setAutoDraw(True)
    
    # *Inst_key_2* updates
    if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key_2.frameNStart = frameN  # exact frame index
        Inst_key_2.tStart = t  # local t and not account for scr refresh
        Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
        Inst_key_2.status = STARTED
        # keyboard checking is just starting
        Inst_key_2.clock.reset()  # now t=0
        Inst_key_2.clearEvents(eventType='keyboard')
    if Inst_key_2.status == STARTED:
        theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
        _Inst_key_2_allKeys.extend(theseKeys)
        if len(_Inst_key_2_allKeys):
            Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
            Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_iNTS"-------
for thisComponent in Block_iNTSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Inst_n = Inst_n+1






# check responses
if Inst_key_2.keys in ['', [], None]:  # No response was made
    Inst_key_2.keys = None
thisExp.addData('Inst_key_2.keys',Inst_key_2.keys)
if Inst_key_2.keys != None:  # we had a response
    thisExp.addData('Inst_key_2.rt', Inst_key_2.rt)
thisExp.nextEntry()
# the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
First_Cond = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con1),
    seed=None, name='First_Cond')
thisExp.addLoop(First_Cond)  # add the loop to the experiment
thisFirst_Cond = First_Cond.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_Cond.rgb)
if thisFirst_Cond != None:
    for paramName in thisFirst_Cond:
        exec('{} = thisFirst_Cond[paramName]'.format(paramName))

for thisFirst_Cond in First_Cond:
    currentLoop = First_Cond
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_Cond.rgb)
    if thisFirst_Cond != None:
        for paramName in thisFirst_Cond:
            exec('{} = thisFirst_Cond[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    First_Cond.addData('Fixation_.started', Fixation_.tStartRefresh)
    First_Cond.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    First_Cond.addData('image.started', image.tStartRefresh)
    First_Cond.addData('image.stopped', image.tStopRefresh)
    First_Cond.addData('text_.started', text_.tStartRefresh)
    First_Cond.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for First_Cond (TrialHandler)
    First_Cond.addData('C_Response.keys',C_Response.keys)
    First_Cond.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        First_Cond.addData('C_Response.rt', C_Response.rt)
    First_Cond.addData('C_Response.started', C_Response.tStartRefresh)
    First_Cond.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'First_Cond'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_iNTS"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Inst_n == 4:
       Block_n = Block_n+1
       Inst_n = 1
    
    if Block_n == 1:
       CON = C1
    if Block_n == 2:
       CON = C2
    if Block_n == 3:
       CON = C3
    if Block_n == 4:
       CON = C4
    
    Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'
    
    print('Phase_ImagePath', Phase_ImagePath)
    inst_Image_2.setImage(Phase_ImagePath)
    Inst_key_2.keys = []
    Inst_key_2.rt = []
    _Inst_key_2_allKeys = []
    # keep track of which components have finished
    Block_iNTSComponents = [inst_Image_2, Inst_key_2]
    for thisComponent in Block_iNTSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_iNTS"-------
    while continueRoutine:
        # get current time
        t = Block_iNTSClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_Image_2* updates
        if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst_Image_2.frameNStart = frameN  # exact frame index
            inst_Image_2.tStart = t  # local t and not account for scr refresh
            inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
            inst_Image_2.setAutoDraw(True)
        
        # *Inst_key_2* updates
        if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            Inst_key_2.frameNStart = frameN  # exact frame index
            Inst_key_2.tStart = t  # local t and not account for scr refresh
            Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
            Inst_key_2.status = STARTED
            # keyboard checking is just starting
            Inst_key_2.clock.reset()  # now t=0
            Inst_key_2.clearEvents(eventType='keyboard')
        if Inst_key_2.status == STARTED:
            theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
            _Inst_key_2_allKeys.extend(theseKeys)
            if len(_Inst_key_2_allKeys):
                Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
                Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_iNTSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_iNTS"-------
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Inst_n = Inst_n+1
    
    
    
    
    
    
    # check responses
    if Inst_key_2.keys in ['', [], None]:  # No response was made
        Inst_key_2.keys = None
    trials_2.addData('Inst_key_2.keys',Inst_key_2.keys)
    if Inst_key_2.keys != None:  # we had a response
        trials_2.addData('Inst_key_2.rt', Inst_key_2.rt)
    # the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
Practice_second_Con = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con2),
    seed=None, name='Practice_second_Con')
thisExp.addLoop(Practice_second_Con)  # add the loop to the experiment
thisPractice_second_Con = Practice_second_Con.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_second_Con.rgb)
if thisPractice_second_Con != None:
    for paramName in thisPractice_second_Con:
        exec('{} = thisPractice_second_Con[paramName]'.format(paramName))

for thisPractice_second_Con in Practice_second_Con:
    currentLoop = Practice_second_Con
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_second_Con.rgb)
    if thisPractice_second_Con != None:
        for paramName in thisPractice_second_Con:
            exec('{} = thisPractice_second_Con[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_second_Con.addData('Fixation_.started', Fixation_.tStartRefresh)
    Practice_second_Con.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    Practice_second_Con.addData('image.started', image.tStartRefresh)
    Practice_second_Con.addData('image.stopped', image.tStopRefresh)
    Practice_second_Con.addData('text_.started', text_.tStartRefresh)
    Practice_second_Con.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Practice_second_Con (TrialHandler)
    Practice_second_Con.addData('C_Response.keys',C_Response.keys)
    Practice_second_Con.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        Practice_second_Con.addData('C_Response.rt', C_Response.rt)
    Practice_second_Con.addData('C_Response.started', C_Response.tStartRefresh)
    Practice_second_Con.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    
    # ------Prepare to start Routine "Blank_3"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text_4.setColor(Feedback_Color, colorSpace='rgb')
    text_4.setText(Feedback)
    # keep track of which components have finished
    Blank_3Components = [Blank_, text_4, text_5]
    for thisComponent in Blank_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Blank_* updates
        if Blank_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank_.frameNStart = frameN  # exact frame index
            Blank_.tStart = t  # local t and not account for scr refresh
            Blank_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank_, 'tStartRefresh')  # time at next scr refresh
            Blank_.setAutoDraw(True)
        if Blank_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank_.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank_.tStop = t  # not accounting for scr refresh
                Blank_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank_, 'tStopRefresh')  # time at next scr refresh
                Blank_.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank_3"-------
    for thisComponent in Blank_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_second_Con.addData('Blank_.started', Blank_.tStartRefresh)
    Practice_second_Con.addData('Blank_.stopped', Blank_.tStopRefresh)
    Practice_second_Con.addData('text_4.started', text_4.tStartRefresh)
    Practice_second_Con.addData('text_4.stopped', text_4.tStopRefresh)
    Practice_second_Con.addData('text_5.started', text_5.tStartRefresh)
    Practice_second_Con.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Practice_second_Con'


# ------Prepare to start Routine "Block_iNTS"-------
continueRoutine = True
# update component parameters for each repeat
if Inst_n == 4:
   Block_n = Block_n+1
   Inst_n = 1

if Block_n == 1:
   CON = C1
if Block_n == 2:
   CON = C2
if Block_n == 3:
   CON = C3
if Block_n == 4:
   CON = C4

Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'

print('Phase_ImagePath', Phase_ImagePath)
inst_Image_2.setImage(Phase_ImagePath)
Inst_key_2.keys = []
Inst_key_2.rt = []
_Inst_key_2_allKeys = []
# keep track of which components have finished
Block_iNTSComponents = [inst_Image_2, Inst_key_2]
for thisComponent in Block_iNTSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block_iNTS"-------
while continueRoutine:
    # get current time
    t = Block_iNTSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image_2* updates
    if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image_2.frameNStart = frameN  # exact frame index
        inst_Image_2.tStart = t  # local t and not account for scr refresh
        inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
        inst_Image_2.setAutoDraw(True)
    
    # *Inst_key_2* updates
    if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key_2.frameNStart = frameN  # exact frame index
        Inst_key_2.tStart = t  # local t and not account for scr refresh
        Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
        Inst_key_2.status = STARTED
        # keyboard checking is just starting
        Inst_key_2.clock.reset()  # now t=0
        Inst_key_2.clearEvents(eventType='keyboard')
    if Inst_key_2.status == STARTED:
        theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
        _Inst_key_2_allKeys.extend(theseKeys)
        if len(_Inst_key_2_allKeys):
            Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
            Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_iNTS"-------
for thisComponent in Block_iNTSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Inst_n = Inst_n+1






# check responses
if Inst_key_2.keys in ['', [], None]:  # No response was made
    Inst_key_2.keys = None
thisExp.addData('Inst_key_2.keys',Inst_key_2.keys)
if Inst_key_2.keys != None:  # we had a response
    thisExp.addData('Inst_key_2.rt', Inst_key_2.rt)
thisExp.nextEntry()
# the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Second_Con = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con2),
    seed=None, name='Second_Con')
thisExp.addLoop(Second_Con)  # add the loop to the experiment
thisSecond_Con = Second_Con.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSecond_Con.rgb)
if thisSecond_Con != None:
    for paramName in thisSecond_Con:
        exec('{} = thisSecond_Con[paramName]'.format(paramName))

for thisSecond_Con in Second_Con:
    currentLoop = Second_Con
    # abbreviate parameter names if possible (e.g. rgb = thisSecond_Con.rgb)
    if thisSecond_Con != None:
        for paramName in thisSecond_Con:
            exec('{} = thisSecond_Con[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Second_Con.addData('Fixation_.started', Fixation_.tStartRefresh)
    Second_Con.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    Second_Con.addData('image.started', image.tStartRefresh)
    Second_Con.addData('image.stopped', image.tStopRefresh)
    Second_Con.addData('text_.started', text_.tStartRefresh)
    Second_Con.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Second_Con (TrialHandler)
    Second_Con.addData('C_Response.keys',C_Response.keys)
    Second_Con.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        Second_Con.addData('C_Response.rt', C_Response.rt)
    Second_Con.addData('C_Response.started', C_Response.tStartRefresh)
    Second_Con.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'Second_Con'


# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7:
        exec('{} = thisTrial_7[paramName]'.format(paramName))

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_iNTS"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Inst_n == 4:
       Block_n = Block_n+1
       Inst_n = 1
    
    if Block_n == 1:
       CON = C1
    if Block_n == 2:
       CON = C2
    if Block_n == 3:
       CON = C3
    if Block_n == 4:
       CON = C4
    
    Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'
    
    print('Phase_ImagePath', Phase_ImagePath)
    inst_Image_2.setImage(Phase_ImagePath)
    Inst_key_2.keys = []
    Inst_key_2.rt = []
    _Inst_key_2_allKeys = []
    # keep track of which components have finished
    Block_iNTSComponents = [inst_Image_2, Inst_key_2]
    for thisComponent in Block_iNTSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_iNTS"-------
    while continueRoutine:
        # get current time
        t = Block_iNTSClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_Image_2* updates
        if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst_Image_2.frameNStart = frameN  # exact frame index
            inst_Image_2.tStart = t  # local t and not account for scr refresh
            inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
            inst_Image_2.setAutoDraw(True)
        
        # *Inst_key_2* updates
        if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            Inst_key_2.frameNStart = frameN  # exact frame index
            Inst_key_2.tStart = t  # local t and not account for scr refresh
            Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
            Inst_key_2.status = STARTED
            # keyboard checking is just starting
            Inst_key_2.clock.reset()  # now t=0
            Inst_key_2.clearEvents(eventType='keyboard')
        if Inst_key_2.status == STARTED:
            theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
            _Inst_key_2_allKeys.extend(theseKeys)
            if len(_Inst_key_2_allKeys):
                Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
                Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_iNTSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_iNTS"-------
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Inst_n = Inst_n+1
    
    
    
    
    
    
    # check responses
    if Inst_key_2.keys in ['', [], None]:  # No response was made
        Inst_key_2.keys = None
    trials_7.addData('Inst_key_2.keys',Inst_key_2.keys)
    if Inst_key_2.keys != None:  # we had a response
        trials_7.addData('Inst_key_2.rt', Inst_key_2.rt)
    # the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_7'


# set up handler to look after randomisation of conditions etc
Practice_Third_Con = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con3),
    seed=None, name='Practice_Third_Con')
thisExp.addLoop(Practice_Third_Con)  # add the loop to the experiment
thisPractice_Third_Con = Practice_Third_Con.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_Third_Con.rgb)
if thisPractice_Third_Con != None:
    for paramName in thisPractice_Third_Con:
        exec('{} = thisPractice_Third_Con[paramName]'.format(paramName))

for thisPractice_Third_Con in Practice_Third_Con:
    currentLoop = Practice_Third_Con
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Third_Con.rgb)
    if thisPractice_Third_Con != None:
        for paramName in thisPractice_Third_Con:
            exec('{} = thisPractice_Third_Con[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_Third_Con.addData('Fixation_.started', Fixation_.tStartRefresh)
    Practice_Third_Con.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    Practice_Third_Con.addData('image.started', image.tStartRefresh)
    Practice_Third_Con.addData('image.stopped', image.tStopRefresh)
    Practice_Third_Con.addData('text_.started', text_.tStartRefresh)
    Practice_Third_Con.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Practice_Third_Con (TrialHandler)
    Practice_Third_Con.addData('C_Response.keys',C_Response.keys)
    Practice_Third_Con.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        Practice_Third_Con.addData('C_Response.rt', C_Response.rt)
    Practice_Third_Con.addData('C_Response.started', C_Response.tStartRefresh)
    Practice_Third_Con.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    
    # ------Prepare to start Routine "Blank_3"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text_4.setColor(Feedback_Color, colorSpace='rgb')
    text_4.setText(Feedback)
    # keep track of which components have finished
    Blank_3Components = [Blank_, text_4, text_5]
    for thisComponent in Blank_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Blank_* updates
        if Blank_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank_.frameNStart = frameN  # exact frame index
            Blank_.tStart = t  # local t and not account for scr refresh
            Blank_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank_, 'tStartRefresh')  # time at next scr refresh
            Blank_.setAutoDraw(True)
        if Blank_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank_.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank_.tStop = t  # not accounting for scr refresh
                Blank_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank_, 'tStopRefresh')  # time at next scr refresh
                Blank_.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank_3"-------
    for thisComponent in Blank_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_Third_Con.addData('Blank_.started', Blank_.tStartRefresh)
    Practice_Third_Con.addData('Blank_.stopped', Blank_.tStopRefresh)
    Practice_Third_Con.addData('text_4.started', text_4.tStartRefresh)
    Practice_Third_Con.addData('text_4.stopped', text_4.tStopRefresh)
    Practice_Third_Con.addData('text_5.started', text_5.tStartRefresh)
    Practice_Third_Con.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Practice_Third_Con'


# ------Prepare to start Routine "Block_iNTS"-------
continueRoutine = True
# update component parameters for each repeat
if Inst_n == 4:
   Block_n = Block_n+1
   Inst_n = 1

if Block_n == 1:
   CON = C1
if Block_n == 2:
   CON = C2
if Block_n == 3:
   CON = C3
if Block_n == 4:
   CON = C4

Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'

print('Phase_ImagePath', Phase_ImagePath)
inst_Image_2.setImage(Phase_ImagePath)
Inst_key_2.keys = []
Inst_key_2.rt = []
_Inst_key_2_allKeys = []
# keep track of which components have finished
Block_iNTSComponents = [inst_Image_2, Inst_key_2]
for thisComponent in Block_iNTSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block_iNTS"-------
while continueRoutine:
    # get current time
    t = Block_iNTSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image_2* updates
    if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image_2.frameNStart = frameN  # exact frame index
        inst_Image_2.tStart = t  # local t and not account for scr refresh
        inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
        inst_Image_2.setAutoDraw(True)
    
    # *Inst_key_2* updates
    if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key_2.frameNStart = frameN  # exact frame index
        Inst_key_2.tStart = t  # local t and not account for scr refresh
        Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
        Inst_key_2.status = STARTED
        # keyboard checking is just starting
        Inst_key_2.clock.reset()  # now t=0
        Inst_key_2.clearEvents(eventType='keyboard')
    if Inst_key_2.status == STARTED:
        theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
        _Inst_key_2_allKeys.extend(theseKeys)
        if len(_Inst_key_2_allKeys):
            Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
            Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_iNTS"-------
for thisComponent in Block_iNTSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Inst_n = Inst_n+1






# check responses
if Inst_key_2.keys in ['', [], None]:  # No response was made
    Inst_key_2.keys = None
thisExp.addData('Inst_key_2.keys',Inst_key_2.keys)
if Inst_key_2.keys != None:  # we had a response
    thisExp.addData('Inst_key_2.rt', Inst_key_2.rt)
thisExp.nextEntry()
# the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Third_Con = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con3),
    seed=None, name='Third_Con')
thisExp.addLoop(Third_Con)  # add the loop to the experiment
thisThird_Con = Third_Con.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisThird_Con.rgb)
if thisThird_Con != None:
    for paramName in thisThird_Con:
        exec('{} = thisThird_Con[paramName]'.format(paramName))

for thisThird_Con in Third_Con:
    currentLoop = Third_Con
    # abbreviate parameter names if possible (e.g. rgb = thisThird_Con.rgb)
    if thisThird_Con != None:
        for paramName in thisThird_Con:
            exec('{} = thisThird_Con[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Third_Con.addData('Fixation_.started', Fixation_.tStartRefresh)
    Third_Con.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    Third_Con.addData('image.started', image.tStartRefresh)
    Third_Con.addData('image.stopped', image.tStopRefresh)
    Third_Con.addData('text_.started', text_.tStartRefresh)
    Third_Con.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Third_Con (TrialHandler)
    Third_Con.addData('C_Response.keys',C_Response.keys)
    Third_Con.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        Third_Con.addData('C_Response.rt', C_Response.rt)
    Third_Con.addData('C_Response.started', C_Response.tStartRefresh)
    Third_Con.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'Third_Con'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_iNTS"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Inst_n == 4:
       Block_n = Block_n+1
       Inst_n = 1
    
    if Block_n == 1:
       CON = C1
    if Block_n == 2:
       CON = C2
    if Block_n == 3:
       CON = C3
    if Block_n == 4:
       CON = C4
    
    Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'
    
    print('Phase_ImagePath', Phase_ImagePath)
    inst_Image_2.setImage(Phase_ImagePath)
    Inst_key_2.keys = []
    Inst_key_2.rt = []
    _Inst_key_2_allKeys = []
    # keep track of which components have finished
    Block_iNTSComponents = [inst_Image_2, Inst_key_2]
    for thisComponent in Block_iNTSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_iNTS"-------
    while continueRoutine:
        # get current time
        t = Block_iNTSClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_Image_2* updates
        if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst_Image_2.frameNStart = frameN  # exact frame index
            inst_Image_2.tStart = t  # local t and not account for scr refresh
            inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
            inst_Image_2.setAutoDraw(True)
        
        # *Inst_key_2* updates
        if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            Inst_key_2.frameNStart = frameN  # exact frame index
            Inst_key_2.tStart = t  # local t and not account for scr refresh
            Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
            Inst_key_2.status = STARTED
            # keyboard checking is just starting
            Inst_key_2.clock.reset()  # now t=0
            Inst_key_2.clearEvents(eventType='keyboard')
        if Inst_key_2.status == STARTED:
            theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
            _Inst_key_2_allKeys.extend(theseKeys)
            if len(_Inst_key_2_allKeys):
                Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
                Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_iNTSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_iNTS"-------
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Inst_n = Inst_n+1
    
    
    
    
    
    
    # check responses
    if Inst_key_2.keys in ['', [], None]:  # No response was made
        Inst_key_2.keys = None
    trials_3.addData('Inst_key_2.keys',Inst_key_2.keys)
    if Inst_key_2.keys != None:  # we had a response
        trials_3.addData('Inst_key_2.rt', Inst_key_2.rt)
    # the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
Practice_Forth_Con = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con4),
    seed=None, name='Practice_Forth_Con')
thisExp.addLoop(Practice_Forth_Con)  # add the loop to the experiment
thisPractice_Forth_Con = Practice_Forth_Con.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_Forth_Con.rgb)
if thisPractice_Forth_Con != None:
    for paramName in thisPractice_Forth_Con:
        exec('{} = thisPractice_Forth_Con[paramName]'.format(paramName))

for thisPractice_Forth_Con in Practice_Forth_Con:
    currentLoop = Practice_Forth_Con
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Forth_Con.rgb)
    if thisPractice_Forth_Con != None:
        for paramName in thisPractice_Forth_Con:
            exec('{} = thisPractice_Forth_Con[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_Forth_Con.addData('Fixation_.started', Fixation_.tStartRefresh)
    Practice_Forth_Con.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    Practice_Forth_Con.addData('image.started', image.tStartRefresh)
    Practice_Forth_Con.addData('image.stopped', image.tStopRefresh)
    Practice_Forth_Con.addData('text_.started', text_.tStartRefresh)
    Practice_Forth_Con.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Practice_Forth_Con (TrialHandler)
    Practice_Forth_Con.addData('C_Response.keys',C_Response.keys)
    Practice_Forth_Con.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        Practice_Forth_Con.addData('C_Response.rt', C_Response.rt)
    Practice_Forth_Con.addData('C_Response.started', C_Response.tStartRefresh)
    Practice_Forth_Con.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    
    # ------Prepare to start Routine "Blank_3"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text_4.setColor(Feedback_Color, colorSpace='rgb')
    text_4.setText(Feedback)
    # keep track of which components have finished
    Blank_3Components = [Blank_, text_4, text_5]
    for thisComponent in Blank_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Blank_* updates
        if Blank_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank_.frameNStart = frameN  # exact frame index
            Blank_.tStart = t  # local t and not account for scr refresh
            Blank_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank_, 'tStartRefresh')  # time at next scr refresh
            Blank_.setAutoDraw(True)
        if Blank_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank_.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank_.tStop = t  # not accounting for scr refresh
                Blank_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank_, 'tStopRefresh')  # time at next scr refresh
                Blank_.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank_3"-------
    for thisComponent in Blank_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_Forth_Con.addData('Blank_.started', Blank_.tStartRefresh)
    Practice_Forth_Con.addData('Blank_.stopped', Blank_.tStopRefresh)
    Practice_Forth_Con.addData('text_4.started', text_4.tStartRefresh)
    Practice_Forth_Con.addData('text_4.stopped', text_4.tStopRefresh)
    Practice_Forth_Con.addData('text_5.started', text_5.tStartRefresh)
    Practice_Forth_Con.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Practice_Forth_Con'


# ------Prepare to start Routine "Block_iNTS"-------
continueRoutine = True
# update component parameters for each repeat
if Inst_n == 4:
   Block_n = Block_n+1
   Inst_n = 1

if Block_n == 1:
   CON = C1
if Block_n == 2:
   CON = C2
if Block_n == 3:
   CON = C3
if Block_n == 4:
   CON = C4

Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'

print('Phase_ImagePath', Phase_ImagePath)
inst_Image_2.setImage(Phase_ImagePath)
Inst_key_2.keys = []
Inst_key_2.rt = []
_Inst_key_2_allKeys = []
# keep track of which components have finished
Block_iNTSComponents = [inst_Image_2, Inst_key_2]
for thisComponent in Block_iNTSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block_iNTS"-------
while continueRoutine:
    # get current time
    t = Block_iNTSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image_2* updates
    if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image_2.frameNStart = frameN  # exact frame index
        inst_Image_2.tStart = t  # local t and not account for scr refresh
        inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
        inst_Image_2.setAutoDraw(True)
    
    # *Inst_key_2* updates
    if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key_2.frameNStart = frameN  # exact frame index
        Inst_key_2.tStart = t  # local t and not account for scr refresh
        Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
        Inst_key_2.status = STARTED
        # keyboard checking is just starting
        Inst_key_2.clock.reset()  # now t=0
        Inst_key_2.clearEvents(eventType='keyboard')
    if Inst_key_2.status == STARTED:
        theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
        _Inst_key_2_allKeys.extend(theseKeys)
        if len(_Inst_key_2_allKeys):
            Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
            Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_iNTS"-------
for thisComponent in Block_iNTSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Inst_n = Inst_n+1






# check responses
if Inst_key_2.keys in ['', [], None]:  # No response was made
    Inst_key_2.keys = None
thisExp.addData('Inst_key_2.keys',Inst_key_2.keys)
if Inst_key_2.keys != None:  # we had a response
    thisExp.addData('Inst_key_2.rt', Inst_key_2.rt)
thisExp.nextEntry()
# the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Forth_Con = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(con4),
    seed=None, name='Forth_Con')
thisExp.addLoop(Forth_Con)  # add the loop to the experiment
thisForth_Con = Forth_Con.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisForth_Con.rgb)
if thisForth_Con != None:
    for paramName in thisForth_Con:
        exec('{} = thisForth_Con[paramName]'.format(paramName))

for thisForth_Con in Forth_Con:
    currentLoop = Forth_Con
    # abbreviate parameter names if possible (e.g. rgb = thisForth_Con.rgb)
    if thisForth_Con != None:
        for paramName in thisForth_Con:
            exec('{} = thisForth_Con[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition"-------
    continueRoutine = True
    routineTimer.add(3.250000)
    # update component parameters for each repeat
    image.setSize((0.055*image_size, 0.037*image_size))
    image.setOri(image_ori)
    image.setImage(Arrow_Image)
    text_.setText(text_stimulus
)
    C_Response.keys = []
    C_Response.rt = []
    _C_Response_allKeys = []
    if Stim == 'ArrLC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrLF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    if Stim == 'ArrRC':
       Arrow_Image = "EXP_DATA\Arrows\Cutout.png" 
    if Stim == 'ArrRF':
       Arrow_Image = "EXP_DATA\Arrows\Full.png" 
    
    
    # keep track of which components have finished
    ConditionComponents = [Fixation_, image, text_, C_Response]
    for thisComponent in ConditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Condition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ConditionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConditionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_* updates
        if Fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_.frameNStart = frameN  # exact frame index
            Fixation_.tStart = t  # local t and not account for scr refresh
            Fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_, 'tStartRefresh')  # time at next scr refresh
            Fixation_.setAutoDraw(True)
        if Fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_.tStop = t  # not accounting for scr refresh
                Fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_, 'tStopRefresh')  # time at next scr refresh
                Fixation_.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        
        # *C_Response* updates
        waitOnFlip = False
        if C_Response.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            C_Response.frameNStart = frameN  # exact frame index
            C_Response.tStart = t  # local t and not account for scr refresh
            C_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_Response, 'tStartRefresh')  # time at next scr refresh
            C_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(C_Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(C_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if C_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C_Response.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                C_Response.tStop = t  # not accounting for scr refresh
                C_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C_Response, 'tStopRefresh')  # time at next scr refresh
                C_Response.status = FINISHED
        if C_Response.status == STARTED and not waitOnFlip:
            theseKeys = C_Response.getKeys(keyList=['space'], waitRelease=False)
            _C_Response_allKeys.extend(theseKeys)
            if len(_C_Response_allKeys):
                C_Response.keys = _C_Response_allKeys[-1].name  # just the last key pressed
                C_Response.rt = _C_Response_allKeys[-1].rt
                # was this correct?
                if (C_Response.keys == str(CorrAns)) or (C_Response.keys == CorrAns):
                    C_Response.corr = 1
                else:
                    C_Response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition"-------
    for thisComponent in ConditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Forth_Con.addData('Fixation_.started', Fixation_.tStartRefresh)
    Forth_Con.addData('Fixation_.stopped', Fixation_.tStopRefresh)
    Forth_Con.addData('image.started', image.tStartRefresh)
    Forth_Con.addData('image.stopped', image.tStopRefresh)
    Forth_Con.addData('text_.started', text_.tStartRefresh)
    Forth_Con.addData('text_.stopped', text_.tStopRefresh)
    # check responses
    if C_Response.keys in ['', [], None]:  # No response was made
        C_Response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           C_Response.corr = 1;  # correct non-response
        else:
           C_Response.corr = 0;  # failed to respond (incorrectly)
    # store data for Forth_Con (TrialHandler)
    Forth_Con.addData('C_Response.keys',C_Response.keys)
    Forth_Con.addData('C_Response.corr', C_Response.corr)
    if C_Response.keys != None:  # we had a response
        Forth_Con.addData('C_Response.rt', C_Response.rt)
    Forth_Con.addData('C_Response.started', C_Response.tStartRefresh)
    Forth_Con.addData('C_Response.stopped', C_Response.tStopRefresh)
    thisExp.addData('condition',CON)
    #(0.075*image_size, 0.05*image_size)
    
    #Feedback
    
    Feedback_Color = 'green'
    Feedback = ''
    
    if GNG_Type == 'go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'no_go' and C_Response.corr == 1: 
       Feedback = "ןוכנ"
    if GNG_Type == 'go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    if GNG_Type == 'no_go' and C_Response.corr == 0: 
       Feedback = "ןוכנ אל"
       Feedback_Color = 'red'
    
    
    
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'Forth_Con'


# ------Prepare to start Routine "Block_iNTS"-------
continueRoutine = True
# update component parameters for each repeat
if Inst_n == 4:
   Block_n = Block_n+1
   Inst_n = 1

if Block_n == 1:
   CON = C1
if Block_n == 2:
   CON = C2
if Block_n == 3:
   CON = C3
if Block_n == 4:
   CON = C4

Phase_ImagePath = 'EXP_DATA/Instructions/Inst_Image/' + CON + '/' + str(Inst_n) + '.JPG'

print('Phase_ImagePath', Phase_ImagePath)
inst_Image_2.setImage(Phase_ImagePath)
Inst_key_2.keys = []
Inst_key_2.rt = []
_Inst_key_2_allKeys = []
# keep track of which components have finished
Block_iNTSComponents = [inst_Image_2, Inst_key_2]
for thisComponent in Block_iNTSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block_iNTSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block_iNTS"-------
while continueRoutine:
    # get current time
    t = Block_iNTSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block_iNTSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image_2* updates
    if inst_Image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image_2.frameNStart = frameN  # exact frame index
        inst_Image_2.tStart = t  # local t and not account for scr refresh
        inst_Image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image_2, 'tStartRefresh')  # time at next scr refresh
        inst_Image_2.setAutoDraw(True)
    
    # *Inst_key_2* updates
    if Inst_key_2.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key_2.frameNStart = frameN  # exact frame index
        Inst_key_2.tStart = t  # local t and not account for scr refresh
        Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
        Inst_key_2.status = STARTED
        # keyboard checking is just starting
        Inst_key_2.clock.reset()  # now t=0
        Inst_key_2.clearEvents(eventType='keyboard')
    if Inst_key_2.status == STARTED:
        theseKeys = Inst_key_2.getKeys(keyList=None, waitRelease=False)
        _Inst_key_2_allKeys.extend(theseKeys)
        if len(_Inst_key_2_allKeys):
            Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
            Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_iNTSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_iNTS"-------
for thisComponent in Block_iNTSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Inst_n = Inst_n+1






# check responses
if Inst_key_2.keys in ['', [], None]:  # No response was made
    Inst_key_2.keys = None
thisExp.addData('Inst_key_2.keys',Inst_key_2.keys)
if Inst_key_2.keys != None:  # we had a response
    thisExp.addData('Inst_key_2.rt', Inst_key_2.rt)
thisExp.nextEntry()
# the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
inst_ImagePath = "EXP_DATA/Instructions/Inst_Image/" + str(inst_ImageCount) + ".JPG"

inst_Image.setImage(inst_ImagePath)
Inst_key.keys = []
Inst_key.rt = []
_Inst_key_allKeys = []
# keep track of which components have finished
InstructionsComponents = [inst_Image, Inst_key]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image* updates
    if inst_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image.frameNStart = frameN  # exact frame index
        inst_Image.tStart = t  # local t and not account for scr refresh
        inst_Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image, 'tStartRefresh')  # time at next scr refresh
        inst_Image.setAutoDraw(True)
    
    # *Inst_key* updates
    if Inst_key.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key.frameNStart = frameN  # exact frame index
        Inst_key.tStart = t  # local t and not account for scr refresh
        Inst_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key, 'tStartRefresh')  # time at next scr refresh
        Inst_key.status = STARTED
        # keyboard checking is just starting
        Inst_key.clock.reset()  # now t=0
        Inst_key.clearEvents(eventType='keyboard')
    if Inst_key.status == STARTED:
        theseKeys = Inst_key.getKeys(keyList=None, waitRelease=False)
        _Inst_key_allKeys.extend(theseKeys)
        if len(_Inst_key_allKeys):
            Inst_key.keys = _Inst_key_allKeys[-1].name  # just the last key pressed
            Inst_key.rt = _Inst_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
inst_ImageCount = inst_ImageCount+1



# check responses
if Inst_key.keys in ['', [], None]:  # No response was made
    Inst_key.keys = None
thisExp.addData('Inst_key.keys',Inst_key.keys)
if Inst_key.keys != None:  # we had a response
    thisExp.addData('Inst_key.rt', Inst_key.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "_Count_Side"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
OP_Cir1 = 1
OP_Cir2 = 2
OP_Cir3 = 3
OP_Cir4 = 4

fini_text = ''
# keep track of which components have finished
_Count_SideComponents = [Cir1_3, Cir2_3, Cir3_3, Cir4_3, mouse_3, key_resp_8, Fini_text]
for thisComponent in _Count_SideComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_Count_SideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "_Count_Side"-------
while continueRoutine:
    # get current time
    t = _Count_SideClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_Count_SideClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cir1_3* updates
    if Cir1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cir1_3.frameNStart = frameN  # exact frame index
        Cir1_3.tStart = t  # local t and not account for scr refresh
        Cir1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cir1_3, 'tStartRefresh')  # time at next scr refresh
        Cir1_3.setAutoDraw(True)
    if Cir1_3.status == STARTED:  # only update if drawing
        Cir1_3.setOpacity(OP_Cir1, log=False)
    
    # *Cir2_3* updates
    if Cir2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cir2_3.frameNStart = frameN  # exact frame index
        Cir2_3.tStart = t  # local t and not account for scr refresh
        Cir2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cir2_3, 'tStartRefresh')  # time at next scr refresh
        Cir2_3.setAutoDraw(True)
    if Cir2_3.status == STARTED:  # only update if drawing
        Cir2_3.setOpacity(OP_Cir2, log=False)
    
    # *Cir3_3* updates
    if Cir3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cir3_3.frameNStart = frameN  # exact frame index
        Cir3_3.tStart = t  # local t and not account for scr refresh
        Cir3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cir3_3, 'tStartRefresh')  # time at next scr refresh
        Cir3_3.setAutoDraw(True)
    if Cir3_3.status == STARTED:  # only update if drawing
        Cir3_3.setOpacity(OP_Cir3, log=False)
    
    # *Cir4_3* updates
    if Cir4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cir4_3.frameNStart = frameN  # exact frame index
        Cir4_3.tStart = t  # local t and not account for scr refresh
        Cir4_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cir4_3, 'tStartRefresh')  # time at next scr refresh
        Cir4_3.setAutoDraw(True)
    if Cir4_3.status == STARTED:  # only update if drawing
        Cir4_3.setOpacity(OP_Cir4, log=False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=None, waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    buttons = mouse_3.getPressed()
    
    if Cir1_3.contains(mouse_3) and buttons[0]>0:
       OP_Cir1 = 0
       
    if Cir2_3.contains(mouse_3) and buttons[0]>0:
       OP_Cir2 = 0
       
    if Cir3_3.contains(mouse_3) and buttons[0]>0:
       OP_Cir3 = 0
      
    if Cir4_3.contains(mouse_3) and buttons[0]>0:
       OP_Cir4 = 0
    
    if buttons[0]>0:
       Posi = mouse_3.getPos()
       mouse_click_locations.append(Posi)
       print(Posi)
       print(mouse_click_locations)
    
    if OP_Cir1 == 0 and OP_Cir2 == 0 and OP_Cir3 == 0 and OP_Cir4 == 0:
       fini_text = 'לחץ על כל מקש לסיום'
    
    
    # *Fini_text* updates
    if Fini_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Fini_text.frameNStart = frameN  # exact frame index
        Fini_text.tStart = t  # local t and not account for scr refresh
        Fini_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fini_text, 'tStartRefresh')  # time at next scr refresh
        Fini_text.setAutoDraw(True)
    if Fini_text.status == STARTED:  # only update if drawing
        Fini_text.setText(fini_text, log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _Count_SideComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_Count_Side"-------
for thisComponent in _Count_SideComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Cir1_3.started', Cir1_3.tStartRefresh)
thisExp.addData('Cir1_3.stopped', Cir1_3.tStopRefresh)
thisExp.addData('Cir2_3.started', Cir2_3.tStartRefresh)
thisExp.addData('Cir2_3.stopped', Cir2_3.tStopRefresh)
thisExp.addData('Cir3_3.started', Cir3_3.tStartRefresh)
thisExp.addData('Cir3_3.stopped', Cir3_3.tStopRefresh)
thisExp.addData('Cir4_3.started', Cir4_3.tStartRefresh)
thisExp.addData('Cir4_3.stopped', Cir4_3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter([cir1, cir2, cir3, cir4])
        clickableList = [cir1, cir2, cir3, cir4]
    except:
        clickableList = [[cir1, cir2, cir3, cir4]]
    for obj in clickableList:
        if obj.contains(mouse_3):
            gotValidClick = True
            mouse_3.clicked_name.append(obj.name)
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
if len(mouse_3.clicked_name):
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
Counting = ''

if mouse_click_locations[-1][0] > mouse_click_locations[0][0]:
    Counting = 'Left_To_Right'
if mouse_click_locations[-1][0] < mouse_click_locations[0][0]:
    Counting = 'Right_To_Left'

thisExp.addData('Counting',Counting)
# the Routine "_Count_Side" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
inst_ImagePath = "EXP_DATA/Instructions/Inst_Image/" + str(inst_ImageCount) + ".JPG"

inst_Image.setImage(inst_ImagePath)
Inst_key.keys = []
Inst_key.rt = []
_Inst_key_allKeys = []
# keep track of which components have finished
InstructionsComponents = [inst_Image, Inst_key]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_Image* updates
    if inst_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_Image.frameNStart = frameN  # exact frame index
        inst_Image.tStart = t  # local t and not account for scr refresh
        inst_Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_Image, 'tStartRefresh')  # time at next scr refresh
        inst_Image.setAutoDraw(True)
    
    # *Inst_key* updates
    if Inst_key.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        Inst_key.frameNStart = frameN  # exact frame index
        Inst_key.tStart = t  # local t and not account for scr refresh
        Inst_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key, 'tStartRefresh')  # time at next scr refresh
        Inst_key.status = STARTED
        # keyboard checking is just starting
        Inst_key.clock.reset()  # now t=0
        Inst_key.clearEvents(eventType='keyboard')
    if Inst_key.status == STARTED:
        theseKeys = Inst_key.getKeys(keyList=None, waitRelease=False)
        _Inst_key_allKeys.extend(theseKeys)
        if len(_Inst_key_allKeys):
            Inst_key.keys = _Inst_key_allKeys[-1].name  # just the last key pressed
            Inst_key.rt = _Inst_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
inst_ImageCount = inst_ImageCount+1



# check responses
if Inst_key.keys in ['', [], None]:  # No response was made
    Inst_key.keys = None
thisExp.addData('Inst_key.keys',Inst_key.keys)
if Inst_key.keys != None:  # we had a response
    thisExp.addData('Inst_key.rt', Inst_key.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
