# Basic theme which only uses colors in 0-15 range

class Color(DefaultColor):
    USERNAME_FG = 7
    USERNAME_BG = 5

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 8 # dark grey
    PATH_FG = 7 # light grey
    CWD_FG = 7 # white
    SEPARATOR_FG = 16

    READONLY_BG = 1
    READONLY_FG = 0

    REPO_CLEAN_BG = 12  # green
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 10  # red
    REPO_DIRTY_FG = 0 # white

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 0
    CMD_PASSED_FG = 7
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0
