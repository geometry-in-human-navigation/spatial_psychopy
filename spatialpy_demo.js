/************************** 
 * Spatialcross_Demo Test *
 **************************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'spatialcross_demo';  // from the Builder filename that created this script
let expInfo = {'participant': '100', 'run': '00'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const loop_instruction_rLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_instruction_rLoopBegin(loop_instruction_rLoopScheduler));
flowScheduler.add(loop_instruction_rLoopScheduler);
flowScheduler.add(loop_instruction_rLoopEnd);
flowScheduler.add(wait_for_startRoutineBegin());
flowScheduler.add(wait_for_startRoutineEachFrame());
flowScheduler.add(wait_for_startRoutineEnd());
flowScheduler.add(fix_cross_r_scanRoutineBegin());
flowScheduler.add(fix_cross_r_scanRoutineEachFrame());
flowScheduler.add(fix_cross_r_scanRoutineEnd());
const loop_videosLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_videosLoopBegin(loop_videosLoopScheduler));
flowScheduler.add(loop_videosLoopScheduler);
flowScheduler.add(loop_videosLoopEnd);
flowScheduler.add(the_endRoutineBegin());
flowScheduler.add(the_endRoutineEachFrame());
flowScheduler.add(the_endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'conditions/question_conditions.xlsx', 'path': 'conditions/question_conditions.xlsx'},
    {'name': 'media/pic/question_left_arrow.png', 'path': 'media/pic/question_left_arrow.png'},
    {'name': 'media/pic/question_right_arrow.png', 'path': 'media/pic/question_right_arrow.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instruction_rClock;
var instruction_img;
var instruction_key;
var wait_for_startClock;
var wait_for_start_txt;
var wait_for_start_key;
var fix_cross_r_scanClock;
var fix_cross_before_scan;
var show_single_video_rClock;
var fix_cross_r_bqClock;
var fix_cross_before_question;
var q_rClock;
var left_image_question_for_know_or_not;
var right_image_question_for_know_or_not;
var key_question_for_know_or_not;
var txt_question_for_know_or_not;
var left_arrow_image;
var right_arrow_image;
var image_answer_green_square;
var a_rClock;
var image_answer_for_know_or_not;
var txt_answer_for_know_or_not;
var fix_cross_r_iqClock;
var fix_cross_question;
var fix_cross_r_aqClock;
var fix_cross_after_question;
var the_endClock;
var the_end_txt;
var the_end_key;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instruction_r"
  instruction_rClock = new util.Clock();
  instruction_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.8, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  instruction_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wait_for_start"
  wait_for_startClock = new util.Clock();
  wait_for_start_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'wait_for_start_txt',
    text: 'The scanner is about to start… \nPlease keep your head still once you hear noise from the scanner.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  wait_for_start_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fix_cross_r_scan"
  fix_cross_r_scanClock = new util.Clock();
  fix_cross_before_scan = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fix_cross_before_scan', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "show_single_video_r"
  show_single_video_rClock = new util.Clock();
  // Initialize components for Routine "fix_cross_r_bq"
  fix_cross_r_bqClock = new util.Clock();
  fix_cross_before_question = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fix_cross_before_question', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "q_r"
  q_rClock = new util.Clock();
  left_image_question_for_know_or_not = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_image_question_for_know_or_not', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.46), 0], size : [0.86, 0.51],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  right_image_question_for_know_or_not = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_image_question_for_know_or_not', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.46, 0], size : [0.86, 0.51],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  key_question_for_know_or_not = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  txt_question_for_know_or_not = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_question_for_know_or_not',
    text: 'Which scene have you NOT seen?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  left_arrow_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_arrow_image', units : undefined, 
    image : 'media/pic/question_left_arrow.png', mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0.4], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  right_arrow_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_arrow_image', units : undefined, 
    image : 'media/pic/question_right_arrow.png', mask : undefined,
    ori : 0.0, pos : [0.5, 0.4], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  image_answer_green_square = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_answer_green_square', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  // Initialize components for Routine "a_r"
  a_rClock = new util.Clock();
  image_answer_for_know_or_not = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_answer_for_know_or_not', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.86, 0.51],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  txt_answer_for_know_or_not = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_answer_for_know_or_not',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('red'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "fix_cross_r_iq"
  fix_cross_r_iqClock = new util.Clock();
  fix_cross_question = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fix_cross_question', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "fix_cross_r_aq"
  fix_cross_r_aqClock = new util.Clock();
  fix_cross_after_question = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fix_cross_after_question', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "the_end"
  the_endClock = new util.Clock();
  the_end_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'the_end_txt',
    text: 'Press space key to end this experiment.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  the_end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var loop_instruction_r;
var currentLoop;
function loop_instruction_rLoopBegin(loop_instruction_rLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_instruction_r = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 100, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop_instruction_r'
    });
    psychoJS.experiment.addLoop(loop_instruction_r); // add the loop to the experiment
    currentLoop = loop_instruction_r;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_instruction_r of loop_instruction_r) {
      const snapshot = loop_instruction_r.getSnapshot();
      loop_instruction_rLoopScheduler.add(importConditions(snapshot));
      loop_instruction_rLoopScheduler.add(instruction_rRoutineBegin(snapshot));
      loop_instruction_rLoopScheduler.add(instruction_rRoutineEachFrame());
      loop_instruction_rLoopScheduler.add(instruction_rRoutineEnd());
      loop_instruction_rLoopScheduler.add(endLoopIteration(loop_instruction_rLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_instruction_rLoopEnd() {
  psychoJS.experiment.removeLoop(loop_instruction_r);

  return Scheduler.Event.NEXT;
}


var loop_videos;
function loop_videosLoopBegin(loop_videosLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_videos = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, (("conditions/groups/" + expInfo["participant"].toString()) + ".xlsx"), [Number.parseInt(expInfo["run"])]),
      seed: undefined, name: 'loop_videos'
    });
    psychoJS.experiment.addLoop(loop_videos); // add the loop to the experiment
    currentLoop = loop_videos;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_video of loop_videos) {
      const snapshot = loop_videos.getSnapshot();
      loop_videosLoopScheduler.add(importConditions(snapshot));
      loop_videosLoopScheduler.add(show_single_video_rRoutineBegin(snapshot));
      loop_videosLoopScheduler.add(show_single_video_rRoutineEachFrame());
      loop_videosLoopScheduler.add(show_single_video_rRoutineEnd());
      loop_videosLoopScheduler.add(fix_cross_r_bqRoutineBegin(snapshot));
      loop_videosLoopScheduler.add(fix_cross_r_bqRoutineEachFrame());
      loop_videosLoopScheduler.add(fix_cross_r_bqRoutineEnd());
      const loop_questionsLoopScheduler = new Scheduler(psychoJS);
      loop_videosLoopScheduler.add(loop_questionsLoopBegin(loop_questionsLoopScheduler, snapshot));
      loop_videosLoopScheduler.add(loop_questionsLoopScheduler);
      loop_videosLoopScheduler.add(loop_questionsLoopEnd);
      loop_videosLoopScheduler.add(fix_cross_r_aqRoutineBegin(snapshot));
      loop_videosLoopScheduler.add(fix_cross_r_aqRoutineEachFrame());
      loop_videosLoopScheduler.add(fix_cross_r_aqRoutineEnd());
      loop_videosLoopScheduler.add(endLoopIteration(loop_videosLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var loop_questions;
function loop_questionsLoopBegin(loop_questionsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_questions = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/question_conditions.xlsx',
      seed: undefined, name: 'loop_questions'
    });
    psychoJS.experiment.addLoop(loop_questions); // add the loop to the experiment
    currentLoop = loop_questions;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_question of loop_questions) {
      const snapshot = loop_questions.getSnapshot();
      loop_questionsLoopScheduler.add(importConditions(snapshot));
      loop_questionsLoopScheduler.add(q_rRoutineBegin(snapshot));
      loop_questionsLoopScheduler.add(q_rRoutineEachFrame());
      loop_questionsLoopScheduler.add(q_rRoutineEnd());
      loop_questionsLoopScheduler.add(a_rRoutineBegin(snapshot));
      loop_questionsLoopScheduler.add(a_rRoutineEachFrame());
      loop_questionsLoopScheduler.add(a_rRoutineEnd());
      loop_questionsLoopScheduler.add(fix_cross_r_iqRoutineBegin(snapshot));
      loop_questionsLoopScheduler.add(fix_cross_r_iqRoutineEachFrame());
      loop_questionsLoopScheduler.add(fix_cross_r_iqRoutineEnd());
      loop_questionsLoopScheduler.add(endLoopIteration(loop_questionsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_questionsLoopEnd() {
  psychoJS.experiment.removeLoop(loop_questions);

  return Scheduler.Event.NEXT;
}


async function loop_videosLoopEnd() {
  psychoJS.experiment.removeLoop(loop_videos);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _instruction_key_allKeys;
var instruction_rComponents;
function instruction_rRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instruction_r'-------
    t = 0;
    instruction_rClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instruction_img.setImage((("instruction/instruction_" + current_instruction.toString()) + ".png"));
    instruction_key.keys = undefined;
    instruction_key.rt = undefined;
    _instruction_key_allKeys = [];
    // keep track of which components have finished
    instruction_rComponents = [];
    instruction_rComponents.push(instruction_img);
    instruction_rComponents.push(instruction_key);
    
    for (const thisComponent of instruction_rComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction_rRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instruction_r'-------
    // get current time
    t = instruction_rClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_img* updates
    if (t >= 0.0 && instruction_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_img.tStart = t;  // (not accounting for frame time here)
      instruction_img.frameNStart = frameN;  // exact frame index
      
      instruction_img.setAutoDraw(true);
    }

    
    // *instruction_key* updates
    if (t >= 0.0 && instruction_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_key.tStart = t;  // (not accounting for frame time here)
      instruction_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruction_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruction_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruction_key.clearEvents(); });
    }

    if (instruction_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruction_key.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _instruction_key_allKeys = _instruction_key_allKeys.concat(theseKeys);
      if (_instruction_key_allKeys.length > 0) {
        instruction_key.keys = _instruction_key_allKeys[_instruction_key_allKeys.length - 1].name;  // just the last key pressed
        instruction_key.rt = _instruction_key_allKeys[_instruction_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_rComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction_rRoutineEnd() {
  return async function () {
    //------Ending Routine 'instruction_r'-------
    for (const thisComponent of instruction_rComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction_key.keys', instruction_key.keys);
    if (typeof instruction_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruction_key.rt', instruction_key.rt);
        routineTimer.reset();
        }
    
    instruction_key.stop();
    // the Routine "instruction_r" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _wait_for_start_key_allKeys;
var wait_for_startComponents;
function wait_for_startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'wait_for_start'-------
    t = 0;
    wait_for_startClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    wait_for_start_key.keys = undefined;
    wait_for_start_key.rt = undefined;
    _wait_for_start_key_allKeys = [];
    // keep track of which components have finished
    wait_for_startComponents = [];
    wait_for_startComponents.push(wait_for_start_txt);
    wait_for_startComponents.push(wait_for_start_key);
    
    for (const thisComponent of wait_for_startComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function wait_for_startRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'wait_for_start'-------
    // get current time
    t = wait_for_startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *wait_for_start_txt* updates
    if (t >= 0.0 && wait_for_start_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wait_for_start_txt.tStart = t;  // (not accounting for frame time here)
      wait_for_start_txt.frameNStart = frameN;  // exact frame index
      
      wait_for_start_txt.setAutoDraw(true);
    }

    
    // *wait_for_start_key* updates
    if (t >= 0.0 && wait_for_start_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wait_for_start_key.tStart = t;  // (not accounting for frame time here)
      wait_for_start_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { wait_for_start_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { wait_for_start_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { wait_for_start_key.clearEvents(); });
    }

    if (wait_for_start_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = wait_for_start_key.getKeys({keyList: ['t', 'space'], waitRelease: false});
      _wait_for_start_key_allKeys = _wait_for_start_key_allKeys.concat(theseKeys);
      if (_wait_for_start_key_allKeys.length > 0) {
        wait_for_start_key.keys = _wait_for_start_key_allKeys.map((key) => key.name);  // storing all keys
        wait_for_start_key.rt = _wait_for_start_key_allKeys.map((key) => key.rt);
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wait_for_startComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wait_for_startRoutineEnd() {
  return async function () {
    //------Ending Routine 'wait_for_start'-------
    for (const thisComponent of wait_for_startComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('wait_for_start_key.keys', wait_for_start_key.keys);
    if (typeof wait_for_start_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('wait_for_start_key.rt', wait_for_start_key.rt);
        routineTimer.reset();
        }
    
    wait_for_start_key.stop();
    // the Routine "wait_for_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fix_cross_r_scanComponents;
function fix_cross_r_scanRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fix_cross_r_scan'-------
    t = 0;
    fix_cross_r_scanClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fix_cross_r_scanComponents = [];
    fix_cross_r_scanComponents.push(fix_cross_before_scan);
    
    for (const thisComponent of fix_cross_r_scanComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fix_cross_r_scanRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fix_cross_r_scan'-------
    // get current time
    t = fix_cross_r_scanClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_cross_before_scan* updates
    if (t >= 0.0 && fix_cross_before_scan.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_cross_before_scan.tStart = t;  // (not accounting for frame time here)
      fix_cross_before_scan.frameNStart = frameN;  // exact frame index
      
      fix_cross_before_scan.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_cross_before_scan.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_cross_before_scan.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fix_cross_r_scanComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix_cross_r_scanRoutineEnd() {
  return async function () {
    //------Ending Routine 'fix_cross_r_scan'-------
    for (const thisComponent of fix_cross_r_scanComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var show_single_clipClock;
var show_single_clip;
var show_single_video_rComponents;
function show_single_video_rRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'show_single_video_r'-------
    t = 0;
    show_single_video_rClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    show_single_clipClock = new util.Clock();
    show_single_clip = new visual.MovieStim({
      win: psychoJS.window,
      name: 'show_single_clip',
      units: undefined,
      movie: (("media/videos/" + town_weather_name.toString()) + ".mp4"),
      pos: [0, 0],
      size: undefined,
      ori: 0.0,
      opacity: undefined,
      loop: false,
      noAudio: false,
      });
    thisExp.addData('wait_for_start_end_routine', globalClock.getTime())
    
    // keep track of which components have finished
    show_single_video_rComponents = [];
    show_single_video_rComponents.push(show_single_clip);
    
    for (const thisComponent of show_single_video_rComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function show_single_video_rRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'show_single_video_r'-------
    // get current time
    t = show_single_video_rClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *show_single_clip* updates
    if (t >= 0.0 && show_single_clip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      show_single_clip.tStart = t;  // (not accounting for frame time here)
      show_single_clip.frameNStart = frameN;  // exact frame index
      
      show_single_clip.setAutoDraw(true);
      show_single_clip.play();
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (show_single_clip.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      show_single_clip.setAutoDraw(false);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of show_single_video_rComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function show_single_video_rRoutineEnd() {
  return async function () {
    //------Ending Routine 'show_single_video_r'-------
    for (const thisComponent of show_single_video_rComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    show_single_clip.stop();
    return Scheduler.Event.NEXT;
  };
}


var fix_cross_r_bqComponents;
function fix_cross_r_bqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fix_cross_r_bq'-------
    t = 0;
    fix_cross_r_bqClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fix_cross_r_bqComponents = [];
    fix_cross_r_bqComponents.push(fix_cross_before_question);
    
    for (const thisComponent of fix_cross_r_bqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fix_cross_r_bqRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fix_cross_r_bq'-------
    // get current time
    t = fix_cross_r_bqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_cross_before_question* updates
    if (t >= 0.0 && fix_cross_before_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_cross_before_question.tStart = t;  // (not accounting for frame time here)
      fix_cross_before_question.frameNStart = frameN;  // exact frame index
      
      fix_cross_before_question.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_cross_before_question.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_cross_before_question.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fix_cross_r_bqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix_cross_r_bqRoutineEnd() {
  return async function () {
    //------Ending Routine 'fix_cross_r_bq'-------
    for (const thisComponent of fix_cross_r_bqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_question_for_know_or_not_allKeys;
var q_rComponents;
function q_rRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'q_r'-------
    t = 0;
    q_rClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    key_question_for_know_or_not.keys = undefined;
    key_question_for_know_or_not.rt = undefined;
    _key_question_for_know_or_not_allKeys = [];
    // keep track of which components have finished
    q_rComponents = [];
    q_rComponents.push(left_image_question_for_know_or_not);
    q_rComponents.push(right_image_question_for_know_or_not);
    q_rComponents.push(key_question_for_know_or_not);
    q_rComponents.push(txt_question_for_know_or_not);
    q_rComponents.push(left_arrow_image);
    q_rComponents.push(right_arrow_image);
    q_rComponents.push(image_answer_green_square);
    
    for (const thisComponent of q_rComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function q_rRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'q_r'-------
    // get current time
    t = q_rClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *left_image_question_for_know_or_not* updates
    if (t >= 0 && left_image_question_for_know_or_not.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_image_question_for_know_or_not.tStart = t;  // (not accounting for frame time here)
      left_image_question_for_know_or_not.frameNStart = frameN;  // exact frame index
      
      left_image_question_for_know_or_not.setAutoDraw(true);
    }

    frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left_image_question_for_know_or_not.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left_image_question_for_know_or_not.setAutoDraw(false);
    }
    
    // *right_image_question_for_know_or_not* updates
    if (t >= 0.0 && right_image_question_for_know_or_not.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_image_question_for_know_or_not.tStart = t;  // (not accounting for frame time here)
      right_image_question_for_know_or_not.frameNStart = frameN;  // exact frame index
      
      right_image_question_for_know_or_not.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right_image_question_for_know_or_not.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right_image_question_for_know_or_not.setAutoDraw(false);
    }
    
    // *key_question_for_know_or_not* updates
    if (t >= 0 && key_question_for_know_or_not.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_question_for_know_or_not.tStart = t;  // (not accounting for frame time here)
      key_question_for_know_or_not.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_question_for_know_or_not.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_question_for_know_or_not.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_question_for_know_or_not.clearEvents(); });
    }

    frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_question_for_know_or_not.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_question_for_know_or_not.status = PsychoJS.Status.FINISHED;
  }

    if (key_question_for_know_or_not.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_question_for_know_or_not.getKeys({keyList: ['left', 'right', '1', '2', '3', '4'], waitRelease: false});
      _key_question_for_know_or_not_allKeys = _key_question_for_know_or_not_allKeys.concat(theseKeys);
      if (_key_question_for_know_or_not_allKeys.length > 0) {
        key_question_for_know_or_not.keys = _key_question_for_know_or_not_allKeys[_key_question_for_know_or_not_allKeys.length - 1].name;  // just the last key pressed
        key_question_for_know_or_not.rt = _key_question_for_know_or_not_allKeys[_key_question_for_know_or_not_allKeys.length - 1].rt;
        // was this correct?
        if (key_question_for_know_or_not.keys == correct_answer) {
            key_question_for_know_or_not.corr = 1;
        } else {
            key_question_for_know_or_not.corr = 0;
        }
      }
    }
    
    
    // *txt_question_for_know_or_not* updates
    if (t >= 0.0 && txt_question_for_know_or_not.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_question_for_know_or_not.tStart = t;  // (not accounting for frame time here)
      txt_question_for_know_or_not.frameNStart = frameN;  // exact frame index
      
      txt_question_for_know_or_not.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (txt_question_for_know_or_not.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      txt_question_for_know_or_not.setAutoDraw(false);
    }
    
    // *left_arrow_image* updates
    if (t >= 0.0 && left_arrow_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_arrow_image.tStart = t;  // (not accounting for frame time here)
      left_arrow_image.frameNStart = frameN;  // exact frame index
      
      left_arrow_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left_arrow_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left_arrow_image.setAutoDraw(false);
    }
    
    // *right_arrow_image* updates
    if (t >= 0.0 && right_arrow_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_arrow_image.tStart = t;  // (not accounting for frame time here)
      right_arrow_image.frameNStart = frameN;  // exact frame index
      
      right_arrow_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right_arrow_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right_arrow_image.setAutoDraw(false);
    }
    image_answer_green_square.i;
    
    
    // *image_answer_green_square* updates
    if (t >= 0.0 && image_answer_green_square.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_answer_green_square.tStart = t;  // (not accounting for frame time here)
      image_answer_green_square.frameNStart = frameN;  // exact frame index
      
      image_answer_green_square.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_answer_green_square.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_answer_green_square.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of q_rComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function q_rRoutineEnd() {
  return async function () {
    //------Ending Routine 'q_r'-------
    for (const thisComponent of q_rComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_question_for_know_or_not.keys === undefined) {
      if (['None','none',undefined].includes(correct_answer)) {
         key_question_for_know_or_not.corr = 1;  // correct non-response
      } else {
         key_question_for_know_or_not.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('key_question_for_know_or_not.keys', key_question_for_know_or_not.keys);
    psychoJS.experiment.addData('key_question_for_know_or_not.corr', key_question_for_know_or_not.corr);
    if (typeof key_question_for_know_or_not.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_question_for_know_or_not.rt', key_question_for_know_or_not.rt);
        }
    
    key_question_for_know_or_not.stop();
    return Scheduler.Event.NEXT;
  };
}


var a_rComponents;
function a_rRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'a_r'-------
    t = 0;
    a_rClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    a_rComponents = [];
    a_rComponents.push(image_answer_for_know_or_not);
    a_rComponents.push(txt_answer_for_know_or_not);
    
    for (const thisComponent of a_rComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function a_rRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'a_r'-------
    // get current time
    t = a_rClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_answer_for_know_or_not* updates
    if (t >= 0.0 && image_answer_for_know_or_not.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_answer_for_know_or_not.tStart = t;  // (not accounting for frame time here)
      image_answer_for_know_or_not.frameNStart = frameN;  // exact frame index
      
      image_answer_for_know_or_not.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_answer_for_know_or_not.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_answer_for_know_or_not.setAutoDraw(false);
    }
    
    // *txt_answer_for_know_or_not* updates
    if (t >= 0.0 && txt_answer_for_know_or_not.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_answer_for_know_or_not.tStart = t;  // (not accounting for frame time here)
      txt_answer_for_know_or_not.frameNStart = frameN;  // exact frame index
      
      txt_answer_for_know_or_not.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (txt_answer_for_know_or_not.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      txt_answer_for_know_or_not.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of a_rComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function a_rRoutineEnd() {
  return async function () {
    //------Ending Routine 'a_r'-------
    for (const thisComponent of a_rComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var fix_cross_r_iqComponents;
function fix_cross_r_iqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fix_cross_r_iq'-------
    t = 0;
    fix_cross_r_iqClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fix_cross_r_iqComponents = [];
    fix_cross_r_iqComponents.push(fix_cross_question);
    
    for (const thisComponent of fix_cross_r_iqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fix_cross_r_iqRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fix_cross_r_iq'-------
    // get current time
    t = fix_cross_r_iqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_cross_question* updates
    if (t >= 0.0 && fix_cross_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_cross_question.tStart = t;  // (not accounting for frame time here)
      fix_cross_question.frameNStart = frameN;  // exact frame index
      
      fix_cross_question.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_cross_question.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_cross_question.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fix_cross_r_iqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix_cross_r_iqRoutineEnd() {
  return async function () {
    //------Ending Routine 'fix_cross_r_iq'-------
    for (const thisComponent of fix_cross_r_iqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var fix_cross_r_aqComponents;
function fix_cross_r_aqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fix_cross_r_aq'-------
    t = 0;
    fix_cross_r_aqClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fix_cross_r_aqComponents = [];
    fix_cross_r_aqComponents.push(fix_cross_after_question);
    
    for (const thisComponent of fix_cross_r_aqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fix_cross_r_aqRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fix_cross_r_aq'-------
    // get current time
    t = fix_cross_r_aqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_cross_after_question* updates
    if (t >= 0.0 && fix_cross_after_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_cross_after_question.tStart = t;  // (not accounting for frame time here)
      fix_cross_after_question.frameNStart = frameN;  // exact frame index
      
      fix_cross_after_question.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_cross_after_question.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_cross_after_question.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fix_cross_r_aqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix_cross_r_aqRoutineEnd() {
  return async function () {
    //------Ending Routine 'fix_cross_r_aq'-------
    for (const thisComponent of fix_cross_r_aqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _the_end_key_allKeys;
var the_endComponents;
function the_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'the_end'-------
    t = 0;
    the_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    the_end_key.keys = undefined;
    the_end_key.rt = undefined;
    _the_end_key_allKeys = [];
    // keep track of which components have finished
    the_endComponents = [];
    the_endComponents.push(the_end_txt);
    the_endComponents.push(the_end_key);
    
    for (const thisComponent of the_endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function the_endRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'the_end'-------
    // get current time
    t = the_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *the_end_txt* updates
    if (t >= 0.0 && the_end_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      the_end_txt.tStart = t;  // (not accounting for frame time here)
      the_end_txt.frameNStart = frameN;  // exact frame index
      
      the_end_txt.setAutoDraw(true);
    }

    
    // *the_end_key* updates
    if (t >= 0.0 && the_end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      the_end_key.tStart = t;  // (not accounting for frame time here)
      the_end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { the_end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { the_end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { the_end_key.clearEvents(); });
    }

    if (the_end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = the_end_key.getKeys({keyList: ['space'], waitRelease: false});
      _the_end_key_allKeys = _the_end_key_allKeys.concat(theseKeys);
      if (_the_end_key_allKeys.length > 0) {
        the_end_key.keys = _the_end_key_allKeys[_the_end_key_allKeys.length - 1].name;  // just the last key pressed
        the_end_key.rt = _the_end_key_allKeys[_the_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of the_endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function the_endRoutineEnd() {
  return async function () {
    //------Ending Routine 'the_end'-------
    for (const thisComponent of the_endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('the_end_key.keys', the_end_key.keys);
    if (typeof the_end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('the_end_key.rt', the_end_key.rt);
        routineTimer.reset();
        }
    
    the_end_key.stop();
    // the Routine "the_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
