Summary:	Disc recovery tools for EXT2FS
Name:		disc-recovery-utils
Version:	1.1
Release:	1
Source0:	ftp://ftp.atnf.csiro.au/pub/people/rgooch/linux/%{name}-%{version}.tgz
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
BuildRequires:	e2fsprogs-devel >= 1.07
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix /
%define		_sbindir %{_prefix}/sbin

%description
A few disc recovery tools (copy_blocks and copy_listed_blocks) and an
inode recovery tool for the EXT2 filesystem (e2fsfind).

%prep
%setup -q -n %{name}

%build
sed 's/cc/$(CC) $(CFLAGS) $(LDFLAGS)/'<Makefile>GNUmakefile
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}" \
	E2FSROOT=$RPM_BUILD_ROOT LDFLAGS="%{?debug:-s}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
cp copy_blocks copy_listed_blocks e2fsfind $RPM_BUILD_ROOT%{_sbindir}
cp *.8 $RPM_BUILD_ROOT%{_mandir}/man8
gzip -9nf README

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/*
%{_mandir}/*/*
%doc README*

%clean
rm -rf $RPM_BUILD_ROOT
