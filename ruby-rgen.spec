%define pkgname rgen
Summary:	Ruby Modeling and Generator Framework
Name:		ruby-%{pkgname}
Version:	0.6.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	47225c37c619ba737cac0d6450afdd3a
URL:		https://rubygems.org/gems/rgen
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RGen is a framework for Model Driven Software Development (MDSD) in
Ruby. This means that it helps you build Metamodels, instantiate
Models, modify and transform Models and finally generate arbitrary
textual content from it.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.rdoc MIT-LICENSE
%{ruby_vendorlibdir}/ea_support
%{ruby_vendorlibdir}/metamodels
%{ruby_vendorlibdir}/mmgen
%{ruby_vendorlibdir}/rgen
%{ruby_vendorlibdir}/transformers
