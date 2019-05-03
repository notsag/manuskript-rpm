%define name    manuskript
%define version 0.9.0
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: Manuskript open source tool for writers
Name: %{name}
Version: %{version}
Release: 1
License: GPL3+
Group: Applications/Editors
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.theologeek.ch/manuskript/
SOURCE0: https://github.com/olivierkes/manuskript/archive/0.9.0.tar.gz#/%{name}-%{version}-%{release}.tar.gz
Packager: Maxime Gaston <maxime@gaston.sh>
Provides: Manuskript
Requires: python3
Requires: python3-qt5 
Requires: python3-qt5-webkit
Requires: qt5-qtsvg
Requires: python3-enchant
Requires: python3-lxml
Requires: python3-markdown
Requires: zlib
Requires: pandoc

%description
Manuskript is an open source tool for writers.  It
provides a rich environment to help writers create
their first draft and then further refine and edit
their masterpiece.

%prep
%autosetup -n %{name}-0.9.0

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/bin
mkdir -p  %{buildroot}/usr/share/applications
mkdir -p  %{buildroot}/usr/share/%{name}
cp -f package/create_deb/%{name} %{buildroot}/usr/bin/
cp -f package/create_deb/%{name}.desktop %{buildroot}/usr/share/applications/
cp -rf CHANGELOG.md COPYING CREDITS i18n icons libs %{name} %{name}.spec README.md resources sample-projects %{buildroot}/usr/share/%{name}/
chmod a+x %{buildroot}/usr/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}
/usr/share/applications/%{name}.desktop
/usr/share/%{name}/*

%changelog
# Empty section.
