Name: kimono
Summary: C# Mono KDE 4 bindings
Version: 4.8.97
Release: 1
Epoch: 1
Group: Development/KDE and Qt
License: GPLv2 LGPLv2
URL: https://projects.kde.org/projects/kde/kdebindings/csharp/kimono
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/%name-%version.tar.xz
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
%_kde_prefix/lib/mono/qyoto/akonadi.dll
%_kde_prefix/lib/mono/gac/kde-dotnet
%_kde_prefix/lib/mono/gac/khtml-dll
%_kde_prefix/lib/mono/gac/soprano
%_kde_prefix/lib/mono/gac/ktexteditor-dotnet
%_kde_prefix/lib/mono/gac/plasma-dll
%_kde_prefix/lib/mono/gac/nepomuk-dll
%_kde_prefix/lib/mono/gac/akonadi
%_kde_libdir/kde4/kimonopluginfactory.so
%_kde_libdir/libkhtml-sharp.so
%_kde_libdir/libnepomuk-sharp.so
%_kde_libdir/libsoprano-sharp.so
%_kde_libdir/libkimono.so
%_kde_libdir/libktexteditor-sharp.so
%_kde_libdir/libplasma-sharp.so
%_kde_libdir/libakonadi-sharp.so
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

