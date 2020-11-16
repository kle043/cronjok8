# Kube Play

An example setup where a cronJob creates jobs for long running jobs using job expansion.
The setup is a star wars server that randomly returns a set of characters that should work for a long time.
A cronJob is used to schedule the work of each character by creating, deleting and listing jobs. If a character is already working the 
cronJob will skip creating a new job so that the character is not overworked.

Minikube was used for this playground and the images need to be built locally.

To build the images and apply the manifests run 

``` bash
eval $(minikube docker-env)
make all
```

Some of the usefull parts of the code is:
* Service account setup for the cron job [scheduler/Manifest.yaml](scheduler/Manifest.yaml)
* Listing, creating and deleting jobs [scheduler/main](scheduler/scheduler/__main__.py)

