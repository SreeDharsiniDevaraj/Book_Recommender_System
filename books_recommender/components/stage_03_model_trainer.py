import os
import sys
import pickle
import zipfile
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException


class ModelTrainer:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
        except Exception as e:
            raise AppException(e, sys) from e

    
    def train(self):
        try:
            # define path to the zip file
            zip_path = self.model_trainer_config.transformed_data_file_dir
            # Extract pickle file from zip archive
            with zipfile.ZipFile(zip_path,'r') as zipf:
                zipf.extract("book_pivot.pkl", path=self.model_trainer_config.transformed_data_file_dir)
            #loading the extracted 'book_pivot' pickle file
            pkl_path = f"{self.model_trainer_config.transformed_data_file_dir}/book_pivot.pkl"
            with open(pkl_path, 'rb') as pkl_file:
                book_pivot = pickle.load(pkl_file)
            # Convert to sparse matrix
            book_sparse = csr_matrix(book_pivot)
            #Training model
            model = NearestNeighbors(algorithm='brute')
            model.fit(book_sparse)

            #Saving model object for recommendations
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
            file_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            pickle.dump(model,open(file_name,'wb'))
            logging.info(f"Saving final model to {file_name}")
            # Removing the temporary pickle file
            os.remove(pkl_path)
            logging.info(f"Removed temporary pickle file: {pkl_path}")

        except Exception as e:
            raise AppException(e, sys) from e

    

    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.train()
            logging.info(f"{'='*20}Model Trainer log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e