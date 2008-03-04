Summary: POSIX File System Archiver
Name: pax
Version: 3.4
Release: %mkrel 3
License: GPL
Group: Archiving/Backup
Source: ftp://ftp.suse.com/pub/people/kukuk/pax/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
URL:	ftp://ftp.suse.com/pub/people/kukuk/pax/
Requires: common-licenses

%description
'pax' is the POSIX standard archive tool.  It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS
%{_bindir}/pax
%{_mandir}/man1/*
