# Spatial fMRI experiments

## Keyboard
1. 't', or 'space' to start the experiment;
2. '0', or 'left' for select the left scene, '1', or 'right' for select the right scene;

## Generate random weather condition seqeuences
First need to run a [script](spatialpy/gen_subject_spatialpy_group.ipynb) to generate a 
weather sequences for different subjects.

## Run psyexp
### [spatialpy_run.psyexp](fMRI_experiment_setup/psychopy/spatialpy/spatialpy_run.psyexp)
1. participant `10`, `13` runs, each 5 min. 
2. six runs from `town01` to `town06` with different weathers.
3. seven runs from `town07` with seven weathers.

## Demo psyexp
### [spatialpy_demo.psyexp](fMRI_experiment_setup/psychopy/spatialpy/spatialpy_demo.psyexp)
1. use default parameters to run the demo with short time videos.

## Parameters
1. This experiment supports 60 participants, from `00` to `59`, to set different group sequences.
2. This experiment supports 07 runs, from `00` to `06`, to set different runs.
3. `gen_participant_group.ipynb` is to generate new groups, if needed.
4. The mouse cursor will automatically hide after start the experiment.
