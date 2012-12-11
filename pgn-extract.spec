%define	version	16.7
%define tarballversion %(echo %version|sed -e 's|\\.|-|') 

Summary:	Portable Game Notation (PGN) Manipulator for Chess Games
Name:		pgn-extract
Version:	%{version}
Release:	%mkrel 2
License:	GPLv2
Group:		Games/Boards
URL:		http://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/
Source0:	ftp://ftp.cs.kent.ac.uk/pub/djb/Extract/pgn-extract-%{tarballversion}.tgz
# (Abel) 15.0-1mdk neater help message
Patch1:		pgn-extract-15.0-help-mesg.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Its purpose is for manipulating chess games written in the Portable
Game Notation (PGN).

There are several ways to specify the criteria on which to extract:
textual move sequences, the position reached after a sequence
of moves, information in the tag fields, and material balance in
the ending.

Extracted games may be written out either including or
excluding comments, NAGs, and variations. Games may be given ECO
classifications derived from the accompanying file eco.pgn, or a
customised version provided by the user.

%prep
%setup -q -n %{name}-%{tarballversion}
%patch1 -p1 -b .helpmsg

%build
%make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
install -D -m 755 pgn-extract ${RPM_BUILD_ROOT}%{_gamesbindir}/pgn-extract

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc help.html eco.pgn
%{_gamesbindir}/*


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 16.7-2mdv2011.0
+ Revision: 614535
- the mass rebuild of 2010.1 packages

* Mon Feb 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 16.7-1mdv2010.1
+ Revision: 506100
- correct patch
- Update to 16.7
- del old patches

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 16.2-5mdv2010.0
+ Revision: 430683
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 16.2-4mdv2009.0
+ Revision: 258932
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 16.2-3mdv2009.0
+ Revision: 246852
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 16.2-1mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Funda Wang <fwang@mandriva.org> 16.2-1mdv2008.0
+ Revision: 49102
- Rediff patch0
- New version
- Import pgn-extract



* Thu Aug 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 15.0-1mdv2007.0
- Fix Group

* Mon Aug 22 2005 Abel Cheung <deaddog@mandriva.org> 15.0-2mdk
- Patch3: Allow checkmate symbol '#' to exist in pgn file

* Sun Jul 03 2005 Abel Cheung <deaddog@mandriva.org> 15.0-1mdk
- First Mandriva package
