%include	/usr/lib/rpm/macros.php
%define         _class          System
%define         _subclass       Mount
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Mount and unmount devices in fstab
Summary(pl):	%{_pearname} - Montowanie i odmontowywanie urz±dzeñ z fstab
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	cf195029ce8274d1b1fd4e5412e290cc
URL:		http://pear.php.net/package/System_Mount/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ystem_Mount provides a simple interface to deal with mounting and
unmounting devices listed in the system's fstab.

Features:
- Very compact, easy-to-read code, based on File_Fstab,
- Examines mount options to determine if a device can be mounted or
  not,
- Extremely easy to use,
- Fully documented with PHPDoc.


In PEAR status of this package is: %{_status}.

%description -l pl
System_Mount dostarcza prostego interfejsu do radzenia sobie z
montowaniem i odmontowywaniem urz±dzeñ wpisanych w pliku fstab.

Cechy:
- Bardzo prosty, czytelny kod bazowany na File-Fstab,
- Bada opcje mount w celu stwierdzenia czy urz±dzenie mo¿e byæ
  zamontowane lub nie,
- Niewiarygodnie ³atwy w u¿yciu,
- W pe³ni udokumentowany za pomoc± PHPDoc.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/example.php
%{php_pear_dir}/%{_class}/*.php
