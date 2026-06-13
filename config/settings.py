"""Game configuration and settings."""

# Game Version
GAME_VERSION = "0.1.0"
GAME_TITLE = "British Military Life Simulator"

# Game Settings
FULL_GAME_ENABLED = True
GOD_MODE = False
DEBUG_MODE = False

# Character Settings
MAX_AGE = 65
MIN_ENTRY_AGE = 16
MAX_ENTRY_AGE = 35
DEFAULT_START_AGE = 18

# Career Settings
YEARS_IN_UKSF = 3  # Standard tour for officers
YEARS_TO_RETIREMENT = 22  # Standard military service

# Game Timing
MONTHS_PER_TURN = 1
TURNS_PER_YEAR = 12

# Service Branch Codes
SERVICES = {
    'ARMY': 'British Army',
    'NAVY': 'Royal Navy',
    'RAF': 'Royal Air Force',
    'MARINES': 'Royal Marines'
}

# Era Settings
ERAS = {
    1980: 'Cold War (1980s)',
    1990: 'Post-Cold War (1990s)',
    2000: 'War on Terror (2000s)',
    2010: 'Modern (2010s)',
    2020: 'Contemporary (2020s)'
}

DEFAULT_START_ERA = 2020
