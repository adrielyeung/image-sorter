# -*- coding: utf-8 -*-
import logsetup
import gui

# Log msg
START_GUI = 'Start GUI'
END_GUI = 'End GUI'

# Formatter
DT_FORMATTER = '%Y-%m-%d %H:%M:%S'

# Root logger
rootlogger = logsetup.setupName()

def main():
    rootlogger.info(START_GUI)
    gui.main()
    rootlogger.info(END_GUI)

if __name__ == '__main__':
    main()
