#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on February 26, 2021, at 11:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'thesis berry'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\kemal\\Desktop\\Thesis Master Doc\\Final Berry Thesis amended\\thesis berry.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "master_code"
master_codeClock = core.Clock()
#experiment settings 

# change if you want different keys.
# DO NOT FORGET TO CHANGE RESPONSE KEYS AFTERWARDS. 
eat = "f" 
fast = "j"

#numbers of trial/blocks. 
num_blocks = 4
# -1 is for accuracy. Change the LEFT number.
num_trials = 31 - 1

#General Health Bar settings 
BG_width = 0.6
BG_height = 0.05

# variable holders
berry_img = []

#Acronyms: 
#TR = Train, TS = Test
#HB = Health Bar, BG = Background
#FC = Fix Cross
#HL = highlight

#health bar settings for Training
TR_HB_Colour = "green" 
TR_HB_Line_Colour = "black"
TR_HB_BG_Colour = "white"
TR_HB_BG_Line_Colour = "black"
Train_HB_Width = 0.0

#health bar settings for Testing
TS_HB_Colour = "green" 
TS_HB_Line_Colour = "black"
TS_HB_BG_Colour = "white"
TS_HB_BG_Line_Colour = "black"
Test_HB_Width = 0.0

#health bar settings for Testing2
TS2_HB_Colour = "green" 
TS2_HB_Line_Colour = "black"
TS2_HB_BG_Colour = "white"
TS2_HB_BG_Line_Colour = "black"
Test2_HB_Width = 0.0

