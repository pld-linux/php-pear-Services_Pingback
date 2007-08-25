%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Pingback
%define		_status		alpha
%define		_pearname	Services_Pingback

Summary:	%{_pearname} - a Pingback User-Agent class
Summary(pl):	%{_pearname} - obsługa pingback
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	06559c575ae0197468e27604d871bea3
URL:		http://pear.php.net/package/Services_Pingback/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.2.4
Requires:	php-pear-Net_URL >= 1.0.14
Requires:	php-pear-PEAR >= 1.4.0
Requires:	php-pear-XML_RPC >= 1.0.3RC1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package implemented of Pingback in PHP, able to sending and
receiving a pingback.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet implentujący obsługe Pingback, umożliwiając wysyłanie oraz
odbieranie zgłoszeń pingback.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_Pingback
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Pingback.php
