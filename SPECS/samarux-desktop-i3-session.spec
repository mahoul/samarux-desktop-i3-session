Name:           samarux-desktop-i3-session
Version:        0.1
Release:        14
Summary:        samarux-desktop-i3-session session files for i3 + gnome subsystem via gnome-flashback
License:        GPL
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Packager: 	Enrique Gil (mahoul@gmail.com)
Requires:	gnome-flashback
BuildArch:	noarch
BuildRequires:	rsync

%description
samarux-desktop-i3-session contains the files needed to run an i3 session with support
for the GNOME subsystem services provided via gnome-session.
Most of the files for this are minimal tweaked versions from files
from the awesome Regolith project (https://regolith-linux.org/)


%prep
#[ -d %{name} ] && rm -Rfv %{name}
#[ -d %{_topdir}/SOURCES ] && rsync -avP --exclude '.git' --delete %{_topdir}/SOURCES/ .
%autosetup


%install
#cd %{name}
%{__install} -D -m644 usr/share/applications/samarux-i3.desktop %{buildroot}/usr/share/applications/samarux-i3.desktop
%{__install} -D -m644 usr/share/gnome-session/sessions/samarux-i3.session %{buildroot}/usr/share/gnome-session/sessions/samarux-i3.session
%{__install} -D -m644 usr/share/xsessions/samarux-i3.desktop %{buildroot}/usr/share/xsessions/samarux-i3.desktop
%{__install} -D -m755 usr/bin/samarux-i3 %{buildroot}/usr/bin/samarux-i3
%{__install} -D -m755 usr/bin/samarux-session %{buildroot}/usr/bin/samarux-session


%clean


%files
%defattr(-, root, root)
/usr/bin/samarux-i3
/usr/bin/samarux-session
/usr/share/applications/samarux-i3.desktop
/usr/share/gnome-session/sessions/samarux-i3.session
/usr/share/xsessions/samarux-i3.desktop

%changelog
* Sun Apr 11 2021 Enrique Gil <mahoul@gmail.com> - 0.1-14
- Replaced prep section with autosetup

* Sun Apr 11 2021 Enrique Gil (mahoul@gmail.com) - 0.1-13
- Renamed pkg to samarux-desktop-i3-session and src files too

* Sat Apr 10 2021 Enrique Gil (mahoul@gmail.com) - 0.1-12
- Renamed package to samarux-i3-gnome

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-11
- Added gnome-flashback as required component to i3-gnome.session

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-10
- Fixed date on first changelog entry

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-9
- Test build with tuned-up script

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-8
- Updated description

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-7
- Removed newline on description

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-6
- Added newline tag to description

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-5
- Added space to description

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-4
- Cleaned up session script and added kudos to regolith

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-3
- Changed arch to noarch

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-2
- Removed group tag

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-1
- Initial release.


