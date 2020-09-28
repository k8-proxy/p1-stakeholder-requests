import os
import shutil

OUT_DIR='./output/'

if __name__ == '__main__':
    command = "docker ps --format '{{.ID}}'"
    stream = os.popen(command)
    output = stream.read()
    containers = output.splitlines()
    try:
        if os.path.exists(OUT_DIR):
            shutil.rmtree(OUT_DIR)
        os.mkdir(OUT_DIR)
    except OSError as error:
        print('Output dir exists')
    for container in containers:
        command = "docker exec -it "+container+" find / -type d \( -perm -g+w -or -perm -o+w \) -exec ls -adl {} \;"
        stream = os.popen(command)
        lines = stream.read()
        for line in lines.splitlines():
            with open(OUT_DIR+container+".txt", "a") as f:
                line = line.rstrip()
                f.write(line+'\n')
    print ('Output to directory - '+OUT_DIR)