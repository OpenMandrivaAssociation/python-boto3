Name:		python-boto3
Version:	1.34.25
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/boto3/boto3-%{version}.tar.gz
Summary:	The AWS SDK for Python
URL:		https://pypi.org/project/boto3/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
The AWS SDK for Python

%prep
%autosetup -p1 -n boto3-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/boto3
%{py_sitedir}/boto3-*.*-info
