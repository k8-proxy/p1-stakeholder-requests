1) The python script file "get_file_permissions_docker_containers.py" can be used to get globally writable files inside all docker containers running in a machine

	Execute the following command 
	python3 get_file_permissions_docker_containers.py
	
	It will create a "output" dirctory in the current working directory.
	It will have text files with container-ids.
	Each file will list all globally writable files inside that container
	
	e.g.
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/games
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/include
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/lib
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/sbin
		drwxrwsr-x. 1 root staff 19 Mar 26  2019 /usr/local/share
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/share/man
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/share/fonts
	
	
2) The python script file get_file_permissions_k8_pods.py" can be used to get globally writable files inside all pods  running in a k8-cluster on a machine

	Execute the following command 
	python3 get_file_permissions_k8_pods.py
	
	It will create a "output" dirctory in the current working directory.
	It will have text files with pod-names.
	Each file will list all globally writable files inside that pod	
	
	
	e.g.
	
	[root@K8Master output]# cat nginx-deployment-574b87c764-fdzfl.txt
		drwxrwxrwt. 2 root root 40 Sep 23 14:51 /dev/shm
		drwxrwxrwt. 2 root root 40 Sep 23 14:51 /dev/mqueue
		drwxrwxrwt. 2 root root 40 Sep 23 14:51 /proc/acpi
		drwxrwxrwt. 2 root root 40 Sep 23 14:51 /proc/scsi		
		drwxrwxrwt. 2 root root 6 Mar 26  2019 /run/lock
		drwxrwxrwt. 3 root root 140 Sep 23 14:51 /run/secrets/kubernetes.io/serviceaccount
		drwxrwxrwt. 2 root root 40 Sep 23 14:51 /sys/firmware
		drwxrwxrwt. 1 root root 6 Mar 26  2019 /tmp
		drwxrwsr-x. 1 root staff 19 Mar 26  2019 /usr/local
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/bin
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/etc
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/games
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/include
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/lib
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/sbin
		drwxrwsr-x. 1 root staff 19 Mar 26  2019 /usr/local/share
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/share/man
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/share/fonts
		drwxrwsr-x. 2 root staff 6 Mar 26  2019 /usr/local/src
		drwxrwsr-x. 2 root staff 6 Feb  3  2019 /var/local
		drwxrwsr-x. 2 root mail 6 Mar 26  2019 /var/mail
		drwxrwxrwt. 2 root root 6 Feb  3  2019 /var/tmp
