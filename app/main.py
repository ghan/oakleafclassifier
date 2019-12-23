from typing import List

from fastapi import FastAPI, File, UploadFile
from starlette.responses import HTMLResponse
from fastai.basics import *
from fastai.vision import *
import torch

app = FastAPI()
defaults.device = torch.device('cpu')

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
  
  try:
    learn = load_learner('./', 'export.pkl')
    img = open_image(file.file)
    x,y,losses = learn.predict(img)

    content = """
      <body>
        <img src=\"{0}\" />
        <p>{1}<br />{2}<br />{3}</p>
      </body>

    """
    return HTMLResponse(content=content.format(file.filename, x, y, losses))
  except Exception as e:
    return {"error": e}

@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="file" type="file">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)