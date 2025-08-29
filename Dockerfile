#Use the official Python 3.11.1 slim version based on the Debian Bookworm as the base image
FROM python:3.11.1-slim-bookworm

#Copy the uv and uvx executables from the latest uv image into /bin/ in this image
#RUN pip install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

#Setting the working directory
WORKDIR /app

#Add the virtual environment's bin directory to the PATH so Python tools work globally
ENV PATH = "/code/.venv/bin:$PATH"

#Copy the project configuration files into the container 
COPY ".python-version" "pyproject.toml" "uv.lock" "./"

#Install dependencies exactly as locked in uv.lock, without updating them
RUN uv sync --locked

#Copy application code and model data into the container
COPY "predict.py" "marketing.py" "pipeline_model.bin" "./"

#Expose the 9696 port to be accessed from outside the container
EXPOSE 9696

#Execute the app using uvicorn
ENTRYPOINT ["uvicorn","predict:app","--host","0.0.0.0","--port","9696"]

#Execute using the following commands
#docker build churn-prediction .

#docker run -it --rm -p 9696:9696 churn-prediction