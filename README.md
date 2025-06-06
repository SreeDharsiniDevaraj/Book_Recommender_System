# End_to_End_Book_Recommendation_System
## Book_Recommender_System

## Workflow

- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/SreeDharsiniDevaraj/Book_Recommender_System.git
```
### STEP 01- Create a python virtual environment after opening the repository

```bash
python -m venv env
```

```bash
E:\End_to_End_Book_Recommendation_System\env\Scripts\activate.bat
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


Now run,
```bash
streamlit run app.py
```


# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone https://github.com/SreeDharsiniDevaraj/Book_Recommender_System.git
```

```bash
docker build -t sreedharsini1999/stapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 sreedharsini1999/stapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push sreedharsini1999/stapp:latest 
```

```bash
docker rmi sreedharsini1999/stapp:latest
```

```bash
docker pull sreedharsini1999/stapp
```






