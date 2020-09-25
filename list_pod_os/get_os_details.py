import os

if __name__ == '__main__':
    command = "kubectl get pods -o=jsonpath=\"{.items[*]['metadata.name']}\""
    stream = os.popen(command)
    output = stream.read()
    pods = output.split(" ")
    pod_name_os_map = {}
    for pod in pods:
        command = "kubectl exec -it {} -- cat /etc/os-release".format(pod)
        stream = os.popen(command)
        lines = stream.read()
        for line in lines.splitlines():
            data = line.split('=')
            found = False
            if data[0] == 'NAME':
                pod_name_os_map[pod] = data[1][1:]
                found = True
            if found:
                break;

    print (pod_name_os_map)
