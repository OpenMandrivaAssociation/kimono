Name:		kimono
Summary:	C# Mono KDE 4 bindings
Version:	4.13.2
Release:	1
Epoch:		1
Group:		Development/KDE and Qt
License:	GPLv2 LGPLv2
URL:		https://projects.kde.org/projects/kde/kdebindings/csharp/kimono
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kimono-4.7.2-fix-link-against-soprano-index-librairies.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	smokekde-devel >= 1:%{version}
BuildRequires:	qyoto-devel >= 1:%{version}
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
Provides:	mono-kde4 = %{EVRD}
Requires:	qyoto >= 1:%{version}

%description
NET/Mono bindings for the KDE libraries.

%files
%doc COPYING.GPLv2 COPYING.LGPLv2
%{_kde_prefix}/lib/mono/qyoto/kde-dotnet.dll
%{_kde_prefix}/lib/mono/qyoto/khtml-dll.dll
%{_kde_prefix}/lib/mono/qyoto/soprano.dll
%{_kde_prefix}/lib/mono/qyoto/ktexteditor-dotnet.dll
%{_kde_prefix}/lib/mono/qyoto/plasma-dll.dll
%{_kde_prefix}/lib/mono/qyoto/nepomuk-dll.dll
%{_kde_prefix}/lib/mono/qyoto/akonadi.dll
%{_kde_prefix}/lib/mono/gac/kde-dotnet
%{_kde_prefix}/lib/mono/gac/khtml-dll
%{_kde_prefix}/lib/mono/gac/soprano
%{_kde_prefix}/lib/mono/gac/ktexteditor-dotnet
%{_kde_prefix}/lib/mono/gac/plasma-dll
%{_kde_prefix}/lib/mono/gac/nepomuk-dll
%{_kde_prefix}/lib/mono/gac/akonadi
%{_kde_libdir}/kde4/kimonopluginfactory.so
%{_kde_libdir}/libkhtml-sharp.so
%{_kde_libdir}/libnepomuk-sharp.so
%{_kde_libdir}/libsoprano-sharp.so
%{_kde_libdir}/libkimono.so
%{_kde_libdir}/libktexteditor-sharp.so
%{_kde_libdir}/libplasma-sharp.so
%{_kde_libdir}/libakonadi-sharp.so
%{_kde_appsdir}/plasma_scriptengine_kimono
%{_kde_services}/plasma-scriptengine-kimono-applet.desktop
%{_kde_services}/plasma-scriptengine-kimono-dataengine.desktop

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Mon Jul 09 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 758060
- Backport to 2010.2 for MIB users
- Update to 4.8.0
- Update file list
- MIB (Mandriva International Backports)

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758060
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 744541
- New upstream tarball
- Remove changelog in the spec file
- import kimono from mageia work ( tks you mikala ;) )
- create repo

