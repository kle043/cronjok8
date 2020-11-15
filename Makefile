.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

build-worker: ## Build the worker
	docker build -t worker:latest worker/

build-server: ## Build the server
	docker build -t server:latest server/

build-server: ## Build the scheduler
	docker build -t scheduler:latest scheduler/