Summary:	Cross Platform Password Manager
Name:		keepassx
Version:	2.0.2
Release:	1
Source0:	https://www.keepassx.org/releases/%{version}/keepassx-%{version}.tar.gz
License:	GPLv2+
Group:		File tools
URL:		http://www.keepassx.org/
BuildRequires:	cmake
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	qt4-devel >= 4.3.0
Provides:	keepass = %{version}-%{release}
Provides:	KeePassX = %{version}-%{release}

%description
KeePassX is a free/open-source password manager or safe which helps
you to manage your passwords in a secure way. You can put all your
passwords in one database, which is locked with one master key or a
key-disk. So you only have to remember one single master password or
insert the key-disk to unlock the whole database. The databases are
encrypted using the best and most secure encryption algorithms
currently known (AES and Twofish).

%prep
%setup -q
%apply_patches

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

%files
%doc CHANGELOG
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/*/mimetypes/*.png

