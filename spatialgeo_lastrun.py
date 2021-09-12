#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Sep  9 10:30:33 2021
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
expInfo = {'participant': '001', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/StateSpace/research_backup/Postdoc_Times/UTokyoPostdoc/CompNeuro/3 Projects/statespace/neuroimage/psychopy/spatialgeometry/spatialgeo_lastrun.py',
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

# Initialize components for Routine "screenshots"
screenshotsClock = core.Clock()
screenshots_img = visual.ImageStim(
    win=win,
    name='screenshots_img', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "wait_scan_start_key"
wait_scan_start_keyClock = core.Clock()
wait_scan_start = keyboard.Keyboard()
wait_scan_start_txt = visual.TextStim(win=win, name='wait_scan_start_txt',
    text='The video is about to start……',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "show_exp_videos"
show_exp_videosClock = core.Clock()
show_current_town_weather = visual.TextStim(win=win, name='show_current_town_weather',
    text='',
    font='Open Sans',
    pos=(0, 0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_question_for_know_or_not = visual.ImageStim(
    win=win,
    name='image_question_for_know_or_not', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_question_for_know_or_not = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
loop_screenshots = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('screenshots/screenshots_conditions.xlsx'),
    seed=None, name='loop_screenshots')
thisExp.addLoop(loop_screenshots)  # add the loop to the experiment
thisLoop_screenshot = loop_screenshots.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_screenshot.rgb)
if thisLoop_screenshot != None:
    for paramName in thisLoop_screenshot:
        exec('{} = thisLoop_screenshot[paramName]'.format(paramName))

for thisLoop_screenshot in loop_screenshots:
    currentLoop = loop_screenshots
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_screenshot.rgb)
    if thisLoop_screenshot != None:
        for paramName in thisLoop_screenshot:
            exec('{} = thisLoop_screenshot[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "screenshots"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    screenshots_img.setImage(screenshots_image)
    # keep track of which components have finished
    screenshotsComponents = [screenshots_img]
    for thisComponent in screenshotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    screenshotsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "screenshots"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = screenshotsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=screenshotsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *screenshots_img* updates
        if screenshots_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            screenshots_img.frameNStart = frameN  # exact frame index
            screenshots_img.tStart = t  # local t and not account for scr refresh
            screenshots_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(screenshots_img, 'tStartRefresh')  # time at next scr refresh
            screenshots_img.setAutoDraw(True)
        if screenshots_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > screenshots_img.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                screenshots_img.tStop = t  # not accounting for scr refresh
                screenshots_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(screenshots_img, 'tStopRefresh')  # time at next scr refresh
                screenshots_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in screenshotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "screenshots"-------
    for thisComponent in screenshotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_screenshots.addData('screenshots_img.started', screenshots_img.tStartRefresh)
    loop_screenshots.addData('screenshots_img.stopped', screenshots_img.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_screenshots'


# ------Prepare to start Routine "wait_scan_start_key"-------
continueRoutine = True
# update component parameters for each repeat
wait_scan_start.keys = []
wait_scan_start.rt = []
_wait_scan_start_allKeys = []
# keep track of which components have finished
wait_scan_start_keyComponents = [wait_scan_start, wait_scan_start_txt]
for thisComponent in wait_scan_start_keyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_scan_start_keyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wait_scan_start_key"-------
while continueRoutine:
    # get current time
    t = wait_scan_start_keyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_scan_start_keyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_scan_start* updates
    waitOnFlip = False
    if wait_scan_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_scan_start.frameNStart = frameN  # exact frame index
        wait_scan_start.tStart = t  # local t and not account for scr refresh
        wait_scan_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_scan_start, 'tStartRefresh')  # time at next scr refresh
        wait_scan_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wait_scan_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wait_scan_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wait_scan_start.status == STARTED and not waitOnFlip:
        theseKeys = wait_scan_start.getKeys(keyList=['5', 'space'], waitRelease=False)
        _wait_scan_start_allKeys.extend(theseKeys)
        if len(_wait_scan_start_allKeys):
            wait_scan_start.keys = _wait_scan_start_allKeys[-1].name  # just the last key pressed
            wait_scan_start.rt = _wait_scan_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *wait_scan_start_txt* updates
    if wait_scan_start_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_scan_start_txt.frameNStart = frameN  # exact frame index
        wait_scan_start_txt.tStart = t  # local t and not account for scr refresh
        wait_scan_start_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_scan_start_txt, 'tStartRefresh')  # time at next scr refresh
        wait_scan_start_txt.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_scan_start_keyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_scan_start_key"-------
for thisComponent in wait_scan_start_keyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if wait_scan_start.keys in ['', [], None]:  # No response was made
    wait_scan_start.keys = None
thisExp.addData('wait_scan_start.keys',wait_scan_start.keys)
if wait_scan_start.keys != None:  # we had a response
    thisExp.addData('wait_scan_start.rt', wait_scan_start.rt)
thisExp.addData('wait_scan_start.started', wait_scan_start.tStartRefresh)
thisExp.addData('wait_scan_start.stopped', wait_scan_start.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('wait_scan_start_txt.started', wait_scan_start_txt.tStartRefresh)
thisExp.addData('wait_scan_start_txt.stopped', wait_scan_start_txt.tStopRefresh)
# the Routine "wait_scan_start_key" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_town = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('videos/show_town_video_conditions.xlsx', selection=np.random.choice(2, size=1, replace=False)),
    seed=None, name='loop_town')
thisExp.addLoop(loop_town)  # add the loop to the experiment
thisLoop_town = loop_town.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_town.rgb)
if thisLoop_town != None:
    for paramName in thisLoop_town:
        exec('{} = thisLoop_town[paramName]'.format(paramName))

for thisLoop_town in loop_town:
    currentLoop = loop_town
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_town.rgb)
    if thisLoop_town != None:
        for paramName in thisLoop_town:
            exec('{} = thisLoop_town[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    loop_weather = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('videos/show_weather_video_conditions.xlsx', selection=np.random.choice(2, size=1, replace=False)),
        seed=None, name='loop_weather')
    thisExp.addLoop(loop_weather)  # add the loop to the experiment
    thisLoop_weather = loop_weather.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_weather.rgb)
    if thisLoop_weather != None:
        for paramName in thisLoop_weather:
            exec('{} = thisLoop_weather[paramName]'.format(paramName))
    
    for thisLoop_weather in loop_weather:
        currentLoop = loop_weather
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_weather.rgb)
        if thisLoop_weather != None:
            for paramName in thisLoop_weather:
                exec('{} = thisLoop_weather[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        loop_single_video = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('videos/show_single_video_conditions.xlsx'),
            seed=None, name='loop_single_video')
        thisExp.addLoop(loop_single_video)  # add the loop to the experiment
        thisLoop_single_video = loop_single_video.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_single_video.rgb)
        if thisLoop_single_video != None:
            for paramName in thisLoop_single_video:
                exec('{} = thisLoop_single_video[paramName]'.format(paramName))
        
        for thisLoop_single_video in loop_single_video:
            currentLoop = loop_single_video
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_single_video.rgb)
            if thisLoop_single_video != None:
                for paramName in thisLoop_single_video:
                    exec('{} = thisLoop_single_video[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "show_exp_videos"-------
            continueRoutine = True
            # update component parameters for each repeat
            show_single_video = visual.VlcMovieStim(
                win=win, name='show_single_video',
                filename="videos/"+str(town_name)+"_"+str(weather_name)+"/"+str(video_name),
                ori=0.0, pos=(0, 0), opacity=None,
                loop=False,
                depth=0.0,
                )
            show_current_town_weather.setText("Town:"+str(town_name)+",Weather:"+str(weather_name)+",Video:"+str(video_name))
            image_question_for_know_or_not.setImage('videos/Town01_ClearNoon/question_1.png')
            key_question_for_know_or_not.keys = []
            key_question_for_know_or_not.rt = []
            _key_question_for_know_or_not_allKeys = []
            # keep track of which components have finished
            show_exp_videosComponents = [show_single_video, show_current_town_weather, image_question_for_know_or_not, key_question_for_know_or_not]
            for thisComponent in show_exp_videosComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            show_exp_videosClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "show_exp_videos"-------
            while continueRoutine:
                # get current time
                t = show_exp_videosClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=show_exp_videosClock)
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
                
                # *image_question_for_know_or_not* updates
                if image_question_for_know_or_not.status == NOT_STARTED and show_single_video.status==FINISHED:
                    # keep track of start time/frame for later
                    image_question_for_know_or_not.frameNStart = frameN  # exact frame index
                    image_question_for_know_or_not.tStart = t  # local t and not account for scr refresh
                    image_question_for_know_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_question_for_know_or_not, 'tStartRefresh')  # time at next scr refresh
                    image_question_for_know_or_not.setAutoDraw(True)
                if image_question_for_know_or_not.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_question_for_know_or_not.tStartRefresh + 5.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_question_for_know_or_not.tStop = t  # not accounting for scr refresh
                        image_question_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_question_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        image_question_for_know_or_not.setAutoDraw(False)
                
                # *key_question_for_know_or_not* updates
                waitOnFlip = False
                if key_question_for_know_or_not.status == NOT_STARTED and show_single_video.status==FINISHED:
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
                    if tThisFlipGlobal > key_question_for_know_or_not.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        key_question_for_know_or_not.tStop = t  # not accounting for scr refresh
                        key_question_for_know_or_not.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_question_for_know_or_not, 'tStopRefresh')  # time at next scr refresh
                        key_question_for_know_or_not.status = FINISHED
                if key_question_for_know_or_not.status == STARTED and not waitOnFlip:
                    theseKeys = key_question_for_know_or_not.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
                    _key_question_for_know_or_not_allKeys.extend(theseKeys)
                    if len(_key_question_for_know_or_not_allKeys):
                        key_question_for_know_or_not.keys = _key_question_for_know_or_not_allKeys[-1].name  # just the last key pressed
                        key_question_for_know_or_not.rt = _key_question_for_know_or_not_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in show_exp_videosComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "show_exp_videos"-------
            for thisComponent in show_exp_videosComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            show_single_video.stop()
            loop_single_video.addData('show_current_town_weather.started', show_current_town_weather.tStartRefresh)
            loop_single_video.addData('show_current_town_weather.stopped', show_current_town_weather.tStopRefresh)
            loop_single_video.addData('image_question_for_know_or_not.started', image_question_for_know_or_not.tStartRefresh)
            loop_single_video.addData('image_question_for_know_or_not.stopped', image_question_for_know_or_not.tStopRefresh)
            # check responses
            if key_question_for_know_or_not.keys in ['', [], None]:  # No response was made
                key_question_for_know_or_not.keys = None
            loop_single_video.addData('key_question_for_know_or_not.keys',key_question_for_know_or_not.keys)
            if key_question_for_know_or_not.keys != None:  # we had a response
                loop_single_video.addData('key_question_for_know_or_not.rt', key_question_for_know_or_not.rt)
            loop_single_video.addData('key_question_for_know_or_not.started', key_question_for_know_or_not.tStartRefresh)
            loop_single_video.addData('key_question_for_know_or_not.stopped', key_question_for_know_or_not.tStopRefresh)
            # the Routine "show_exp_videos" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop_single_video'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'loop_weather'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_town'


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
