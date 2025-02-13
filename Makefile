PKG_NAME := pypi-safetensors
URL = https://files.pythonhosted.org/packages/f4/4f/2ef9ef1766f8c194b01b67a63a444d2e557c8fe1d82faf3ebd85f370a917/safetensors-0.5.2.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/pypi-safetensors/snapshot/pypi-safetensors-2024-01-30-19-13-59.tar.xz ./vendor $(CGIT_BASE_URL)/vendor/pypi-safetensors/snapshot/pypi-safetensors-2025-02-13-23-47-10.tar.gz ./vendor

include ../common/Makefile.common
