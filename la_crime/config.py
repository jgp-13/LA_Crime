import os
import sys

# Get absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Define key directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'd0-raw')
INTERIM_DATA_DIR= os.path.join(DATA_DIR, 'd1-interim')
CLEANED_DATA_DIR= os.path.join(DATA_DIR, 'd2-cleaned')

NOTEBOOKS_DIR = os.path.join(BASE_DIR, 'notebooks')
IMAGES_DIR = os.path.join(NOTEBOOKS_DIR,'images')
FIGURES_DIR = os.path.join(NOTEBOOKS_DIR, 'figures')

PROJECT_DIR = os.path.join(BASE_DIR, 'la_crimes')

SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')