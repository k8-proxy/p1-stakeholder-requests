import os
import shutil

OUT_DIR='./output/'

if __name__ == '__main__':
    command = "kubectl get pods --template \'{{range .items}}{{.metadata.name}}{{\"\\n\"}}{{end}}\'"
    stream = os.popen(command)
    output = stream.read()
    pods = output.splitlines()
    try:
        if os.path.exists(OUT_DIR):
            shutil.rmtree(OUT_DIR)
        os.mkdir(OUT_DIR)
    except OSError as error:
        print('Output dir exists')
    for pod in pods:
        command = "kubectl exec -it "+ pod + " -- find / -type d \( -perm -g+w -or -perm -o+w \) -exec ls -adl {} \;"
        stream = os.popen(command)
        lines = stream.read()
        for line in lines.splitlines():
            with open(OUT_DIR+pod+".txt", "a") as f:
                line = line.rstrip()
                f.write(line+'\n')
    print ('Output to directory - '+OUT_DIR)