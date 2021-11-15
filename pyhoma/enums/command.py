from enum import Enum, unique


@unique
class OverkizCommand(str, Enum):
    """Device commands used by Overkiz."""

    ALARM_OFF = "alarmOff"
    ALARM_ON = "alarmOn"
    ALARM_PARTIAL_1 = "alarmPartial1"
    ALARM_PARTIAL_2 = "alarmPartial2"
    ARM = "arm"
    ARM_PARTIAL_DAY = "armPartialDay"
    ARM_PARTIAL_NIGHT = "armPartialNight"
    CLOSE = "close"
    CLOSE_SLATS = "closeSlats"
    CYCLE = "cycle"
    DEPLOY = "deploy"
    DISARM = "disarm"
    DOWN = "down"
    GLOBAL_CONTROL = "globalControl"
    IDENTIFY = "identify"
    MEMORIZED_VOLUME = "memorizedVolume"
    MY = "my"
    OFF = "off"
    ON = "on"
    OPEN = "open"
    OPEN_SLATS = "openSlats"
    PARTIAL = "partial"
    RING_WITH_SINGLE_SIMPLE_SEQUENCE = "ringWithSingleSimpleSequence"
    SET_ABSENCE_MODE = "setAbsenceMode"
    SET_ALARM_STATUS = "setAlarmStatus"
    SET_ALL_MODE_TEMPERATURES = "setAllModeTemperatures"
    SET_BOOST_MODE = "setBoostMode"
    SET_COMFORT_TEMPERATURE = "setComfortTemperature"
    SET_CLOSURE = "setClosure"
    SET_CLOSURE_AND_LINEAR_SPEED = "setClosureAndLinearSpeed"
    SET_CONTROL_DHW = "setControlDHW"
    SET_CONTROL_DHW_SETTING_TEMPERATURE = "setControlDHWSettingTemperature"
    SET_CURRENT_OPERATING_MODE = "setCurrentOperatingMode"
    SET_DEPLOYMENT = "setDeployment"
    SET_DEROGATION = "setDerogation"
    SET_DHW_MODE = "setDHWMode"
    SET_ECO_TEMPERATURE = "setEcoTemperature"
    SET_EXPECTED_NUMBER_OF_SHOWER = "setExpectedNumberOfShower"
    SET_FORCE_HEATING = "setForceHeating"
    SET_INTENSITY = "setIntensity"
    SET_MEMORIZED_SIMPLE_VOLUME = "setMemorizedSimpleVolume"
    SET_MEMORIZED_1_POSITION = "setMemorized1Position"
    SET_ORIENTATION = "setOrientation"
    SET_PEDESTRIAN_POSITION = "setPedestrianPosition"
    SET_RGB = "setRGB"
    SET_SECURED_POSITION_TEMPERATURE = "setSecuredPositionTemperature"
    SET_TARGET_TEMPERATURE = "setTargetTemperature"
    STANDARD = "standard"
    STOP = "stop"
    STOP_IDENTIFY = "stopIdentify"
    WINK = "wink"
    LOCK = "lock"
    UNLOCK = "unlock"
    UNDEPLOY = "undeploy"
    UP = "up"


@unique
class OverkizCommandParam(str, Enum):
    """Parameter used by Overkiz commands and/or states."""

    ABSENCE = "absence"
    ARMED = "armed"
    ARMED_DAY = "armedDay"
    ARMED_NIGHT = "armedNight"
    AWAY = "away"
    AUTO = "auto"
    AUTO_MODE = "autoMode"
    AVAILABLE = "available"
    BOOST = "boost"
    COMFORT = "comfort"
    CLOSED = "closed"
    DEAD = "dead"
    DETECTED = "detected"
    DISARMED = "disarmed"
    ECO = "eco"
    FREE = "free"
    FROSTPROTECTION = "frostprotection"
    FULL = "full"
    GEOFENCING_MODE = "geofencingMode"
    HIGH_DEMAND = "high demand"  # not a typo...
    HIGHEST = "highest"
    LOW = "low"
    LOCKED = "locked"
    MANU = "manu"
    MANUAL = "manual"
    MANUAL_ECO_ACTIVE = "manualEcoActive"
    MANUAL_ECO_INACTIVE = "manualEcoInactive"
    NORMAL = "normal"
    ON = "on"
    OFF = "off"
    OPEN = "open"
    PARTIAL = "partial"
    PENDING = "pending"
    PEDESTRIAN = "pedestrian"
    PERSON_INSIDE = "personInside"
    PROG = "prog"
    RELAUNCH = "relaunch"
    SECURED = "secured"
    STANDARD = "standard"
    STOP = "stop"
    TOTAL = "total"
    UNDETECTED = "undetected"
    VERY_LOW = "verylow"
    ZONE_1 = "zone1"
    ZONE_2 = "zone2"


@unique
class CommandMode(str, Enum):
    HIGH_PRIORITY = "highPriority"
    GEOLOCATED = "geolocated"
    INTERNAL = "internal"
