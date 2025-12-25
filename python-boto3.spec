Name:		python-boto3
Version:	1.42.16
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/boto3/boto3-%{version}.tar.gz
Summary:	The AWS SDK for Python
URL:		https://pypi.org/project/boto3/
License:	Apache License 2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
The AWS SDK for Python

%files
%{py_sitedir}/boto3
%{py_sitedir}/boto3-*.*-info
