%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	System_Mount
Summary:	%{_pearname} - mount and unmount devices in fstab
Summary(pl.UTF-8):	%{_pearname} - montowanie i odmontowywanie urządzeń z fstab
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c4d586a8cc91e056cf311ae89c9c1341
URL:		http://pear.php.net/package/System_Mount/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pear
Requires:	php-pear-File_Fstab >= 2.0.0-0.beta1
Requires:	php-pear-System_Command
Suggests:	php-pear-File
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(File.*)

%description
System_Mount provides a simple interface to deal with mounting and
unmounting devices listed in the system's fstab.

Features:
- Very compact, easy-to-read code, based on File_Fstab,
- Examines mount options to determine if a device can be mounted or
  not,
- Extremely easy to use,
- Fully documented with PHPDoc.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
System_Mount dostarcza prostego interfejsu do radzenia sobie z
montowaniem i odmontowywaniem urządzeń wpisanych w pliku fstab.

Cechy:
- Bardzo prosty, czytelny kod bazowany na File-Fstab,
- Bada opcje mount w celu stwierdzenia czy urządzenie może być
  zamontowane lub nie,
- Niewiarygodnie łatwy w użyciu,
- W pełni udokumentowany za pomocą PHPDoc.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d examples
mv docs/System_Mount/docs/example.php examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/System/Mount.php

%{_examplesdir}/%{name}-%{version}
