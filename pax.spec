Summary: POSIX File System Archiver
Name: pax
Version: 3.4
Release: 11
License: GPL
Group: Archiving/Backup
Source0: ftp://ftp.suse.com/pub/people/kukuk/pax/%{name}-%{version}.tar.bz2
Patch0: pax-3.4-gcc46.patch
Patch1: pax-automake-1.13.patch
URL:	ftp://ftp.suse.com/pub/people/kukuk/pax/

%description
'pax' is the POSIX standard archive tool.  It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .am113~

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS
%{_bindir}/pax
%{_mandir}/man1/*


%changelog
* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 3.4-9mdv2011.0
+ Revision: 669286
- fix build with gcc 4.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4-8mdv2011.0
+ Revision: 607078
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4-7mdv2010.1
+ Revision: 520197
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.4-6mdv2010.0
+ Revision: 426358
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.4-5mdv2009.1
+ Revision: 351665
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.4-4mdv2009.0
+ Revision: 223442
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3.4-3mdv2008.1
+ Revision: 179142
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 3.4-2mdv2008.0
+ Revision: 74314
- Import pax



* Fri Sep 01 2006 Stew Benedict <sbenedict@mandriva.com> 3.4-2mdv2007.0
- rebuild

* Thu Aug 18 2005 Stew Benedict <sbenedict@mandriva.com> 3.4-1mdk
- 3.4, drop gcc patch

* Fri Jun 03 2005 Stew Benedict <sbenedict@mandriva.com> 3.2-2mdk
- rebuild, patch for gcc4.0 (P0)

* Sat May 15 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 3.2-1mdk
- Release 3.2.

* Mon Jul 21 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.0-4mdk
- rebuild
- rm -rf $RPM_BUILD_ROOT in the beginning of %%install

* Fri Dec 27 2002 Stew Benedict <sbenedict@mandrakesoft.com> 3.0-3mdk
- rebuild for new glibc/rpm

* Mon Jul 22 2002 Jeff Garzik <jgarzik@mandrakesoft.com> 3.0-2mdk
- use %%configure2_5x and %%makeinstall_std
- fix License: s/BSD/GPL/
- Requires: common-licenses
- add %%doc documentation (AUTHORS, NEWS, README, THANKS)

* Wed Apr 10 2002 Stew Benedict <sbenedict@mandrakesoft.com> 3.0-1mdk
- new "unbroken" version, courtesy of Thorsten Kukuk <kukuk@suse.de>

* Tue Feb 19 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.5-3mdk
- rebuild to fix the "expected size" not matching the "actual size"

* Wed Aug 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5-2mdk
- bzip2 sources & patches

* Sun Aug  5 2001 Stew Benedict <sbenedict@mandrakesoft.com> 1.5-1mdk
- borrowed RedHat SRPM - used by lsb-testsuite
