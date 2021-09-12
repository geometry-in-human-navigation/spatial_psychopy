#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sun Sep 12 16:37:36 2021
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
expInfo = {'participant': '', 'session': '001', 'group': '0'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/taiping/Workspace/statespace/neuroimage/psychopy/spatialgeometry/spatialgeo_demo_lastrun.py',
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
    size=[1280, 720], fullscr=False, screen=0, 
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

# Initialize components for Routine "guidelines"
guidelinesClock = core.Clock()
guidelines_img = visual.ImageStim(
    win=win,
    name='guidelines_img', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

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

# Initialize components for Routine "show_single_r"
show_single_rClock = core.Clock()
show_current_town_weather = visual.TextStim(win=win, name='show_current_town_weather',
    text='',
    font='Open Sans',
    pos=(0, 0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fix_cross_r_6"
fix_cross_r_6Clock = core.Clock()
fixation_cross_6s = visual.ShapeStim(
    win=win, name='fixation_cross_6s', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "q_r"
q_rClock = core.Clock()
left_image_question_for_know_or_not = visual.ImageStim(
    win=win,
    name='left_image_question_for_know_or_not', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.46, 0), size=(0.86, 0.51),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
right_image_question_for_know_or_not = visual.ImageStim(
    win=win,
    name='right_image_question_for_know_or_not', 
    image='sin', mask=None,
    ori=0.0, pos=(0.46, 0), size=(0.86, 0.51),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_question_for_know_or_not = keyboard.Keyboard()
txt_question_for_know_or_not = visual.TextStim(win=win, name='txt_question_for_know_or_not',
    text='Press the left, right buttons to confirm.',
    font='Open Sans',
    pos=(0, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
left_arrow_image = visual.ImageStim(
    win=win,
    name='left_arrow_image', 
    image='media/question_left_arrow.png', mask=None,
    ori=0.0, pos=(-0.5, 0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
right_arrow_image = visual.ImageStim(
    win=win,
    name='right_arrow_image', 
    image='media/question_right_arrow.png', mask=None,
    ori=0.0, pos=(0.5, 0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

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

# Initialize components for Routine "fix_cross_r_05"
fix_cross_r_05Clock = core.Clock()
fixation_cross_05 = visual.ShapeStim(
    win=win, name='fixation_cross_05', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "fix_cross_r_10"
fix_cross_r_10Clock = core.Clock()
fixation_cross_10 = visual.ShapeStim(
    win=win, name='fixation_cross_10', vertices='cross',
    size=(0.5, 0.5),
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
loop_guidelines = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('screenshots/screenshots_conditions.xlsx'),
    seed=None, name='loop_guidelines')
thisExp.addLoop(loop_guidelines)  # add the loop to the experiment
thisLoop_guideline = loop_guidelines.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_guideline.rgb)
if thisLoop_guideline != None:
    for paramName in thisLoop_guideline:
        exec('{} = thisLoop_guideline[paramName]'.format(paramName))

for thisLoop_guideline in loop_guidelines:
    currentLoop = loop_guidelines
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_guideline.rgb)
    if thisLoop_guideline != None:
        for paramName in thisLoop_guideline:
            exec('{} = thisLoop_guideline[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "guidelines"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    guidelines_img.setImage(screenshots_image)
    # keep track of which components have finished
    guidelinesComponents = [guidelines_img]
    for thisComponent in guidelinesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    guidelinesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "guidelines"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = guidelinesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=guidelinesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *guidelines_img* updates
        if guidelines_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            guidelines_img.frameNStart = frameN  # exact frame index
            guidelines_img.tStart = t  # local t and not account for scr refresh
            guidelines_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(guidelines_img, 'tStartRefresh')  # time at next scr refresh
            guidelines_img.setAutoDraw(True)
        if guidelines_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > guidelines_img.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                guidelines_img.tStop = t  # not accounting for scr refresh
                guidelines_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(guidelines_img, 'tStopRefresh')  # time at next scr refresh
                guidelines_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in guidelinesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "guidelines"-------
    for thisComponent in guidelinesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_guidelines.addData('guidelines_img.started', guidelines_img.tStartRefresh)
    loop_guidelines.addData('guidelines_img.stopped', guidelines_img.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_guidelines'


# ------Prepare to start Routine "wait_for_start"-------
continueRoutine = True
# update component parameters for each repeat
wait_for_start_key.keys = []
wait_for_start_key.rt = []
_wait_for_start_key_allKeys = []
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
        theseKeys = wait_for_start_key.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _wait_for_start_key_allKeys.extend(theseKeys)
        if len(_wait_for_start_key_allKeys):
            wait_for_start_key.keys = _wait_for_start_key_allKeys[-1].name  # just the last key pressed
            wait_for_start_key.rt = _wait_for_start_key_allKeys[-1].rt
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
# the Routine "wait_for_start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_videos = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('media/show_group_conditions.xlsx'),
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
        trialList=data.importConditions('media/show_clips_conditions.xlsx'),
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
        
        # ------Prepare to start Routine "show_single_r"-------
        continueRoutine = True
        # update component parameters for each repeat
        show_single_video = visual.MovieStim3(
            win=win, name='show_single_video',
            noAudio = False,
            filename="media/"+str(town_weather_name)+"/"+str(video_name)+".mp4",
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False,
            depth=0.0,
            )
        show_current_town_weather.setText("Town_Weather:"+str(town_weather_name)+",Video:"+str(video_name))
        # keep track of which components have finished
        show_single_rComponents = [show_single_video, show_current_town_weather]
        for thisComponent in show_single_rComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        show_single_rClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "show_single_r"-------
        while continueRoutine:
            # get current time
            t = show_single_rClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=show_single_rClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *show_single_video* updates
            if show_single_video.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                show_single_video.frameNStart = frameN  # exact frame index
                show_single_video.tStart = t  # local t and not account for scr refresh
                show_single_video.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(show_single_video, 'tStartRefresh')  # time at next scr refresh
                show_single_video.setAutoDraw(True)
            if show_single_video.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > show_single_video.tStartRefresh + video_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    show_single_video.tStop = t  # not accounting for scr refresh
                    show_single_video.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(show_single_video, 'tStopRefresh')  # time at next scr refresh
                    show_single_video.setAutoDraw(False)
            
            # *show_current_town_weather* updates
            if show_current_town_weather.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                show_current_town_weather.frameNStart = frameN  # exact frame index
                show_current_town_weather.tStart = t  # local t and not account for scr refresh
                show_current_town_weather.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(show_current_town_weather, 'tStartRefresh')  # time at next scr refresh
                show_current_town_weather.setAutoDraw(True)
            if show_current_town_weather.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > show_current_town_weather.tStartRefresh + video_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    show_current_town_weather.tStop = t  # not accounting for scr refresh
                    show_current_town_weather.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(show_current_town_weather, 'tStopRefresh')  # time at next scr refresh
                    show_current_town_weather.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in show_single_rComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "show_single_r"-------
        for thisComponent in show_single_rComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        show_single_video.stop()
        loop_clips.addData('show_current_town_weather.started', show_current_town_weather.tStartRefresh)
        loop_clips.addData('show_current_town_weather.stopped', show_current_town_weather.tStopRefresh)
        # the Routine "show_single_r" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fix_cross_r_6"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_cross_r_6Components = [fixation_cross_6s]
        for thisComponent in fix_cross_r_6Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_cross_r_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross_r_6"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fix_cross_r_6Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_cross_r_6Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross_6s* updates
            if fixation_cross_6s.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross_6s.frameNStart = frameN  # exact frame index
                fixation_cross_6s.tStart = t  # local t and not account for scr refresh
                fixation_cross_6s.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross_6s, 'tStartRefresh')  # time at next scr refresh
                fixation_cross_6s.setAutoDraw(True)
            if fixation_cross_6s.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross_6s.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross_6s.tStop = t  # not accounting for scr refresh
                    fixation_cross_6s.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_cross_6s, 'tStopRefresh')  # time at next scr refresh
                    fixation_cross_6s.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_cross_r_6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross_r_6"-------
        for thisComponent in fix_cross_r_6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_clips.addData('fixation_cross_6s.started', fixation_cross_6s.tStartRefresh)
        loop_clips.addData('fixation_cross_6s.stopped', fixation_cross_6s.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        loop_questions = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('media/Town01_ClearNoon/question_conditions.xlsx'),
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
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            left_image_question_for_know_or_not.setImage("media/"+str(left_town_weather_name)+"/"+str(video_name)+"_"+str(left_image_name)+".jpg")
            right_image_question_for_know_or_not.setImage("media/"+str(right_town_weather_name)+"/"+str(video_name)+"_"+str(right_image_name)+".jpg")
            key_question_for_know_or_not.keys = []
            key_question_for_know_or_not.rt = []
            _key_question_for_know_or_not_allKeys = []
            # keep track of which components have finished
            q_rComponents = [left_image_question_for_know_or_not, right_image_question_for_know_or_not, key_question_for_know_or_not, txt_question_for_know_or_not, left_arrow_image, right_arrow_image]
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
                    if tThisFlipGlobal > left_image_question_for_know_or_not.tStartRefresh + 2.0-frameTolerance:
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
                    if tThisFlipGlobal > right_image_question_for_know_or_not.tStartRefresh + 2.0-frameTolerance:
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
                    if tThisFlipGlobal > key_question_for_know_or_not.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        key_question_for_know_or_not.tStop = t  # not accounting for scr refresh
                        key_question_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_question_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        key_question_for_know_or_not.status = FINISHED
                if key_question_for_know_or_not.status == STARTED and not waitOnFlip:
                    theseKeys = key_question_for_know_or_not.getKeys(keyList=['left', 'right'], waitRelease=False)
                    _key_question_for_know_or_not_allKeys.extend(theseKeys)
                    if len(_key_question_for_know_or_not_allKeys):
                        key_question_for_know_or_not.keys = _key_question_for_know_or_not_allKeys[-1].name  # just the last key pressed
                        key_question_for_know_or_not.rt = _key_question_for_know_or_not_allKeys[-1].rt
                        # was this correct?
                        if (key_question_for_know_or_not.keys == str(correct_answer)) or (key_question_for_know_or_not.keys == correct_answer):
                            key_question_for_know_or_not.corr = 1
                        else:
                            key_question_for_know_or_not.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
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
                    if tThisFlipGlobal > txt_question_for_know_or_not.tStartRefresh + 2.0-frameTolerance:
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
                    if tThisFlipGlobal > left_arrow_image.tStartRefresh + 2.0-frameTolerance:
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
                    if tThisFlipGlobal > right_arrow_image.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        right_arrow_image.tStop = t  # not accounting for scr refresh
                        right_arrow_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(right_arrow_image, 'tStopRefresh')  # time at next scr refresh
                        right_arrow_image.setAutoDraw(False)
                
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
            
            # ------Prepare to start Routine "a_r"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            if (key_question_for_know_or_not.keys == str('None')) or (key_question_for_know_or_not.keys == None):
                txt_answer_for_know_or_not.text = "You did not press the key!"
                image_answer_for_know_or_not.size=(0.6, 0.6)
                image_answer_for_know_or_not.setImage("media/no_symbol.png")
            else:
                image_answer_for_know_or_not.size=(0.86, 0.51)
                if str(correct_answer) == 'left':
                    image_answer_for_know_or_not.setImage("media/"+str(left_town_weather_name)+"/"+str(video_name)+"_"+str(left_image_name)+".jpg")
                elif str(correct_answer) == 'right':
                    image_answer_for_know_or_not.setImage("media/"+str(right_town_weather_name)+"/"+str(video_name)+"_"+str(right_image_name)+".jpg")
            
                if (key_question_for_know_or_not.keys == str(correct_answer)) or (key_question_for_know_or_not.keys == correct_answer):
                    key_question_for_know_or_not.corr = 1
                    txt_answer_for_know_or_not.text = "Your answer is right!"
                else:
                    key_question_for_know_or_not.corr = 0
                    txt_answer_for_know_or_not.text = "Your answer is wrong!"
            
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
                    if tThisFlipGlobal > image_answer_for_know_or_not.tStartRefresh + 0.5-frameTolerance:
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
                    if tThisFlipGlobal > txt_answer_for_know_or_not.tStartRefresh + 0.5-frameTolerance:
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
            
            # ------Prepare to start Routine "fix_cross_r_05"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            fix_cross_r_05Components = [fixation_cross_05]
            for thisComponent in fix_cross_r_05Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            fix_cross_r_05Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "fix_cross_r_05"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = fix_cross_r_05Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=fix_cross_r_05Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross_05* updates
                if fixation_cross_05.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross_05.frameNStart = frameN  # exact frame index
                    fixation_cross_05.tStart = t  # local t and not account for scr refresh
                    fixation_cross_05.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross_05, 'tStartRefresh')  # time at next scr refresh
                    fixation_cross_05.setAutoDraw(True)
                if fixation_cross_05.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross_05.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross_05.tStop = t  # not accounting for scr refresh
                        fixation_cross_05.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_cross_05, 'tStopRefresh')  # time at next scr refresh
                        fixation_cross_05.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fix_cross_r_05Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "fix_cross_r_05"-------
            for thisComponent in fix_cross_r_05Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            loop_questions.addData('fixation_cross_05.started', fixation_cross_05.tStartRefresh)
            loop_questions.addData('fixation_cross_05.stopped', fixation_cross_05.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop_questions'
        
        
        # ------Prepare to start Routine "fix_cross_r_10"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_cross_r_10Components = [fixation_cross_10]
        for thisComponent in fix_cross_r_10Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_cross_r_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross_r_10"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fix_cross_r_10Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_cross_r_10Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross_10* updates
            if fixation_cross_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross_10.frameNStart = frameN  # exact frame index
                fixation_cross_10.tStart = t  # local t and not account for scr refresh
                fixation_cross_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross_10, 'tStartRefresh')  # time at next scr refresh
                fixation_cross_10.setAutoDraw(True)
            if fixation_cross_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross_10.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross_10.tStop = t  # not accounting for scr refresh
                    fixation_cross_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_cross_10, 'tStopRefresh')  # time at next scr refresh
                    fixation_cross_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_cross_r_10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross_r_10"-------
        for thisComponent in fix_cross_r_10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_clips.addData('fixation_cross_10.started', fixation_cross_10.tStartRefresh)
        loop_clips.addData('fixation_cross_10.stopped', fixation_cross_10.tStopRefresh)
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
        theseKeys = the_end_key.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
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
