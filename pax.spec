Summary:	POSIX File System Archiver
Name:		pax
Version:	3.4
Release:	15
License:	GPLv2
Group:		Archiving/Backup
Url:		ftp://ftp.suse.com/pub/people/kukuk/pax/
Source0:	ftp://ftp.suse.com/pub/people/kukuk/pax/%{name}-%{version}.tar.bz2
Patch0:		pax-3.4-gcc46.patch
Patch1:		pax-automake-1.13.patch

%description
'pax' is the POSIX standard archive tool.  It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall_std

%files
%doc AUTHORS NEWS README THANKS
%{_bindir}/pax
%{_mandir}/man1/*

