#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v3
# autospec commit: c1050fe
#
Name     : pypi-safetensors
Version  : 0.4.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/32/b4/24d2855f668c2fbee5855cc6551684bdd3f7b935af324c9c8b20290d8443/safetensors-0.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/32/b4/24d2855f668c2fbee5855cc6551684bdd3f7b935af324c9c8b20290d8443/safetensors-0.4.2.tar.gz
Source1  : http://localhost/cgit/vendor/pypi-safetensors/snapshot/pypi-safetensors-2024-01-30-19-13-59.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSL-1.0 MIT Unicode-DFS-2016
Requires: pypi-safetensors-license = %{version}-%{release}
Requires: pypi-safetensors-python = %{version}-%{release}
Requires: pypi-safetensors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(maturin)
BuildRequires : pypi-maturin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://huggingface.co/datasets/safetensors/assets/raw/main/banner-dark.svg">
<source media="(prefers-color-scheme: light)" srcset="https://huggingface.co/datasets/safetensors/assets/raw/main/banner-light.svg">
<img alt="Hugging Face Safetensors Library" src="https://huggingface.co/datasets/safetensors/assets/raw/main/banner-light.svg" style="max-width: 100%;">
</picture>
<br/>
<br/>
</p>

%package license
Summary: license components for the pypi-safetensors package.
Group: Default

%description license
license components for the pypi-safetensors package.


%package python
Summary: python components for the pypi-safetensors package.
Group: Default
Requires: pypi-safetensors-python3 = %{version}-%{release}

%description python
python components for the pypi-safetensors package.


%package python3
Summary: python3 components for the pypi-safetensors package.
Group: Default
Requires: python3-core
Provides: pypi(safetensors)
Provides: pypi(safetensors)

%description python3
python3 components for the pypi-safetensors package.


%prep
%setup -q -n safetensors-0.4.2
cd %{_builddir}
tar xf %{_sourcedir}/pypi-safetensors-2024-01-30-19-13-59.tar.xz
cd %{_builddir}/safetensors-0.4.2
mkdir -p ./vendor
cp -r %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/* %{_builddir}/safetensors-0.4.2/./vendor
mkdir -p .cargo
echo '[source.crates-io]' >> .cargo/config.toml
echo 'replace-with = "vendored-sources"' >> .cargo/config.toml
echo '[source.vendored-sources]' >> .cargo/config.toml
echo 'directory = "vendor"' >> .cargo/config.toml
pushd ..
cp -a safetensors-0.4.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1706643146
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-safetensors
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/e6d32072ef5f584a805b429ecbd4eec428316dde || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/heck/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/heck/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/indoc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/indoc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/itoa/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/itoa/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/lock_api/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/lock_api/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/memmap2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/c1f96d6a54446beefad79ef49b3c123c597b7a40 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/memmap2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/d5c0c6beed5e77d571189516c53cf05f1e58d9ca || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/memoffset/LICENSE %{buildroot}/usr/share/package-licenses/pypi-safetensors/02bf11a87b9bbacedf2fcf4856af3b933faef82e || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/parking_lot/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/parking_lot/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/parking_lot_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/parking_lot_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-build-config/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-build-config/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-ffi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-ffi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-macros-backend/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-macros-backend/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-macros/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3-macros/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3/pyo3-runtime/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/pyo3/pyo3-runtime/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/redox_syscall/LICENSE %{buildroot}/usr/share/package-licenses/pypi-safetensors/a00165152c82ea55b9fc254890dc8860c25e3bb6 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/ryu/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/ryu/LICENSE-BOOST %{buildroot}/usr/share/package-licenses/pypi-safetensors/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/scopeguard/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/scopeguard/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/f498d95a48889a0b1432e420e6754881eff1d593 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/serde/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/serde/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/serde_derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/serde_derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/serde_json/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/serde_json/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/smallvec/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/smallvec/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/c61640f6c218caf86d1b8072e09668a8362dba04 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/target-lexicon/LICENSE %{buildroot}/usr/share/package-licenses/pypi-safetensors/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pypi-safetensors/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/unindent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/unindent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows-targets/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows-targets/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_aarch64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_aarch64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_aarch64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_aarch64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_i686_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_i686_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_i686_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_i686_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_x86_64_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_x86_64_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_x86_64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_x86_64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_x86_64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-safetensors-2024-01-30-19-13-59/windows_x86_64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/safetensors-%{version}/safetensors/LICENSE %{buildroot}/usr/share/package-licenses/pypi-safetensors/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-safetensors/02bf11a87b9bbacedf2fcf4856af3b933faef82e
/usr/share/package-licenses/pypi-safetensors/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-safetensors/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-safetensors/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/pypi-safetensors/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-safetensors/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/pypi-safetensors/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
/usr/share/package-licenses/pypi-safetensors/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/pypi-safetensors/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/pypi-safetensors/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-safetensors/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-safetensors/959ce149b1615b8bff3437f59282396756987859
/usr/share/package-licenses/pypi-safetensors/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/pypi-safetensors/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/pypi-safetensors/a00165152c82ea55b9fc254890dc8860c25e3bb6
/usr/share/package-licenses/pypi-safetensors/a3b3a65335e78bde163f84d599fa899776552994
/usr/share/package-licenses/pypi-safetensors/c1f96d6a54446beefad79ef49b3c123c597b7a40
/usr/share/package-licenses/pypi-safetensors/c61640f6c218caf86d1b8072e09668a8362dba04
/usr/share/package-licenses/pypi-safetensors/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-safetensors/d5c0c6beed5e77d571189516c53cf05f1e58d9ca
/usr/share/package-licenses/pypi-safetensors/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/pypi-safetensors/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/pypi-safetensors/f498d95a48889a0b1432e420e6754881eff1d593

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
