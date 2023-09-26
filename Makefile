PKG_NAME := pypi-safetensors
URL = https://files.pythonhosted.org/packages/ea/43/9911dc3ab9c8da3ef0ecf9c81cca132327f73beb22be9b03eaa9f3070d40/safetensors-0.3.3.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/pypi-safetensors/snapshot/pypi-safetensors-2023-09-26-23-39-44.tar.xz ./vendor

include ../common/Makefile.common
