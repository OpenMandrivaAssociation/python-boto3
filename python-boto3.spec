%define module boto3

Name:		python-boto3
Summary:	The AWS SDK for Python
Version:	1.42.96
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/boto3/
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
The AWS SDK for Python.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