# Initialize components for Routine "info_1_card"
info_1_cardClock = core.Clock()
info1_img = visual.ImageStim(
    win=win,
    name='info1_img', 
    image='info1.png', mask=None,
    ori=0, pos=(0, 0.05), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
info1_resp = keyboard.Keyboard()
info1_txt = visual.TextStim(win=win, name='info1_txt',
    text='press "space" to continue.',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "info_2_card"
info_2_cardClock = core.Clock()
info2_img = visual.ImageStim(
    win=win,
    name='info2_img', 
    image='info2.png', mask=None,
    ori=0, pos=(0, 0.05), size=(0.90, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
info2_resp = keyboard.Keyboard()
info2_text = visual.TextStim(win=win, name='info2_text',
    text='press "space" to continue.',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "info_3_card"
info_3_cardClock = core.Clock()
info3_img = visual.ImageStim(
    win=win,
    name='info3_img', 
    image='info3.png', mask=None,
    ori=0, pos=(0, 0.05), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
info3_resp = keyboard.Keyboard()
info3_text = visual.TextStim(win=win, name='info3_text',
    text='press "space" to continue.',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "info_4_card"
info_4_cardClock = core.Clock()
info4_img = visual.ImageStim(
    win=win,
    name='info4_img', 
    image='info4.png', mask=None,
    ori=0, pos=(0, 0.05), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
info4_resp = keyboard.Keyboard()
info4_txt = visual.TextStim(win=win, name='info4_txt',
    text='press "space" to continue.',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "consent_card"
consent_cardClock = core.Clock()
consent_rep = 0
consent_img = visual.ImageStim(
    win=win,
    name='consent_img', 
    image='consent1.png', mask=None,
    ori=0, pos=(0, 0.05), size=(1, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
consent_resp = keyboard.Keyboard()
consent_text = visual.TextStim(win=win, name='consent_text',
    text='press "y" if you consent.\npress "n" if you do NOT consent.\n\n',
    font='Arial',
    pos=(0, -0.46), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "consent_corrector"
consent_correctorClock = core.Clock()

# Initialize components for Routine "welcome_card"
welcome_cardClock = core.Clock()
wlcm_text = visual.TextStim(win=win, name='wlcm_text',
    text='welcome to the experiment.\n\npress "space" to continue',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wlcm_resp = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
buffer_500 = visual.TextStim(win=win, name='buffer_500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "train_info_card"
train_info_cardClock = core.Clock()
info_text = visual.TextStim(win=win, name='info_text',
    text='You will see berries. \nResponses are through your keyboard clicks.\n\nPlease Decide whether to;\nEAT "F", or FAST "J". \n\nCorrect answers increase the health-bar to the right (green)\nIncorrect answers increase the health-bar to the left (red)\n\npress "space" to start',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
info_resp = keyboard.Keyboard()

# Initialize components for Routine "train_HB_reset"
train_HB_resetClock = core.Clock()

# Initialize components for Routine "train_code"
train_codeClock = core.Clock()
#monki brain#

#imported libraries
import random


#variables to prevent crashing
trtcorrRep = 0 
trtincorrRep = 0
TrainCorrANS = ""
tr_xpos = 0

# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
FC_TR_HB_BG = visual.Rect(
    win=win, name='FC_TR_HB_BG',
    width=(BG_width, BG_height)[0], height=(BG_width, BG_height)[1],
    ori=0, pos=(0, 0.25),
    lineWidth=1, lineColor=TR_HB_BG_Line_Colour, lineColorSpace='rgb',
    fillColor=TR_HB_BG_Colour, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
FC_TR_HB_DYN = visual.Rect(
    win=win, name='FC_TR_HB_DYN',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=TR_HB_Line_Colour, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
TR_FC = visual.ShapeStim(
    win=win, name='TR_FC', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "training"
trainingClock = core.Clock()
Train_HB_BG = visual.Rect(
    win=win, name='Train_HB_BG',
    width=(BG_width, 0.05)[0], height=(BG_width, 0.05)[1],
    ori=0, pos=(0, 0.25),
    lineWidth=1, lineColor=TR_HB_BG_Line_Colour, lineColorSpace='rgb',
    fillColor=TR_HB_BG_Colour, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Train_HB_DYN = visual.Rect(
    win=win, name='Train_HB_DYN',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=TR_HB_Line_Colour, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
train_berry_image = visual.ImageStim(
    win=win,
    name='train_berry_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
train_berry_resp = keyboard.Keyboard()
eat_tr_text = visual.TextStim(win=win, name='eat_tr_text',
    text='EAT',
    font='Arial',
    pos=(-0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
fast_tr_text = visual.TextStim(win=win, name='fast_tr_text',
    text='FAST',
    font='Arial',
    pos=(0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "tr_hl_disp"
tr_hl_dispClock = core.Clock()
HL_TR_HB_BG = visual.Rect(
    win=win, name='HL_TR_HB_BG',
    width=(BG_width, BG_height)[0], height=(BG_width, BG_height)[1],
    ori=0, pos=(0, 0.25),
    lineWidth=1, lineColor=TR_HB_BG_Line_Colour, lineColorSpace='rgb',
    fillColor=TR_HB_BG_Colour, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
HL_TR_HB_DYN = visual.Rect(
    win=win, name='HL_TR_HB_DYN',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=TR_HB_Line_Colour, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
tr_eat_hl_text = visual.TextStim(win=win, name='tr_eat_hl_text',
    text='EAT',
    font='Arial',
    pos=(-0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
tr_fast_hl_text = visual.TextStim(win=win, name='tr_fast_hl_text',
    text='FAST',
    font='Arial',
    pos=(0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "tr_corrector_code"
tr_corrector_codeClock = core.Clock()

# Initialize components for Routine "train_block_counter"
train_block_counterClock = core.Clock()
train_block_text = visual.TextStim(win=win, name='train_block_text',
    text='you finished the block \n\npress "space" to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
block_skip = keyboard.Keyboard()

# Initialize components for Routine "train_end_card"
train_end_cardClock = core.Clock()
TR_end_txt = visual.TextStim(win=win, name='TR_end_txt',
    text='You have finished the training task.\n\npress "space" to continue. ',
    font='Arial',
    pos=(0, 0.0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
TR_end_cont = keyboard.Keyboard()

# Initialize components for Routine "test_info_card"
test_info_cardClock = core.Clock()
test_info_txt = visual.TextStim(win=win, name='test_info_txt',
    text='You will once again see berries. \n\nAgain, decide whether to;\nEAT ("F"), or FAST ("J"). \n\npress "space" to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
test_info_skip = keyboard.Keyboard()

# Initialize components for Routine "HB_reset_test"
HB_reset_testClock = core.Clock()

# Initialize components for Routine "test_code"
test_codeClock = core.Clock()
#variable holders to prevent crashing. 
ts_xpos = 0

# Initialize components for Routine "ts_fix_cross"
ts_fix_crossClock = core.Clock()
ts_FC = visual.ShapeStim(
    win=win, name='ts_FC', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "test"
testClock = core.Clock()
test_berry_img = visual.ImageStim(
    win=win,
    name='test_berry_img', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test_berry_resp = keyboard.Keyboard()
eat_ts_text = visual.TextStim(win=win, name='eat_ts_text',
    text='EAT',
    font='Arial',
    pos=(-0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
fast_ts_text = visual.TextStim(win=win, name='fast_ts_text',
    text='FAST',
    font='Arial',
    pos=(0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ts1_hl_disp"
ts1_hl_dispClock = core.Clock()
ts_eat_hl_text = visual.TextStim(win=win, name='ts_eat_hl_text',
    text='EAT',
    font='Arial',
    pos=(-0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ts_fast_hl_text = visual.TextStim(win=win, name='ts_fast_hl_text',
    text='FAST',
    font='Arial',
    pos=(0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ts_corrector_code"
ts_corrector_codeClock = core.Clock()

# Initialize components for Routine "test_block_counter"
test_block_counterClock = core.Clock()
TS_block_text = visual.TextStim(win=win, name='TS_block_text',
    text='You have finished this block.\n\npress "space" to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
TS_block_skip = keyboard.Keyboard()

# Initialize components for Routine "end_card"
end_cardClock = core.Clock()
first_section_end_txt = visual.TextStim(win=win, name='first_section_end_txt',
    text='You have finished the first half of the experiment.\n\nPress space to continue to the next section.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
first_section_end_resp = keyboard.Keyboard()

# Initialize components for Routine "test_2_info_card"
test_2_info_cardClock = core.Clock()
quiescence_txt = visual.TextStim(win=win, name='quiescence_txt',
    text='We would like you to close your eyes and relax\nfor 5 minutes. \nYou will hear a sound when 5 minutes have passed. \n\nYou will be able to press "space" to continue after 5 minutes.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
quiescence_resp = keyboard.Keyboard()
sound_1 = sound.Sound('Computer_Magic-Microsift-1901299923.wav', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)

# Initialize components for Routine "test_2_proc_card"
test_2_proc_cardClock = core.Clock()
test2_proc_text = visual.TextStim(win=win, name='test2_proc_text',
    text='Thank you for your patience. \n\nYou will once again see berries and decide whether:\n to eat("F") or fast("J").\n\npress "space" to start',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
test2_proc_resp = keyboard.Keyboard()

# Initialize components for Routine "test2_HB_reset"
test2_HB_resetClock = core.Clock()

# Initialize components for Routine "test2_code"
test2_codeClock = core.Clock()
#holder to prevent crash
ts2_xpos = 0

# Initialize components for Routine "ts2_fix_cross"
ts2_fix_crossClock = core.Clock()
TS2_FC = visual.ShapeStim(
    win=win, name='TS2_FC', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "test2"
test2Clock = core.Clock()
test2_berry_img = visual.ImageStim(
    win=win,
    name='test2_berry_img', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test2_berry_resp = keyboard.Keyboard()
ts2_eat_txt = visual.TextStim(win=win, name='ts2_eat_txt',
    text='EAT',
    font='Arial',
    pos=(-0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ts2_fast_txt = visual.TextStim(win=win, name='ts2_fast_txt',
    text='FAST',
    font='Arial',
    pos=(0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ts2_hl_disp"
ts2_hl_dispClock = core.Clock()
ts2_eat_hl_text = visual.TextStim(win=win, name='ts2_eat_hl_text',
    text='EAT',
    font='Arial',
    pos=(-0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ts2_fast_hl_text = visual.TextStim(win=win, name='ts2_fast_hl_text',
    text='FAST',
    font='Arial',
    pos=(0.4, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ts2_corrector_code"
ts2_corrector_codeClock = core.Clock()

# Initialize components for Routine "ts2_block_counter"
ts2_block_counterClock = core.Clock()
ts2_block_txt = visual.TextStim(win=win, name='ts2_block_txt',
    text='you have finished this block. \n\npress "space" to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
test2_block_resp = keyboard.Keyboard()

# Initialize components for Routine "full_finish"
full_finishClock = core.Clock()
finish_text = visual.TextStim(win=win, name='finish_text',
    text='You have finished the experiment.\n\npress "space" to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finish_resp = keyboard.Keyboard()

# Initialize components for Routine "debrief_1_card"
debrief_1_cardClock = core.Clock()
debrief1_img = visual.ImageStim(
    win=win,
    name='debrief1_img', 
    image='debrief1.png', mask=None,
    ori=0, pos=(0, 0.05), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
debrief1_text = visual.TextStim(win=win, name='debrief1_text',
    text='press "space" to continue',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
debrief1_resp = keyboard.Keyboard()

# Initialize components for Routine "debrief_2_card"
debrief_2_cardClock = core.Clock()
debrief2_img = visual.ImageStim(
    win=win,
    name='debrief2_img', 
    image='debrief2.png', mask=None,
    ori=0, pos=(0, 0.05), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
debrief2_text = visual.TextStim(win=win, name='debrief2_text',
    text='press "space" to continue.',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
debrief2_resp = keyboard.Keyboard()

# Initialize components for Routine "end_card_2"
end_card_2Clock = core.Clock()
end_txt = visual.TextStim(win=win, name='end_txt',
    text='You have finished the experiment. \n\nthank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "master_code"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
master_codeComponents = []
for thisComponent in master_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
master_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "master_code"-------
while continueRoutine:
    # get current time
    t = master_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=master_codeClock)
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
    for thisComponent in master_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "master_code"-------
for thisComponent in master_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "master_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "info_1_card"-------
continueRoutine = True
# update component parameters for each repeat
info1_resp.keys = []
info1_resp.rt = []
_info1_resp_allKeys = []
# keep track of which components have finished
info_1_cardComponents = [info1_img, info1_resp, info1_txt]
for thisComponent in info_1_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
info_1_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "info_1_card"-------
while continueRoutine:
    # get current time
    t = info_1_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=info_1_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info1_img* updates
    if info1_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info1_img.frameNStart = frameN  # exact frame index
        info1_img.tStart = t  # local t and not account for scr refresh
        info1_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info1_img, 'tStartRefresh')  # time at next scr refresh
        info1_img.setAutoDraw(True)
    
    # *info1_resp* updates
    waitOnFlip = False
    if info1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info1_resp.frameNStart = frameN  # exact frame index
        info1_resp.tStart = t  # local t and not account for scr refresh
        info1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info1_resp, 'tStartRefresh')  # time at next scr refresh
        info1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(info1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(info1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if info1_resp.status == STARTED and not waitOnFlip:
        theseKeys = info1_resp.getKeys(keyList=['space'], waitRelease=False)
        _info1_resp_allKeys.extend(theseKeys)
        if len(_info1_resp_allKeys):
            info1_resp.keys = _info1_resp_allKeys[-1].name  # just the last key pressed
            info1_resp.rt = _info1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *info1_txt* updates
    if info1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info1_txt.frameNStart = frameN  # exact frame index
        info1_txt.tStart = t  # local t and not account for scr refresh
        info1_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info1_txt, 'tStartRefresh')  # time at next scr refresh
        info1_txt.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info_1_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "info_1_card"-------
for thisComponent in info_1_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('info1_img.started', info1_img.tStartRefresh)
thisExp.addData('info1_img.stopped', info1_img.tStopRefresh)
# check responses
if info1_resp.keys in ['', [], None]:  # No response was made
    info1_resp.keys = None
thisExp.addData('info1_resp.keys',info1_resp.keys)
if info1_resp.keys != None:  # we had a response
    thisExp.addData('info1_resp.rt', info1_resp.rt)
thisExp.addData('info1_resp.started', info1_resp.tStartRefresh)
thisExp.addData('info1_resp.stopped', info1_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('info1_txt.started', info1_txt.tStartRefresh)
thisExp.addData('info1_txt.stopped', info1_txt.tStopRefresh)
# the Routine "info_1_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "info_2_card"-------
continueRoutine = True
# update component parameters for each repeat
info2_resp.keys = []
info2_resp.rt = []
_info2_resp_allKeys = []
# keep track of which components have finished
info_2_cardComponents = [info2_img, info2_resp, info2_text]
for thisComponent in info_2_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
info_2_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "info_2_card"-------
while continueRoutine:
    # get current time
    t = info_2_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=info_2_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info2_img* updates
    if info2_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info2_img.frameNStart = frameN  # exact frame index
        info2_img.tStart = t  # local t and not account for scr refresh
        info2_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info2_img, 'tStartRefresh')  # time at next scr refresh
        info2_img.setAutoDraw(True)
    
    # *info2_resp* updates
    waitOnFlip = False
    if info2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info2_resp.frameNStart = frameN  # exact frame index
        info2_resp.tStart = t  # local t and not account for scr refresh
        info2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info2_resp, 'tStartRefresh')  # time at next scr refresh
        info2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(info2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(info2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if info2_resp.status == STARTED and not waitOnFlip:
        theseKeys = info2_resp.getKeys(keyList=['space'], waitRelease=False)
        _info2_resp_allKeys.extend(theseKeys)
        if len(_info2_resp_allKeys):
            info2_resp.keys = _info2_resp_allKeys[-1].name  # just the last key pressed
            info2_resp.rt = _info2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *info2_text* updates
    if info2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info2_text.frameNStart = frameN  # exact frame index
        info2_text.tStart = t  # local t and not account for scr refresh
        info2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info2_text, 'tStartRefresh')  # time at next scr refresh
        info2_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info_2_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "info_2_card"-------
for thisComponent in info_2_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('info2_img.started', info2_img.tStartRefresh)
thisExp.addData('info2_img.stopped', info2_img.tStopRefresh)
# check responses
if info2_resp.keys in ['', [], None]:  # No response was made
    info2_resp.keys = None
thisExp.addData('info2_resp.keys',info2_resp.keys)
if info2_resp.keys != None:  # we had a response
    thisExp.addData('info2_resp.rt', info2_resp.rt)
thisExp.addData('info2_resp.started', info2_resp.tStartRefresh)
thisExp.addData('info2_resp.stopped', info2_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('info2_text.started', info2_text.tStartRefresh)
thisExp.addData('info2_text.stopped', info2_text.tStopRefresh)
# the Routine "info_2_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "info_3_card"-------
continueRoutine = True
# update component parameters for each repeat
info3_resp.keys = []
info3_resp.rt = []
_info3_resp_allKeys = []
# keep track of which components have finished
info_3_cardComponents = [info3_img, info3_resp, info3_text]
for thisComponent in info_3_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
info_3_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "info_3_card"-------
while continueRoutine:
    # get current time
    t = info_3_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=info_3_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info3_img* updates
    if info3_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info3_img.frameNStart = frameN  # exact frame index
        info3_img.tStart = t  # local t and not account for scr refresh
        info3_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info3_img, 'tStartRefresh')  # time at next scr refresh
        info3_img.setAutoDraw(True)
    
    # *info3_resp* updates
    waitOnFlip = False
    if info3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info3_resp.frameNStart = frameN  # exact frame index
        info3_resp.tStart = t  # local t and not account for scr refresh
        info3_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info3_resp, 'tStartRefresh')  # time at next scr refresh
        info3_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(info3_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(info3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if info3_resp.status == STARTED and not waitOnFlip:
        theseKeys = info3_resp.getKeys(keyList=['space'], waitRelease=False)
        _info3_resp_allKeys.extend(theseKeys)
        if len(_info3_resp_allKeys):
            info3_resp.keys = _info3_resp_allKeys[-1].name  # just the last key pressed
            info3_resp.rt = _info3_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *info3_text* updates
    if info3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info3_text.frameNStart = frameN  # exact frame index
        info3_text.tStart = t  # local t and not account for scr refresh
        info3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info3_text, 'tStartRefresh')  # time at next scr refresh
        info3_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info_3_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "info_3_card"-------
for thisComponent in info_3_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('info3_img.started', info3_img.tStartRefresh)
thisExp.addData('info3_img.stopped', info3_img.tStopRefresh)
# check responses
if info3_resp.keys in ['', [], None]:  # No response was made
    info3_resp.keys = None
thisExp.addData('info3_resp.keys',info3_resp.keys)
if info3_resp.keys != None:  # we had a response
    thisExp.addData('info3_resp.rt', info3_resp.rt)
thisExp.addData('info3_resp.started', info3_resp.tStartRefresh)
thisExp.addData('info3_resp.stopped', info3_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('info3_text.started', info3_text.tStartRefresh)
thisExp.addData('info3_text.stopped', info3_text.tStopRefresh)
# the Routine "info_3_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "info_4_card"-------
continueRoutine = True
# update component parameters for each repeat
info4_resp.keys = []
info4_resp.rt = []
_info4_resp_allKeys = []
# keep track of which components have finished
info_4_cardComponents = [info4_img, info4_resp, info4_txt]
for thisComponent in info_4_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
info_4_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "info_4_card"-------
while continueRoutine:
    # get current time
    t = info_4_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=info_4_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info4_img* updates
    if info4_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info4_img.frameNStart = frameN  # exact frame index
        info4_img.tStart = t  # local t and not account for scr refresh
        info4_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info4_img, 'tStartRefresh')  # time at next scr refresh
        info4_img.setAutoDraw(True)
    
    # *info4_resp* updates
    waitOnFlip = False
    if info4_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info4_resp.frameNStart = frameN  # exact frame index
        info4_resp.tStart = t  # local t and not account for scr refresh
        info4_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info4_resp, 'tStartRefresh')  # time at next scr refresh
        info4_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(info4_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(info4_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if info4_resp.status == STARTED and not waitOnFlip:
        theseKeys = info4_resp.getKeys(keyList=['space'], waitRelease=False)
        _info4_resp_allKeys.extend(theseKeys)
        if len(_info4_resp_allKeys):
            info4_resp.keys = _info4_resp_allKeys[-1].name  # just the last key pressed
            info4_resp.rt = _info4_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *info4_txt* updates
    if info4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info4_txt.frameNStart = frameN  # exact frame index
        info4_txt.tStart = t  # local t and not account for scr refresh
        info4_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info4_txt, 'tStartRefresh')  # time at next scr refresh
        info4_txt.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info_4_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "info_4_card"-------
for thisComponent in info_4_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('info4_img.started', info4_img.tStartRefresh)
thisExp.addData('info4_img.stopped', info4_img.tStopRefresh)
# check responses
if info4_resp.keys in ['', [], None]:  # No response was made
    info4_resp.keys = None
thisExp.addData('info4_resp.keys',info4_resp.keys)
if info4_resp.keys != None:  # we had a response
    thisExp.addData('info4_resp.rt', info4_resp.rt)
thisExp.addData('info4_resp.started', info4_resp.tStartRefresh)
thisExp.addData('info4_resp.stopped', info4_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('info4_txt.started', info4_txt.tStartRefresh)
thisExp.addData('info4_txt.stopped', info4_txt.tStopRefresh)
# the Routine "info_4_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "consent_card"-------
continueRoutine = True
# update component parameters for each repeat
consent_resp.keys = []
consent_resp.rt = []
_consent_resp_allKeys = []
# keep track of which components have finished
consent_cardComponents = [consent_img, consent_resp, consent_text]
for thisComponent in consent_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consent_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent_card"-------
while continueRoutine:
    # get current time
    t = consent_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consent_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consent_img* updates
    if consent_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_img.frameNStart = frameN  # exact frame index
        consent_img.tStart = t  # local t and not account for scr refresh
        consent_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_img, 'tStartRefresh')  # time at next scr refresh
        consent_img.setAutoDraw(True)
    
    # *consent_resp* updates
    waitOnFlip = False
    if consent_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_resp.frameNStart = frameN  # exact frame index
        consent_resp.tStart = t  # local t and not account for scr refresh
        consent_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_resp, 'tStartRefresh')  # time at next scr refresh
        consent_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(consent_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(consent_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if consent_resp.status == STARTED and not waitOnFlip:
        theseKeys = consent_resp.getKeys(keyList=['y', 'n'], waitRelease=False)
        _consent_resp_allKeys.extend(theseKeys)
        if len(_consent_resp_allKeys):
            consent_resp.keys = _consent_resp_allKeys[-1].name  # just the last key pressed
            consent_resp.rt = _consent_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *consent_text* updates
    if consent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_text.frameNStart = frameN  # exact frame index
        consent_text.tStart = t  # local t and not account for scr refresh
        consent_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_text, 'tStartRefresh')  # time at next scr refresh
        consent_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consent_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent_card"-------
for thisComponent in consent_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('consent_img.started', consent_img.tStartRefresh)
thisExp.addData('consent_img.stopped', consent_img.tStopRefresh)
# check responses
if consent_resp.keys in ['', [], None]:  # No response was made
    consent_resp.keys = None
thisExp.addData('consent_resp.keys',consent_resp.keys)
if consent_resp.keys != None:  # we had a response
    thisExp.addData('consent_resp.rt', consent_resp.rt)
thisExp.addData('consent_resp.started', consent_resp.tStartRefresh)
thisExp.addData('consent_resp.stopped', consent_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('consent_text.started', consent_text.tStartRefresh)
thisExp.addData('consent_text.stopped', consent_text.tStopRefresh)
# the Routine "consent_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "consent_corrector"-------
continueRoutine = True
# update component parameters for each repeat
if consent_resp.keys == 'y':
    consent_rep = 1
elif consent_resp.keys == 'n':
    consent_rep = 0
# keep track of which components have finished
consent_correctorComponents = []
for thisComponent in consent_correctorComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consent_correctorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent_corrector"-------
while continueRoutine:
    # get current time
    t = consent_correctorClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consent_correctorClock)
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
    for thisComponent in consent_correctorComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent_corrector"-------
for thisComponent in consent_correctorComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "consent_corrector" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
consent_check = data.TrialHandler(nReps=consent_rep, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='consent_check')
thisExp.addLoop(consent_check)  # add the loop to the experiment
thisConsent_check = consent_check.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConsent_check.rgb)
if thisConsent_check != None:
    for paramName in thisConsent_check:
        exec('{} = thisConsent_check[paramName]'.format(paramName))

for thisConsent_check in consent_check:
    currentLoop = consent_check
    # abbreviate parameter names if possible (e.g. rgb = thisConsent_check.rgb)
    if thisConsent_check != None:
        for paramName in thisConsent_check:
            exec('{} = thisConsent_check[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "welcome_card"-------
    continueRoutine = True
    # update component parameters for each repeat
    wlcm_resp.keys = []
    wlcm_resp.rt = []
    _wlcm_resp_allKeys = []
    # keep track of which components have finished
    welcome_cardComponents = [wlcm_text, wlcm_resp]
    for thisComponent in welcome_cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    welcome_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "welcome_card"-------
    while continueRoutine:
        # get current time
        t = welcome_cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=welcome_cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wlcm_text* updates
        if wlcm_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wlcm_text.frameNStart = frameN  # exact frame index
            wlcm_text.tStart = t  # local t and not account for scr refresh
            wlcm_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wlcm_text, 'tStartRefresh')  # time at next scr refresh
            wlcm_text.setAutoDraw(True)
        
        # *wlcm_resp* updates
        waitOnFlip = False
        if wlcm_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wlcm_resp.frameNStart = frameN  # exact frame index
            wlcm_resp.tStart = t  # local t and not account for scr refresh
            wlcm_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wlcm_resp, 'tStartRefresh')  # time at next scr refresh
            wlcm_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wlcm_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wlcm_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wlcm_resp.status == STARTED and not waitOnFlip:
            theseKeys = wlcm_resp.getKeys(keyList=['space'], waitRelease=False)
            _wlcm_resp_allKeys.extend(theseKeys)
            if len(_wlcm_resp_allKeys):
                wlcm_resp.keys = _wlcm_resp_allKeys[-1].name  # just the last key pressed
                wlcm_resp.rt = _wlcm_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome_cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "welcome_card"-------
    for thisComponent in welcome_cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('wlcm_text.started', wlcm_text.tStartRefresh)
    consent_check.addData('wlcm_text.stopped', wlcm_text.tStopRefresh)
    # check responses
    if wlcm_resp.keys in ['', [], None]:  # No response was made
        wlcm_resp.keys = None
    consent_check.addData('wlcm_resp.keys',wlcm_resp.keys)
    if wlcm_resp.keys != None:  # we had a response
        consent_check.addData('wlcm_resp.rt', wlcm_resp.rt)
    consent_check.addData('wlcm_resp.started', wlcm_resp.tStartRefresh)
    consent_check.addData('wlcm_resp.stopped', wlcm_resp.tStopRefresh)
    # the Routine "welcome_card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [buffer_500]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *buffer_500* updates
        if buffer_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buffer_500.frameNStart = frameN  # exact frame index
            buffer_500.tStart = t  # local t and not account for scr refresh
            buffer_500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buffer_500, 'tStartRefresh')  # time at next scr refresh
            buffer_500.setAutoDraw(True)
        if buffer_500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buffer_500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                buffer_500.tStop = t  # not accounting for scr refresh
                buffer_500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(buffer_500, 'tStopRefresh')  # time at next scr refresh
                buffer_500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('buffer_500.started', buffer_500.tStartRefresh)
    consent_check.addData('buffer_500.stopped', buffer_500.tStopRefresh)
    
    # ------Prepare to start Routine "train_info_card"-------
    continueRoutine = True
    # update component parameters for each repeat
    info_resp.keys = []
    info_resp.rt = []
    _info_resp_allKeys = []
    # keep track of which components have finished
    train_info_cardComponents = [info_text, info_resp]
    for thisComponent in train_info_cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    train_info_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "train_info_card"-------
    while continueRoutine:
        # get current time
        t = train_info_cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=train_info_cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *info_text* updates
        if info_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            info_text.frameNStart = frameN  # exact frame index
            info_text.tStart = t  # local t and not account for scr refresh
            info_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_text, 'tStartRefresh')  # time at next scr refresh
            info_text.setAutoDraw(True)
        
        # *info_resp* updates
        waitOnFlip = False
        if info_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            info_resp.frameNStart = frameN  # exact frame index
            info_resp.tStart = t  # local t and not account for scr refresh
            info_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_resp, 'tStartRefresh')  # time at next scr refresh
            info_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(info_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(info_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if info_resp.status == STARTED and not waitOnFlip:
            theseKeys = info_resp.getKeys(keyList=['space'], waitRelease=False)
            _info_resp_allKeys.extend(theseKeys)
            if len(_info_resp_allKeys):
                info_resp.keys = _info_resp_allKeys[-1].name  # just the last key pressed
                info_resp.rt = _info_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in train_info_cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "train_info_card"-------
    for thisComponent in train_info_cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('info_text.started', info_text.tStartRefresh)
    consent_check.addData('info_text.stopped', info_text.tStopRefresh)
    # check responses
    if info_resp.keys in ['', [], None]:  # No response was made
        info_resp.keys = None
    consent_check.addData('info_resp.keys',info_resp.keys)
    if info_resp.keys != None:  # we had a response
        consent_check.addData('info_resp.rt', info_resp.rt)
    consent_check.addData('info_resp.started', info_resp.tStartRefresh)
    consent_check.addData('info_resp.stopped', info_resp.tStopRefresh)
    # the Routine "train_info_card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    train_blocks = data.TrialHandler(nReps=num_blocks, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='train_blocks')
    thisExp.addLoop(train_blocks)  # add the loop to the experiment
    thisTrain_block = train_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_block.rgb)
    if thisTrain_block != None:
        for paramName in thisTrain_block:
            exec('{} = thisTrain_block[paramName]'.format(paramName))
    
    for thisTrain_block in train_blocks:
        currentLoop = train_blocks
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_block.rgb)
        if thisTrain_block != None:
            for paramName in thisTrain_block:
                exec('{} = thisTrain_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "train_HB_reset"-------
        continueRoutine = True
        # update component parameters for each repeat
        Train_HB_Width = 0
        tr_xpos = 0
        # keep track of which components have finished
        train_HB_resetComponents = []
        for thisComponent in train_HB_resetComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        train_HB_resetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "train_HB_reset"-------
        while continueRoutine:
            # get current time
            t = train_HB_resetClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=train_HB_resetClock)
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
            for thisComponent in train_HB_resetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "train_HB_reset"-------
        for thisComponent in train_HB_resetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "train_HB_reset" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        train_trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('train-data-holder.xlsx'),
            seed=None, name='train_trials')
        thisExp.addLoop(train_trials)  # add the loop to the experiment
        thisTrain_trial = train_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_trial.rgb)
        if thisTrain_trial != None:
            for paramName in thisTrain_trial:
                exec('{} = thisTrain_trial[paramName]'.format(paramName))
        
        for thisTrain_trial in train_trials:
            currentLoop = train_trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrain_trial.rgb)
            if thisTrain_trial != None:
                for paramName in thisTrain_trial:
                    exec('{} = thisTrain_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "train_code"-------
            continueRoutine = True
            # update component parameters for each repeat
            #randomly decide whether its eat or fast.
            #create a random interger (number) between 0-1.
            #compare to percentage from excel file.
            
            ##rand_num = random.randint(1, 10) / 10
            
            ##if rand_num <= TrainPercCorrAns:
            ##    TrainCorrANS = eat
            ##else:
            ##    TrainCorrANS = fast
            # keep track of which components have finished
            train_codeComponents = []
            for thisComponent in train_codeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            train_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "train_code"-------
            while continueRoutine:
                # get current time
                t = train_codeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=train_codeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #Health Bar Code 
                #Make big or small depending on answer.
                if train_berry_resp.corr:
                    Train_HB_Width += 0.01
                    tr_xpos += 0.01/2
                else:
                    Train_HB_Width -= 0.01
                    tr_xpos -= 0.01/2
                
                #decide whether if the participant is 
                #in correct direction or not.
                if Train_HB_Width >= 0.01:
                    TR_HB_Colour = "green"
                elif Train_HB_Width <= 0.01:
                    TR_HB_Colour = "red"
                
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in train_codeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "train_code"-------
            for thisComponent in train_codeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "train_code" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "fix_cross"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            fix_crossComponents = [FC_TR_HB_BG, FC_TR_HB_DYN, TR_FC]
            for thisComponent in fix_crossComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            fix_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "fix_cross"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = fix_crossClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=fix_crossClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *FC_TR_HB_BG* updates
                if FC_TR_HB_BG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FC_TR_HB_BG.frameNStart = frameN  # exact frame index
                    FC_TR_HB_BG.tStart = t  # local t and not account for scr refresh
                    FC_TR_HB_BG.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FC_TR_HB_BG, 'tStartRefresh')  # time at next scr refresh
                    FC_TR_HB_BG.setAutoDraw(True)
                if FC_TR_HB_BG.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > FC_TR_HB_BG.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        FC_TR_HB_BG.tStop = t  # not accounting for scr refresh
                        FC_TR_HB_BG.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(FC_TR_HB_BG, 'tStopRefresh')  # time at next scr refresh
                        FC_TR_HB_BG.setAutoDraw(False)
                
                # *FC_TR_HB_DYN* updates
                if FC_TR_HB_DYN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FC_TR_HB_DYN.frameNStart = frameN  # exact frame index
                    FC_TR_HB_DYN.tStart = t  # local t and not account for scr refresh
                    FC_TR_HB_DYN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FC_TR_HB_DYN, 'tStartRefresh')  # time at next scr refresh
                    FC_TR_HB_DYN.setAutoDraw(True)
                if FC_TR_HB_DYN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > FC_TR_HB_DYN.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        FC_TR_HB_DYN.tStop = t  # not accounting for scr refresh
                        FC_TR_HB_DYN.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(FC_TR_HB_DYN, 'tStopRefresh')  # time at next scr refresh
                        FC_TR_HB_DYN.setAutoDraw(False)
                if FC_TR_HB_DYN.status == STARTED:  # only update if drawing
                    FC_TR_HB_DYN.setPos((tr_xpos, 0.25), log=False)
                    FC_TR_HB_DYN.setSize((Train_HB_Width, 0.05), log=False)
                    FC_TR_HB_DYN.setFillColor(TR_HB_Colour, log=False)
                
                # *TR_FC* updates
                if TR_FC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TR_FC.frameNStart = frameN  # exact frame index
                    TR_FC.tStart = t  # local t and not account for scr refresh
                    TR_FC.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TR_FC, 'tStartRefresh')  # time at next scr refresh
                    TR_FC.setAutoDraw(True)
                if TR_FC.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > TR_FC.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        TR_FC.tStop = t  # not accounting for scr refresh
                        TR_FC.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TR_FC, 'tStopRefresh')  # time at next scr refresh
                        TR_FC.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fix_crossComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "fix_cross"-------
            for thisComponent in fix_crossComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            train_trials.addData('FC_TR_HB_BG.started', FC_TR_HB_BG.tStartRefresh)
            train_trials.addData('FC_TR_HB_BG.stopped', FC_TR_HB_BG.tStopRefresh)
            train_trials.addData('FC_TR_HB_DYN.started', FC_TR_HB_DYN.tStartRefresh)
            train_trials.addData('FC_TR_HB_DYN.stopped', FC_TR_HB_DYN.tStopRefresh)
            train_trials.addData('TR_FC.started', TR_FC.tStartRefresh)
            train_trials.addData('TR_FC.stopped', TR_FC.tStopRefresh)
            
            # ------Prepare to start Routine "training"-------
            continueRoutine = True
            routineTimer.add(2.500000)
            # update component parameters for each repeat
            train_berry_image.setImage(berry_train)
            train_berry_resp.keys = []
            train_berry_resp.rt = []
            _train_berry_resp_allKeys = []
            # keep track of which components have finished
            trainingComponents = [Train_HB_BG, Train_HB_DYN, train_berry_image, train_berry_resp, eat_tr_text, fast_tr_text]
            for thisComponent in trainingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "training"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trainingClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trainingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Train_HB_BG* updates
                if Train_HB_BG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Train_HB_BG.frameNStart = frameN  # exact frame index
                    Train_HB_BG.tStart = t  # local t and not account for scr refresh
                    Train_HB_BG.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Train_HB_BG, 'tStartRefresh')  # time at next scr refresh
                    Train_HB_BG.setAutoDraw(True)
                if Train_HB_BG.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Train_HB_BG.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Train_HB_BG.tStop = t  # not accounting for scr refresh
                        Train_HB_BG.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Train_HB_BG, 'tStopRefresh')  # time at next scr refresh
                        Train_HB_BG.setAutoDraw(False)
                
                # *Train_HB_DYN* updates
                if Train_HB_DYN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Train_HB_DYN.frameNStart = frameN  # exact frame index
                    Train_HB_DYN.tStart = t  # local t and not account for scr refresh
                    Train_HB_DYN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Train_HB_DYN, 'tStartRefresh')  # time at next scr refresh
                    Train_HB_DYN.setAutoDraw(True)
                if Train_HB_DYN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Train_HB_DYN.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Train_HB_DYN.tStop = t  # not accounting for scr refresh
                        Train_HB_DYN.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Train_HB_DYN, 'tStopRefresh')  # time at next scr refresh
                        Train_HB_DYN.setAutoDraw(False)
                if Train_HB_DYN.status == STARTED:  # only update if drawing
                    Train_HB_DYN.setPos((tr_xpos, 0.25), log=False)
                    Train_HB_DYN.setSize((Train_HB_Width, 0.05), log=False)
                    Train_HB_DYN.setFillColor(TR_HB_Colour, log=False)
                
                # *train_berry_image* updates
                if train_berry_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    train_berry_image.frameNStart = frameN  # exact frame index
                    train_berry_image.tStart = t  # local t and not account for scr refresh
                    train_berry_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(train_berry_image, 'tStartRefresh')  # time at next scr refresh
                    train_berry_image.setAutoDraw(True)
                if train_berry_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > train_berry_image.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        train_berry_image.tStop = t  # not accounting for scr refresh
                        train_berry_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(train_berry_image, 'tStopRefresh')  # time at next scr refresh
                        train_berry_image.setAutoDraw(False)
                
                # *train_berry_resp* updates
                waitOnFlip = False
                if train_berry_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    train_berry_resp.frameNStart = frameN  # exact frame index
                    train_berry_resp.tStart = t  # local t and not account for scr refresh
                    train_berry_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(train_berry_resp, 'tStartRefresh')  # time at next scr refresh
                    train_berry_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(train_berry_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(train_berry_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if train_berry_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > train_berry_resp.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        train_berry_resp.tStop = t  # not accounting for scr refresh
                        train_berry_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(train_berry_resp, 'tStopRefresh')  # time at next scr refresh
                        train_berry_resp.status = FINISHED
                if train_berry_resp.status == STARTED and not waitOnFlip:
                    theseKeys = train_berry_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _train_berry_resp_allKeys.extend(theseKeys)
                    if len(_train_berry_resp_allKeys):
                        train_berry_resp.keys = _train_berry_resp_allKeys[-1].name  # just the last key pressed
                        train_berry_resp.rt = _train_berry_resp_allKeys[-1].rt
                        # was this correct?
                        if (train_berry_resp.keys == str(train_ANS)) or (train_berry_resp.keys == train_ANS):
                            train_berry_resp.corr = 1
                        else:
                            train_berry_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *eat_tr_text* updates
                if eat_tr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    eat_tr_text.frameNStart = frameN  # exact frame index
                    eat_tr_text.tStart = t  # local t and not account for scr refresh
                    eat_tr_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(eat_tr_text, 'tStartRefresh')  # time at next scr refresh
                    eat_tr_text.setAutoDraw(True)
                if eat_tr_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > eat_tr_text.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        eat_tr_text.tStop = t  # not accounting for scr refresh
                        eat_tr_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(eat_tr_text, 'tStopRefresh')  # time at next scr refresh
                        eat_tr_text.setAutoDraw(False)
                
                # *fast_tr_text* updates
                if fast_tr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fast_tr_text.frameNStart = frameN  # exact frame index
                    fast_tr_text.tStart = t  # local t and not account for scr refresh
                    fast_tr_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fast_tr_text, 'tStartRefresh')  # time at next scr refresh
                    fast_tr_text.setAutoDraw(True)
                if fast_tr_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fast_tr_text.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fast_tr_text.tStop = t  # not accounting for scr refresh
                        fast_tr_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fast_tr_text, 'tStopRefresh')  # time at next scr refresh
                        fast_tr_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trainingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "training"-------
            for thisComponent in trainingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            train_trials.addData('Train_HB_BG.started', Train_HB_BG.tStartRefresh)
            train_trials.addData('Train_HB_BG.stopped', Train_HB_BG.tStopRefresh)
            train_trials.addData('Train_HB_DYN.started', Train_HB_DYN.tStartRefresh)
            train_trials.addData('Train_HB_DYN.stopped', Train_HB_DYN.tStopRefresh)
            train_trials.addData('train_berry_image.started', train_berry_image.tStartRefresh)
            train_trials.addData('train_berry_image.stopped', train_berry_image.tStopRefresh)
            # check responses
            if train_berry_resp.keys in ['', [], None]:  # No response was made
                train_berry_resp.keys = None
                # was no response the correct answer?!
                if str(train_ANS).lower() == 'none':
                   train_berry_resp.corr = 1;  # correct non-response
                else:
                   train_berry_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for train_trials (TrialHandler)
            train_trials.addData('train_berry_resp.keys',train_berry_resp.keys)
            train_trials.addData('train_berry_resp.corr', train_berry_resp.corr)
            if train_berry_resp.keys != None:  # we had a response
                train_trials.addData('train_berry_resp.rt', train_berry_resp.rt)
            train_trials.addData('train_berry_resp.started', train_berry_resp.tStartRefresh)
            train_trials.addData('train_berry_resp.stopped', train_berry_resp.tStopRefresh)
            train_trials.addData('eat_tr_text.started', eat_tr_text.tStartRefresh)
            train_trials.addData('eat_tr_text.stopped', eat_tr_text.tStopRefresh)
            train_trials.addData('fast_tr_text.started', fast_tr_text.tStartRefresh)
            train_trials.addData('fast_tr_text.stopped', fast_tr_text.tStopRefresh)
            
            # ------Prepare to start Routine "tr_hl_disp"-------
            continueRoutine = True
            routineTimer.add(0.350000)
            # update component parameters for each repeat
            # keep track of which components have finished
            tr_hl_dispComponents = [HL_TR_HB_BG, HL_TR_HB_DYN, tr_eat_hl_text, tr_fast_hl_text]
            for thisComponent in tr_hl_dispComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            tr_hl_dispClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "tr_hl_disp"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = tr_hl_dispClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=tr_hl_dispClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *HL_TR_HB_BG* updates
                if HL_TR_HB_BG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    HL_TR_HB_BG.frameNStart = frameN  # exact frame index
                    HL_TR_HB_BG.tStart = t  # local t and not account for scr refresh
                    HL_TR_HB_BG.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(HL_TR_HB_BG, 'tStartRefresh')  # time at next scr refresh
                    HL_TR_HB_BG.setAutoDraw(True)
                if HL_TR_HB_BG.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > HL_TR_HB_BG.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        HL_TR_HB_BG.tStop = t  # not accounting for scr refresh
                        HL_TR_HB_BG.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(HL_TR_HB_BG, 'tStopRefresh')  # time at next scr refresh
                        HL_TR_HB_BG.setAutoDraw(False)
                
                # *HL_TR_HB_DYN* updates
                if HL_TR_HB_DYN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    HL_TR_HB_DYN.frameNStart = frameN  # exact frame index
                    HL_TR_HB_DYN.tStart = t  # local t and not account for scr refresh
                    HL_TR_HB_DYN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(HL_TR_HB_DYN, 'tStartRefresh')  # time at next scr refresh
                    HL_TR_HB_DYN.setAutoDraw(True)
                if HL_TR_HB_DYN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > HL_TR_HB_DYN.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        HL_TR_HB_DYN.tStop = t  # not accounting for scr refresh
                        HL_TR_HB_DYN.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(HL_TR_HB_DYN, 'tStopRefresh')  # time at next scr refresh
                        HL_TR_HB_DYN.setAutoDraw(False)
                if HL_TR_HB_DYN.status == STARTED:  # only update if drawing
                    HL_TR_HB_DYN.setPos((tr_xpos, 0.25), log=False)
                    HL_TR_HB_DYN.setSize((Train_HB_Width, 0.05), log=False)
                    HL_TR_HB_DYN.setFillColor(TR_HB_Colour, log=False)
                if train_berry_resp.keys == 'f':
                    tr_eat_hl_text.color = "red"
                elif train_berry_resp.keys == "j":
                    tr_fast_hl_text.color = "red"
                
                # *tr_eat_hl_text* updates
                if tr_eat_hl_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    tr_eat_hl_text.frameNStart = frameN  # exact frame index
                    tr_eat_hl_text.tStart = t  # local t and not account for scr refresh
                    tr_eat_hl_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tr_eat_hl_text, 'tStartRefresh')  # time at next scr refresh
                    tr_eat_hl_text.setAutoDraw(True)
                if tr_eat_hl_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > tr_eat_hl_text.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        tr_eat_hl_text.tStop = t  # not accounting for scr refresh
                        tr_eat_hl_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(tr_eat_hl_text, 'tStopRefresh')  # time at next scr refresh
                        tr_eat_hl_text.setAutoDraw(False)
                
                # *tr_fast_hl_text* updates
                if tr_fast_hl_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    tr_fast_hl_text.frameNStart = frameN  # exact frame index
                    tr_fast_hl_text.tStart = t  # local t and not account for scr refresh
                    tr_fast_hl_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tr_fast_hl_text, 'tStartRefresh')  # time at next scr refresh
                    tr_fast_hl_text.setAutoDraw(True)
                if tr_fast_hl_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > tr_fast_hl_text.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        tr_fast_hl_text.tStop = t  # not accounting for scr refresh
                        tr_fast_hl_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(tr_fast_hl_text, 'tStopRefresh')  # time at next scr refresh
                        tr_fast_hl_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in tr_hl_dispComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "tr_hl_disp"-------
            for thisComponent in tr_hl_dispComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            train_trials.addData('HL_TR_HB_BG.started', HL_TR_HB_BG.tStartRefresh)
            train_trials.addData('HL_TR_HB_BG.stopped', HL_TR_HB_BG.tStopRefresh)
            train_trials.addData('HL_TR_HB_DYN.started', HL_TR_HB_DYN.tStartRefresh)
            train_trials.addData('HL_TR_HB_DYN.stopped', HL_TR_HB_DYN.tStopRefresh)
            tr_eat_hl_text.color = "black"
            tr_fast_hl_text.color = "black"
            train_trials.addData('tr_eat_hl_text.started', tr_eat_hl_text.tStartRefresh)
            train_trials.addData('tr_eat_hl_text.stopped', tr_eat_hl_text.tStopRefresh)
            train_trials.addData('tr_fast_hl_text.started', tr_fast_hl_text.tStartRefresh)
            train_trials.addData('tr_fast_hl_text.stopped', tr_fast_hl_text.tStopRefresh)
            
            # ------Prepare to start Routine "tr_corrector_code"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            tr_corrector_codeComponents = []
            for thisComponent in tr_corrector_codeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            tr_corrector_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "tr_corrector_code"-------
            while continueRoutine:
                # get current time
                t = tr_corrector_codeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=tr_corrector_codeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #trial per block
                
                if train_trials.thisN == num_trials:
                    train_trials.finished = True
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in tr_corrector_codeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "tr_corrector_code"-------
            for thisComponent in tr_corrector_codeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "tr_corrector_code" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'train_trials'
        
        # get names of stimulus parameters
        if train_trials.trialList in ([], [None], None):
            params = []
        else:
            params = train_trials.trialList[0].keys()
        # save data for this loop
        train_trials.saveAsExcel(filename + '.xlsx', sheetName='train_trials',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "train_block_counter"-------
        continueRoutine = True
        # update component parameters for each repeat
        block_skip.keys = []
        block_skip.rt = []
        _block_skip_allKeys = []
        # keep track of which components have finished
        train_block_counterComponents = [train_block_text, block_skip]
        for thisComponent in train_block_counterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        train_block_counterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "train_block_counter"-------
        while continueRoutine:
            # get current time
            t = train_block_counterClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=train_block_counterClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *train_block_text* updates
            if train_block_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                train_block_text.frameNStart = frameN  # exact frame index
                train_block_text.tStart = t  # local t and not account for scr refresh
                train_block_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train_block_text, 'tStartRefresh')  # time at next scr refresh
                train_block_text.setAutoDraw(True)
            
            # *block_skip* updates
            waitOnFlip = False
            if block_skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_skip.frameNStart = frameN  # exact frame index
                block_skip.tStart = t  # local t and not account for scr refresh
                block_skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_skip, 'tStartRefresh')  # time at next scr refresh
                block_skip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(block_skip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(block_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if block_skip.status == STARTED and not waitOnFlip:
                theseKeys = block_skip.getKeys(keyList=['space'], waitRelease=False)
                _block_skip_allKeys.extend(theseKeys)
                if len(_block_skip_allKeys):
                    block_skip.keys = _block_skip_allKeys[-1].name  # just the last key pressed
                    block_skip.rt = _block_skip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in train_block_counterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "train_block_counter"-------
        for thisComponent in train_block_counterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        train_blocks.addData('train_block_text.started', train_block_text.tStartRefresh)
        train_blocks.addData('train_block_text.stopped', train_block_text.tStopRefresh)
        # check responses
        if block_skip.keys in ['', [], None]:  # No response was made
            block_skip.keys = None
        train_blocks.addData('block_skip.keys',block_skip.keys)
        if block_skip.keys != None:  # we had a response
            train_blocks.addData('block_skip.rt', block_skip.rt)
        train_blocks.addData('block_skip.started', block_skip.tStartRefresh)
        train_blocks.addData('block_skip.stopped', block_skip.tStopRefresh)
        # the Routine "train_block_counter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed num_blocks repeats of 'train_blocks'
    
    
    # ------Prepare to start Routine "train_end_card"-------
    continueRoutine = True
    # update component parameters for each repeat
    TR_end_cont.keys = []
    TR_end_cont.rt = []
    _TR_end_cont_allKeys = []
    # keep track of which components have finished
    train_end_cardComponents = [TR_end_txt, TR_end_cont]
    for thisComponent in train_end_cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    train_end_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "train_end_card"-------
    while continueRoutine:
        # get current time
        t = train_end_cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=train_end_cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TR_end_txt* updates
        if TR_end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_end_txt.frameNStart = frameN  # exact frame index
            TR_end_txt.tStart = t  # local t and not account for scr refresh
            TR_end_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_end_txt, 'tStartRefresh')  # time at next scr refresh
            TR_end_txt.setAutoDraw(True)
        
        # *TR_end_cont* updates
        waitOnFlip = False
        if TR_end_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_end_cont.frameNStart = frameN  # exact frame index
            TR_end_cont.tStart = t  # local t and not account for scr refresh
            TR_end_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_end_cont, 'tStartRefresh')  # time at next scr refresh
            TR_end_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TR_end_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TR_end_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TR_end_cont.status == STARTED and not waitOnFlip:
            theseKeys = TR_end_cont.getKeys(keyList=['space'], waitRelease=False)
            _TR_end_cont_allKeys.extend(theseKeys)
            if len(_TR_end_cont_allKeys):
                TR_end_cont.keys = _TR_end_cont_allKeys[-1].name  # just the last key pressed
                TR_end_cont.rt = _TR_end_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in train_end_cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "train_end_card"-------
    for thisComponent in train_end_cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('TR_end_txt.started', TR_end_txt.tStartRefresh)
    consent_check.addData('TR_end_txt.stopped', TR_end_txt.tStopRefresh)
    # check responses
    if TR_end_cont.keys in ['', [], None]:  # No response was made
        TR_end_cont.keys = None
    consent_check.addData('TR_end_cont.keys',TR_end_cont.keys)
    if TR_end_cont.keys != None:  # we had a response
        consent_check.addData('TR_end_cont.rt', TR_end_cont.rt)
    consent_check.addData('TR_end_cont.started', TR_end_cont.tStartRefresh)
    consent_check.addData('TR_end_cont.stopped', TR_end_cont.tStopRefresh)
    # the Routine "train_end_card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test_info_card"-------
    continueRoutine = True
    # update component parameters for each repeat
    test_info_skip.keys = []
    test_info_skip.rt = []
    _test_info_skip_allKeys = []
    # keep track of which components have finished
    test_info_cardComponents = [test_info_txt, test_info_skip]
    for thisComponent in test_info_cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test_info_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test_info_card"-------
    while continueRoutine:
        # get current time
        t = test_info_cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test_info_cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_info_txt* updates
        if test_info_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_info_txt.frameNStart = frameN  # exact frame index
            test_info_txt.tStart = t  # local t and not account for scr refresh
            test_info_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_info_txt, 'tStartRefresh')  # time at next scr refresh
            test_info_txt.setAutoDraw(True)
        
        # *test_info_skip* updates
        waitOnFlip = False
        if test_info_skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_info_skip.frameNStart = frameN  # exact frame index
            test_info_skip.tStart = t  # local t and not account for scr refresh
            test_info_skip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_info_skip, 'tStartRefresh')  # time at next scr refresh
            test_info_skip.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test_info_skip.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test_info_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test_info_skip.status == STARTED and not waitOnFlip:
            theseKeys = test_info_skip.getKeys(keyList=['space'], waitRelease=False)
            _test_info_skip_allKeys.extend(theseKeys)
            if len(_test_info_skip_allKeys):
                test_info_skip.keys = _test_info_skip_allKeys[-1].name  # just the last key pressed
                test_info_skip.rt = _test_info_skip_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_info_cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_info_card"-------
    for thisComponent in test_info_cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('test_info_txt.started', test_info_txt.tStartRefresh)
    consent_check.addData('test_info_txt.stopped', test_info_txt.tStopRefresh)
    # check responses
    if test_info_skip.keys in ['', [], None]:  # No response was made
        test_info_skip.keys = None
    consent_check.addData('test_info_skip.keys',test_info_skip.keys)
    if test_info_skip.keys != None:  # we had a response
        consent_check.addData('test_info_skip.rt', test_info_skip.rt)
    consent_check.addData('test_info_skip.started', test_info_skip.tStartRefresh)
    consent_check.addData('test_info_skip.stopped', test_info_skip.tStopRefresh)
    # the Routine "test_info_card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    test_blocks = data.TrialHandler(nReps=num_blocks, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='test_blocks')
    thisExp.addLoop(test_blocks)  # add the loop to the experiment
    thisTest_block = test_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest_block.rgb)
    if thisTest_block != None:
        for paramName in thisTest_block:
            exec('{} = thisTest_block[paramName]'.format(paramName))
    
    for thisTest_block in test_blocks:
        currentLoop = test_blocks
        # abbreviate parameter names if possible (e.g. rgb = thisTest_block.rgb)
        if thisTest_block != None:
            for paramName in thisTest_block:
                exec('{} = thisTest_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "HB_reset_test"-------
        continueRoutine = True
        # update component parameters for each repeat
        Test_HB_Width = 0
        ts_xpos = 0
        # keep track of which components have finished
        HB_reset_testComponents = []
        for thisComponent in HB_reset_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        HB_reset_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "HB_reset_test"-------
        while continueRoutine:
            # get current time
            t = HB_reset_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=HB_reset_testClock)
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
            for thisComponent in HB_reset_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "HB_reset_test"-------
        for thisComponent in HB_reset_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "HB_reset_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        test_trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('test-data-holder.xlsx'),
            seed=None, name='test_trials')
        thisExp.addLoop(test_trials)  # add the loop to the experiment
        thisTest_trial = test_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
        if thisTest_trial != None:
            for paramName in thisTest_trial:
                exec('{} = thisTest_trial[paramName]'.format(paramName))
        
        for thisTest_trial in test_trials:
            currentLoop = test_trials
            # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
            if thisTest_trial != None:
                for paramName in thisTest_trial:
                    exec('{} = thisTest_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "test_code"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            test_codeComponents = []
            for thisComponent in test_codeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            test_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "test_code"-------
            while continueRoutine:
                # get current time
                t = test_codeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=test_codeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #Health Bar Code 
                #Make big or small depending on answer.
                if test_berry_resp.corr:
                    Test_HB_Width += 0.01
                    ts_xpos += 0.01/2
                else:
                    Test_HB_Width -= 0.01
                    ts_xpos -= 0.01/2
                
                #decide whether if the participant is 
                #in correct direction or not.
                if Test_HB_Width >= 0.01:
                    TS_HB_Colour = "green"
                elif Test_HB_Width <= 0.01:
                    TS_HB_Colour = "red"
                
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in test_codeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "test_code"-------
            for thisComponent in test_codeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "test_code" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ts_fix_cross"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ts_fix_crossComponents = [ts_FC]
            for thisComponent in ts_fix_crossComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ts_fix_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ts_fix_cross"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ts_fix_crossClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ts_fix_crossClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ts_FC* updates
                if ts_FC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ts_FC.frameNStart = frameN  # exact frame index
                    ts_FC.tStart = t  # local t and not account for scr refresh
                    ts_FC.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ts_FC, 'tStartRefresh')  # time at next scr refresh
                    ts_FC.setAutoDraw(True)
                if ts_FC.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ts_FC.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        ts_FC.tStop = t  # not accounting for scr refresh
                        ts_FC.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ts_FC, 'tStopRefresh')  # time at next scr refresh
                        ts_FC.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ts_fix_crossComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ts_fix_cross"-------
            for thisComponent in ts_fix_crossComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            test_trials.addData('ts_FC.started', ts_FC.tStartRefresh)
            test_trials.addData('ts_FC.stopped', ts_FC.tStopRefresh)
            
            # ------Prepare to start Routine "test"-------
            continueRoutine = True
            routineTimer.add(2.500000)
            # update component parameters for each repeat
            test_berry_img.setImage(test_berry)
            test_berry_resp.keys = []
            test_berry_resp.rt = []
            _test_berry_resp_allKeys = []
            # keep track of which components have finished
            testComponents = [test_berry_img, test_berry_resp, eat_ts_text, fast_ts_text]
            for thisComponent in testComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "test"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = testClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=testClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *test_berry_img* updates
                if test_berry_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    test_berry_img.frameNStart = frameN  # exact frame index
                    test_berry_img.tStart = t  # local t and not account for scr refresh
                    test_berry_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_berry_img, 'tStartRefresh')  # time at next scr refresh
                    test_berry_img.setAutoDraw(True)
                if test_berry_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > test_berry_img.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        test_berry_img.tStop = t  # not accounting for scr refresh
                        test_berry_img.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(test_berry_img, 'tStopRefresh')  # time at next scr refresh
                        test_berry_img.setAutoDraw(False)
                
                # *test_berry_resp* updates
                waitOnFlip = False
                if test_berry_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    test_berry_resp.frameNStart = frameN  # exact frame index
                    test_berry_resp.tStart = t  # local t and not account for scr refresh
                    test_berry_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_berry_resp, 'tStartRefresh')  # time at next scr refresh
                    test_berry_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(test_berry_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(test_berry_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if test_berry_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > test_berry_resp.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        test_berry_resp.tStop = t  # not accounting for scr refresh
                        test_berry_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(test_berry_resp, 'tStopRefresh')  # time at next scr refresh
                        test_berry_resp.status = FINISHED
                if test_berry_resp.status == STARTED and not waitOnFlip:
                    theseKeys = test_berry_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _test_berry_resp_allKeys.extend(theseKeys)
                    if len(_test_berry_resp_allKeys):
                        test_berry_resp.keys = _test_berry_resp_allKeys[-1].name  # just the last key pressed
                        test_berry_resp.rt = _test_berry_resp_allKeys[-1].rt
                        # was this correct?
                        if (test_berry_resp.keys == str(test_ANS)) or (test_berry_resp.keys == test_ANS):
                            test_berry_resp.corr = 1
                        else:
                            test_berry_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *eat_ts_text* updates
                if eat_ts_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    eat_ts_text.frameNStart = frameN  # exact frame index
                    eat_ts_text.tStart = t  # local t and not account for scr refresh
                    eat_ts_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(eat_ts_text, 'tStartRefresh')  # time at next scr refresh
                    eat_ts_text.setAutoDraw(True)
                if eat_ts_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > eat_ts_text.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        eat_ts_text.tStop = t  # not accounting for scr refresh
                        eat_ts_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(eat_ts_text, 'tStopRefresh')  # time at next scr refresh
                        eat_ts_text.setAutoDraw(False)
                
                # *fast_ts_text* updates
                if fast_ts_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fast_ts_text.frameNStart = frameN  # exact frame index
                    fast_ts_text.tStart = t  # local t and not account for scr refresh
                    fast_ts_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fast_ts_text, 'tStartRefresh')  # time at next scr refresh
                    fast_ts_text.setAutoDraw(True)
                if fast_ts_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fast_ts_text.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fast_ts_text.tStop = t  # not accounting for scr refresh
                        fast_ts_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fast_ts_text, 'tStopRefresh')  # time at next scr refresh
                        fast_ts_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in testComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "test"-------
            for thisComponent in testComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            test_trials.addData('test_berry_img.started', test_berry_img.tStartRefresh)
            test_trials.addData('test_berry_img.stopped', test_berry_img.tStopRefresh)
            # check responses
            if test_berry_resp.keys in ['', [], None]:  # No response was made
                test_berry_resp.keys = None
                # was no response the correct answer?!
                if str(test_ANS).lower() == 'none':
                   test_berry_resp.corr = 1;  # correct non-response
                else:
                   test_berry_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for test_trials (TrialHandler)
            test_trials.addData('test_berry_resp.keys',test_berry_resp.keys)
            test_trials.addData('test_berry_resp.corr', test_berry_resp.corr)
            if test_berry_resp.keys != None:  # we had a response
                test_trials.addData('test_berry_resp.rt', test_berry_resp.rt)
            test_trials.addData('test_berry_resp.started', test_berry_resp.tStartRefresh)
            test_trials.addData('test_berry_resp.stopped', test_berry_resp.tStopRefresh)
            test_trials.addData('eat_ts_text.started', eat_ts_text.tStartRefresh)
            test_trials.addData('eat_ts_text.stopped', eat_ts_text.tStopRefresh)
            test_trials.addData('fast_ts_text.started', fast_ts_text.tStartRefresh)
            test_trials.addData('fast_ts_text.stopped', fast_ts_text.tStopRefresh)
            
            # ------Prepare to start Routine "ts1_hl_disp"-------
            continueRoutine = True
            routineTimer.add(0.350000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ts1_hl_dispComponents = [ts_eat_hl_text, ts_fast_hl_text]
            for thisComponent in ts1_hl_dispComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ts1_hl_dispClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ts1_hl_disp"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ts1_hl_dispClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ts1_hl_dispClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if test_berry_resp.keys == 'f':
                    ts_eat_hl_text.color = "red"
                elif test_berry_resp.keys == 'j':
                    ts_fast_hl_text.color = "red"
                
                # *ts_eat_hl_text* updates
                if ts_eat_hl_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ts_eat_hl_text.frameNStart = frameN  # exact frame index
                    ts_eat_hl_text.tStart = t  # local t and not account for scr refresh
                    ts_eat_hl_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ts_eat_hl_text, 'tStartRefresh')  # time at next scr refresh
                    ts_eat_hl_text.setAutoDraw(True)
                if ts_eat_hl_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ts_eat_hl_text.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        ts_eat_hl_text.tStop = t  # not accounting for scr refresh
                        ts_eat_hl_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ts_eat_hl_text, 'tStopRefresh')  # time at next scr refresh
                        ts_eat_hl_text.setAutoDraw(False)
                
                # *ts_fast_hl_text* updates
                if ts_fast_hl_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ts_fast_hl_text.frameNStart = frameN  # exact frame index
                    ts_fast_hl_text.tStart = t  # local t and not account for scr refresh
                    ts_fast_hl_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ts_fast_hl_text, 'tStartRefresh')  # time at next scr refresh
                    ts_fast_hl_text.setAutoDraw(True)
                if ts_fast_hl_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ts_fast_hl_text.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        ts_fast_hl_text.tStop = t  # not accounting for scr refresh
                        ts_fast_hl_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ts_fast_hl_text, 'tStopRefresh')  # time at next scr refresh
                        ts_fast_hl_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ts1_hl_dispComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ts1_hl_disp"-------
            for thisComponent in ts1_hl_dispComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ts_eat_hl_text.color = "black"
            ts_fast_hl_text.color = "black"
            test_trials.addData('ts_eat_hl_text.started', ts_eat_hl_text.tStartRefresh)
            test_trials.addData('ts_eat_hl_text.stopped', ts_eat_hl_text.tStopRefresh)
            test_trials.addData('ts_fast_hl_text.started', ts_fast_hl_text.tStartRefresh)
            test_trials.addData('ts_fast_hl_text.stopped', ts_fast_hl_text.tStopRefresh)
            
            # ------Prepare to start Routine "ts_corrector_code"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ts_corrector_codeComponents = []
            for thisComponent in ts_corrector_codeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ts_corrector_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ts_corrector_code"-------
            while continueRoutine:
                # get current time
                t = ts_corrector_codeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ts_corrector_codeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #trial per block
                
                if test_trials.thisN == num_trials:
                    test_trials.finished = True
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ts_corrector_codeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ts_corrector_code"-------
            for thisComponent in ts_corrector_codeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ts_corrector_code" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'test_trials'
        
        # get names of stimulus parameters
        if test_trials.trialList in ([], [None], None):
            params = []
        else:
            params = test_trials.trialList[0].keys()
        # save data for this loop
        test_trials.saveAsExcel(filename + '.xlsx', sheetName='test_trials',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "test_block_counter"-------
        continueRoutine = True
        # update component parameters for each repeat
        TS_block_skip.keys = []
        TS_block_skip.rt = []
        _TS_block_skip_allKeys = []
        # keep track of which components have finished
        test_block_counterComponents = [TS_block_text, TS_block_skip]
        for thisComponent in test_block_counterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        test_block_counterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "test_block_counter"-------
        while continueRoutine:
            # get current time
            t = test_block_counterClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=test_block_counterClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TS_block_text* updates
            if TS_block_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TS_block_text.frameNStart = frameN  # exact frame index
                TS_block_text.tStart = t  # local t and not account for scr refresh
                TS_block_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TS_block_text, 'tStartRefresh')  # time at next scr refresh
                TS_block_text.setAutoDraw(True)
            
            # *TS_block_skip* updates
            waitOnFlip = False
            if TS_block_skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TS_block_skip.frameNStart = frameN  # exact frame index
                TS_block_skip.tStart = t  # local t and not account for scr refresh
                TS_block_skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TS_block_skip, 'tStartRefresh')  # time at next scr refresh
                TS_block_skip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TS_block_skip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TS_block_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TS_block_skip.status == STARTED and not waitOnFlip:
                theseKeys = TS_block_skip.getKeys(keyList=['space'], waitRelease=False)
                _TS_block_skip_allKeys.extend(theseKeys)
                if len(_TS_block_skip_allKeys):
                    TS_block_skip.keys = _TS_block_skip_allKeys[-1].name  # just the last key pressed
                    TS_block_skip.rt = _TS_block_skip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_block_counterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "test_block_counter"-------
        for thisComponent in test_block_counterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        test_blocks.addData('TS_block_text.started', TS_block_text.tStartRefresh)
        test_blocks.addData('TS_block_text.stopped', TS_block_text.tStopRefresh)
        # check responses
        if TS_block_skip.keys in ['', [], None]:  # No response was made
            TS_block_skip.keys = None
        test_blocks.addData('TS_block_skip.keys',TS_block_skip.keys)
        if TS_block_skip.keys != None:  # we had a response
            test_blocks.addData('TS_block_skip.rt', TS_block_skip.rt)
        test_blocks.addData('TS_block_skip.started', TS_block_skip.tStartRefresh)
        test_blocks.addData('TS_block_skip.stopped', TS_block_skip.tStopRefresh)
        # the Routine "test_block_counter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed num_blocks repeats of 'test_blocks'
    
    
    # ------Prepare to start Routine "end_card"-------
    continueRoutine = True
    # update component parameters for each repeat
    first_section_end_resp.keys = []
    first_section_end_resp.rt = []
    _first_section_end_resp_allKeys = []
    # keep track of which components have finished
    end_cardComponents = [first_section_end_txt, first_section_end_resp]
    for thisComponent in end_cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_card"-------
    while continueRoutine:
        # get current time
        t = end_cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *first_section_end_txt* updates
        if first_section_end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            first_section_end_txt.frameNStart = frameN  # exact frame index
            first_section_end_txt.tStart = t  # local t and not account for scr refresh
            first_section_end_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_section_end_txt, 'tStartRefresh')  # time at next scr refresh
            first_section_end_txt.setAutoDraw(True)
        
        # *first_section_end_resp* updates
        waitOnFlip = False
        if first_section_end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            first_section_end_resp.frameNStart = frameN  # exact frame index
            first_section_end_resp.tStart = t  # local t and not account for scr refresh
            first_section_end_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_section_end_resp, 'tStartRefresh')  # time at next scr refresh
            first_section_end_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(first_section_end_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(first_section_end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if first_section_end_resp.status == STARTED and not waitOnFlip:
            theseKeys = first_section_end_resp.getKeys(keyList=['space'], waitRelease=False)
            _first_section_end_resp_allKeys.extend(theseKeys)
            if len(_first_section_end_resp_allKeys):
                first_section_end_resp.keys = _first_section_end_resp_allKeys[-1].name  # just the last key pressed
                first_section_end_resp.rt = _first_section_end_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_card"-------
    for thisComponent in end_cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('first_section_end_txt.started', first_section_end_txt.tStartRefresh)
    consent_check.addData('first_section_end_txt.stopped', first_section_end_txt.tStopRefresh)
    # check responses
    if first_section_end_resp.keys in ['', [], None]:  # No response was made
        first_section_end_resp.keys = None
    consent_check.addData('first_section_end_resp.keys',first_section_end_resp.keys)
    if first_section_end_resp.keys != None:  # we had a response
        consent_check.addData('first_section_end_resp.rt', first_section_end_resp.rt)
    consent_check.addData('first_section_end_resp.started', first_section_end_resp.tStartRefresh)
    consent_check.addData('first_section_end_resp.stopped', first_section_end_resp.tStopRefresh)
    # the Routine "end_card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test_2_info_card"-------
    continueRoutine = True
    # update component parameters for each repeat
    quiescence_resp.keys = []
    quiescence_resp.rt = []
    _quiescence_resp_allKeys = []
    sound_1.setSound('Computer_Magic-Microsift-1901299923.wav', secs=5, hamming=True)
    sound_1.setVolume(1, log=False)
    # keep track of which components have finished
    test_2_info_cardComponents = [quiescence_txt, quiescence_resp, sound_1]
    for thisComponent in test_2_info_cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test_2_info_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test_2_info_card"-------
    while continueRoutine:
        # get current time
        t = test_2_info_cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test_2_info_cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *quiescence_txt* updates
        if quiescence_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            quiescence_txt.frameNStart = frameN  # exact frame index
            quiescence_txt.tStart = t  # local t and not account for scr refresh
            quiescence_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(quiescence_txt, 'tStartRefresh')  # time at next scr refresh
            quiescence_txt.setAutoDraw(True)
        if quiescence_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > quiescence_txt.tStartRefresh + 300-frameTolerance:
                # keep track of stop time/frame for later
                quiescence_txt.tStop = t  # not accounting for scr refresh
                quiescence_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(quiescence_txt, 'tStopRefresh')  # time at next scr refresh
                quiescence_txt.setAutoDraw(False)
        
        # *quiescence_resp* updates
        waitOnFlip = False
        if quiescence_resp.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
            # keep track of start time/frame for later
            quiescence_resp.frameNStart = frameN  # exact frame index
            quiescence_resp.tStart = t  # local t and not account for scr refresh
            quiescence_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(quiescence_resp, 'tStartRefresh')  # time at next scr refresh
            quiescence_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(quiescence_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(quiescence_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if quiescence_resp.status == STARTED and not waitOnFlip:
            theseKeys = quiescence_resp.getKeys(keyList=['space'], waitRelease=False)
            _quiescence_resp_allKeys.extend(theseKeys)
            if len(_quiescence_resp_allKeys):
                quiescence_resp.keys = _quiescence_resp_allKeys[-1].name  # just the last key pressed
                quiescence_resp.rt = _quiescence_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_2_info_cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_2_info_card"-------
    for thisComponent in test_2_info_cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('quiescence_txt.started', quiescence_txt.tStartRefresh)
    consent_check.addData('quiescence_txt.stopped', quiescence_txt.tStopRefresh)
    # check responses
    if quiescence_resp.keys in ['', [], None]:  # No response was made
        quiescence_resp.keys = None
    consent_check.addData('quiescence_resp.keys',quiescence_resp.keys)
    if quiescence_resp.keys != None:  # we had a response
        consent_check.addData('quiescence_resp.rt', quiescence_resp.rt)
    consent_check.addData('quiescence_resp.started', quiescence_resp.tStartRefresh)
    consent_check.addData('quiescence_resp.stopped', quiescence_resp.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    consent_check.addData('sound_1.started', sound_1.tStartRefresh)
    consent_check.addData('sound_1.stopped', sound_1.tStopRefresh)
    # the Routine "test_2_info_card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "test_2_proc_card"-------
    continueRoutine = True
    # update component parameters for each repeat
    test2_proc_resp.keys = []
    test2_proc_resp.rt = []
    _test2_proc_resp_allKeys = []
    # keep track of which components have finished
    test_2_proc_cardComponents = [test2_proc_text, test2_proc_resp]
    for thisComponent in test_2_proc_cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test_2_proc_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test_2_proc_card"-------
    while continueRoutine:
        # get current time
        t = test_2_proc_cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test_2_proc_cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test2_proc_text* updates
        if test2_proc_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2_proc_text.frameNStart = frameN  # exact frame index
            test2_proc_text.tStart = t  # local t and not account for scr refresh
            test2_proc_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2_proc_text, 'tStartRefresh')  # time at next scr refresh
            test2_proc_text.setAutoDraw(True)
        
        # *test2_proc_resp* updates
        waitOnFlip = False
        if test2_proc_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2_proc_resp.frameNStart = frameN  # exact frame index
            test2_proc_resp.tStart = t  # local t and not account for scr refresh
            test2_proc_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2_proc_resp, 'tStartRefresh')  # time at next scr refresh
            test2_proc_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test2_proc_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test2_proc_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test2_proc_resp.status == STARTED and not waitOnFlip:
            theseKeys = test2_proc_resp.getKeys(keyList=['space'], waitRelease=False)
            _test2_proc_resp_allKeys.extend(theseKeys)
            if len(_test2_proc_resp_allKeys):
                test2_proc_resp.keys = _test2_proc_resp_allKeys[-1].name  # just the last key pressed
                test2_proc_resp.rt = _test2_proc_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_2_proc_cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_2_proc_card"-------
    for thisComponent in test_2_proc_cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_check.addData('test2_proc_text.started', test2_proc_text.tStartRefresh)
    consent_check.addData('test2_proc_text.stopped', test2_proc_text.tStopRefresh)
    # check responses
    if test2_proc_resp.keys in ['', [], None]:  # No response was made
        test2_proc_resp.keys = None
    consent_check.addData('test2_proc_resp.keys',test2_proc_resp.keys)
    if test2_proc_resp.keys != None:  # we had a response
        consent_check.addData('test2_proc_resp.rt', test2_proc_resp.rt)
    consent_check.addData('test2_proc_resp.started', test2_proc_resp.tStartRefresh)
    consent_check.addData('test2_proc_resp.stopped', test2_proc_resp.tStopRefresh)
    # the Routine "test_2_proc_card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    test2_blocks = data.TrialHandler(nReps=num_blocks, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='test2_blocks')
    thisExp.addLoop(test2_blocks)  # add the loop to the experiment
    thisTest2_block = test2_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest2_block.rgb)
    if thisTest2_block != None:
        for paramName in thisTest2_block:
            exec('{} = thisTest2_block[paramName]'.format(paramName))
    
    for thisTest2_block in test2_blocks:
        currentLoop = test2_blocks
        # abbreviate parameter names if possible (e.g. rgb = thisTest2_block.rgb)
        if thisTest2_block != None:
            for paramName in thisTest2_block:
                exec('{} = thisTest2_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "test2_HB_reset"-------
        continueRoutine = True
        # update component parameters for each repeat
        Test2_HB_Width = 0
        ts2_xpos = 0
        # keep track of which components have finished
        test2_HB_resetComponents = []
        for thisComponent in test2_HB_resetComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        test2_HB_resetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "test2_HB_reset"-------
        while continueRoutine:
            # get current time
            t = test2_HB_resetClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=test2_HB_resetClock)
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
            for thisComponent in test2_HB_resetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "test2_HB_reset"-------
        for thisComponent in test2_HB_resetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "test2_HB_reset" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        test2_trials = data.TrialHandler(nReps=num_trials, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('test-data-holder.xlsx'),
            seed=None, name='test2_trials')
        thisExp.addLoop(test2_trials)  # add the loop to the experiment
        thisTest2_trial = test2_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTest2_trial.rgb)
        if thisTest2_trial != None:
            for paramName in thisTest2_trial:
                exec('{} = thisTest2_trial[paramName]'.format(paramName))
        
        for thisTest2_trial in test2_trials:
            currentLoop = test2_trials
            # abbreviate parameter names if possible (e.g. rgb = thisTest2_trial.rgb)
            if thisTest2_trial != None:
                for paramName in thisTest2_trial:
                    exec('{} = thisTest2_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "test2_code"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            test2_codeComponents = []
            for thisComponent in test2_codeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            test2_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "test2_code"-------
            while continueRoutine:
                # get current time
                t = test2_codeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=test2_codeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #Health Bar Code
                # Make big or small depending on answer.
                
                if test2_berry_resp.corr:
                    Test2_HB_Width += 0.01
                    ts2_xpos += 0.01/2
                else:
                    Test2_HB_Width -= 0.01
                    ts2_xpos -= 0.01/2
                
                #Decide whether if the participant is
                #in correct direction or not.
                if Test2_HB_Width >= 0.01:
                    TS2_HB_Colour = "green"
                elif Test2_HB_Width <= 0.01:
                    TS2_HB_Colour = "red"
                
                
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in test2_codeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "test2_code"-------
            for thisComponent in test2_codeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "test2_code" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ts2_fix_cross"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ts2_fix_crossComponents = [TS2_FC]
            for thisComponent in ts2_fix_crossComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ts2_fix_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ts2_fix_cross"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ts2_fix_crossClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ts2_fix_crossClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *TS2_FC* updates
                if TS2_FC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TS2_FC.frameNStart = frameN  # exact frame index
                    TS2_FC.tStart = t  # local t and not account for scr refresh
                    TS2_FC.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TS2_FC, 'tStartRefresh')  # time at next scr refresh
                    TS2_FC.setAutoDraw(True)
                if TS2_FC.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > TS2_FC.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        TS2_FC.tStop = t  # not accounting for scr refresh
                        TS2_FC.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TS2_FC, 'tStopRefresh')  # time at next scr refresh
                        TS2_FC.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ts2_fix_crossComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ts2_fix_cross"-------
            for thisComponent in ts2_fix_crossComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            test2_trials.addData('TS2_FC.started', TS2_FC.tStartRefresh)
            test2_trials.addData('TS2_FC.stopped', TS2_FC.tStopRefresh)
            
            # ------Prepare to start Routine "test2"-------
            continueRoutine = True
            routineTimer.add(2.500000)
            # update component parameters for each repeat
            test2_berry_img.setImage(test_berry)
            test2_berry_resp.keys = []
            test2_berry_resp.rt = []
            _test2_berry_resp_allKeys = []
            # keep track of which components have finished
            test2Components = [test2_berry_img, test2_berry_resp, ts2_eat_txt, ts2_fast_txt]
            for thisComponent in test2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            test2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "test2"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = test2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=test2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *test2_berry_img* updates
                if test2_berry_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    test2_berry_img.frameNStart = frameN  # exact frame index
                    test2_berry_img.tStart = t  # local t and not account for scr refresh
                    test2_berry_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test2_berry_img, 'tStartRefresh')  # time at next scr refresh
                    test2_berry_img.setAutoDraw(True)
                if test2_berry_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > test2_berry_img.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        test2_berry_img.tStop = t  # not accounting for scr refresh
                        test2_berry_img.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(test2_berry_img, 'tStopRefresh')  # time at next scr refresh
                        test2_berry_img.setAutoDraw(False)
                
                # *test2_berry_resp* updates
                waitOnFlip = False
                if test2_berry_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    test2_berry_resp.frameNStart = frameN  # exact frame index
                    test2_berry_resp.tStart = t  # local t and not account for scr refresh
                    test2_berry_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test2_berry_resp, 'tStartRefresh')  # time at next scr refresh
                    test2_berry_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(test2_berry_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(test2_berry_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if test2_berry_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > test2_berry_resp.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        test2_berry_resp.tStop = t  # not accounting for scr refresh
                        test2_berry_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(test2_berry_resp, 'tStopRefresh')  # time at next scr refresh
                        test2_berry_resp.status = FINISHED
                if test2_berry_resp.status == STARTED and not waitOnFlip:
                    theseKeys = test2_berry_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _test2_berry_resp_allKeys.extend(theseKeys)
                    if len(_test2_berry_resp_allKeys):
                        test2_berry_resp.keys = _test2_berry_resp_allKeys[-1].name  # just the last key pressed
                        test2_berry_resp.rt = _test2_berry_resp_allKeys[-1].rt
                        # was this correct?
                        if (test2_berry_resp.keys == str(test_ANS)) or (test2_berry_resp.keys == test_ANS):
                            test2_berry_resp.corr = 1
                        else:
                            test2_berry_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *ts2_eat_txt* updates
                if ts2_eat_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ts2_eat_txt.frameNStart = frameN  # exact frame index
                    ts2_eat_txt.tStart = t  # local t and not account for scr refresh
                    ts2_eat_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ts2_eat_txt, 'tStartRefresh')  # time at next scr refresh
                    ts2_eat_txt.setAutoDraw(True)
                if ts2_eat_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ts2_eat_txt.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        ts2_eat_txt.tStop = t  # not accounting for scr refresh
                        ts2_eat_txt.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ts2_eat_txt, 'tStopRefresh')  # time at next scr refresh
                        ts2_eat_txt.setAutoDraw(False)
                
                # *ts2_fast_txt* updates
                if ts2_fast_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ts2_fast_txt.frameNStart = frameN  # exact frame index
                    ts2_fast_txt.tStart = t  # local t and not account for scr refresh
                    ts2_fast_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ts2_fast_txt, 'tStartRefresh')  # time at next scr refresh
                    ts2_fast_txt.setAutoDraw(True)
                if ts2_fast_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ts2_fast_txt.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        ts2_fast_txt.tStop = t  # not accounting for scr refresh
                        ts2_fast_txt.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ts2_fast_txt, 'tStopRefresh')  # time at next scr refresh
                        ts2_fast_txt.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in test2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "test2"-------
            for thisComponent in test2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            test2_trials.addData('test2_berry_img.started', test2_berry_img.tStartRefresh)
            test2_trials.addData('test2_berry_img.stopped', test2_berry_img.tStopRefresh)
            # check responses
            if test2_berry_resp.keys in ['', [], None]:  # No response was made
                test2_berry_resp.keys = None
                # was no response the correct answer?!
                if str(test_ANS).lower() == 'none':
                   test2_berry_resp.corr = 1;  # correct non-response
                else:
                   test2_berry_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for test2_trials (TrialHandler)
            test2_trials.addData('test2_berry_resp.keys',test2_berry_resp.keys)
            test2_trials.addData('test2_berry_resp.corr', test2_berry_resp.corr)
            if test2_berry_resp.keys != None:  # we had a response
                test2_trials.addData('test2_berry_resp.rt', test2_berry_resp.rt)
            test2_trials.addData('test2_berry_resp.started', test2_berry_resp.tStartRefresh)
            test2_trials.addData('test2_berry_resp.stopped', test2_berry_resp.tStopRefresh)
            test2_trials.addData('ts2_eat_txt.started', ts2_eat_txt.tStartRefresh)
            test2_trials.addData('ts2_eat_txt.stopped', ts2_eat_txt.tStopRefresh)
            test2_trials.addData('ts2_fast_txt.started', ts2_fast_txt.tStartRefresh)
            test2_trials.addData('ts2_fast_txt.stopped', ts2_fast_txt.tStopRefresh)
            
            # ------Prepare to start Routine "ts2_hl_disp"-------
            continueRoutine = True
            routineTimer.add(0.350000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ts2_hl_dispComponents = [ts2_eat_hl_text, ts2_fast_hl_text]
            for thisComponent in ts2_hl_dispComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ts2_hl_dispClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ts2_hl_disp"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ts2_hl_dispClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ts2_hl_dispClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if test2_berry_resp.keys == 'f':
                    ts2_eat_hl_text.color = "red"
                elif test2_berry_resp.keys == 'j':
                    ts2_fast_hl_text.color = "red"
                
                # *ts2_eat_hl_text* updates
                if ts2_eat_hl_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ts2_eat_hl_text.frameNStart = frameN  # exact frame index
                    ts2_eat_hl_text.tStart = t  # local t and not account for scr refresh
                    ts2_eat_hl_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ts2_eat_hl_text, 'tStartRefresh')  # time at next scr refresh
                    ts2_eat_hl_text.setAutoDraw(True)
                if ts2_eat_hl_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ts2_eat_hl_text.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        ts2_eat_hl_text.tStop = t  # not accounting for scr refresh
                        ts2_eat_hl_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ts2_eat_hl_text, 'tStopRefresh')  # time at next scr refresh
                        ts2_eat_hl_text.setAutoDraw(False)
                
                # *ts2_fast_hl_text* updates
                if ts2_fast_hl_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ts2_fast_hl_text.frameNStart = frameN  # exact frame index
                    ts2_fast_hl_text.tStart = t  # local t and not account for scr refresh
                    ts2_fast_hl_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ts2_fast_hl_text, 'tStartRefresh')  # time at next scr refresh
                    ts2_fast_hl_text.setAutoDraw(True)
                if ts2_fast_hl_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ts2_fast_hl_text.tStartRefresh + 0.35-frameTolerance:
                        # keep track of stop time/frame for later
                        ts2_fast_hl_text.tStop = t  # not accounting for scr refresh
                        ts2_fast_hl_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ts2_fast_hl_text, 'tStopRefresh')  # time at next scr refresh
                        ts2_fast_hl_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ts2_hl_dispComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ts2_hl_disp"-------
            for thisComponent in ts2_hl_dispComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ts2_eat_hl_text.color = "black"
            ts2_fast_hl_text.color = "black"
            test2_trials.addData('ts2_eat_hl_text.started', ts2_eat_hl_text.tStartRefresh)
            test2_trials.addData('ts2_eat_hl_text.stopped', ts2_eat_hl_text.tStopRefresh)
            test2_trials.addData('ts2_fast_hl_text.started', ts2_fast_hl_text.tStartRefresh)
            test2_trials.addData('ts2_fast_hl_text.stopped', ts2_fast_hl_text.tStopRefresh)
            
            # ------Prepare to start Routine "ts2_corrector_code"-------
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ts2_corrector_codeComponents = []
            for thisComponent in ts2_corrector_codeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ts2_corrector_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ts2_corrector_code"-------
            while continueRoutine:
                # get current time
                t = ts2_corrector_codeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ts2_corrector_codeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #trial per block
                
                if test2_trials.thisN == num_trials:
                    test2_trials.finished = True
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ts2_corrector_codeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ts2_corrector_code"-------
            for thisComponent in ts2_corrector_codeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ts2_corrector_code" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed num_trials repeats of 'test2_trials'
        
        # get names of stimulus parameters
        if test2_trials.trialList in ([], [None], None):
            params = []
        else:
            params = test2_trials.trialList[0].keys()
        # save data for this loop
        test2_trials.saveAsExcel(filename + '.xlsx', sheetName='test2_trials',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "ts2_block_counter"-------
        continueRoutine = True
        # update component parameters for each repeat
        test2_block_resp.keys = []
        test2_block_resp.rt = []
        _test2_block_resp_allKeys = []
        # keep track of which components have finished
        ts2_block_counterComponents = [ts2_block_txt, test2_block_resp]
        for thisComponent in ts2_block_counterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ts2_block_counterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ts2_block_counter"-------
        while continueRoutine:
            # get current time
            t = ts2_block_counterClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ts2_block_counterClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ts2_block_txt* updates
            if ts2_block_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ts2_block_txt.frameNStart = frameN  # exact frame index
                ts2_block_txt.tStart = t  # local t and not account for scr refresh
                ts2_block_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ts2_block_txt, 'tStartRefresh')  # time at next scr refresh
                ts2_block_txt.setAutoDraw(True)
            
            # *test2_block_resp* updates
            waitOnFlip = False
            if test2_block_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test2_block_resp.frameNStart = frameN  # exact frame index
                test2_block_resp.tStart = t  # local t and not account for scr refresh
                test2_block_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test2_block_resp, 'tStartRefresh')  # time at next scr refresh
                test2_block_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(test2_block_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(test2_block_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if test2_block_resp.status == STARTED and not waitOnFlip:
                theseKeys = test2_block_resp.getKeys(keyList=['space'], waitRelease=False)
                _test2_block_resp_allKeys.extend(theseKeys)
                if len(_test2_block_resp_allKeys):
                    test2_block_resp.keys = _test2_block_resp_allKeys[-1].name  # just the last key pressed
                    test2_block_resp.rt = _test2_block_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ts2_block_counterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ts2_block_counter"-------
        for thisComponent in ts2_block_counterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        test2_blocks.addData('ts2_block_txt.started', ts2_block_txt.tStartRefresh)
        test2_blocks.addData('ts2_block_txt.stopped', ts2_block_txt.tStopRefresh)
        # check responses
        if test2_block_resp.keys in ['', [], None]:  # No response was made
            test2_block_resp.keys = None
        test2_blocks.addData('test2_block_resp.keys',test2_block_resp.keys)
        if test2_block_resp.keys != None:  # we had a response
            test2_blocks.addData('test2_block_resp.rt', test2_block_resp.rt)
        test2_blocks.addData('test2_block_resp.started', test2_block_resp.tStartRefresh)
        test2_blocks.addData('test2_block_resp.stopped', test2_block_resp.tStopRefresh)
        # the Routine "ts2_block_counter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed num_blocks repeats of 'test2_blocks'
    
# completed consent_rep repeats of 'consent_check'


# ------Prepare to start Routine "full_finish"-------
continueRoutine = True
# update component parameters for each repeat
finish_resp.keys = []
finish_resp.rt = []
_finish_resp_allKeys = []
# keep track of which components have finished
full_finishComponents = [finish_text, finish_resp]
for thisComponent in full_finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
full_finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "full_finish"-------
while continueRoutine:
    # get current time
    t = full_finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=full_finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_text* updates
    if finish_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_text.frameNStart = frameN  # exact frame index
        finish_text.tStart = t  # local t and not account for scr refresh
        finish_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_text, 'tStartRefresh')  # time at next scr refresh
        finish_text.setAutoDraw(True)
    
    # *finish_resp* updates
    waitOnFlip = False
    if finish_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_resp.frameNStart = frameN  # exact frame index
        finish_resp.tStart = t  # local t and not account for scr refresh
        finish_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_resp, 'tStartRefresh')  # time at next scr refresh
        finish_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finish_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(finish_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if finish_resp.status == STARTED and not waitOnFlip:
        theseKeys = finish_resp.getKeys(keyList=['space'], waitRelease=False)
        _finish_resp_allKeys.extend(theseKeys)
        if len(_finish_resp_allKeys):
            finish_resp.keys = _finish_resp_allKeys[-1].name  # just the last key pressed
            finish_resp.rt = _finish_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in full_finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "full_finish"-------
for thisComponent in full_finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finish_text.started', finish_text.tStartRefresh)
thisExp.addData('finish_text.stopped', finish_text.tStopRefresh)
# check responses
if finish_resp.keys in ['', [], None]:  # No response was made
    finish_resp.keys = None
thisExp.addData('finish_resp.keys',finish_resp.keys)
if finish_resp.keys != None:  # we had a response
    thisExp.addData('finish_resp.rt', finish_resp.rt)
thisExp.addData('finish_resp.started', finish_resp.tStartRefresh)
thisExp.addData('finish_resp.stopped', finish_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "full_finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "debrief_1_card"-------
continueRoutine = True
# update component parameters for each repeat
debrief1_resp.keys = []
debrief1_resp.rt = []
_debrief1_resp_allKeys = []
# keep track of which components have finished
debrief_1_cardComponents = [debrief1_img, debrief1_text, debrief1_resp]
for thisComponent in debrief_1_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debrief_1_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debrief_1_card"-------
while continueRoutine:
    # get current time
    t = debrief_1_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debrief_1_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debrief1_img* updates
    if debrief1_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief1_img.frameNStart = frameN  # exact frame index
        debrief1_img.tStart = t  # local t and not account for scr refresh
        debrief1_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief1_img, 'tStartRefresh')  # time at next scr refresh
        debrief1_img.setAutoDraw(True)
    
    # *debrief1_text* updates
    if debrief1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief1_text.frameNStart = frameN  # exact frame index
        debrief1_text.tStart = t  # local t and not account for scr refresh
        debrief1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief1_text, 'tStartRefresh')  # time at next scr refresh
        debrief1_text.setAutoDraw(True)
    
    # *debrief1_resp* updates
    waitOnFlip = False
    if debrief1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief1_resp.frameNStart = frameN  # exact frame index
        debrief1_resp.tStart = t  # local t and not account for scr refresh
        debrief1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief1_resp, 'tStartRefresh')  # time at next scr refresh
        debrief1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(debrief1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(debrief1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if debrief1_resp.status == STARTED and not waitOnFlip:
        theseKeys = debrief1_resp.getKeys(keyList=['space'], waitRelease=False)
        _debrief1_resp_allKeys.extend(theseKeys)
        if len(_debrief1_resp_allKeys):
            debrief1_resp.keys = _debrief1_resp_allKeys[-1].name  # just the last key pressed
            debrief1_resp.rt = _debrief1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debrief_1_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debrief_1_card"-------
for thisComponent in debrief_1_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debrief1_img.started', debrief1_img.tStartRefresh)
thisExp.addData('debrief1_img.stopped', debrief1_img.tStopRefresh)
thisExp.addData('debrief1_text.started', debrief1_text.tStartRefresh)
thisExp.addData('debrief1_text.stopped', debrief1_text.tStopRefresh)
# check responses
if debrief1_resp.keys in ['', [], None]:  # No response was made
    debrief1_resp.keys = None
thisExp.addData('debrief1_resp.keys',debrief1_resp.keys)
if debrief1_resp.keys != None:  # we had a response
    thisExp.addData('debrief1_resp.rt', debrief1_resp.rt)
thisExp.addData('debrief1_resp.started', debrief1_resp.tStartRefresh)
thisExp.addData('debrief1_resp.stopped', debrief1_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "debrief_1_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "debrief_2_card"-------
continueRoutine = True
# update component parameters for each repeat
debrief2_resp.keys = []
debrief2_resp.rt = []
_debrief2_resp_allKeys = []
# keep track of which components have finished
debrief_2_cardComponents = [debrief2_img, debrief2_text, debrief2_resp]
for thisComponent in debrief_2_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debrief_2_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debrief_2_card"-------
while continueRoutine:
    # get current time
    t = debrief_2_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debrief_2_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debrief2_img* updates
    if debrief2_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief2_img.frameNStart = frameN  # exact frame index
        debrief2_img.tStart = t  # local t and not account for scr refresh
        debrief2_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief2_img, 'tStartRefresh')  # time at next scr refresh
        debrief2_img.setAutoDraw(True)
    
    # *debrief2_text* updates
    if debrief2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief2_text.frameNStart = frameN  # exact frame index
        debrief2_text.tStart = t  # local t and not account for scr refresh
        debrief2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief2_text, 'tStartRefresh')  # time at next scr refresh
        debrief2_text.setAutoDraw(True)
    
    # *debrief2_resp* updates
    waitOnFlip = False
    if debrief2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief2_resp.frameNStart = frameN  # exact frame index
        debrief2_resp.tStart = t  # local t and not account for scr refresh
        debrief2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief2_resp, 'tStartRefresh')  # time at next scr refresh
        debrief2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(debrief2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(debrief2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if debrief2_resp.status == STARTED and not waitOnFlip:
        theseKeys = debrief2_resp.getKeys(keyList=['space'], waitRelease=False)
        _debrief2_resp_allKeys.extend(theseKeys)
        if len(_debrief2_resp_allKeys):
            debrief2_resp.keys = _debrief2_resp_allKeys[-1].name  # just the last key pressed
            debrief2_resp.rt = _debrief2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debrief_2_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debrief_2_card"-------
for thisComponent in debrief_2_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debrief2_img.started', debrief2_img.tStartRefresh)
thisExp.addData('debrief2_img.stopped', debrief2_img.tStopRefresh)
thisExp.addData('debrief2_text.started', debrief2_text.tStartRefresh)
thisExp.addData('debrief2_text.stopped', debrief2_text.tStopRefresh)
# check responses
if debrief2_resp.keys in ['', [], None]:  # No response was made
    debrief2_resp.keys = None
thisExp.addData('debrief2_resp.keys',debrief2_resp.keys)
if debrief2_resp.keys != None:  # we had a response
    thisExp.addData('debrief2_resp.rt', debrief2_resp.rt)
thisExp.addData('debrief2_resp.started', debrief2_resp.tStartRefresh)
thisExp.addData('debrief2_resp.stopped', debrief2_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "debrief_2_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end_card_2"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
end_card_2Components = [end_txt, end_resp]
for thisComponent in end_card_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_card_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_card_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_card_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_card_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_txt* updates
    if end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_txt.frameNStart = frameN  # exact frame index
        end_txt.tStart = t  # local t and not account for scr refresh
        end_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_txt, 'tStartRefresh')  # time at next scr refresh
        end_txt.setAutoDraw(True)
    if end_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_txt.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            end_txt.tStop = t  # not accounting for scr refresh
            end_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_txt, 'tStopRefresh')  # time at next scr refresh
            end_txt.setAutoDraw(False)
    
    # *end_resp* updates
    waitOnFlip = False
    if end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_resp.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            end_resp.tStop = t  # not accounting for scr refresh
            end_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_resp, 'tStopRefresh')  # time at next scr refresh
            end_resp.status = FINISHED
    if end_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_resp.getKeys(keyList=['q'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_card_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_card_2"-------
for thisComponent in end_card_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_txt.started', end_txt.tStartRefresh)
thisExp.addData('end_txt.stopped', end_txt.tStopRefresh)
# check responses
if end_resp.keys in ['', [], None]:  # No response was made
    end_resp.keys = None
thisExp.addData('end_resp.keys',end_resp.keys)
if end_resp.keys != None:  # we had a response
    thisExp.addData('end_resp.rt', end_resp.rt)
thisExp.addData('end_resp.started', end_resp.tStartRefresh)
thisExp.addData('end_resp.stopped', end_resp.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
