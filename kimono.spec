Name: kimono
Summary: C# Mono KDE 4 bindings
Version: 4.7.90
Release: 1
Epoch: 1
Group: Development/KDE and Qt
License: GPLv2 LGPLv2
URL: https://projects.kde.org/projects/kde/kdebindings/csharp/kimono
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
Patch0: kimono-4.7.2-fix-link-against-soprano-index-librairies.patch

BuildRequires: kdelibs4-devel >= 2:%version
BuildRequires: smokekde-devel >= 1:%version
BuildRequires: qyoto-devel >= 1:%version
BuildRequires: pkgconfig(mono)
BuildRequires: pkgconfig(shared-desktop-ontologies)

Provides: mono-kde4 = %epoch:%version-%release

Requires: qyoto >= 1:%version

%description
NET/Mono bindings for the KDE libraries.

%files
%doc COPYING.GPLv2  COPYING.LGPLv2
%_kde_prefix/lib/mono/qyoto/kde-dotnet.dll
%_kde_prefix/lib/mono/qyoto/khtml-dll.dll
%_kde_prefix/lib/mono/qyoto/soprano.dll
%_kde_prefix/lib/mono/qyoto/ktexteditor-dotnet.dll
%_kde_prefix/lib/mono/qyoto/plasma-dll.dll
%_kde_prefix/lib/mono/qyoto/nepomuk-dll.dll
%_kde_prefix/lib/mono/gac/kde-dotnet
%_kde_prefix/lib/mono/gac/khtml-dll
%_kde_prefix/lib/mono/gac/soprano
%_kde_prefix/lib/mono/gac/ktexteditor-dotnet
%_kde_prefix/lib/mono/gac/plasma-dll
%_kde_prefix/lib/mono/gac/nepomuk-dll
%_kde_libdir/kde4/kimonopluginfactory.so
%_kde_libdir/libkhtml-sharp.so
%_kde_libdir/libnepomuk-sharp.so
%_kde_libdir/libsoprano-sharp.so
%_kde_libdir/libkimono.so
%_kde_libdir/libktexteditor-sharp.so
%_kde_libdir/libplasma-sharp.so
%_kde_appsdir/plasma_scriptengine_kimono
%_kde_services/plasma-scriptengine-kimono-applet.desktop
%_kde_services/plasma-scriptengine-kimono-dataengine.desktop

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export LD=/usr/bin/ld.gold
%cmake_kde4  -DKDE4_ENABLE_FINAL=ON
%make

%install
%makeinstall_std -C build


%changelog

* Thu Dec 15 2011 mikala <mikala@mageia.org> 1:4.7.90-1.mga2
+ Revision: 182121
- Update tarball to KDE SC 4.7.90

* Sun Dec 04 2011 mikala <mikala@mageia.org> 1:4.7.4-1.mga2
+ Revision: 176453
- Update tarball to KDE SC 4.7.4

* Wed Nov 02 2011 mikala <mikala@mageia.org> 1:4.7.3-1.mga2
+ Revision: 161349
- Update tarball to KDE SC 4.7.3

* Thu Oct 06 2011 mikala <mikala@mageia.org> 1:4.7.2-1.mga2
+ Revision: 152437
- Add patch1 to not link against soprano index librairies (we don't build them anymore)
- Update tarball to KDE SC 4.7.2

* Wed Sep 07 2011 mikala <mikala@mageia.org> 1:4.7.1-1.mga2
+ Revision: 140653
- Update tarball to KDE SC 4.7.1
- Update tarball to KDE SC 4.7.0
- remove %%defattr
- use kde4 macros
- fix license

* Tue Jul 12 2011 mikala <mikala@mageia.org> 1:4.6.95-1.mga2
+ Revision: 122672
- Update tarball to KDE 4.6.95 (KDE SC 4.7 RC2)

* Fri Jul 08 2011 fwang <fwang@mageia.org> 1:4.6.90-1.mga2
+ Revision: 120331
- update file list
- imported package kimono

