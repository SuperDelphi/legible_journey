### WHEEL_METER.PY

PIN = 17 # The GPIO pin used for the sensor's digital output
BOUNCE_TIME = 0.005 # The time span during which the sensor ingores inputs after a trigger (necessary)
DEFAULT_DIAMETER = 622 # The default diameter of the wheel (in millimeters)
PERIOD = 2 # The duration between each measuring (in seconds)
USE_AVG_SPEED = False # Whether to use the average speed instead of the direct speed
AVG_SMOOTHNESS = 5 # The amount of stored previous speed (used to compute a rolling average)

### LEGIBLE.PY

# VOLUME_CURVES contains the volume configuration for each track. For each pair of values, the first one represents the speed (percentage), while the second one represents the volume (from 0 to 1).
# For example, if the maximum speed is set to 50 km/h, and we have (30, 0.5), it means that when 30 % of 50 km/h (= 15 km/h) is reached, the volume of the associated track will reach 50 %.
# Feel free to add, remove and modify the values and value pairs for each track, but you MUST keep them in ascending order (according to the speed percentage).
# You also need to specify at least the 0 % and 100 % pairs.

VOLUME_CURVES = {
    "abstract": [(0, 0.0), (1, 1.0)], # The track is fully muted at 0 km/h and out loud at maximum speed. (Remove this comment if changed)
    "deconstr": [(0, 0.0), (30, 0.1), (50, 1.0), (100, 0.7)], # The track begins to be heard at 30 % of the maximum speed, is out loud at 50 % and gets quieter at maximum speed. (Remove this comment if changed)
    "narrative": [(0, 1.0), (70, 0.0), (100, 0.0)] # This track is out loud at 0 km/h then gets muted at 70 % of the maximum speed. (Remove this comment if changed)
}

FADE_MS = 1000 # The fade-in effect (in milliseconds) when a track (re)starts
MAX_SPEED = 50 # The maximum speed (in km/h) used to make interpolations between tracks
LERP_SPEED = 0.05 # The speed at which the volume changes
MONITOR_VOLUMES = False # Not recommended, because it takes ressources that are needed for continuous audio. Only use for testing purposes.
