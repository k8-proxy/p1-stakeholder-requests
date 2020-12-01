# Privileges management

## Get pods running with elevated privileges. 

The command bellow will list all pods running with elevated privileges on the cluster.

```
kubectl get pods -o=jsonpath='{range .items[?(@.spec.containers[*].securityContext.privileged==true)]}{.metadata.name}{"\n"}{end}' --all-namespaces
```

## Check if glasswall container runs as root
The check above only make sure the container doesn't run as priviledged container, but it can still run as root if the docker image is configured with the root user. To check that run the command

```
kubectl -n <glasswall_namespace_name> exec -it <glasswall_pod_name> -- bash -c "id -u"
```

Make sure the returned user ID is not zero (root)


## Best Practices
- It's necessary to have a good mecanism to enforce and block pods trying to run with elevated privileges (for instance images configured with root user).
- To achieve that, we need to enable when installing the cluster the [PodSecurityPolicy admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#podsecuritypolicy"). 
- Admission controllers in kubernetes is a mecanism to add some addtionnal validation on k8s ressources before they are admitted to the cluster. PodSecurityPolicy Admission controller will act on the creation or modification of pods in order to determine if they should be admitted based on the policy defined by the administrator.
- Once that admission controller is enabled, we can setup a default Pod Security Policy that will be inforced to all pods.

```
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
  annotations:
    seccomp.security.alpha.kubernetes.io/allowedProfileNames: 'docker/default'
    apparmor.security.beta.kubernetes.io/allowedProfileNames: 'runtime/default'
    seccomp.security.alpha.kubernetes.io/defaultProfileName:  'docker/default'
    apparmor.security.beta.kubernetes.io/defaultProfileName:  'runtime/default'
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
    - ALL
  # Allow core volume types.
  volumes:
    - 'configMap'
    - 'emptyDir'
    - 'projected'
    - 'secret'
    - 'downwardAPI'
    - 'persistentVolumeClaim'
  hostNetwork: false
  hostIPC: false
  hostPID: false
  runAsUser:
    # Require the container to run without root privileges.
    rule: 'MustRunAsNonRoot'
  supplementalGroups:
    rule: 'MustRunAs'
    ranges:
      # Forbid adding the root group.
      - min: 1
        max: 65535
  fsGroup:
    rule: 'MustRunAs'
    ranges:
      # Forbid adding the root group.
      - min: 1
        max: 65535
  readOnlyRootFilesystem: false
```

With that, we are preventing any pod trying to run as root to be scheduled as well as any privileged pod.

Dockerfile should therefore be configure to not use the root as default user. As presented bellow :

```
FROM nginx:latest
USER 1001
CMD ["nginx","-g","daemon off;"]
```


- The cluster admin can still configure other security policies with more privileges which can be granted to a service account in case of a real need for privilege escalation.


