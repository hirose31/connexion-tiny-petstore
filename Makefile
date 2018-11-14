.PHONY: help codegen spec
.DEFAULT_GOAL := help
PROJECT_ROOT = $(PWD)
APPDIR = tiny_petstore

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

codegen: ## generate code
	@openapi-generator-cli generate \
	  -g python-flask \
	  -c etc/codegen-config.json \
	  -i tiny-petstore.yaml \
	  -o $(PROJECT_ROOT)

spec: ## generate only spec
	@$(RM) $(APPDIR)/openapi/openapi.yaml
	@openapi-generator-cli generate \
	  -g python-flask \
	  -c etc/codegen-config.json \
	  -i tiny-petstore.yaml \
	  -o $(PROJECT_ROOT) \
	  --skip-overwrite
	-@$(RM) git_push.sh
	-@$(RM) $(APPDIR)/__main__.py \
	  $(APPDIR)/models/base_model_.py \
	  $(APPDIR)/models/*_param.py \
	  $(APPDIR)/models/*_{core,new,update,ref}.py \
	;
	-@rm -fr $(APPDIR)/test/

version: ## update version string for several files
	@./bin/update-version
