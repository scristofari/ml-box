.PHONY: run help test
.DEFAULT_GOAL := help

help: ## List all the command helps.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


protoc: ## Generate the proto-buffer
	@cd ml && python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. *.proto
