%define _disable_lto 1

Summary:	POSIX File System Archiver
Name:		pax
Version:	3.4
Release:	22
License:	GPLv2
Group:		Archiving/Backup
Url:		ftp://ftp.suse.com/pub/people/kukuk/pax/
Source0:	ftp://ftp.suse.com/pub/people/kukuk/pax/%{name}-%{version}.tar.bz2
Patch0:		https://src.fedoraproject.org/rpms/pax/raw/master/f/pax-3.0-PATHMAX.patch
Patch1:		https://src.fedoraproject.org/rpms/pax/raw/master/f/pax-3.4-abs100.patch
Patch2:		https://src.fedoraproject.org/rpms/pax/raw/master/f/pax-3.4-disable-Werror.patch
Patch3:		https://src.fedoraproject.org/rpms/pax/raw/master/f/pax-3.4-manpage.patch
Patch4:		https://src.fedoraproject.org/rpms/pax/raw/master/f/pax-3.4-rdtruncate.patch
Patch5:		https://src.fedoraproject.org/rpms/pax/raw/master/f/pax-gcc46.patch
Patch6:		pax-automake-1.13.patch

%description
'pax' is the POSIX standard archive tool.  It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%autosetup -p1
autoreconf -fi

%build
%configure
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%make_install

%files
%doc AUTHORS NEWS README THANKS
%{_bindir}/pax
%{_mandir}/man1/*
