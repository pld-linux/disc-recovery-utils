Summary:	Disc recovery tools for EXT2FS
Summary(pl):	Narzêdzia ratunkowe do ext2fs
Name:		disc-recovery-utils
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.atnf.csiro.au/pub/people/rgooch/linux/%{name}-%{version}.tgz
BuildRequires:	e2fsprogs-devel >= 1.07
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
A few disc recovery tools (copy_blocks and copy_listed_blocks) and an
inode recovery tool for the EXT2 filesystem (e2fsfind).

%description -l pl
Kilka narzêdzi ratunkowych (copy_blocks i copy_listed_blocks) oraz
narzêdzie do odzyskiwania inodów z systemu plików ext2 (e2fsfind).

%prep
%setup -q -n %{name}

%build
sed 's/cc/$(CC) $(CFLAGS) $(LDFLAGS)/'< Makefile >GNUmakefile
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" E2FSROOT=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install copy_blocks copy_listed_blocks e2fsfind $RPM_BUILD_ROOT%{_sbindir}
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/*/*
