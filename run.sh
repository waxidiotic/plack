#!/bin/bash

gunicorn -b 0.0.0.0:5678 app:app