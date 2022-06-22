FROM python:3
RUN apt-get update

RUN apt-get upgrade -y
# Change TimeZone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo $(date)
# Copy files to working directory
COPY ./ /app/
WORKDIR /app 
# Install python packages using requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD pytest -s src/test_script.py