import os
import sys

# Set the MongoDB URL environment variable
os.environ['MONGODB_URL'] = 'mongodb+srv://tejeshyewale917_db_user:D6p7MhudyHz7VUAK@cluster0.099fjel.mongodb.net/?appName=Cluster0'

# Now run the demo
from src.logger import logging

logging.info("This is an info message.")

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()