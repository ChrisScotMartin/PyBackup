"""
PyBackup - A simple personal backup utility
Copyright (C) 2023  Robert T. Fowler IV

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import configparser
import os
from pathlib import Path

# Read config values into variables
config = configparser.ConfigParser()
config.read('config.ini')

varSavedBackups = Path(config['saved_backups']['location'])

if not os.path.isfile(varSavedBackups):
    print("ERROR: Saved backups location not set in config.ini or invalid path")
    print("Using default location: ./backups.json")
    varSavedBackups = Path('./backups.json')




