Build docker image
docker build -t kd/mypy:latest .

#Mount program directory and run disposable container in interactive mode
#For example - let's say your programs are located in directory: /Users/KD/coding_interview
docker run --rm -it -v /Users/KD/coding_interview:/data kd/mypy:latest /bin/bash
