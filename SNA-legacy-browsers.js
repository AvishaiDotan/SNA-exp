/************ 
 * Sna Test *
 ************/


// store info about the experiment session:
let expName = 'SNA';  // from the Builder filename that created this script
let expInfo = {'Group': '', 'participant': ''};

// Start code blocks for 'Before Experiment'
window.cardWidthPX;
window.px2mm;
window.center = 900 * 0.5;
window.dotX = [];
window.cardAspectRatio = 817 / 1284;
window.cardWidthPXMax = window.center * 2;
window.cardWidthMM = 85.6;


function rounder(value, decimals = 2) {
  return Number(Math.round(`${value}e${decimals}`) + `e-${decimals}`);
}

        // add-on: list(s: string): string[]
        
function list(s) {
            // if s is a string, we return a list of its characters
            if (typeof s === 'string')
                return s.split('');
            else
                // otherwise we return s:
                return s;
        }

        
function split(word) {
    return list(word);
}

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
flowScheduler.add(InitRoutineBegin());
flowScheduler.add(InitRoutineEachFrame());
flowScheduler.add(InitRoutineEnd());
const Inst_Loop01LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Inst_Loop01LoopBegin(Inst_Loop01LoopScheduler));
flowScheduler.add(Inst_Loop01LoopScheduler);
flowScheduler.add(Inst_Loop01LoopEnd);
flowScheduler.add(Animation01RoutineBegin());
flowScheduler.add(Animation01RoutineEachFrame());
flowScheduler.add(Animation01RoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
flowScheduler.add(estimate_screen_sizeRoutineBegin());
flowScheduler.add(estimate_screen_sizeRoutineEachFrame());
flowScheduler.add(estimate_screen_sizeRoutineEnd());
flowScheduler.add(ResultsRoutineBegin());
flowScheduler.add(ResultsRoutineEachFrame());
flowScheduler.add(ResultsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(Init_CounterRoutineBegin());
flowScheduler.add(Init_CounterRoutineEachFrame());
flowScheduler.add(Init_CounterRoutineEnd());
flowScheduler.add(Block_iNTSRoutineBegin());
flowScheduler.add(Block_iNTSRoutineEachFrame());
flowScheduler.add(Block_iNTSRoutineEnd());
const Practice_First_ConLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Practice_First_ConLoopBegin(Practice_First_ConLoopScheduler));
flowScheduler.add(Practice_First_ConLoopScheduler);
flowScheduler.add(Practice_First_ConLoopEnd);
flowScheduler.add(Block_iNTSRoutineBegin());
flowScheduler.add(Block_iNTSRoutineEachFrame());
flowScheduler.add(Block_iNTSRoutineEnd());
const First_CondLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(First_CondLoopBegin(First_CondLoopScheduler));
flowScheduler.add(First_CondLoopScheduler);
flowScheduler.add(First_CondLoopEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
const Practice_second_ConLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Practice_second_ConLoopBegin(Practice_second_ConLoopScheduler));
flowScheduler.add(Practice_second_ConLoopScheduler);
flowScheduler.add(Practice_second_ConLoopEnd);
flowScheduler.add(Block_iNTSRoutineBegin());
flowScheduler.add(Block_iNTSRoutineEachFrame());
flowScheduler.add(Block_iNTSRoutineEnd());
const Second_ConLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Second_ConLoopBegin(Second_ConLoopScheduler));
flowScheduler.add(Second_ConLoopScheduler);
flowScheduler.add(Second_ConLoopEnd);
const trials_7LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_7LoopBegin(trials_7LoopScheduler));
flowScheduler.add(trials_7LoopScheduler);
flowScheduler.add(trials_7LoopEnd);
const Practice_Third_ConLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Practice_Third_ConLoopBegin(Practice_Third_ConLoopScheduler));
flowScheduler.add(Practice_Third_ConLoopScheduler);
flowScheduler.add(Practice_Third_ConLoopEnd);
flowScheduler.add(Block_iNTSRoutineBegin());
flowScheduler.add(Block_iNTSRoutineEachFrame());
flowScheduler.add(Block_iNTSRoutineEnd());
const Third_ConLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Third_ConLoopBegin(Third_ConLoopScheduler));
flowScheduler.add(Third_ConLoopScheduler);
flowScheduler.add(Third_ConLoopEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
const Practice_Forth_ConLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Practice_Forth_ConLoopBegin(Practice_Forth_ConLoopScheduler));
flowScheduler.add(Practice_Forth_ConLoopScheduler);
flowScheduler.add(Practice_Forth_ConLoopEnd);
flowScheduler.add(Block_iNTSRoutineBegin());
flowScheduler.add(Block_iNTSRoutineEachFrame());
flowScheduler.add(Block_iNTSRoutineEnd());
const Forth_ConLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Forth_ConLoopBegin(Forth_ConLoopScheduler));
flowScheduler.add(Forth_ConLoopScheduler);
flowScheduler.add(Forth_ConLoopEnd);
flowScheduler.add(Block_iNTSRoutineBegin());
flowScheduler.add(Block_iNTSRoutineEachFrame());
flowScheduler.add(Block_iNTSRoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
flowScheduler.add(_Count_SideRoutineBegin());
flowScheduler.add(_Count_SideRoutineEachFrame());
flowScheduler.add(_Count_SideRoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'EXP_DATA/Conditions/SNA/con1.xlsx', 'path': 'EXP_DATA/Conditions/SNA/con1.xlsx'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/3.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/3.JPG'},
    {'name': 'EXP_DATA/Card/card.png', 'path': 'EXP_DATA/Card/card.png'},
    {'name': 'EXP_DATA/Arrows/2.png', 'path': 'EXP_DATA/Arrows/2.png'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/3/1.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/3/1.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/3/2.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/3/2.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/3/3.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/3/3.JPG'},
    {'name': 'EXP_DATA/Instructions/Credit_Animation.mp4', 'path': 'EXP_DATA/Instructions/Credit_Animation.mp4'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/1/1.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/1/1.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/6.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/6.JPG'},
    {'name': 'EXP_DATA/Arrows/1`.png', 'path': 'EXP_DATA/Arrows/1`.png'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/2/1.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/2/1.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/8.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/8.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/1.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/1.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/1/3.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/1/3.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/4.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/4.JPG'},
    {'name': 'EXP_DATA/Arrows/Full.png', 'path': 'EXP_DATA/Arrows/Full.png'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/2.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/2.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/5.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/5.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/9.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/9.JPG'},
    {'name': 'EXP_DATA/Conditions/SNA/con4.xlsx', 'path': 'EXP_DATA/Conditions/SNA/con4.xlsx'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/2/2.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/2/2.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/11.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/11.JPG'},
    {'name': 'EXP_DATA/Conditions/SNA/con3.xlsx', 'path': 'EXP_DATA/Conditions/SNA/con3.xlsx'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/4/1.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/4/1.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/4/2.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/4/2.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/7.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/7.JPG'},
    {'name': 'EXP_DATA/Arrows/Arrow.png', 'path': 'EXP_DATA/Arrows/Arrow.png'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/1/2.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/1/2.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/2/3.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/2/3.JPG'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/4/3.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/4/3.JPG'},
    {'name': 'EXP_DATA/Conditions/SNA/con2.xlsx', 'path': 'EXP_DATA/Conditions/SNA/con2.xlsx'},
    {'name': 'EXP_DATA/Instructions/Inst_Image/10.JPG', 'path': 'EXP_DATA/Instructions/Inst_Image/10.JPG'},
    {'name': 'EXP_DATA/Arrows/Cutout.png', 'path': 'EXP_DATA/Arrows/Cutout.png'}
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


var InitClock;
var InstructionsClock;
var inst_ImageCount;
var inst_Image;
var Inst_key;
var Animation01Clock;
var Animation01_VideoClock;
var Animation01_Video;
var Animation01_Key;
var Animation01_text;
var estimate_screen_sizeClock;
var card;
var slider;
var key_resp_2;
var ResultsClock;
var Res_text;
var key_resp_4;
var Results_Text_Cont;
var Hcm;
var Init_CounterClock;
var Block_iNTSClock;
var Block_n;
var Inst_n;
var inst_Image_2;
var Inst_key_2;
var ConditionClock;
var Fixation;
var image;
var text;
var C_Response;
var Arrow_Image;
var Blank_3Clock;
var Blank;
var text_4;
var text_5;
var _Count_SideClock;
var Cir1_3;
var Cir2_3;
var Cir3_3;
var Cir4_3;
var mouse_3;
var key_resp_8;
var mouse_click_locations;
var Fini_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Init"
  InitClock = new util.Clock();
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  inst_ImageCount = 1;
  
  inst_Image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'inst_Image', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.88, 0.66],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  Inst_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Animation01"
  Animation01Clock = new util.Clock();
  Animation01_VideoClock = new util.Clock();
  Animation01_Video = new visual.MovieStim({
    win: psychoJS.window,
    name: 'Animation01_Video',
    units: 'height',
    movie: 'EXP_DATA/Instructions/Credit_Animation.mp4',
    pos: [0, 0],
    size: [0.9, 0.5],
    ori: 0.0,
    opacity: undefined,
    loop: true,
    noAudio: false,
    });
  Animation01_Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Animation01_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Animation01_text',
    text: 'לחץ על כל מקש להמשך',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, (- 0.35)], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "estimate_screen_size"
  estimate_screen_sizeClock = new util.Clock();
  card = new visual.ImageStim({
    win : psychoJS.window,
    name : 'card', units : 'pix', 
    image : 'EXP_DATA/Card/card.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [450, (450 * (817 / 1284))],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [1.0, 0.1], pos: [0, (- 0.4)], units: 'height',
    labels: undefined, ticks: [0, 1],
    granularity: (0.001), style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('yellow'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Results"
  ResultsClock = new util.Clock();
  
  
  Res_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Res_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Results_Text_Cont = new visual.TextStim({
    win: psychoJS.window,
    name: 'Results_Text_Cont',
    text: 'לחץ על כל מקש להמשך',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, (- 0.35)], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  Hcm = 0;
  
  // Initialize components for Routine "Init_Counter"
  Init_CounterClock = new util.Clock();
  // Initialize components for Routine "Block_iNTS"
  Block_iNTSClock = new util.Clock();
  Block_n = 1;
  Inst_n = 1;
  
  inst_Image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'inst_Image_2', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.88, 0.66],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  Inst_key_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Condition"
  ConditionClock = new util.Clock();
  Fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  C_Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Arrow_Image = "EXP_DATA/Arrows/Cutout.png";
  
  // Initialize components for Routine "Blank_3"
  Blank_3Clock = new util.Clock();
  Blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'Blank',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "_Count_Side"
  _Count_SideClock = new util.Clock();
  Cir1_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'Cir1_3', units : 'height', 
    edges: 100, size:0.3,
    ori: 0.0, pos: [(- 0.675), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: 0, interpolate: true,
  });
  
  Cir2_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'Cir2_3', units : 'height', 
    edges: 100, size:0.3,
    ori: 0.0, pos: [(- 0.225), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  Cir3_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'Cir3_3', units : 'height', 
    edges: 100, size:0.3,
    ori: 0.0, pos: [0.225, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -2, interpolate: true,
  });
  
  Cir4_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'Cir4_3', units : 'height', 
    edges: 100, size:0.3,
    ori: 0.0, pos: [0.675, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -3, interpolate: true,
  });
  
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse_click_locations = [];
  
  Fini_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fini_text',
    text: '',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, (- 0.35)], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var InitComponents;
function InitRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Init'-------
    t = 0;
    InitClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    InitComponents = [];
    
    InitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InitRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Init'-------
    // get current time
    t = InitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InitRoutineEnd() {
  return async function () {
    //------Ending Routine 'Init'-------
    InitComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Init" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Inst_Loop01;
var currentLoop;
function Inst_Loop01LoopBegin(Inst_Loop01LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Inst_Loop01 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'Inst_Loop01'
    });
    psychoJS.experiment.addLoop(Inst_Loop01); // add the loop to the experiment
    currentLoop = Inst_Loop01;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Inst_Loop01.forEach(function() {
      const snapshot = Inst_Loop01.getSnapshot();
    
      Inst_Loop01LoopScheduler.add(importConditions(snapshot));
      Inst_Loop01LoopScheduler.add(InstructionsRoutineBegin(snapshot));
      Inst_Loop01LoopScheduler.add(InstructionsRoutineEachFrame());
      Inst_Loop01LoopScheduler.add(InstructionsRoutineEnd());
      Inst_Loop01LoopScheduler.add(endLoopIteration(Inst_Loop01LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Inst_Loop01LoopEnd() {
  psychoJS.experiment.removeLoop(Inst_Loop01);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(InstructionsRoutineBegin(snapshot));
      trialsLoopScheduler.add(InstructionsRoutineEachFrame());
      trialsLoopScheduler.add(InstructionsRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var Practice_First_Con;
function Practice_First_ConLoopBegin(Practice_First_ConLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Practice_First_Con = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con1,
      seed: undefined, name: 'Practice_First_Con'
    });
    psychoJS.experiment.addLoop(Practice_First_Con); // add the loop to the experiment
    currentLoop = Practice_First_Con;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Practice_First_Con.forEach(function() {
      const snapshot = Practice_First_Con.getSnapshot();
    
      Practice_First_ConLoopScheduler.add(importConditions(snapshot));
      Practice_First_ConLoopScheduler.add(ConditionRoutineBegin(snapshot));
      Practice_First_ConLoopScheduler.add(ConditionRoutineEachFrame());
      Practice_First_ConLoopScheduler.add(ConditionRoutineEnd());
      Practice_First_ConLoopScheduler.add(Blank_3RoutineBegin(snapshot));
      Practice_First_ConLoopScheduler.add(Blank_3RoutineEachFrame());
      Practice_First_ConLoopScheduler.add(Blank_3RoutineEnd());
      Practice_First_ConLoopScheduler.add(endLoopIteration(Practice_First_ConLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Practice_First_ConLoopEnd() {
  psychoJS.experiment.removeLoop(Practice_First_Con);

  return Scheduler.Event.NEXT;
}


var First_Cond;
function First_CondLoopBegin(First_CondLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    First_Cond = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 8, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con1,
      seed: undefined, name: 'First_Cond'
    });
    psychoJS.experiment.addLoop(First_Cond); // add the loop to the experiment
    currentLoop = First_Cond;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    First_Cond.forEach(function() {
      const snapshot = First_Cond.getSnapshot();
    
      First_CondLoopScheduler.add(importConditions(snapshot));
      First_CondLoopScheduler.add(ConditionRoutineBegin(snapshot));
      First_CondLoopScheduler.add(ConditionRoutineEachFrame());
      First_CondLoopScheduler.add(ConditionRoutineEnd());
      First_CondLoopScheduler.add(endLoopIteration(First_CondLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function First_CondLoopEnd() {
  psychoJS.experiment.removeLoop(First_Cond);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      const snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(Block_iNTSRoutineBegin(snapshot));
      trials_2LoopScheduler.add(Block_iNTSRoutineEachFrame());
      trials_2LoopScheduler.add(Block_iNTSRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var Practice_second_Con;
function Practice_second_ConLoopBegin(Practice_second_ConLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Practice_second_Con = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con2,
      seed: undefined, name: 'Practice_second_Con'
    });
    psychoJS.experiment.addLoop(Practice_second_Con); // add the loop to the experiment
    currentLoop = Practice_second_Con;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Practice_second_Con.forEach(function() {
      const snapshot = Practice_second_Con.getSnapshot();
    
      Practice_second_ConLoopScheduler.add(importConditions(snapshot));
      Practice_second_ConLoopScheduler.add(ConditionRoutineBegin(snapshot));
      Practice_second_ConLoopScheduler.add(ConditionRoutineEachFrame());
      Practice_second_ConLoopScheduler.add(ConditionRoutineEnd());
      Practice_second_ConLoopScheduler.add(Blank_3RoutineBegin(snapshot));
      Practice_second_ConLoopScheduler.add(Blank_3RoutineEachFrame());
      Practice_second_ConLoopScheduler.add(Blank_3RoutineEnd());
      Practice_second_ConLoopScheduler.add(endLoopIteration(Practice_second_ConLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Practice_second_ConLoopEnd() {
  psychoJS.experiment.removeLoop(Practice_second_Con);

  return Scheduler.Event.NEXT;
}


var Second_Con;
function Second_ConLoopBegin(Second_ConLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Second_Con = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 8, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con2,
      seed: undefined, name: 'Second_Con'
    });
    psychoJS.experiment.addLoop(Second_Con); // add the loop to the experiment
    currentLoop = Second_Con;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Second_Con.forEach(function() {
      const snapshot = Second_Con.getSnapshot();
    
      Second_ConLoopScheduler.add(importConditions(snapshot));
      Second_ConLoopScheduler.add(ConditionRoutineBegin(snapshot));
      Second_ConLoopScheduler.add(ConditionRoutineEachFrame());
      Second_ConLoopScheduler.add(ConditionRoutineEnd());
      Second_ConLoopScheduler.add(endLoopIteration(Second_ConLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Second_ConLoopEnd() {
  psychoJS.experiment.removeLoop(Second_Con);

  return Scheduler.Event.NEXT;
}


var trials_7;
function trials_7LoopBegin(trials_7LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_7 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_7'
    });
    psychoJS.experiment.addLoop(trials_7); // add the loop to the experiment
    currentLoop = trials_7;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_7.forEach(function() {
      const snapshot = trials_7.getSnapshot();
    
      trials_7LoopScheduler.add(importConditions(snapshot));
      trials_7LoopScheduler.add(Block_iNTSRoutineBegin(snapshot));
      trials_7LoopScheduler.add(Block_iNTSRoutineEachFrame());
      trials_7LoopScheduler.add(Block_iNTSRoutineEnd());
      trials_7LoopScheduler.add(endLoopIteration(trials_7LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_7LoopEnd() {
  psychoJS.experiment.removeLoop(trials_7);

  return Scheduler.Event.NEXT;
}


var Practice_Third_Con;
function Practice_Third_ConLoopBegin(Practice_Third_ConLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Practice_Third_Con = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con3,
      seed: undefined, name: 'Practice_Third_Con'
    });
    psychoJS.experiment.addLoop(Practice_Third_Con); // add the loop to the experiment
    currentLoop = Practice_Third_Con;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Practice_Third_Con.forEach(function() {
      const snapshot = Practice_Third_Con.getSnapshot();
    
      Practice_Third_ConLoopScheduler.add(importConditions(snapshot));
      Practice_Third_ConLoopScheduler.add(ConditionRoutineBegin(snapshot));
      Practice_Third_ConLoopScheduler.add(ConditionRoutineEachFrame());
      Practice_Third_ConLoopScheduler.add(ConditionRoutineEnd());
      Practice_Third_ConLoopScheduler.add(Blank_3RoutineBegin(snapshot));
      Practice_Third_ConLoopScheduler.add(Blank_3RoutineEachFrame());
      Practice_Third_ConLoopScheduler.add(Blank_3RoutineEnd());
      Practice_Third_ConLoopScheduler.add(endLoopIteration(Practice_Third_ConLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Practice_Third_ConLoopEnd() {
  psychoJS.experiment.removeLoop(Practice_Third_Con);

  return Scheduler.Event.NEXT;
}


var Third_Con;
function Third_ConLoopBegin(Third_ConLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Third_Con = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 8, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con3,
      seed: undefined, name: 'Third_Con'
    });
    psychoJS.experiment.addLoop(Third_Con); // add the loop to the experiment
    currentLoop = Third_Con;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Third_Con.forEach(function() {
      const snapshot = Third_Con.getSnapshot();
    
      Third_ConLoopScheduler.add(importConditions(snapshot));
      Third_ConLoopScheduler.add(ConditionRoutineBegin(snapshot));
      Third_ConLoopScheduler.add(ConditionRoutineEachFrame());
      Third_ConLoopScheduler.add(ConditionRoutineEnd());
      Third_ConLoopScheduler.add(endLoopIteration(Third_ConLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Third_ConLoopEnd() {
  psychoJS.experiment.removeLoop(Third_Con);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_3.forEach(function() {
      const snapshot = trials_3.getSnapshot();
    
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(Block_iNTSRoutineBegin(snapshot));
      trials_3LoopScheduler.add(Block_iNTSRoutineEachFrame());
      trials_3LoopScheduler.add(Block_iNTSRoutineEnd());
      trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var Practice_Forth_Con;
function Practice_Forth_ConLoopBegin(Practice_Forth_ConLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Practice_Forth_Con = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con4,
      seed: undefined, name: 'Practice_Forth_Con'
    });
    psychoJS.experiment.addLoop(Practice_Forth_Con); // add the loop to the experiment
    currentLoop = Practice_Forth_Con;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Practice_Forth_Con.forEach(function() {
      const snapshot = Practice_Forth_Con.getSnapshot();
    
      Practice_Forth_ConLoopScheduler.add(importConditions(snapshot));
      Practice_Forth_ConLoopScheduler.add(ConditionRoutineBegin(snapshot));
      Practice_Forth_ConLoopScheduler.add(ConditionRoutineEachFrame());
      Practice_Forth_ConLoopScheduler.add(ConditionRoutineEnd());
      Practice_Forth_ConLoopScheduler.add(Blank_3RoutineBegin(snapshot));
      Practice_Forth_ConLoopScheduler.add(Blank_3RoutineEachFrame());
      Practice_Forth_ConLoopScheduler.add(Blank_3RoutineEnd());
      Practice_Forth_ConLoopScheduler.add(endLoopIteration(Practice_Forth_ConLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Practice_Forth_ConLoopEnd() {
  psychoJS.experiment.removeLoop(Practice_Forth_Con);

  return Scheduler.Event.NEXT;
}


var Forth_Con;
function Forth_ConLoopBegin(Forth_ConLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Forth_Con = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 8, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: con4,
      seed: undefined, name: 'Forth_Con'
    });
    psychoJS.experiment.addLoop(Forth_Con); // add the loop to the experiment
    currentLoop = Forth_Con;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Forth_Con.forEach(function() {
      const snapshot = Forth_Con.getSnapshot();
    
      Forth_ConLoopScheduler.add(importConditions(snapshot));
      Forth_ConLoopScheduler.add(ConditionRoutineBegin(snapshot));
      Forth_ConLoopScheduler.add(ConditionRoutineEachFrame());
      Forth_ConLoopScheduler.add(ConditionRoutineEnd());
      Forth_ConLoopScheduler.add(endLoopIteration(Forth_ConLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Forth_ConLoopEnd() {
  psychoJS.experiment.removeLoop(Forth_Con);

  return Scheduler.Event.NEXT;
}


var inst_ImagePath;
var _Inst_key_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instructions'-------
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    inst_ImagePath = (("EXP_DATA/Instructions/Inst_Image/" + inst_ImageCount.toString()) + ".JPG");
    
    inst_Image.setImage(inst_ImagePath);
    Inst_key.keys = undefined;
    Inst_key.rt = undefined;
    _Inst_key_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(inst_Image);
    InstructionsComponents.push(Inst_key);
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instructions'-------
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *inst_Image* updates
    if (t >= 0.0 && inst_Image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst_Image.tStart = t;  // (not accounting for frame time here)
      inst_Image.frameNStart = frameN;  // exact frame index
      
      inst_Image.setAutoDraw(true);
    }

    
    // *Inst_key* updates
    if (t >= 1 && Inst_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Inst_key.tStart = t;  // (not accounting for frame time here)
      Inst_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      Inst_key.clock.reset();
      Inst_key.start();
      Inst_key.clearEvents();
    }

    if (Inst_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Inst_key.getKeys({keyList: [], waitRelease: false});
      _Inst_key_allKeys = _Inst_key_allKeys.concat(theseKeys);
      if (_Inst_key_allKeys.length > 0) {
        Inst_key.keys = _Inst_key_allKeys[_Inst_key_allKeys.length - 1].name;  // just the last key pressed
        Inst_key.rt = _Inst_key_allKeys[_Inst_key_allKeys.length - 1].rt;
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
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instructions'-------
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    inst_ImageCount = (inst_ImageCount + 1);
    
    psychoJS.experiment.addData('Inst_key.keys', Inst_key.keys);
    if (typeof Inst_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Inst_key.rt', Inst_key.rt);
        routineTimer.reset();
        }
    
    Inst_key.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Animation01_Key_allKeys;
var Animation01Components;
function Animation01RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Animation01'-------
    t = 0;
    Animation01Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Animation01_Key.keys = undefined;
    Animation01_Key.rt = undefined;
    _Animation01_Key_allKeys = [];
    // keep track of which components have finished
    Animation01Components = [];
    Animation01Components.push(Animation01_Video);
    Animation01Components.push(Animation01_Key);
    Animation01Components.push(Animation01_text);
    
    Animation01Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Animation01RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Animation01'-------
    // get current time
    t = Animation01Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Animation01_Video* updates
    if (t >= 0.0 && Animation01_Video.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Animation01_Video.tStart = t;  // (not accounting for frame time here)
      Animation01_Video.frameNStart = frameN;  // exact frame index
      
      Animation01_Video.setAutoDraw(true);
      Animation01_Video.play();
    }

    if (Animation01_Video.status === PsychoJS.Status.FINISHED) {  // force-end the routine
        continueRoutine = false;
    }
    
    // *Animation01_Key* updates
    if (t >= 1 && Animation01_Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Animation01_Key.tStart = t;  // (not accounting for frame time here)
      Animation01_Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      Animation01_Key.clock.reset();
      Animation01_Key.start();
      Animation01_Key.clearEvents();
    }

    if (Animation01_Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Animation01_Key.getKeys({keyList: [], waitRelease: false});
      _Animation01_Key_allKeys = _Animation01_Key_allKeys.concat(theseKeys);
      if (_Animation01_Key_allKeys.length > 0) {
        Animation01_Key.keys = _Animation01_Key_allKeys[_Animation01_Key_allKeys.length - 1].name;  // just the last key pressed
        Animation01_Key.rt = _Animation01_Key_allKeys[_Animation01_Key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Animation01_text* updates
    if (t >= 14 && Animation01_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Animation01_text.tStart = t;  // (not accounting for frame time here)
      Animation01_text.frameNStart = frameN;  // exact frame index
      
      Animation01_text.setAutoDraw(true);
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
    Animation01Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Animation01RoutineEnd() {
  return async function () {
    //------Ending Routine 'Animation01'-------
    Animation01Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    Animation01_Video.stop();
    psychoJS.experiment.addData('Animation01_Key.keys', Animation01_Key.keys);
    if (typeof Animation01_Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Animation01_Key.rt', Animation01_Key.rt);
        routineTimer.reset();
        }
    
    Animation01_Key.stop();
    // the Routine "Animation01" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var estimate_screen_sizeComponents;
function estimate_screen_sizeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'estimate_screen_size'-------
    t = 0;
    estimate_screen_sizeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slider.reset()
    slider.markerPos = 0.5;
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    estimate_screen_sizeComponents = [];
    estimate_screen_sizeComponents.push(card);
    estimate_screen_sizeComponents.push(slider);
    estimate_screen_sizeComponents.push(key_resp_2);
    
    estimate_screen_sizeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function estimate_screen_sizeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'estimate_screen_size'-------
    // get current time
    t = estimate_screen_sizeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *card* updates
    if (t >= 0.0 && card.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      card.tStart = t;  // (not accounting for frame time here)
      card.frameNStart = frameN;  // exact frame index
      
      card.setAutoDraw(true);
    }

    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    if (slider.markerPos !== undefined) {
      const newW = window.cardWidthPXMax * slider.markerPos;
      const newH = newW * window.cardAspectRatio;
    
      card.size = [newW, newH];
    
      window.cardWidthPX = newW;
      window.px2mm = window.cardWidthPX / window.cardWidthMM;
    }
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['return'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
    estimate_screen_sizeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function estimate_screen_sizeRoutineEnd() {
  return async function () {
    //------Ending Routine 'estimate_screen_size'-------
    estimate_screen_sizeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "estimate_screen_size" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Wcm;
var dist_text;
var _key_resp_4_allKeys;
var ResultsComponents;
function ResultsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Results'-------
    t = 0;
    ResultsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var w;
    var h;
    var Wcm;
    
    var dist_text;
    
    [w, h] = psychoJS.window.size;
    console.log("w: ");
    console.log(w);
    console.log("h: ");
    console.log(h);
    
    Wcm = ((w / px2mm) / 10);
    Hcm = ((h / px2mm) / 10);
    Wcm = ((w / px2mm) / 10);
    Hcm = ((h / px2mm) / 10);
    
    console.log('Hcm:', Hcm)
    console.log('Wcm:', Wcm)
    console.log('px2mm:', px2mm)
    console.log('w:', w)
    console.log('h:', h)
    dist_text = (((((((((("Your screen Height is " + Math.round(Hcm).toString()) + " Cm") + "\n") + "Your screen Width is ") + Math.round(Wcm).toString()) + " Cm") + "\n") + "Your screen Resolution is ") + psychoJS.window.size.toString()) + " Pixels");
    Res_text.setText(dist_text);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    ResultsComponents = [];
    ResultsComponents.push(Res_text);
    ResultsComponents.push(key_resp_4);
    ResultsComponents.push(Results_Text_Cont);
    
    ResultsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ResultsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Results'-------
    // get current time
    t = ResultsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Res_text* updates
    if (t >= 0.0 && Res_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Res_text.tStart = t;  // (not accounting for frame time here)
      Res_text.frameNStart = frameN;  // exact frame index
      
      Res_text.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: [], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Results_Text_Cont* updates
    if (t >= 0 && Results_Text_Cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Results_Text_Cont.tStart = t;  // (not accounting for frame time here)
      Results_Text_Cont.frameNStart = frameN;  // exact frame index
      
      Results_Text_Cont.setAutoDraw(true);
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
    ResultsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var screen_Prop;
function ResultsRoutineEnd() {
  return async function () {
    //------Ending Routine 'Results'-------
    ResultsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    screen_Prop = (Hcm / 29.5);
    psychoJS.experiment.addData("screen_Prop", screen_Prop);
    
    // the Routine "Results" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var G_Condition;
var e_LIST;
var C1;
var C2;
var C3;
var C4;
var con1;
var con2;
var con3;
var con4;
var Init_CounterComponents;
function Init_CounterRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Init_Counter'-------
    t = 0;
    Init_CounterClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    G_Condition = expInfo["Group"];
    e_LIST = split(G_Condition);
    C1 = e_LIST[0];
    C2 = e_LIST[1];
    C3 = e_LIST[2];
    C4 = e_LIST[3];
    con1 = (("EXP_DATA/Conditions/SNA/con" + C1) + ".xlsx");
    con2 = (("EXP_DATA/Conditions/SNA/con" + C2) + ".xlsx");
    con3 = (("EXP_DATA/Conditions/SNA/con" + C3) + ".xlsx");
    con4 = (("EXP_DATA/Conditions/SNA/con" + C4) + ".xlsx");
    console.log("e_LIST:", e_LIST);
    
    
    // keep track of which components have finished
    Init_CounterComponents = [];
    
    Init_CounterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Init_CounterRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Init_Counter'-------
    // get current time
    t = Init_CounterClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Init_CounterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Init_CounterRoutineEnd() {
  return async function () {
    //------Ending Routine 'Init_Counter'-------
    Init_CounterComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Init_Counter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var CON;
var Phase_ImagePath;
var _Inst_key_2_allKeys;
var Block_iNTSComponents;
function Block_iNTSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Block_iNTS'-------
    t = 0;
    Block_iNTSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((Inst_n === 4)) {
        Block_n = (Block_n + 1);
        Inst_n = 1;
    }
    if ((Block_n === 1)) {
        CON = C1;
    }
    if ((Block_n === 2)) {
        CON = C2;
    }
    if ((Block_n === 3)) {
        CON = C3;
    }
    if ((Block_n === 4)) {
        CON = C4;
    }
    Phase_ImagePath = (((("EXP_DATA/Instructions/Inst_Image/" + CON) + "/") + Inst_n.toString()) + ".JPG");
    console.log("Phase_ImagePath", Phase_ImagePath);
    
    inst_Image_2.setImage(Phase_ImagePath);
    Inst_key_2.keys = undefined;
    Inst_key_2.rt = undefined;
    _Inst_key_2_allKeys = [];
    // keep track of which components have finished
    Block_iNTSComponents = [];
    Block_iNTSComponents.push(inst_Image_2);
    Block_iNTSComponents.push(Inst_key_2);
    
    Block_iNTSComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Block_iNTSRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Block_iNTS'-------
    // get current time
    t = Block_iNTSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *inst_Image_2* updates
    if (t >= 0.0 && inst_Image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst_Image_2.tStart = t;  // (not accounting for frame time here)
      inst_Image_2.frameNStart = frameN;  // exact frame index
      
      inst_Image_2.setAutoDraw(true);
    }

    
    // *Inst_key_2* updates
    if (t >= 1 && Inst_key_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Inst_key_2.tStart = t;  // (not accounting for frame time here)
      Inst_key_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      Inst_key_2.clock.reset();
      Inst_key_2.start();
      Inst_key_2.clearEvents();
    }

    if (Inst_key_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = Inst_key_2.getKeys({keyList: [], waitRelease: false});
      _Inst_key_2_allKeys = _Inst_key_2_allKeys.concat(theseKeys);
      if (_Inst_key_2_allKeys.length > 0) {
        Inst_key_2.keys = _Inst_key_2_allKeys[_Inst_key_2_allKeys.length - 1].name;  // just the last key pressed
        Inst_key_2.rt = _Inst_key_2_allKeys[_Inst_key_2_allKeys.length - 1].rt;
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
    Block_iNTSComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Block_iNTSRoutineEnd() {
  return async function () {
    //------Ending Routine 'Block_iNTS'-------
    Block_iNTSComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    Inst_n = (Inst_n + 1);
    
    psychoJS.experiment.addData('Inst_key_2.keys', Inst_key_2.keys);
    if (typeof Inst_key_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Inst_key_2.rt', Inst_key_2.rt);
        routineTimer.reset();
        }
    
    Inst_key_2.stop();
    // the Routine "Block_iNTS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _C_Response_allKeys;
var ConditionComponents;
function ConditionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Condition'-------
    t = 0;
    ConditionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.250000);
    // update component parameters for each repeat
    image.setSize([(0.055 * image_size), (0.037 * image_size)]);
    image.setOri(image_ori);
    image.setImage(Arrow_Image);
    text.setText(text_stimulus);
    C_Response.keys = undefined;
    C_Response.rt = undefined;
    _C_Response_allKeys = [];
    if ((Stim === "ArrLC")) {
        Arrow_Image = "EXP_DATA/Arrows/Cutout.png";
    }
    if ((Stim === "ArrLF")) {
        Arrow_Image = "EXP_DATA/Arrows/Full.png";
    }
    if ((Stim === "ArrRC")) {
        Arrow_Image = "EXP_DATA/Arrows/Cutout.png";
    }
    if ((Stim === "ArrRF")) {
        Arrow_Image = "EXP_DATA/Arrows/Full.png";
    }
    console.log("Stim", Stim)
    // keep track of which components have finished
    ConditionComponents = [];
    ConditionComponents.push(Fixation);
    ConditionComponents.push(image);
    ConditionComponents.push(text);
    ConditionComponents.push(C_Response);
    
    ConditionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ConditionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Condition'-------
    // get current time
    t = ConditionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation* updates
    if (t >= 0.0 && Fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation.tStart = t;  // (not accounting for frame time here)
      Fixation.frameNStart = frameN;  // exact frame index
      
      Fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation.setAutoDraw(false);
    }
    
    // *image* updates
    if (t >= 1.25 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 1.25 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *text* updates
    if (t >= 1.25 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 1.25 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *C_Response* updates
    if (t >= 1.25 && C_Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      C_Response.tStart = t;  // (not accounting for frame time here)
      C_Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { C_Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { C_Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { C_Response.clearEvents(); });
    }

    frameRemains = 1.25 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (C_Response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      C_Response.status = PsychoJS.Status.FINISHED;
  }

    if (C_Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = C_Response.getKeys({keyList: ['space'], waitRelease: false});
      _C_Response_allKeys = _C_Response_allKeys.concat(theseKeys);
      if (_C_Response_allKeys.length > 0) {
        C_Response.keys = _C_Response_allKeys[_C_Response_allKeys.length - 1].name;  // just the last key pressed
        C_Response.rt = _C_Response_allKeys[_C_Response_allKeys.length - 1].rt;
        // was this correct?
        if (C_Response.keys == CorrAns) {
            C_Response.corr = 1;
        } else {
            C_Response.corr = 0;
        }
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
    ConditionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var Feedback_Color;
var Feedback;
function ConditionRoutineEnd() {
  return async function () {
    //------Ending Routine 'Condition'-------
    ConditionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (C_Response.keys === undefined) {
      if (['None','none',undefined].includes(CorrAns)) {
         C_Response.corr = 1;  // correct non-response
      } else {
         C_Response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('C_Response.keys', C_Response.keys);
    psychoJS.experiment.addData('C_Response.corr', C_Response.corr);
    if (typeof C_Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('C_Response.rt', C_Response.rt);
        routineTimer.reset();
        }
    
    C_Response.stop();
    psychoJS.experiment.addData("condition", CON);
    
    // was no response the correct answer?!
    if (C_Response.keys === undefined) {
      if (['None','none',undefined].includes(CorrAns)) {
         C_Response.corr = 1;  // correct non-response
      } else {
         C_Response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    
    
    Feedback_Color = "green";
    Feedback = "";
    if (((GNG_Type === "go") && (C_Response.corr === 1))) {
        Feedback = "נכון";
    }
    if (((GNG_Type === "no_go") && (C_Response.corr === 1))) {
        Feedback = "נכון";
    }
    if (((GNG_Type === "go") && (C_Response.corr === 0))) {
        Feedback = "לא נכון";
        Feedback_Color = "red";
    }
    if (((GNG_Type === "no_go") && (C_Response.corr === 0))) {
        Feedback = "לא נכון";
        Feedback_Color = "red";
    }
    console.log("GNG_Type", GNG_Type)
    return Scheduler.Event.NEXT;
  };
}


var Blank_3Components;
function Blank_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Blank_3'-------
    t = 0;
    Blank_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    text_4.setColor(new util.Color(Feedback_Color));
    text_4.setText(Feedback);
    // keep track of which components have finished
    Blank_3Components = [];
    Blank_3Components.push(Blank);
    Blank_3Components.push(text_4);
    Blank_3Components.push(text_5);
    
    Blank_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Blank_3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Blank_3'-------
    // get current time
    t = Blank_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Blank* updates
    if (t >= 0.0 && Blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Blank.tStart = t;  // (not accounting for frame time here)
      Blank.frameNStart = frameN;  // exact frame index
      
      Blank.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Blank.setAutoDraw(false);
    }
    
    // *text_4* updates
    if (t >= 0.5 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    
    // *text_5* updates
    if (t >= 1.5 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    frameRemains = 1.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
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
    Blank_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank_3RoutineEnd() {
  return async function () {
    //------Ending Routine 'Blank_3'-------
    Blank_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var _key_resp_8_allKeys;
var OP_Cir1;
var OP_Cir2;
var OP_Cir3;
var OP_Cir4;
var fini_text;
var _Count_SideComponents;
function _Count_SideRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine '_Count_Side'-------
    t = 0;
    _Count_SideClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    OP_Cir1 = 1;
    OP_Cir2 = 2;
    OP_Cir3 = 3;
    OP_Cir4 = 4;
    fini_text = "";
    
    // keep track of which components have finished
    _Count_SideComponents = [];
    _Count_SideComponents.push(Cir1_3);
    _Count_SideComponents.push(Cir2_3);
    _Count_SideComponents.push(Cir3_3);
    _Count_SideComponents.push(Cir4_3);
    _Count_SideComponents.push(mouse_3);
    _Count_SideComponents.push(key_resp_8);
    _Count_SideComponents.push(Fini_text);
    
    _Count_SideComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var buttons;
var Posi;
function _Count_SideRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine '_Count_Side'-------
    // get current time
    t = _Count_SideClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Cir1_3* updates
    if (t >= 0.0 && Cir1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cir1_3.tStart = t;  // (not accounting for frame time here)
      Cir1_3.frameNStart = frameN;  // exact frame index
      
      Cir1_3.setAutoDraw(true);
    }

    
    if (Cir1_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Cir1_3.setOpacity(OP_Cir1, false);
    }
    
    // *Cir2_3* updates
    if (t >= 0.0 && Cir2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cir2_3.tStart = t;  // (not accounting for frame time here)
      Cir2_3.frameNStart = frameN;  // exact frame index
      
      Cir2_3.setAutoDraw(true);
    }

    
    if (Cir2_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Cir2_3.setOpacity(OP_Cir2, false);
    }
    
    // *Cir3_3* updates
    if (t >= 0.0 && Cir3_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cir3_3.tStart = t;  // (not accounting for frame time here)
      Cir3_3.frameNStart = frameN;  // exact frame index
      
      Cir3_3.setAutoDraw(true);
    }

    
    if (Cir3_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Cir3_3.setOpacity(OP_Cir3, false);
    }
    
    // *Cir4_3* updates
    if (t >= 0.0 && Cir4_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cir4_3.tStart = t;  // (not accounting for frame time here)
      Cir4_3.frameNStart = frameN;  // exact frame index
      
      Cir4_3.setAutoDraw(true);
    }

    
    if (Cir4_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Cir4_3.setOpacity(OP_Cir4, false);
    }
    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: [], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    buttons = mouse_3.getPressed();
    if ((Cir1_3.contains(mouse_3) && (buttons[0] > 0))) {
        OP_Cir1 = 0;
    }
    if ((Cir2_3.contains(mouse_3) && (buttons[0] > 0))) {
        OP_Cir2 = 0;
    }
    if ((Cir3_3.contains(mouse_3) && (buttons[0] > 0))) {
        OP_Cir3 = 0;
    }
    if ((Cir4_3.contains(mouse_3) && (buttons[0] > 0))) {
        OP_Cir4 = 0;
    }
    if ((buttons[0] > 0)) {
        Posi = mouse_3.getPos();
        mouse_click_locations.push(Posi);
        console.log(Posi);
        console.log(mouse_click_locations);
    }
    if (((((OP_Cir1 === 0) && (OP_Cir2 === 0)) && (OP_Cir3 === 0)) && (OP_Cir4 === 0))) {
        fini_text = "\u05dc\u05d7\u05e5 \u05e2\u05dc \u05db\u05dc \u05de\u05e7\u05e9 \u05dc\u05e1\u05d9\u05d5\u05dd";
    }
    
    
    // *Fini_text* updates
    if (t >= 0 && Fini_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fini_text.tStart = t;  // (not accounting for frame time here)
      Fini_text.frameNStart = frameN;  // exact frame index
      
      Fini_text.setAutoDraw(true);
    }

    
    if (Fini_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Fini_text.setText(fini_text, false);
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
    _Count_SideComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var _mouseButtons;
var Counting;
function _Count_SideRoutineEnd() {
  return async function () {
    //------Ending Routine '_Count_Side'-------
    _Count_SideComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_3.getPos();
    _mouseButtons = mouse_3.getPressed();
    psychoJS.experiment.addData('mouse_3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_3.rightButton', _mouseButtons[2]);
    if (mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0]);}
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    Counting = "";
    if ((mouse_click_locations.slice((- 1))[0][0] > mouse_click_locations[0][0])) {
        Counting = "Left_To_Right";
    }
    if ((mouse_click_locations.slice((- 1))[0][0] < mouse_click_locations[0][0])) {
        Counting = "Right_To_Left";
    }
    psychoJS.experiment.addData("Counting", Counting);
    
    // the Routine "_Count_Side" was not non-slip safe, so reset the non-slip timer
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
