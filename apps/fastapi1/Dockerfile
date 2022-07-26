# Step1 : base images
FROM python

# Step2 : Copy files 
RUN mkdir /app
COPY main.py /app
COPY requirements.txt /app

# Step3 : Specify a working directory 
WORKDIR '/app'

# Step4 : config file copy
RUN pip install -r requirements.txt 

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
