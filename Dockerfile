FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install python-multipart
RUN pip install --no-cache-dir torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install fastai
COPY ./app /app