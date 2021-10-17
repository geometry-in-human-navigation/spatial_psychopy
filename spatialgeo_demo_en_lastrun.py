#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sun Oct 17 16:02:04 2021
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'spatial geometry'  # from the Builder filename that created this script
expInfo = {'participant': '00', 'run': '00'}
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
    originPath='/Volumes/StateSpace/research_backup/Postdoc_Times/UTokyoPostdoc/CompNeuro/3 Projects/spatialnavigation/decisionmaking/neuroimage/psychopy/spatialgeometry/spatialgeo_demo_en_lastrun.py',
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
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "instruction_r"
instruction_rClock = core.Clock()
instruction_img = visual.ImageStim(
    win=win,
    name='instruction_img', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instruction_key = keyboard.Keyboard()
current_instruction = 1

# Initialize components for Routine "wait_for_start"
wait_for_startClock = core.Clock()
wait_for_start_txt = visual.TextStim(win=win, name='wait_for_start_txt',
    text='The experiment demo is about to start…',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
wait_for_start_key = keyboard.Keyboard()

# Initialize components for Routine "fix_cross_r_scan"
fix_cross_r_scanClock = core.Clock()
fix_cross_before_scan = visual.ShapeStim(
    win=win, name='fix_cross_before_scan', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "show_single_clip_r"
show_single_clip_rClock = core.Clock()

# Initialize components for Routine "fix_cross_r_bq"
fix_cross_r_bqClock = core.Clock()
fix_cross_before_question = visual.ShapeStim(
    win=win, name='fix_cross_before_question', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "q_r"
q_rClock = core.Clock()
left_image_question_for_know_or_not = visual.ImageStim(
    win=win,
    name='left_image_question_for_know_or_not', 
    image=None, mask=None,
    ori=0.0, pos=(-0.46, 0), size=(0.86, 0.51),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
right_image_question_for_know_or_not = visual.ImageStim(
    win=win,
    name='right_image_question_for_know_or_not', 
    image=None, mask=None,
    ori=0.0, pos=(0.46, 0), size=(0.86, 0.51),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_question_for_know_or_not = keyboard.Keyboard()
txt_question_for_know_or_not = visual.TextStim(win=win, name='txt_question_for_know_or_not',
    text='Which scene have you NOT seen?',
    font='Open Sans',
    pos=(0, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
left_arrow_image = visual.ImageStim(
    win=win,
    name='left_arrow_image', 
    image='media/pic/question_left_arrow.png', mask=None,
    ori=0.0, pos=(-0.5, 0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
right_arrow_image = visual.ImageStim(
    win=win,
    name='right_arrow_image', 
    image='media/pic/question_right_arrow.png', mask=None,
    ori=0.0, pos=(0.5, 0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_answer_green_square = visual.ImageStim(
    win=win,
    name='image_answer_green_square', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# Initialize components for Routine "a_r"
a_rClock = core.Clock()
image_answer_for_know_or_not = visual.ImageStim(
    win=win,
    name='image_answer_for_know_or_not', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.86, 0.51),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
txt_answer_for_know_or_not = visual.TextStim(win=win, name='txt_answer_for_know_or_not',
    text=None,
    font='Open Sans',
    pos=(0, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fix_cross_r_iq"
fix_cross_r_iqClock = core.Clock()
fix_cross_question = visual.ShapeStim(
    win=win, name='fix_cross_question', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "fix_cross_r_aq"
fix_cross_r_aqClock = core.Clock()
fix_cross_after_question = visual.ShapeStim(
    win=win, name='fix_cross_after_question', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "the_end"
the_endClock = core.Clock()
the_end_txt = visual.TextStim(win=win, name='the_end_txt',
    text='Press space key to end this demo.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
the_end_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
loop_instruction_r = data.TrialHandler(nReps=100.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_instruction_r')
thisExp.addLoop(loop_instruction_r)  # add the loop to the experiment
thisLoop_instruction_r = loop_instruction_r.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_instruction_r.rgb)
if thisLoop_instruction_r != None:
    for paramName in thisLoop_instruction_r:
        exec('{} = thisLoop_instruction_r[paramName]'.format(paramName))

for thisLoop_instruction_r in loop_instruction_r:
    currentLoop = loop_instruction_r
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_instruction_r.rgb)
    if thisLoop_instruction_r != None:
        for paramName in thisLoop_instruction_r:
            exec('{} = thisLoop_instruction_r[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instruction_r"-------
    continueRoutine = True
    # update component parameters for each repeat
    instruction_img.setImage('instruction/instruction_' + str(current_instruction) + '.png')
    instruction_key.keys = []
    instruction_key.rt = []
    _instruction_key_allKeys = []
    # keep track of which components have finished
    instruction_rComponents = [instruction_img, instruction_key]
    for thisComponent in instruction_rComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruction_rClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruction_r"-------
    while continueRoutine:
        # get current time
        t = instruction_rClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruction_rClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_img* updates
        if instruction_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_img.frameNStart = frameN  # exact frame index
            instruction_img.tStart = t  # local t and not account for scr refresh
            instruction_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_img, 'tStartRefresh')  # time at next scr refresh
            instruction_img.setAutoDraw(True)
        
        # *instruction_key* updates
        waitOnFlip = False
        if instruction_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_key.frameNStart = frameN  # exact frame index
            instruction_key.tStart = t  # local t and not account for scr refresh
            instruction_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_key, 'tStartRefresh')  # time at next scr refresh
            instruction_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruction_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruction_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_key.status == STARTED and not waitOnFlip:
            theseKeys = instruction_key.getKeys(keyList=['left', 'right'], waitRelease=False)
            _instruction_key_allKeys.extend(theseKeys)
            if len(_instruction_key_allKeys):
                instruction_key.keys = _instruction_key_allKeys[-1].name  # just the last key pressed
                instruction_key.rt = _instruction_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if instruction_key.keys == 'left' and current_instruction > 1:
            current_instruction = current_instruction - 1
        elif instruction_key.keys == 'right':
            current_instruction = current_instruction + 1
            
        if current_instruction == 5: # pressed 'right' on the last instructions
            loop_instruction_r.finished = True
            continueRoutine = False
            
        if current_instruction < 5: # pressed 'right' on the last instructions
            str_instruction_img = 'instruction/instruction_' + str(current_instruction) + '.png'
            instruction_img.setImage(str_instruction_img)
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_rComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruction_r"-------
    for thisComponent in instruction_rComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_instruction_r.addData('instruction_img.started', instruction_img.tStartRefresh)
    loop_instruction_r.addData('instruction_img.stopped', instruction_img.tStopRefresh)
    # check responses
    if instruction_key.keys in ['', [], None]:  # No response was made
        instruction_key.keys = None
    loop_instruction_r.addData('instruction_key.keys',instruction_key.keys)
    if instruction_key.keys != None:  # we had a response
        loop_instruction_r.addData('instruction_key.rt', instruction_key.rt)
    loop_instruction_r.addData('instruction_key.started', instruction_key.tStartRefresh)
    loop_instruction_r.addData('instruction_key.stopped', instruction_key.tStopRefresh)
    # the Routine "instruction_r" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 100.0 repeats of 'loop_instruction_r'


# ------Prepare to start Routine "wait_for_start"-------
continueRoutine = True
# update component parameters for each repeat
wait_for_start_key.keys = []
wait_for_start_key.rt = []
_wait_for_start_key_allKeys = []
thisExp.addData('wait_for_start_begin_routine', core.monotonicClock.getTime())
win.mouseVisible = False
# keep track of which components have finished
wait_for_startComponents = [wait_for_start_txt, wait_for_start_key]
for thisComponent in wait_for_startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_for_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wait_for_start"-------
while continueRoutine:
    # get current time
    t = wait_for_startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_for_startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_for_start_txt* updates
    if wait_for_start_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_for_start_txt.frameNStart = frameN  # exact frame index
        wait_for_start_txt.tStart = t  # local t and not account for scr refresh
        wait_for_start_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_for_start_txt, 'tStartRefresh')  # time at next scr refresh
        wait_for_start_txt.setAutoDraw(True)
    
    # *wait_for_start_key* updates
    waitOnFlip = False
    if wait_for_start_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_for_start_key.frameNStart = frameN  # exact frame index
        wait_for_start_key.tStart = t  # local t and not account for scr refresh
        wait_for_start_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_for_start_key, 'tStartRefresh')  # time at next scr refresh
        wait_for_start_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wait_for_start_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wait_for_start_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wait_for_start_key.status == STARTED and not waitOnFlip:
        theseKeys = wait_for_start_key.getKeys(keyList=['5', 'space'], waitRelease=False)
        _wait_for_start_key_allKeys.extend(theseKeys)
        if len(_wait_for_start_key_allKeys):
            wait_for_start_key.keys = [key.name for key in _wait_for_start_key_allKeys]  # storing all keys
            wait_for_start_key.rt = [key.rt for key in _wait_for_start_key_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_start"-------
for thisComponent in wait_for_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wait_for_start_txt.started', wait_for_start_txt.tStartRefresh)
thisExp.addData('wait_for_start_txt.stopped', wait_for_start_txt.tStopRefresh)
# check responses
if wait_for_start_key.keys in ['', [], None]:  # No response was made
    wait_for_start_key.keys = None
thisExp.addData('wait_for_start_key.keys',wait_for_start_key.keys)
if wait_for_start_key.keys != None:  # we had a response
    thisExp.addData('wait_for_start_key.rt', wait_for_start_key.rt)
thisExp.addData('wait_for_start_key.started', wait_for_start_key.tStartRefresh)
thisExp.addData('wait_for_start_key.stopped', wait_for_start_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('wait_for_start_end_routine', core.monotonicClock.getTime())

# the Routine "wait_for_start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fix_cross_r_scan"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
fix_cross_r_scanComponents = [fix_cross_before_scan]
for thisComponent in fix_cross_r_scanComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fix_cross_r_scanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fix_cross_r_scan"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fix_cross_r_scanClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fix_cross_r_scanClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix_cross_before_scan* updates
    if fix_cross_before_scan.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix_cross_before_scan.frameNStart = frameN  # exact frame index
        fix_cross_before_scan.tStart = t  # local t and not account for scr refresh
        fix_cross_before_scan.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix_cross_before_scan, 'tStartRefresh')  # time at next scr refresh
        fix_cross_before_scan.setAutoDraw(True)
    if fix_cross_before_scan.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix_cross_before_scan.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            fix_cross_before_scan.tStop = t  # not accounting for scr refresh
            fix_cross_before_scan.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cross_before_scan, 'tStopRefresh')  # time at next scr refresh
            fix_cross_before_scan.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fix_cross_r_scanComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fix_cross_r_scan"-------
for thisComponent in fix_cross_r_scanComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix_cross_before_scan.started', fix_cross_before_scan.tStartRefresh)
thisExp.addData('fix_cross_before_scan.stopped', fix_cross_before_scan.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_videos = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("conditions/groups/"+str(expInfo['participant'])+".xlsx", selection=[int(expInfo['run'])]),
    seed=None, name='loop_videos')
thisExp.addLoop(loop_videos)  # add the loop to the experiment
thisLoop_video = loop_videos.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_video.rgb)
if thisLoop_video != None:
    for paramName in thisLoop_video:
        exec('{} = thisLoop_video[paramName]'.format(paramName))

for thisLoop_video in loop_videos:
    currentLoop = loop_videos
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_video.rgb)
    if thisLoop_video != None:
        for paramName in thisLoop_video:
            exec('{} = thisLoop_video[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    loop_clips = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/show_clips_demo_conditions.xlsx'),
        seed=None, name='loop_clips')
    thisExp.addLoop(loop_clips)  # add the loop to the experiment
    thisLoop_clip = loop_clips.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_clip.rgb)
    if thisLoop_clip != None:
        for paramName in thisLoop_clip:
            exec('{} = thisLoop_clip[paramName]'.format(paramName))
    
    for thisLoop_clip in loop_clips:
        currentLoop = loop_clips
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_clip.rgb)
        if thisLoop_clip != None:
            for paramName in thisLoop_clip:
                exec('{} = thisLoop_clip[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "show_single_clip_r"-------
        continueRoutine = True
        # update component parameters for each repeat
        show_single_clip = visual.MovieStim3(
            win=win, name='show_single_clip',
            noAudio = False,
            filename="media/videos/"+str(town_weather_name)+"/"+str(town_weather_name)+"_"+str(video_name)+".mp4",
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False,
            depth=0.0,
            )
        thisExp.addData('show_single_clip_begin_routine', core.monotonicClock.getTime())
        # keep track of which components have finished
        show_single_clip_rComponents = [show_single_clip]
        for thisComponent in show_single_clip_rComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        show_single_clip_rClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "show_single_clip_r"-------
        while continueRoutine:
            # get current time
            t = show_single_clip_rClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=show_single_clip_rClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *show_single_clip* updates
            if show_single_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                show_single_clip.frameNStart = frameN  # exact frame index
                show_single_clip.tStart = t  # local t and not account for scr refresh
                show_single_clip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(show_single_clip, 'tStartRefresh')  # time at next scr refresh
                show_single_clip.setAutoDraw(True)
            if show_single_clip.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > show_single_clip.tStartRefresh + video_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    show_single_clip.tStop = t  # not accounting for scr refresh
                    show_single_clip.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(show_single_clip, 'tStopRefresh')  # time at next scr refresh
                    show_single_clip.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in show_single_clip_rComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "show_single_clip_r"-------
        for thisComponent in show_single_clip_rComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        show_single_clip.stop()
        thisExp.addData('show_single_clip_end_routine', core.monotonicClock.getTime())
        # the Routine "show_single_clip_r" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fix_cross_r_bq"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_cross_r_bqComponents = [fix_cross_before_question]
        for thisComponent in fix_cross_r_bqComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_cross_r_bqClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross_r_bq"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fix_cross_r_bqClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_cross_r_bqClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross_before_question* updates
            if fix_cross_before_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_before_question.frameNStart = frameN  # exact frame index
                fix_cross_before_question.tStart = t  # local t and not account for scr refresh
                fix_cross_before_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_before_question, 'tStartRefresh')  # time at next scr refresh
                fix_cross_before_question.setAutoDraw(True)
            if fix_cross_before_question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross_before_question.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross_before_question.tStop = t  # not accounting for scr refresh
                    fix_cross_before_question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_cross_before_question, 'tStopRefresh')  # time at next scr refresh
                    fix_cross_before_question.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_cross_r_bqComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross_r_bq"-------
        for thisComponent in fix_cross_r_bqComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_clips.addData('fix_cross_before_question.started', fix_cross_before_question.tStartRefresh)
        loop_clips.addData('fix_cross_before_question.stopped', fix_cross_before_question.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        loop_questions = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions/question_conditions.xlsx'),
            seed=None, name='loop_questions')
        thisExp.addLoop(loop_questions)  # add the loop to the experiment
        thisLoop_question = loop_questions.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_question.rgb)
        if thisLoop_question != None:
            for paramName in thisLoop_question:
                exec('{} = thisLoop_question[paramName]'.format(paramName))
        
        for thisLoop_question in loop_questions:
            currentLoop = loop_questions
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_question.rgb)
            if thisLoop_question != None:
                for paramName in thisLoop_question:
                    exec('{} = thisLoop_question[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "q_r"-------
            continueRoutine = True
            routineTimer.add(9.000000)
            # update component parameters for each repeat
            key_question_for_know_or_not.keys = []
            key_question_for_know_or_not.rt = []
            _key_question_for_know_or_not_allKeys = []
            image_answer_green_square.size=(0.0, 0.0)
            
            #-- set left and right image
            video_question_dict = {
              "clip0_q1": "rgb_002000.jpg",
              "clip0_q2": "rgb_004000.jpg",
              "clip1_q1": "rgb_008000.jpg",
              "clip1_q2": "rgb_010000.jpg",
              "clip2_q1": "rgb_014000.jpg",
              "clip2_q2": "rgb_016000.jpg",
            }
            
            # random choose left or right as a correct image, 0 for left, 1 for right
            rand_binary = np.random.randint(2, size=1)[0]
            current_video_img=str(video_name)+"_"+str(question_name)
            correct_img_str="media/question_images/"+str(town_weather_name)+"/"+str(video_question_dict[current_video_img])
            
            # random choose compared image from other towns except current town
            current_town_num=town_weather_name.split("_")[0].split("n")[1]
            current_weather=town_weather_name.split("_")[1]
            town_index_list = [1, 2, 3, 4, 5, 6, 7, 8]
            town_name_list = ["Town01","Town02","Town03","Town04","Town05","Town06","Town07","Town10HD"] 
            compared_town_num = np.random.choice([ele for ele in town_index_list if ele != int(current_town_num)])
            compared_town_weather_name = str(town_name_list[compared_town_num-1])+"_"+str(current_weather)
            compared_img_str = "media/question_images/"+str(compared_town_weather_name)+"/"+str(video_question_dict[current_video_img])
            
            # display image
            if rand_binary == 0: # 0 for left as correct
                correct_answer='left'
                correct_num='1'
                left_image_question_for_know_or_not.setImage(correct_img_str)
                right_image_question_for_know_or_not.setImage(compared_img_str)
            elif rand_binary == 1: # 1 for right as correct
                correct_answer='right'
                correct_num='4'
                left_image_question_for_know_or_not.setImage(compared_img_str)
                right_image_question_for_know_or_not.setImage(correct_img_str)
            
            
            # keep track of which components have finished
            q_rComponents = [left_image_question_for_know_or_not, right_image_question_for_know_or_not, key_question_for_know_or_not, txt_question_for_know_or_not, left_arrow_image, right_arrow_image, image_answer_green_square]
            for thisComponent in q_rComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            q_rClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "q_r"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = q_rClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=q_rClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *left_image_question_for_know_or_not* updates
                if left_image_question_for_know_or_not.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    left_image_question_for_know_or_not.frameNStart = frameN  # exact frame index
                    left_image_question_for_know_or_not.tStart = t  # local t and not account for scr refresh
                    left_image_question_for_know_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_image_question_for_know_or_not, 'tStartRefresh')  # time at next scr refresh
                    left_image_question_for_know_or_not.setAutoDraw(True)
                if left_image_question_for_know_or_not.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > left_image_question_for_know_or_not.tStartRefresh + 9-frameTolerance:
                        # keep track of stop time/frame for later
                        left_image_question_for_know_or_not.tStop = t  # not accounting for scr refresh
                        left_image_question_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(left_image_question_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        left_image_question_for_know_or_not.setAutoDraw(False)
                
                # *right_image_question_for_know_or_not* updates
                if right_image_question_for_know_or_not.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    right_image_question_for_know_or_not.frameNStart = frameN  # exact frame index
                    right_image_question_for_know_or_not.tStart = t  # local t and not account for scr refresh
                    right_image_question_for_know_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_image_question_for_know_or_not, 'tStartRefresh')  # time at next scr refresh
                    right_image_question_for_know_or_not.setAutoDraw(True)
                if right_image_question_for_know_or_not.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > right_image_question_for_know_or_not.tStartRefresh + 9-frameTolerance:
                        # keep track of stop time/frame for later
                        right_image_question_for_know_or_not.tStop = t  # not accounting for scr refresh
                        right_image_question_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(right_image_question_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        right_image_question_for_know_or_not.setAutoDraw(False)
                
                # *key_question_for_know_or_not* updates
                waitOnFlip = False
                if key_question_for_know_or_not.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    key_question_for_know_or_not.frameNStart = frameN  # exact frame index
                    key_question_for_know_or_not.tStart = t  # local t and not account for scr refresh
                    key_question_for_know_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_question_for_know_or_not, 'tStartRefresh')  # time at next scr refresh
                    key_question_for_know_or_not.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_question_for_know_or_not.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_question_for_know_or_not.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_question_for_know_or_not.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_question_for_know_or_not.tStartRefresh + 9-frameTolerance:
                        # keep track of stop time/frame for later
                        key_question_for_know_or_not.tStop = t  # not accounting for scr refresh
                        key_question_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_question_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        key_question_for_know_or_not.status = FINISHED
                if key_question_for_know_or_not.status == STARTED and not waitOnFlip:
                    theseKeys = key_question_for_know_or_not.getKeys(keyList=['left', 'right', '1', '4'], waitRelease=False)
                    _key_question_for_know_or_not_allKeys.extend(theseKeys)
                    if len(_key_question_for_know_or_not_allKeys):
                        key_question_for_know_or_not.keys = _key_question_for_know_or_not_allKeys[-1].name  # just the last key pressed
                        key_question_for_know_or_not.rt = _key_question_for_know_or_not_allKeys[-1].rt
                        # was this correct?
                        if (key_question_for_know_or_not.keys == str(correct_answer)) or (key_question_for_know_or_not.keys == correct_answer):
                            key_question_for_know_or_not.corr = 1
                        else:
                            key_question_for_know_or_not.corr = 0
                
                # *txt_question_for_know_or_not* updates
                if txt_question_for_know_or_not.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_question_for_know_or_not.frameNStart = frameN  # exact frame index
                    txt_question_for_know_or_not.tStart = t  # local t and not account for scr refresh
                    txt_question_for_know_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_question_for_know_or_not, 'tStartRefresh')  # time at next scr refresh
                    txt_question_for_know_or_not.setAutoDraw(True)
                if txt_question_for_know_or_not.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_question_for_know_or_not.tStartRefresh + 9-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_question_for_know_or_not.tStop = t  # not accounting for scr refresh
                        txt_question_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_question_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        txt_question_for_know_or_not.setAutoDraw(False)
                
                # *left_arrow_image* updates
                if left_arrow_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    left_arrow_image.frameNStart = frameN  # exact frame index
                    left_arrow_image.tStart = t  # local t and not account for scr refresh
                    left_arrow_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_arrow_image, 'tStartRefresh')  # time at next scr refresh
                    left_arrow_image.setAutoDraw(True)
                if left_arrow_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > left_arrow_image.tStartRefresh + 9-frameTolerance:
                        # keep track of stop time/frame for later
                        left_arrow_image.tStop = t  # not accounting for scr refresh
                        left_arrow_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(left_arrow_image, 'tStopRefresh')  # time at next scr refresh
                        left_arrow_image.setAutoDraw(False)
                
                # *right_arrow_image* updates
                if right_arrow_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    right_arrow_image.frameNStart = frameN  # exact frame index
                    right_arrow_image.tStart = t  # local t and not account for scr refresh
                    right_arrow_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_arrow_image, 'tStartRefresh')  # time at next scr refresh
                    right_arrow_image.setAutoDraw(True)
                if right_arrow_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > right_arrow_image.tStartRefresh + 9-frameTolerance:
                        # keep track of stop time/frame for later
                        right_arrow_image.tStop = t  # not accounting for scr refresh
                        right_arrow_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(right_arrow_image, 'tStopRefresh')  # time at next scr refresh
                        right_arrow_image.setAutoDraw(False)
                # detect the key press
                if key_question_for_know_or_not.status == STARTED:
                    
                    if (key_question_for_know_or_not.keys == 'left' or key_question_for_know_or_not.keys == '1'):
                        image_answer_green_square.pos=(-0.5, 0.4)
                        image_answer_green_square.size=(0.22, 0.22)
                        image_answer_green_square.setImage("media/pic/green_square.png")
                
                    elif (key_question_for_know_or_not.keys == 'right' or key_question_for_know_or_not.keys == '4'):
                        image_answer_green_square.pos=(0.5, 0.4)
                        image_answer_green_square.size=(0.22, 0.22)
                        image_answer_green_square.setImage("media/pic/green_square.png")
                
                
                
                
                
                
                # *image_answer_green_square* updates
                if image_answer_green_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_answer_green_square.frameNStart = frameN  # exact frame index
                    image_answer_green_square.tStart = t  # local t and not account for scr refresh
                    image_answer_green_square.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_answer_green_square, 'tStartRefresh')  # time at next scr refresh
                    image_answer_green_square.setAutoDraw(True)
                if image_answer_green_square.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_answer_green_square.tStartRefresh + 9-frameTolerance:
                        # keep track of stop time/frame for later
                        image_answer_green_square.tStop = t  # not accounting for scr refresh
                        image_answer_green_square.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_answer_green_square, 'tStopRefresh')  # time at next scr refresh
                        image_answer_green_square.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in q_rComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "q_r"-------
            for thisComponent in q_rComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            loop_questions.addData('left_image_question_for_know_or_not.started', left_image_question_for_know_or_not.tStartRefresh)
            loop_questions.addData('left_image_question_for_know_or_not.stopped', left_image_question_for_know_or_not.tStopRefresh)
            loop_questions.addData('right_image_question_for_know_or_not.started', right_image_question_for_know_or_not.tStartRefresh)
            loop_questions.addData('right_image_question_for_know_or_not.stopped', right_image_question_for_know_or_not.tStopRefresh)
            # check responses
            if key_question_for_know_or_not.keys in ['', [], None]:  # No response was made
                key_question_for_know_or_not.keys = None
                # was no response the correct answer?!
                if str(correct_answer).lower() == 'none':
                   key_question_for_know_or_not.corr = 1;  # correct non-response
                else:
                   key_question_for_know_or_not.corr = 0;  # failed to respond (incorrectly)
            # store data for loop_questions (TrialHandler)
            loop_questions.addData('key_question_for_know_or_not.keys',key_question_for_know_or_not.keys)
            loop_questions.addData('key_question_for_know_or_not.corr', key_question_for_know_or_not.corr)
            if key_question_for_know_or_not.keys != None:  # we had a response
                loop_questions.addData('key_question_for_know_or_not.rt', key_question_for_know_or_not.rt)
            loop_questions.addData('key_question_for_know_or_not.started', key_question_for_know_or_not.tStartRefresh)
            loop_questions.addData('key_question_for_know_or_not.stopped', key_question_for_know_or_not.tStopRefresh)
            loop_questions.addData('txt_question_for_know_or_not.started', txt_question_for_know_or_not.tStartRefresh)
            loop_questions.addData('txt_question_for_know_or_not.stopped', txt_question_for_know_or_not.tStopRefresh)
            loop_questions.addData('left_arrow_image.started', left_arrow_image.tStartRefresh)
            loop_questions.addData('left_arrow_image.stopped', left_arrow_image.tStopRefresh)
            loop_questions.addData('right_arrow_image.started', right_arrow_image.tStartRefresh)
            loop_questions.addData('right_arrow_image.stopped', right_arrow_image.tStopRefresh)
            loop_questions.addData('image_answer_green_square.started', image_answer_green_square.tStartRefresh)
            loop_questions.addData('image_answer_green_square.stopped', image_answer_green_square.tStopRefresh)
            
            # ------Prepare to start Routine "a_r"-------
            continueRoutine = True
            routineTimer.add(5.000000)
            # update component parameters for each repeat
            if (key_question_for_know_or_not.keys == str('None')) or (key_question_for_know_or_not.keys == None):
                txt_answer_for_know_or_not.text = "You did not press the key!"
                txt_answer_for_know_or_not.color = "red"
                image_answer_for_know_or_not.size=(0.6, 0.6)
                image_answer_for_know_or_not.setImage("media/pic/no_symbol.png")
                thisExp.addData('show_single_clip_answer', "none")
                
            else:
                image_answer_for_know_or_not.size=(0.86, 0.51)
            #    if str(correct_answer) == 'left':
            #        image_answer_for_know_or_not.setImage(correct_img_str)
            #    elif str(correct_answer) == 'right':
            #        image_answer_for_know_or_not.setImage(correct_img_str)
                image_answer_for_know_or_not.setImage(compared_img_str)
            
                if (key_question_for_know_or_not.keys == str(correct_answer) or key_question_for_know_or_not.keys == str(correct_num)):
                    key_question_for_know_or_not.corr = 0
                    txt_answer_for_know_or_not.text = "Wrong!"
                    txt_answer_for_know_or_not.color = "red"
                    txt_answer_for_know_or_not.height = 0.08
                    thisExp.addData('show_single_clip_answer', "wrong")
                else:
                    key_question_for_know_or_not.corr = 1
                    txt_answer_for_know_or_not.text = "Correct!"
                    txt_answer_for_know_or_not.color = "green"
                    txt_answer_for_know_or_not.height = 0.08
                    thisExp.addData('show_single_clip_answer', "correct")
            
            # keep track of which components have finished
            a_rComponents = [image_answer_for_know_or_not, txt_answer_for_know_or_not]
            for thisComponent in a_rComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            a_rClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "a_r"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = a_rClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=a_rClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_answer_for_know_or_not* updates
                if image_answer_for_know_or_not.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_answer_for_know_or_not.frameNStart = frameN  # exact frame index
                    image_answer_for_know_or_not.tStart = t  # local t and not account for scr refresh
                    image_answer_for_know_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_answer_for_know_or_not, 'tStartRefresh')  # time at next scr refresh
                    image_answer_for_know_or_not.setAutoDraw(True)
                if image_answer_for_know_or_not.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_answer_for_know_or_not.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_answer_for_know_or_not.tStop = t  # not accounting for scr refresh
                        image_answer_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_answer_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        image_answer_for_know_or_not.setAutoDraw(False)
                
                # *txt_answer_for_know_or_not* updates
                if txt_answer_for_know_or_not.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    txt_answer_for_know_or_not.frameNStart = frameN  # exact frame index
                    txt_answer_for_know_or_not.tStart = t  # local t and not account for scr refresh
                    txt_answer_for_know_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(txt_answer_for_know_or_not, 'tStartRefresh')  # time at next scr refresh
                    txt_answer_for_know_or_not.setAutoDraw(True)
                if txt_answer_for_know_or_not.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > txt_answer_for_know_or_not.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        txt_answer_for_know_or_not.tStop = t  # not accounting for scr refresh
                        txt_answer_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(txt_answer_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        txt_answer_for_know_or_not.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in a_rComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "a_r"-------
            for thisComponent in a_rComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            loop_questions.addData('image_answer_for_know_or_not.started', image_answer_for_know_or_not.tStartRefresh)
            loop_questions.addData('image_answer_for_know_or_not.stopped', image_answer_for_know_or_not.tStopRefresh)
            loop_questions.addData('txt_answer_for_know_or_not.started', txt_answer_for_know_or_not.tStartRefresh)
            loop_questions.addData('txt_answer_for_know_or_not.stopped', txt_answer_for_know_or_not.tStopRefresh)
            
            # ------Prepare to start Routine "fix_cross_r_iq"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            fix_cross_r_iqComponents = [fix_cross_question]
            for thisComponent in fix_cross_r_iqComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            fix_cross_r_iqClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "fix_cross_r_iq"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = fix_cross_r_iqClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=fix_cross_r_iqClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fix_cross_question* updates
                if fix_cross_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix_cross_question.frameNStart = frameN  # exact frame index
                    fix_cross_question.tStart = t  # local t and not account for scr refresh
                    fix_cross_question.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix_cross_question, 'tStartRefresh')  # time at next scr refresh
                    fix_cross_question.setAutoDraw(True)
                if fix_cross_question.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix_cross_question.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fix_cross_question.tStop = t  # not accounting for scr refresh
                        fix_cross_question.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fix_cross_question, 'tStopRefresh')  # time at next scr refresh
                        fix_cross_question.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fix_cross_r_iqComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "fix_cross_r_iq"-------
            for thisComponent in fix_cross_r_iqComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            loop_questions.addData('fix_cross_question.started', fix_cross_question.tStartRefresh)
            loop_questions.addData('fix_cross_question.stopped', fix_cross_question.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop_questions'
        
        
        # ------Prepare to start Routine "fix_cross_r_aq"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_cross_r_aqComponents = [fix_cross_after_question]
        for thisComponent in fix_cross_r_aqComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_cross_r_aqClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross_r_aq"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fix_cross_r_aqClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_cross_r_aqClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross_after_question* updates
            if fix_cross_after_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_after_question.frameNStart = frameN  # exact frame index
                fix_cross_after_question.tStart = t  # local t and not account for scr refresh
                fix_cross_after_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_after_question, 'tStartRefresh')  # time at next scr refresh
                fix_cross_after_question.setAutoDraw(True)
            if fix_cross_after_question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross_after_question.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross_after_question.tStop = t  # not accounting for scr refresh
                    fix_cross_after_question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_cross_after_question, 'tStopRefresh')  # time at next scr refresh
                    fix_cross_after_question.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_cross_r_aqComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross_r_aq"-------
        for thisComponent in fix_cross_r_aqComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_clips.addData('fix_cross_after_question.started', fix_cross_after_question.tStartRefresh)
        loop_clips.addData('fix_cross_after_question.stopped', fix_cross_after_question.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'loop_clips'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_videos'


# ------Prepare to start Routine "the_end"-------
continueRoutine = True
# update component parameters for each repeat
the_end_key.keys = []
the_end_key.rt = []
_the_end_key_allKeys = []
# keep track of which components have finished
the_endComponents = [the_end_txt, the_end_key]
for thisComponent in the_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
the_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "the_end"-------
while continueRoutine:
    # get current time
    t = the_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=the_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *the_end_txt* updates
    if the_end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        the_end_txt.frameNStart = frameN  # exact frame index
        the_end_txt.tStart = t  # local t and not account for scr refresh
        the_end_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(the_end_txt, 'tStartRefresh')  # time at next scr refresh
        the_end_txt.setAutoDraw(True)
    
    # *the_end_key* updates
    waitOnFlip = False
    if the_end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        the_end_key.frameNStart = frameN  # exact frame index
        the_end_key.tStart = t  # local t and not account for scr refresh
        the_end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(the_end_key, 'tStartRefresh')  # time at next scr refresh
        the_end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(the_end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(the_end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if the_end_key.status == STARTED and not waitOnFlip:
        theseKeys = the_end_key.getKeys(keyList=['space'], waitRelease=False)
        _the_end_key_allKeys.extend(theseKeys)
        if len(_the_end_key_allKeys):
            the_end_key.keys = _the_end_key_allKeys[-1].name  # just the last key pressed
            the_end_key.rt = _the_end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "the_end"-------
for thisComponent in the_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('the_end_txt.started', the_end_txt.tStartRefresh)
thisExp.addData('the_end_txt.stopped', the_end_txt.tStopRefresh)
# check responses
if the_end_key.keys in ['', [], None]:  # No response was made
    the_end_key.keys = None
thisExp.addData('the_end_key.keys',the_end_key.keys)
if the_end_key.keys != None:  # we had a response
    thisExp.addData('the_end_key.rt', the_end_key.rt)
thisExp.addData('the_end_key.started', the_end_key.tStartRefresh)
thisExp.addData('the_end_key.stopped', the_end_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "the_end" was not non-slip safe, so reset the non-slip timer
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
