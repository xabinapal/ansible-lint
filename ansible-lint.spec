# All tests require Internet access
# to test in mock use:  --enable-network --with check
# to test in a privileged environment use:
#   --with check --with privileged_tests
%bcond_with     check
%bcond_with     privileged_tests

Name:           ansible-lint
Version:        VERSION_PLACEHOLDER
Release:        1%{?dist}
Summary:        TBD Ansible-lint summary

License:        MIT
URL:            https://github.com/ansible-community/ansible-lint
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-setuptools_scm_git_archive
%if %{with check}
# These are required for tests:
BuildRequires:  python%{python3_pkgversion}-pyyaml
BuildRequires:  python%{python3_pkgversion}-tabulate
BuildRequires:  python%{python3_pkgversion}-jsonschema
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-flexmock
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
BuildRequires:  python%{python3_pkgversion}-libselinux
BuildRequires:  ansible
BuildRequires:  podman
BuildRequires:  buildah
BuildRequires:  git
%endif
Requires:       ansible
Requires:       buildah

%description
TBD Ansible-lint description

%prep
%autosetup


%build
%py3_build


%install
%py3_install


%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  pytest-3 \
  -v \
  --disable-pytest-warnings \
  --numprocesses=auto \
%if %{with privileged_tests}
  tests
%else
  tests/unit
%endif
%endif


%files
%{python3_sitelib}/ansiblelint/
%{python3_sitelib}/ansible_lint-*.egg-info/
%{_bindir}/ansible-lint
%license LICENSE
%doc docs/* README.rst



%changelog

Available at https://github.com/ansible-community/ansible-lint/releases
