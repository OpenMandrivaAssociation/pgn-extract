%define	version	15.0
%define release	%mkrel 3

Summary:	Portable Game Notation (PGN) Manipulator for Chess Games
Name:		pgn-extract
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/
Source0:	ftp://ftp.cs.kent.ac.uk/pub/djb/Extract/pgn-extract.tar.bz2
# (Abel) 15.0-1mdk use mandriva optimization flags
Patch0:		pgn-extract-15.0-makefile.patch.bz2
# (Abel) 15.0-1mdk treat '--help' option as '-h'
Patch1:		pgn-extract-15.0-help-option.patch.bz2
# (Abel) 15.0-1mdk neater help message
Patch2:		pgn-extract-15.0-help-mesg.patch.bz2
# (Abel) 15.0-1mdk allow checkmate symbol '#'
Patch3:		pgn-extract-15.0-allow-checkmate.patch.bz2
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
%setup -q -c
%patch0 -p1 -b .mdk
%patch1 -p1 -b .helpopt
%patch2 -p1 -b .helpmsg
%patch3 -p1 -b .checkmate

find -type f -print0 | xargs -0 -r chmod 0644

%build
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
install -D -m 755 pgn-extract ${RPM_BUILD_ROOT}%{_gamesbindir}/pgn-extract

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README help.html eco.pgn
%{_gamesbindir}/*
